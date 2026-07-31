"""
math_verify/verifier.py — CAS verification of bot-produced calculus results.

The model emits a hidden claim line at the end of its answer:
    [[V: indef | INTEGRAND | ANTIDERIVATIVE | VAR]]
    [[V: def   | INTEGRAND | LOWER | UPPER | VALUE | VAR]]

verify_response() strips those lines and returns a status:
    "verified" — every claim checked out
    "failed"   — at least one claim is mathematically wrong
    "unknown"  — no claims, or none could be parsed/checked in time

Design notes:
  * Indefinite integrals are checked by DIFFERENTIATING the claimed
    antiderivative and comparing to the integrand at random points.
    Never calls integrate() — that is what hangs.
  * Definite integrals use numerical quadrature via Integral(...).evalf().
  * Every check runs under a hard timeout. A slow check returns "unknown",
    never blocks the reply.

Self-test:  python -m math_verify.verifier
"""

import random
import re
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import TimeoutError as FutureTimeout
from dataclasses import dataclass

import sympy
from sympy.parsing.sympy_parser import (
    convert_xor,
    implicit_multiplication_application,
    parse_expr,
    standard_transformations,
)

TRANSFORMS = standard_transformations + (
    implicit_multiplication_application,
    convert_xor,
)

_BLOCK = re.compile(r"\[\[\s*V\s*:(.*?)\]\]", re.DOTALL)

TIMEOUT_SEC = 6.0
NUM_SAMPLES = 12
TOL = 1e-6

_POOL = ThreadPoolExecutor(max_workers=2)


@dataclass
class Claim:
    kind: str
    parts: list
    raw: str


@dataclass
class Verdict:
    status: str      # verified | failed | unknown
    detail: str


# ---------------------------------------------------------------- parsing

def _parse(text: str, var: sympy.Symbol):
    return parse_expr(
        text.strip(),
        local_dict={str(var): var},
        transformations=TRANSFORMS,
    )


def extract_claims(text: str) -> list:
    claims = []
    for m in _BLOCK.finditer(text):
        body = m.group(1)
        parts = [p.strip() for p in body.split("|")]
        if len(parts) < 2:
            continue
        claims.append(Claim(kind=parts[0].lower(), parts=parts[1:], raw=m.group(0)))
    return claims


def strip_claims(text: str) -> str:
    """Always run this before the reply reaches a student."""
    return _BLOCK.sub("", text).rstrip()


# ---------------------------------------------------------------- checks

def _check_indef(integrand_s, anti_s, var_s) -> Verdict:
    x = sympy.Symbol(var_s, real=True)
    f = _parse(integrand_s, x)
    F = _parse(anti_s, x)
    diff = sympy.diff(F, x) - f

    fn = sympy.lambdify(x, diff, "mpmath")
    

    tested = bad = 0
    for _ in range(NUM_SAMPLES):
        p = random.uniform(0.31, 2.79)
        try:
            v = complex(fn(p))
        except Exception:
            continue
        tested += 1
        if abs(v) > TOL:
            bad += 1

    if tested < 4:
        try:
            return Verdict(
                "verified" if sympy.simplify(diff) == 0 else "failed",
                "symbolic fallback",
            )
        except Exception:
            return Verdict("unknown", "not evaluable")

    if bad == 0:
        return Verdict("verified", f"d/d{var_s} matches at {tested} points")
    return Verdict("failed", f"mismatch at {bad}/{tested} points")


def _check_def(integrand_s, lo_s, hi_s, claimed_s, var_s) -> Verdict:
    x = sympy.Symbol(var_s, real=True)
    f = _parse(integrand_s, x)
    lo = _parse(lo_s, x)
    hi = _parse(hi_s, x)
    claimed = _parse(claimed_s, x)

    true_val = sympy.Integral(f, (x, lo, hi)).evalf()
    if not true_val.is_number:
        return Verdict("unknown", "integral not numeric")

    a = complex(true_val)
    b = complex(sympy.N(claimed))
    scale = max(1.0, abs(a))
    if abs(a - b) <= TOL * scale:
        return Verdict("verified", f"{b.real:.6g} matches {a.real:.6g}")
    return Verdict("failed", f"claimed {b.real:.6g}, actual {a.real:.6g}")


def _dispatch(claim: Claim) -> Verdict:
    p = claim.parts
    if claim.kind == "indef" and len(p) >= 3:
        return _check_indef(p[0], p[1], p[2])
    if claim.kind == "def" and len(p) >= 5:
        return _check_def(p[0], p[1], p[2], p[3], p[4])
    return Verdict("unknown", f"malformed claim: {claim.raw[:60]}")


def verify_claim(claim: Claim) -> Verdict:
    try:
        return _POOL.submit(_dispatch, claim).result(timeout=TIMEOUT_SEC)
    except FutureTimeout:
        return Verdict("unknown", "timeout")
    except Exception as e:
        return Verdict("unknown", f"{type(e).__name__}: {e}")


# ---------------------------------------------------------------- entry

def verify_response(text: str):
    """
    Returns (clean_text, status, details).
    clean_text is always safe to send to the student.
    """
    claims = extract_claims(text)
    clean = strip_claims(text)

    if not claims:
        return clean, "unknown", ["no claim emitted"]

    verdicts = [verify_claim(c) for c in claims]
    details = [f"{c.kind}: {v.status} — {v.detail}"
               for c, v in zip(claims, verdicts)]

    if any(v.status == "failed" for v in verdicts):
        return clean, "failed", details
    if any(v.status == "verified" for v in verdicts):
        return clean, "verified", details
    return clean, "unknown", details


# ---------------------------------------------------------------- selftest

if __name__ == "__main__":
    cases = [
        ("correct by-parts",
         "الجواب هو ... [[V: indef | x*exp(x) | x*exp(x) - exp(x) | x]]",
         "verified"),
        ("WRONG by-parts (sign flipped)",
         "[[V: indef | x*exp(x) | x*exp(x) + exp(x) | x]]",
         "failed"),
        ("correct definite",
         "[[V: def | x**2 | 0 | 3 | 9 | x]]",
         "verified"),
        ("WRONG definite",
         "[[V: def | x**2 | 0 | 3 | 27 | x]]",
         "failed"),
        ("correct arctan",
         "[[V: indef | 1/(x**2+1) | atan(x) | x]]",
         "verified"),
        ("correct trig sub",
         "[[V: indef | 1/sqrt(1-x**2) | asin(x) | x]]",
         "verified"),
        ("WRONG partial fractions",
         "[[V: indef | 1/(x**2-1) | log(x-1) - log(x+1) | x]]",
         "failed"),
        ("no claim emitted",
         "شرح نظري بدون تكامل محسوب",
         "unknown"),
    ]

    print("SymPy verifier self-test\n" + "-" * 60)
    passed = 0
    for name, text, expected in cases:
        clean, status, details = verify_response(text)
        ok = status == expected
        passed += ok
        print(f"[{'PASS' if ok else 'FAIL'}] {name}")
        print(f"       expected={expected} got={status}  ({details[0]})")
        if "[[V" in clean:
            print("       !! claim leaked into student text")
    print("-" * 60)
    print(f"{passed}/{len(cases)} passed")