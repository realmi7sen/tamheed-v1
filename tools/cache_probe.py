"""
tools/cache_probe.py — find the real minimum cacheable prefix for Haiku 4.5.

Isolates ONE variable: prefix length. cache_control stays on system_blocks[0]
in every run, so placement cannot confound the result.

Run from repo root:  python tools/cache_probe.py
Requires ANTHROPIC_API_KEY in env. Costs roughly $0.02 total.
"""

import time
from anthropic import Anthropic

MODEL = "claude-haiku-4-5-20251001"
TARGETS = (800, 1024, 1500, 2048, 2500, 3000, 4200)

client = Anthropic()

FILLER = (
    "Integration by parts is chosen when the integrand is a product of an "
    "algebraic factor and a transcendental factor, and substitution is chosen "
    "when one factor is the derivative of the other up to a constant. "
)


def count(text: str) -> int:
    return client.messages.count_tokens(
        model=MODEL,
        system=[{"type": "text", "text": text}],
        messages=[{"role": "user", "content": "x"}],
    ).input_tokens


def build(target: int) -> tuple[str, int]:
    """Grow filler until the counted prefix reaches target."""
    text = FILLER
    n = count(text)
    while n < target:
        text += FILLER * max(1, (target - n) // 40)
        n = count(text)
    return text, n


def probe(target: int) -> bool:
    text, n = build(target)
    system = [{
        "type": "text",
        "text": text,
        "cache_control": {"type": "ephemeral"},
    }]

    created = read = 0
    for i in range(2):
        r = client.messages.create(
            model=MODEL,
            max_tokens=16,
            system=system,
            messages=[{"role": "user", "content": "قل تمام فقط"}],
        )
        u = r.usage
        if i == 0:
            created = u.cache_creation_input_tokens
        else:
            read = u.cache_read_input_tokens
        time.sleep(2)

    hit = read > 0
    print(f"{n:>6} tok | created={created:<6} read={read:<6} | "
          f"{'CACHED' if hit else 'NOT CACHED'}")
    return hit


if __name__ == "__main__":
    print(f"model: {MODEL}\n")
    floor = None
    for t in TARGETS:
        if probe(t) and floor is None:
            floor = t
    print()
    if floor is None:
        print("No target cached. Placement or account config is the problem, "
              "not length. Stop and check cache_control placement.")
    else:
        print(f"Minimum cacheable prefix lies between the last NOT CACHED "
              f"row and ~{floor} tokens.")