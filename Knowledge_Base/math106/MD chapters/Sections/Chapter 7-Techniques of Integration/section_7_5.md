---
course: MATH106
book_chapter: 7
book_section: 7.5
ksu_chapter: 3
section_title: Quadratic Expressions and Miscellaneous Substitutions
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: [1, 3, 5, 6, 10, 12, 25, 26, 27, 28, 32, 47, 48, 49, 50]
topic_tags: [completing-the-square, miscellaneous-substitution, half-angle-substitution]
difficulty: UNKNOWN
in_syllabus: true
enrichment: UNKNOWN
status: draft
---

# Quadratic Expressions and Miscellaneous Substitutions

## Metadata
**Course:** MATH106
**Book:** Calculus (Swokowski)
**Edition:** 6th
**Chapter Number:** 7
**Chapter Title:** Techniques of Integration
**Section Number:** 7.5
**Section Title:** Quadratic Expressions and Miscellaneous Substitutions

## Definitions
No formal boxed definitions are introduced in this section.

## Theorems
**Theorem (7.6) — Weierstrass Half-Angle Substitution**
If the integrand is a rational expression in $\sin x$ and $\cos x$, the substitution $u = \tan(x/2)$ for $-\pi < x < \pi$ produces a rational expression in $u$ via:
$$\sin x = \frac{2u}{1 + u^2}, \qquad \cos x = \frac{1 - u^2}{1 + u^2}, \qquad dx = \frac{2}{1 + u^2} \, du.$$

## Formulas
(1) Completing the square: $ax^2 + bx + c = a\left(x + \frac{b}{2a}\right)^2 + c - \frac{b^2}{4a}$.
(2) Half-angle relations used in Theorem (7.6): $\cos(x/2) = 1/\sqrt{1+u^2}$, $\sin(x/2) = u/\sqrt{1+u^2}$, so $\sin x = 2u/(1+u^2)$ and $\cos x = (1-u^2)/(1+u^2)$.

## Guidelines / Methods
**Integrals involving quadratic expressions:** if the integrand contains an irreducible quadratic $ax^2 + bx + c$ with $b \neq 0$, complete the square as above, then substitute $u = x + b/(2a)$. This often leads to a standard form (either a rational integral or one requiring trigonometric substitution).

**Miscellaneous substitutions:**
- If the integrand contains $\sqrt[n]{f(x)}$, try either $u = \sqrt[n]{f(x)}$ or $u = f(x)$.
- If the integrand contains $x^{1/2}$ AND $x^{1/3}$ (or other mixed roots), use $u = x^{1/n}$ where $n$ is the LCM of the denominators.
- If the integrand is a rational expression in $\sin x$ and $\cos x$, Theorem (7.6) always works — but a simpler substitution (like $u = \sin x$ or $u = \cos x$) may be available.

## Worked Examples
### Example 1
Evaluate $\int \frac{2x - 1}{x^2 - 6x + 13} \, dx$.
**Solution**
$x^2 - 6x + 13$ is irreducible ($b^2 - 4ac = -16 < 0$). Complete the square: $x^2 - 6x + 13 = (x-3)^2 + 4$. Let $u = x - 3$, $dx = du$:
$$\int \frac{2(u+3) - 1}{u^2 + 4} \, du = \int \frac{2u}{u^2 + 4} \, du + 5\int \frac{1}{u^2 + 4} \, du = \ln(u^2 + 4) + \tfrac{5}{2}\tan^{-1}\tfrac{u}{2} + C.$$
Returning to $x$:
$$\int = \ln(x^2 - 6x + 13) + \tfrac{5}{2}\tan^{-1}\frac{x - 3}{2} + C.$$

### Example 2
Evaluate $\int \frac{1}{\sqrt{x^2 + 8x + 25}} \, dx$.
**Solution**
Complete the square: $x^2 + 8x + 25 = (x+4)^2 + 9$. Let $x + 4 = 3\tan\theta$, $dx = 3\sec^2\theta \, d\theta$; then $\sqrt{(x+4)^2 + 9} = 3\sec\theta$:
$$\int \frac{3\sec^2\theta}{3\sec\theta} \, d\theta = \int \sec\theta \, d\theta = \ln|\sec\theta + \tan\theta| + C.$$
From the reference triangle: $\sec\theta = \sqrt{(x+4)^2+9}/3$, $\tan\theta = (x+4)/3$:
$$\int = \ln\left|\sqrt{x^2 + 8x + 25} + x + 4\right| + K.$$

### Example 3
Evaluate $\int \frac{x^3}{\sqrt[3]{x^2 + 4}} \, dx$.
**Solution (using $u = \sqrt[3]{x^2 + 4}$)**
Then $u^3 = x^2 + 4$, so $x^2 = u^3 - 4$, and $2x \, dx = 3u^2 \, du \Rightarrow x \, dx = \tfrac{3}{2}u^2 \, du$:
$$\int \frac{x^2}{\sqrt[3]{x^2+4}} \cdot x \, dx = \int \frac{u^3 - 4}{u} \cdot \tfrac{3}{2}u^2 \, du = \tfrac{3}{2}\int (u^4 - 4u) \, du = \tfrac{3}{10}u^2(u^3 - 10) + C$$
$$= \tfrac{3}{10}(x^2 + 4)^{2/3}(x^2 - 6) + C.$$

### Example 4
Evaluate $\int \frac{1}{\sqrt{x} + \sqrt[3]{x}} \, dx$.
**Solution**
$\text{LCM}(2, 3) = 6$, so let $u = x^{1/6}$, i.e. $x = u^6$, $dx = 6u^5 \, du$, $\sqrt{x} = u^3$, $\sqrt[3]{x} = u^2$:
$$\int \frac{6u^5}{u^3 + u^2} \, du = 6\int \frac{u^3}{u + 1} \, du.$$
By long division: $\frac{u^3}{u+1} = u^2 - u + 1 - \frac{1}{u+1}$. Integrating:
$$= 6\left(\tfrac{1}{3}u^3 - \tfrac{1}{2}u^2 + u - \ln|u+1|\right) + C = 2\sqrt{x} - 3\sqrt[3]{x} + 6\sqrt[6]{x} - 6\ln(\sqrt[6]{x} + 1) + C.$$

### Example 5
Evaluate $\int \frac{1}{4\sin x - 3\cos x} \, dx$.
**Solution**
By Theorem (7.6):
$$\int \frac{1}{4\left(\frac{2u}{1+u^2}\right) - 3\left(\frac{1-u^2}{1+u^2}\right)} \cdot \frac{2}{1+u^2} \, du = 2\int \frac{1}{3u^2 + 8u - 3} \, du.$$
Partial fractions: $\frac{1}{3u^2 + 8u - 3} = \frac{1}{10}\left(\frac{3}{3u-1} - \frac{1}{u+3}\right)$:
$$= \tfrac{1}{5}\left(\ln|3u - 1| - \ln|u + 3|\right) + C = \tfrac{1}{5}\ln\left|\frac{3\tan(x/2) - 1}{\tan(x/2) + 3}\right| + C.$$

### Example 6
Evaluate $\int \frac{\cos x}{1 + \sin^2 x} \, dx$.
**Solution**
Theorem (7.6) would work, but a simpler substitution suffices. Let $u = \sin x$, $du = \cos x \, dx$:
$$\int \frac{1}{1 + u^2} \, du = \arctan u + C = \arctan(\sin x) + C.$$

## Exercises
*   1. Evaluate the integral: $\int \frac{1}{(x + 1)^2 + 4} \, dx$
*   3. Evaluate the integral: $\int \frac{1}{x^2 - 4x + 8} \, dx$
*   5. Evaluate the integral: $\int \frac{1}{\sqrt{4x - x^2}} \, dx$
*   6. Evaluate the integral: $\int \frac{1}{\sqrt{7 + 6x - x^2}} \, dx$
*   10. Evaluate the integral: $\int \frac{1}{(x^2 - 6x + 34)^{3/2}} \, dx$
*   12. Evaluate the integral: $\int \sqrt{x(6 - x)} \, dx$
*   25. Evaluate the integral: $\int_1^9 \frac{1}{\sqrt{x} + 4} \, dx$
*   26. Evaluate the integral: $\int_0^{25} \frac{1}{\sqrt{4 + \sqrt{x}}} \, dx$
*   27. Evaluate the integral: $\int \frac{\sqrt{x}}{1 + \sqrt{x}} \, dx$
*   28. Evaluate the integral: $\int \frac{1}{\sqrt{x} + \sqrt[3]{x}} \, dx$
*   32. Evaluate the integral: $\int \frac{x^{1/3} + 1}{x^{1/3} - 1} \, dx$
*   47. Use Theorem (7.6) to evaluate the integral: $\int \frac{1}{2 + \sin x} \, dx$
*   48. Use Theorem (7.6) to evaluate the integral: $\int \frac{1}{3 + 2\cos x} \, dx$
*   49. Use Theorem (7.6) to evaluate the integral: $\int \frac{1}{1 + \sin x + \cos x} \, dx$
*   50. Use Theorem (7.6) to evaluate the integral: $\int \frac{1}{\tan x + \sin x} \, dx$