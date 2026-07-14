# section_7_2.md

course: MATH106
book_chapter: 7
book_section: 7.2
ksu_chapter: 3
section_title: Trigonometric Integrals
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: [1, 3, 4, 5, 7, 9, 11, 13, 15]
topic_tags: [trigonometric-integrals, half-angle-formula, powers-of-sine-and-cosine]
difficulty: UNKNOWN
in_syllabus: true
enrichment: UNKNOWN
status: draft

---

# Trigonometric Integrals

---

## Metadata

- **Course:** MATH106
- **Book:** Calculus (Swokowski)
- **Edition:** 6th
- **Chapter Number:** 7
- **Chapter Title:** Techniques of Integration
- **Section Number:** 7.2
- **Section Title:** Trigonometric Integrals

---

## Definitions

No formal boxed definitions are introduced in this section.

---

## Theorems

No formally numbered theorems are introduced in this section.

---

## Formulas

- **Half-angle formulas:**

$$\sin^2 x = \frac{1 - \cos 2x}{2} \qquad \cos^2 x = \frac{1 + \cos 2x}{2}$$

- **Guidelines for Evaluating $\int \sin^m x \cos^n x \, dx$ (7.2):**
  1. If $m$ is an odd integer: Write the integral as

  $$\int \sin^m x \cos^n x \, dx = \int \sin^{m-1} x \cos^n x \sin x \, dx$$

  and express $\sin^{m-1} x$ in terms of $\cos x$ by using the trigonometric identity $\sin^2 x = 1 - \cos^2 x$. Make the substitution

  $$u = \cos x, \quad du = -\sin x \, dx$$

  and evaluate the resulting integral.
  2. If $n$ is an odd integer: Write the integral as

  $$\int \sin^m x \cos^n x \, dx = \int \sin^m x \cos^{n-1} x \cos x \, dx$$

  and express $\cos^{n-1} x$ in terms of $\sin x$ by using the trigonometric identity $\cos^2 x = 1 - \sin^2 x$. Make the substitution

  $$u = \sin x, \quad du = \cos x \, dx$$

  and evaluate the resulting integral.
  3. If $m$ and $n$ are even: Use half-angle formulas for $\sin^2 x$ and $\cos^2 x$ to reduce the exponents by one-half.

- **Guidelines for Evaluating $\int \tan^m x \sec^n x \, dx$ (7.3):**
  1. If $m$ is an odd integer: Write the integral as

  $$\int \tan^m x \sec^n x \, dx = \int \tan^{m-1} x \sec^{n-1} x \sec x \tan x \, dx$$

  and express $\tan^{m-1} x$ in terms of $\sec x$ by using the trigonometric identity $\tan^2 x = \sec^2 x - 1$. Make the substitution

  $$u = \sec x, \quad du = \sec x \tan x \, dx$$

  and evaluate the resulting integral.
  2. If $n$ is an even integer: Write the integral as

  $$\int \tan^m x \sec^n x \, dx = \int \tan^m x \sec^{n-2} x \sec^2 x \, dx$$

  and express $\sec^{n-2} x$ in terms of $\tan x$ by using the trigonometric identity $\sec^2 x = 1 + \tan^2 x$. Make the substitution

  $$u = \tan x, \quad du = \sec^2 x \, dx$$

  and evaluate the resulting integral.
  3. If $m$ is even and $n$ is odd: There is no standard method of evaluation. Possibly use integration by parts.

---

## Concepts

In this section, we examine integrals of functions that are products of powers of the trigonometric functions. In particular, we consider integrals of the form

$$\int \sin^m x \cos^n x \, dx,$$

where $m$ and $n$ are integers. In Example 7 of Section 7.1, we obtained a reduction formula for $\int \sin^n x \, dx$. Integrals of this type may also be found without using integration by parts. If $n$ is an odd positive integer, we begin by writing

$$\int \sin^n x \, dx = \int \sin^{n-1} x \sin x \, dx.$$

Since the integer $n - 1$ is even, we may then use the trigonometric identity $\sin^2 x = 1 - \cos^2 x$ to obtain a form that is easy to integrate.

Similarly, for odd powers of $\cos x$, we write

$$\int \cos^n x \, dx = \int \cos^{n-1} x \cos x \, dx$$

and use the fact that $\cos^2 x = 1 - \sin^2 x$ to obtain an integrable form.

If the integrand is $\sin^n x$ or $\cos^n x$ and $n$ is even, then the half-angle formula

$$\sin^2 x = \frac{1 - \cos 2x}{2} \qquad \text{or} \qquad \cos^2 x = \frac{1 + \cos 2x}{2}$$

may be used to simplify the integrand.

Integrals involving only products of $\sin x$ and $\cos x$ may be evaluated using the guidelines (7.2).

The following guidelines (7.3) are analogous to those in (7.2) for integrands of the form $\tan^m x \sec^n x$.

Integrals of the form $\int \cot^m x \csc^n x \, dx$ may be evaluated in similar fashion.

Finally, if an integrand has one of the forms $\cos mx \cos nx$, $\sin mx \sin nx$, or $\sin mx \cos nx$, we use a product-to-sum formula to help evaluate the integral.

---

## Examples

### Example 1

#### Problem

Evaluate $\displaystyle\int \sin^5 x \, dx$.

#### Solution

As in the preceding discussion, we write

$$\int \sin^5 x \, dx = \int \sin^4 x \sin x \, dx$$

$$= \int (\sin^2 x)^2 \sin x \, dx$$

$$= \int (1 - \cos^2 x)^2 \sin x \, dx$$

$$= \int (1 - 2\cos^2 x + \cos^4 x) \sin x \, dx.$$

If we substitute

$$u = \cos x, \qquad du = -\sin x \, dx,$$

we obtain

$$\int \sin^5 x \, dx = -\int (1 - 2\cos^2 x + \cos^4 x)(-\sin x) \, dx$$

$$= -\int (1 - 2u^2 + u^4) \, du$$

$$= -u + \tfrac{2}{3}u^3 - \tfrac{1}{5}u^5 + C$$

$$= -\cos x + \tfrac{2}{3}\cos^3 x - \tfrac{1}{5}\cos^5 x + C.$$

---

### Example 2

#### Problem

Evaluate $\displaystyle\int \cos^2 x \, dx$.

#### Solution

Using a half-angle formula, we have

$$\int \cos^2 x \, dx = \tfrac{1}{2}\int (1 + \cos 2x) \, dx$$

$$= \tfrac{1}{2}x + \tfrac{1}{4}\sin 2x + C.$$

---

### Example 3

#### Problem

Evaluate $\displaystyle\int \sin^4 x \, dx$.

#### Solution

$$\int \sin^4 x \, dx = \int (\sin^2 x)^2 \, dx$$

$$= \int \left(\frac{1 - \cos 2x}{2}\right)^2 dx$$

$$= \tfrac{1}{4}\int (1 - 2\cos 2x + \cos^2 2x) \, dx$$

We apply a half-angle formula again and write

$$\cos^2 2x = \tfrac{1}{2}(1 + \cos 4x) = \tfrac{1}{2} + \tfrac{1}{2}\cos 4x.$$

Substituting in the last integral and simplifying gives us

$$\int \sin^4 x \, dx = \tfrac{1}{4}\int \left(\tfrac{3}{2} - 2\cos 2x + \tfrac{1}{2}\cos 4x\right) dx$$

$$= \tfrac{3}{8}x - \tfrac{1}{4}\sin 2x + \tfrac{1}{32}\sin 4x + C.$$

---

### Example 4

#### Problem

Evaluate $\displaystyle\int \cos^3 x \sin^4 x \, dx$.

#### Solution

By guideline (2) of (7.2),

$$\int \cos^3 x \sin^4 x \, dx = \int \cos^2 x \sin^4 x \cos x \, dx$$

$$= \int (1 - \sin^2 x)\sin^4 x \cos x \, dx.$$

If we let $u = \sin x$, then $du = \cos x \, dx$, and the integral may be written

$$\int \cos^3 x \sin^4 x \, dx = \int (1 - u^2)u^4 \, du = \int (u^4 - u^6) \, du$$

$$= \tfrac{1}{5}u^5 - \tfrac{1}{7}u^7 + C$$

$$= \tfrac{1}{5}\sin^5 x - \tfrac{1}{7}\sin^7 x + C.$$

---

### Example 5

#### Problem

Evaluate $\displaystyle\int \tan^3 x \sec^5 x \, dx$.

#### Solution

By guideline (1) of (7.3),

$$\int \tan^3 x \sec^5 x \, dx = \int \tan^2 x \sec^4 x (\sec x \tan x) \, dx$$

$$= \int (\sec^2 x - 1)\sec^4 x (\sec x \tan x) \, dx.$$

Substituting $u = \sec x$ and $du = \sec x \tan x \, dx$, we obtain

$$\int \tan^3 x \sec^5 x \, dx = \int (u^2 - 1)u^4 \, du$$

$$= \int (u^6 - u^4) \, du$$

$$= \tfrac{1}{7}u^7 - \tfrac{1}{5}u^5 + C$$

$$= \tfrac{1}{7}\sec^7 x - \tfrac{1}{5}\sec^5 x + C.$$

---

### Example 6

#### Problem

Evaluate $\displaystyle\int \tan^2 x \sec^4 x \, dx$.

#### Solution

By guideline (2) of (7.3),

$$\int \tan^2 x \sec^4 x \, dx = \int \tan^2 x \sec^2 x \sec^2 x \, dx$$

$$= \int \tan^2 x (\tan^2 x + 1)\sec^2 x \, dx.$$

If we let $u = \tan x$, then $du = \sec^2 x \, dx$, and

$$\int \tan^2 x \sec^4 x \, dx = \int u^2(u^2 + 1) \, du$$

$$= \int (u^4 + u^2) \, du$$

$$= \tfrac{1}{5}\tan^5 x + \tfrac{1}{3}\tan^3 x + C.$$

---

### Example 7

#### Problem

Evaluate $\displaystyle\int \cos 5x \cos 3x \, dx$.

#### Solution

Using the product-to-sum formula for $\cos u \cos v$, we obtain

$$\int \cos 5x \cos 3x \, dx = \int \tfrac{1}{2}(\cos 8x + \cos 2x) \, dx$$

$$= \tfrac{1}{16}\sin 8x + \tfrac{1}{4}\sin 2x + C.$$

---

## Remarks

- Integrals of the form $\int \cot^m x \csc^n x \, dx$ may be evaluated in similar fashion to $\int \tan^m x \sec^n x \, dx$.

- If an integrand has one of the forms $\cos mx \cos nx$, $\sin mx \sin nx$, or $\sin mx \cos nx$, a product-to-sum formula should be used to help evaluate the integral.

---

## Figures

No figures, graphs, or diagrams appear in this section.

---

## Keywords

- Trigonometric integrals
- Half-angle formula
- Product-to-sum formula
- Powers of sine and cosine
- Powers of tangent and secant
- Trigonometric identity
- Substitution
- Reduction formula
