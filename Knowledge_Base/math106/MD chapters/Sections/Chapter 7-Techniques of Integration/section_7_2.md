---
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

## Metadata
**Course:** MATH106
**Book:** Calculus (Swokowski)
**Edition:** 6th
**Chapter Number:** 7
**Chapter Title:** Techniques of Integration
**Section Number:** 7.2
**Section Title:** Trigonometric Integrals

## Definitions
No formal boxed definitions are introduced in this section.

## Theorems
No formally numbered theorems are introduced in this section.

## Formulas
(1) Half-angle formulas: $\sin^2 x = \frac{1 - \cos 2x}{2}$, $\cos^2 x = \frac{1 + \cos 2x}{2}$

## Guidelines / Methods
**Guidelines for Evaluating $\int \sin^m x \cos^n x \, dx$ (7.2):**
1. If $m$ is an odd integer: write $\int \sin^m x \cos^n x \, dx = \int \sin^{m-1} x \cos^n x \sin x \, dx$, express $\sin^{m-1} x$ in terms of $\cos x$ using $\sin^2 x = 1 - \cos^2 x$, and substitute $u = \cos x$, $du = -\sin x \, dx$.
2. If $n$ is an odd integer: write $\int \sin^m x \cos^n x \, dx = \int \sin^m x \cos^{n-1} x \cos x \, dx$, express $\cos^{n-1} x$ in terms of $\sin x$ using $\cos^2 x = 1 - \sin^2 x$, and substitute $u = \sin x$, $du = \cos x \, dx$.
3. If $m$ and $n$ are both even: use half-angle formulas for $\sin^2 x$ and $\cos^2 x$ to reduce the exponents.

**Guidelines for Evaluating $\int \tan^m x \sec^n x \, dx$ (7.3):**
1. If $m$ is odd: write $\int \tan^m x \sec^n x \, dx = \int \tan^{m-1} x \sec^{n-1} x \sec x \tan x \, dx$, express $\tan^{m-1} x$ using $\tan^2 x = \sec^2 x - 1$, and substitute $u = \sec x$, $du = \sec x \tan x \, dx$.
2. If $n$ is even: write $\int \tan^m x \sec^n x \, dx = \int \tan^m x \sec^{n-2} x \sec^2 x \, dx$, express $\sec^{n-2} x$ using $\sec^2 x = 1 + \tan^2 x$, and substitute $u = \tan x$, $du = \sec^2 x \, dx$.
3. If $m$ is even and $n$ is odd: no standard method — possibly use integration by parts.

For integrands of the form $\cos mx \cos nx$, $\sin mx \sin nx$, or $\sin mx \cos nx$, use a product-to-sum formula. Integrals of the form $\int \cot^m x \csc^n x \, dx$ may be evaluated similarly to $\int \tan^m x \sec^n x \, dx$.

## Worked Examples
### Example 1
Evaluate $\int \sin^5 x \, dx$.
**Solution**
$$\int \sin^5 x \, dx = \int \sin^4 x \sin x \, dx = \int (1 - \cos^2 x)^2 \sin x \, dx = \int (1 - 2\cos^2 x + \cos^4 x) \sin x \, dx.$$
Substituting $u = \cos x$, $du = -\sin x \, dx$:
$$= -\int (1 - 2u^2 + u^4) \, du = -u + \tfrac{2}{3}u^3 - \tfrac{1}{5}u^5 + C$$
$$= -\cos x + \tfrac{2}{3}\cos^3 x - \tfrac{1}{5}\cos^5 x + C.$$

### Example 2
Evaluate $\int \cos^2 x \, dx$.
**Solution**
Using the half-angle formula:
$$\int \cos^2 x \, dx = \tfrac{1}{2}\int (1 + \cos 2x) \, dx = \tfrac{1}{2}x + \tfrac{1}{4}\sin 2x + C.$$

### Example 3
Evaluate $\int \sin^4 x \, dx$.
**Solution**
$$\int \sin^4 x \, dx = \int \left(\frac{1 - \cos 2x}{2}\right)^2 dx = \tfrac{1}{4}\int (1 - 2\cos 2x + \cos^2 2x) \, dx.$$
Applying the half-angle formula to $\cos^2 2x = \tfrac{1}{2} + \tfrac{1}{2}\cos 4x$:
$$\int \sin^4 x \, dx = \tfrac{1}{4}\int \left(\tfrac{3}{2} - 2\cos 2x + \tfrac{1}{2}\cos 4x\right) dx = \tfrac{3}{8}x - \tfrac{1}{4}\sin 2x + \tfrac{1}{32}\sin 4x + C.$$

### Example 4
Evaluate $\int \cos^3 x \sin^4 x \, dx$.
**Solution**
By guideline (2) of (7.2):
$$\int \cos^3 x \sin^4 x \, dx = \int (1 - \sin^2 x)\sin^4 x \cos x \, dx.$$
Let $u = \sin x$, $du = \cos x \, dx$:
$$= \int (1 - u^2)u^4 \, du = \int (u^4 - u^6) \, du = \tfrac{1}{5}\sin^5 x - \tfrac{1}{7}\sin^7 x + C.$$

### Example 5
Evaluate $\int \tan^3 x \sec^5 x \, dx$.
**Solution**
By guideline (1) of (7.3):
$$\int \tan^3 x \sec^5 x \, dx = \int (\sec^2 x - 1)\sec^4 x (\sec x \tan x) \, dx.$$
Let $u = \sec x$, $du = \sec x \tan x \, dx$:
$$= \int (u^2 - 1)u^4 \, du = \int (u^6 - u^4) \, du = \tfrac{1}{7}\sec^7 x - \tfrac{1}{5}\sec^5 x + C.$$

### Example 6
Evaluate $\int \tan^2 x \sec^4 x \, dx$.
**Solution**
By guideline (2) of (7.3):
$$\int \tan^2 x \sec^4 x \, dx = \int \tan^2 x (\tan^2 x + 1)\sec^2 x \, dx.$$
Let $u = \tan x$, $du = \sec^2 x \, dx$:
$$= \int u^2(u^2 + 1) \, du = \tfrac{1}{5}\tan^5 x + \tfrac{1}{3}\tan^3 x + C.$$

### Example 7
Evaluate $\int \cos 5x \cos 3x \, dx$.
**Solution**
Using the product-to-sum formula:
$$\int \cos 5x \cos 3x \, dx = \tfrac{1}{2}\int (\cos 8x + \cos 2x) \, dx = \tfrac{1}{16}\sin 8x + \tfrac{1}{4}\sin 2x + C.$$

## Exercises
*   1. Evaluate the integral: $\int \cos^3 x \, dx$
*   3. Evaluate the integral: $\int \sin^2 x \cos^2 x \, dx$
*   4. Evaluate the integral: $\int \cos^7 x \, dx$
*   5. Evaluate the integral: $\int \sin^3 x \cos^2 x \, dx$
*   7. Evaluate the integral: $\int \sin^6 x \, dx$
*   9. Evaluate the integral: $\int \tan^3 x \sec^4 x \, dx$
*   11. Evaluate the integral: $\int \tan^3 x \sec^3 x \, dx$
*   13. Evaluate the integral: $\int \tan^6 x \, dx$
*   15. Evaluate the integral: $\int \sqrt{\sin x} \cos^3 x \, dx$