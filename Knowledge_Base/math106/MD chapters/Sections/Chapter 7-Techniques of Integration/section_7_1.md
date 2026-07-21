---
course: MATH106
book_chapter: 7
book_section: 7.1
ksu_chapter: 3
section_title: Integration by Parts
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: [1, 2, 7, 11, 12, 13, 16, 17, 31]
topic_tags: [integration-by-parts, reduction-formula, product-rule]
difficulty: UNKNOWN
in_syllabus: true
enrichment: UNKNOWN
status: draft
---

# Integration by Parts

## Metadata
**Course:** MATH106
**Book:** Calculus (Swokowski)
**Edition:** 6th
**Chapter Number:** 7
**Chapter Title:** Techniques of Integration
**Section Number:** 7.1
**Section Title:** Integration by Parts

## Definitions
No formal boxed definitions are introduced in this section.

## Theorems
**Integration by Parts Formula (7.1)**
If $u = f(x)$ and $v = g(x)$ and if $f'$ and $g'$ are continuous, then
$$\int u \, dv = uv - \int v \, du.$$

**Proof of Formula (7.1)**
By the product rule,
$$\frac{d}{dx}(f(x)g(x)) = f(x)g'(x) + g(x)f'(x),$$
or, equivalently,
$$f(x)g'(x) = \frac{d}{dx}(f(x)g(x)) - g(x)f'(x).$$
Integrating both sides gives us
$$\int f(x)g'(x) \, dx = \int \frac{d}{dx}(f(x)g(x)) \, dx - \int g(x)f'(x) \, dx.$$
By Theorem (4.5)(i), the first integral on the right side is $f(x)g(x) + C$. Because another constant of integration is obtained from the second integral, we may omit $C$:
$$\int f(x)g'(x) \, dx = f(x)g(x) - \int g(x)f'(x) \, dx.$$
Since $dv = g'(x) \, dx$ and $du = f'(x) \, dx$, we may write the preceding formula as in (7.1). $\blacksquare$

## Formulas
(1) $\int u \, dv = uv - \int v \, du$
(2) Reduction Formula for $\int \sin^n x \, dx$: $\int \sin^n x \, dx = -\frac{1}{n}\cos x \sin^{n-1} x + \frac{n-1}{n}\int \sin^{n-2} x \, dx$

## Guidelines / Methods
When applying Formula (7.1), begin by letting one part of the integrand correspond to $dv$. The expression chosen for $dv$ must include the differential $dx$. After selecting $dv$, designate the remaining part of the integrand by $u$ and then find $du$. A proper choice for $dv$ is crucial: generally let $dv$ equal the most complicated part of the integrand that can be readily integrated.

Sometimes it is necessary to use integration by parts more than once in the same problem. Integration by parts may also be employed to obtain reduction formulas, which write an integral involving powers of an expression in terms of integrals involving lower powers.

## Worked Examples
### Example 1
Evaluate $\int x e^{2x} \, dx$.
**Solution**
The following list contains all possible choices for $dv$:
$$dx, \quad x \, dx, \quad e^{2x} \, dx, \quad xe^{2x} \, dx$$
The most complicated of these expressions that can be readily integrated is $e^{2x} \, dx$. Thus, we let $dv = e^{2x} \, dx$ and $u = x$. Integrating $dv$ gives $v = \frac{1}{2}e^{2x}$, and $du = dx$. For ease of reference:
$$dv = e^{2x} \, dx \qquad u = x$$
$$v = \tfrac{1}{2}e^{2x} \qquad du = dx$$
Substituting in Formula (7.1):
$$\int xe^{2x} \, dx = x\left(\tfrac{1}{2}e^{2x}\right) - \int \tfrac{1}{2}e^{2x} \, dx = \tfrac{1}{2}xe^{2x} - \tfrac{1}{4}e^{2x} + C.$$

If we had chosen $dv = x \, dx$ instead, then $u = e^{2x}$, $v = \tfrac{1}{2}x^2$, $du = 2e^{2x} \, dx$, giving
$$\int xe^{2x} \, dx = \tfrac{1}{2}x^2 e^{2x} - \int x^2 e^{2x} \, dx.$$
The exponent associated with $x$ has increased, so the integral on the right is more complicated than the given integral — an incorrect choice for $dv$.

### Example 2
Evaluate (a) $\int x \sec^2 x \, dx$ and (b) $\int_0^{\pi/3} x \sec^2 x \, dx$.
**Solution**
(a) The most complicated of the possible choices for $dv$ that can be readily integrated is $\sec^2 x \, dx$. Let
$$dv = \sec^2 x \, dx \qquad u = x$$
$$v = \tan x \qquad du = dx.$$
Integrating by parts:
$$\int x \sec^2 x \, dx = x \tan x - \int \tan x \, dx = x \tan x + \ln|\cos x| + C.$$
(b) Using the antiderivative from (a):
$$\int_0^{\pi/3} x \sec^2 x \, dx = \Big[x \tan x + \ln|\cos x|\Big]_0^{\pi/3}$$
$$= \left(\frac{\pi}{3}\sqrt{3} + \ln\frac{1}{2}\right) - (0 + 0) = \frac{\pi}{3}\sqrt{3} - \ln 2 \approx 1.12.$$

### Example 3
Evaluate $\int \ln x \, dx$.
**Solution**
Let $dv = dx$, $u = \ln x$; then $v = x$, $du = \frac{1}{x} \, dx$. Integrating by parts:
$$\int \ln x \, dx = (\ln x)x - \int (x)\frac{1}{x} \, dx = x \ln x - \int dx = x \ln x - x + C.$$

### Example 4
Evaluate $\int x^2 e^{2x} \, dx$.
**Solution**
Let $dv = e^{2x} \, dx$, $u = x^2$; then $v = \tfrac{1}{2}e^{2x}$, $du = 2x \, dx$. Integrating by parts:
$$\int x^2 e^{2x} \, dx = \tfrac{1}{2}x^2 e^{2x} - \int xe^{2x} \, dx.$$
Applying Example 1 to the remaining integral:
$$\int x^2 e^{2x} \, dx = \tfrac{1}{2}x^2 e^{2x} - \tfrac{1}{2}xe^{2x} + \tfrac{1}{4}e^{2x} + C.$$

### Example 5
Evaluate $\int e^x \cos x \, dx$.
**Solution**
Let $dv = \cos x \, dx$, $u = e^x$; then $v = \sin x$, $du = e^x \, dx$. Integrating by parts:
$$(1) \qquad \int e^x \cos x \, dx = e^x \sin x - \int e^x \sin x \, dx.$$
Apply integration by parts again with a trigonometric $dv$ (consistent with the first choice). Let $dv = \sin x \, dx$, $u = e^x$; then $v = -\cos x$, $du = e^x \, dx$:
$$(2) \qquad \int e^x \sin x \, dx = -e^x \cos x + \int e^x \cos x \, dx.$$
Substituting (2) into (1):
$$\int e^x \cos x \, dx = e^x \sin x + e^x \cos x - \int e^x \cos x \, dx.$$
Adding $\int e^x \cos x \, dx$ to both sides:
$$2\int e^x \cos x \, dx = e^x(\sin x + \cos x),$$
$$\int e^x \cos x \, dx = \tfrac{1}{2}e^x(\sin x + \cos x) + C.$$

Warning: If for the second application of parts we had instead used $dv = e^x \, dx$, $u = \sin x$, we would arrive at the tautology $\int e^x \cos x \, dx = \int e^x \cos x \, dx$ — a true statement but not an evaluation. Be consistent with the trigonometric-form choice throughout.

### Example 6
Evaluate $\int \sec^3 x \, dx$.
**Solution**
Let $dv = \sec^2 x \, dx$, $u = \sec x$; then $v = \tan x$, $du = \sec x \tan x \, dx$:
$$\int \sec^3 x \, dx = \sec x \tan x - \int \sec x \tan^2 x \, dx.$$
Use $1 + \tan^2 x = \sec^2 x$:
$$\int \sec^3 x \, dx = \sec x \tan x - \int \sec^3 x \, dx + \int \sec x \, dx.$$
Adding $\int \sec^3 x \, dx$ to both sides:
$$2\int \sec^3 x \, dx = \sec x \tan x + \int \sec x \, dx,$$
$$\int \sec^3 x \, dx = \tfrac{1}{2}\sec x \tan x + \tfrac{1}{2}\ln|\sec x + \tan x| + C.$$

### Example 7
Find a reduction formula for $\int \sin^n x \, dx$.
**Solution**
Let $dv = \sin x \, dx$, $u = \sin^{n-1} x$; then $v = -\cos x$, $du = (n-1)\sin^{n-2} x \cos x \, dx$:
$$\int \sin^n x \, dx = -\cos x \sin^{n-1} x + (n-1)\int \sin^{n-2} x \cos^2 x \, dx.$$
Using $\cos^2 x = 1 - \sin^2 x$:
$$\int \sin^n x \, dx = -\cos x \sin^{n-1} x + (n-1)\int \sin^{n-2} x \, dx - (n-1)\int \sin^n x \, dx.$$
Combining $\sin^n x$ terms:
$$n\int \sin^n x \, dx = -\cos x \sin^{n-1} x + (n-1)\int \sin^{n-2} x \, dx,$$
$$\int \sin^n x \, dx = -\frac{1}{n}\cos x \sin^{n-1} x + \frac{n-1}{n}\int \sin^{n-2} x \, dx.$$

### Example 8
Use the reduction formula in Example 7 to evaluate $\int \sin^4 x \, dx$.
**Solution**
With $n = 4$:
$$\int \sin^4 x \, dx = -\tfrac{1}{4}\cos x \sin^3 x + \tfrac{3}{4}\int \sin^2 x \, dx.$$
Applying the reduction formula with $n = 2$:
$$\int \sin^2 x \, dx = -\tfrac{1}{2}\cos x \sin x + \tfrac{1}{2}x + C.$$
Consequently:
$$\int \sin^4 x \, dx = -\tfrac{1}{4}\cos x \sin^3 x - \tfrac{3}{8}\cos x \sin x + \tfrac{3}{8}x + D.$$

## Exercises
*   1. Evaluate the integral: $\int x e^{-x} \, dx$
*   2. Evaluate the integral: $\int x \sin x \, dx$
*   7. Evaluate the integral: $\int x \sec x \tan x \, dx$
*   11. Evaluate the integral: $\int \tan^{-1} x \, dx$
*   12. Evaluate the integral: $\int \sin^{-1} x \, dx$
*   13. Evaluate the integral: $\int \sqrt{x} \ln x \, dx$
*   16. Evaluate the integral: $\int x \tan^{-1} x \, dx$
*   17. Evaluate the integral: $\int e^{-x} \sin x \, dx$
*   31. Evaluate the integral: $\int (\ln x)^2 \, dx$