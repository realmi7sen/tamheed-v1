---
course: MATH106
book_chapter: 7
book_section: 7.3
ksu_chapter: 3
section_title: Trigonometric Substitutions
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: [1, 3, 5, 7, 9, 10, 21, 22]
topic_tags: [trigonometric-substitution, radical-elimination, inverse-trigonometric-function]
difficulty: UNKNOWN
in_syllabus: true
enrichment: UNKNOWN
status: draft
---

# Trigonometric Substitutions

## Metadata
**Course:** MATH106
**Book:** Calculus (Swokowski)
**Edition:** 6th
**Chapter Number:** 7
**Chapter Title:** Techniques of Integration
**Section Number:** 7.3
**Section Title:** Trigonometric Substitutions

## Definitions
No formal boxed definitions are introduced in this section.

## Theorems
No formally numbered theorems are introduced in this section.

## Formulas
**Trigonometric Substitutions (7.4):**
(1) For $\sqrt{a^2 - x^2}$: substitute $x = a\sin\theta$, giving $\sqrt{a^2 - x^2} = a\cos\theta$
(2) For $\sqrt{a^2 + x^2}$: substitute $x = a\tan\theta$, giving $\sqrt{a^2 + x^2} = a\sec\theta$
(3) For $\sqrt{x^2 - a^2}$: substitute $x = a\sec\theta$, giving $\sqrt{x^2 - a^2} = a\tan\theta$

## Guidelines / Methods
Trigonometric substitutions eliminate radicals from certain integrands. When making a trigonometric substitution, assume $\theta$ is in the range of the corresponding inverse trigonometric function:
- For $x = a\sin\theta$: $-\pi/2 \leq \theta \leq \pi/2$, so $\cos\theta \geq 0$. If the radical appears in a denominator, restrict to $-\pi/2 < \theta < \pi/2$.
- For $x = a\tan\theta$: $-\pi/2 < \theta < \pi/2$, so $\sec\theta > 0$.
- For $x = a\sec\theta$: $0 \leq \theta < \pi/2$ or $\pi \leq \theta < 3\pi/2$, so $\tan\theta \geq 0$.

After evaluating the trigonometric integral, return to the variable $x$ using a reference right triangle constructed from the substitution.

Trigonometric substitutions may also be used to evaluate integrals involving $(a^2 - x^2)^r$, $(a^2 + x^2)^r$, or $(x^2 - a^2)^r$ for values of $r$ other than $\frac{1}{2}$.

Keep earlier methods in mind: for example, $\int (x/\sqrt{9 + x^2}) \, dx$ could be evaluated by $x = 3\tan\theta$, but the algebraic substitution $u = 9 + x^2$, $du = 2x \, dx$ is simpler.

## Worked Examples
### Example 1
Evaluate $\int \frac{1}{x^2\sqrt{16 - x^2}} \, dx$.
**Solution**
The integrand contains $\sqrt{16 - x^2}$ (form $\sqrt{a^2 - x^2}$ with $a = 4$). Let $x = 4\sin\theta$, $-\pi/2 < \theta < \pi/2$. Then $\sqrt{16 - x^2} = 4\cos\theta$ and $dx = 4\cos\theta \, d\theta$:
$$\int \frac{1}{x^2\sqrt{16 - x^2}} \, dx = \int \frac{1}{(16\sin^2\theta)(4\cos\theta)} \cdot 4\cos\theta \, d\theta = \frac{1}{16}\int \csc^2\theta \, d\theta = -\frac{1}{16}\cot\theta + C.$$
Returning to $x$: from the reference right triangle (opposite $x$, hypotenuse $4$, adjacent $\sqrt{16 - x^2}$), $\cot\theta = \sqrt{16 - x^2}/x$. Therefore:
$$\int \frac{1}{x^2\sqrt{16 - x^2}} \, dx = -\frac{\sqrt{16 - x^2}}{16x} + C.$$

### Example 2
Evaluate $\int \frac{1}{\sqrt{4 + x^2}} \, dx$.
**Solution**
Form $\sqrt{a^2 + x^2}$ with $a = 2$. Let $x = 2\tan\theta$, $dx = 2\sec^2\theta \, d\theta$. Then $\sqrt{4 + x^2} = 2\sec\theta$:
$$\int \frac{1}{\sqrt{4 + x^2}} \, dx = \int \frac{2\sec^2\theta}{2\sec\theta} \, d\theta = \int \sec\theta \, d\theta = \ln|\sec\theta + \tan\theta| + C.$$
From the reference right triangle (opposite $x$, adjacent $2$, hypotenuse $\sqrt{4 + x^2}$), $\sec\theta = \sqrt{4 + x^2}/2$, $\tan\theta = x/2$:
$$\int \frac{1}{\sqrt{4 + x^2}} \, dx = \ln\left|\frac{\sqrt{4 + x^2} + x}{2}\right| + C = \ln\left(\sqrt{4 + x^2} + x\right) + D,$$
where $D = C - \ln 2$ and the absolute value is dropped since $\sqrt{4 + x^2} + x > 0$ for all $x$.

### Example 3
Evaluate $\int \frac{\sqrt{x^2 - 9}}{x} \, dx$.
**Solution**
Form $\sqrt{x^2 - a^2}$ with $a = 3$. Let $x = 3\sec\theta$, $dx = 3\sec\theta\tan\theta \, d\theta$. Then $\sqrt{x^2 - 9} = 3\tan\theta$:
$$\int \frac{\sqrt{x^2 - 9}}{x} \, dx = \int \frac{3\tan\theta}{3\sec\theta} \cdot 3\sec\theta\tan\theta \, d\theta = 3\int \tan^2\theta \, d\theta$$
$$= 3\int (\sec^2\theta - 1) \, d\theta = 3\tan\theta - 3\theta + C.$$
From the reference right triangle (hypotenuse $x$, adjacent $3$, opposite $\sqrt{x^2 - 9}$), $\tan\theta = \sqrt{x^2 - 9}/3$ and $\theta = \sec^{-1}(x/3)$:
$$\int \frac{\sqrt{x^2 - 9}}{x} \, dx = \sqrt{x^2 - 9} - 3\sec^{-1}\left(\frac{x}{3}\right) + C.$$

### Example 4
Evaluate $\int \frac{(1 - x^2)^{3/2}}{x^6} \, dx$.
**Solution**
Form $a^2 - x^2$ with $a = 1$. Let $x = \sin\theta$, $dx = \cos\theta \, d\theta$. Then $1 - x^2 = \cos^2\theta$:
$$\int \frac{(1 - x^2)^{3/2}}{x^6} \, dx = \int \frac{\cos^3\theta}{\sin^6\theta} \cos\theta \, d\theta = \int \cot^4\theta \csc^2\theta \, d\theta = -\tfrac{1}{5}\cot^5\theta + C.$$
From the reference right triangle (hypotenuse $1$, opposite $x$, adjacent $\sqrt{1 - x^2}$), $\cot\theta = \sqrt{1 - x^2}/x$:
$$\int \frac{(1 - x^2)^{3/2}}{x^6} \, dx = -\frac{(1 - x^2)^{5/2}}{5x^5} + C.$$

### Example 5
Find the area of the region bounded by an ellipse whose major and minor axes have lengths $2a$ and $2b$.
**Solution**
The ellipse has equation $(x^2/a^2) + (y^2/b^2) = 1$, giving $y = \pm(b/a)\sqrt{a^2 - x^2}$. By symmetry:
$$A = 4\int_0^a y \, dx = \frac{4b}{a}\int_0^a \sqrt{a^2 - x^2} \, dx.$$
Substitute $x = a\sin\theta$: $\sqrt{a^2 - x^2} = a\cos\theta$, $dx = a\cos\theta \, d\theta$. Limits: $x = 0 \to \theta = 0$; $x = a \to \theta = \pi/2$:
$$A = \frac{4b}{a}\int_0^{\pi/2} a^2\cos^2\theta \, d\theta = 4ab\int_0^{\pi/2} \frac{1 + \cos 2\theta}{2} \, d\theta = 2ab\left[\theta + \tfrac{1}{2}\sin 2\theta\right]_0^{\pi/2} = \pi ab.$$
Special case: if $b = a$, the ellipse is a circle and $A = \pi a^2$.

## Exercises
*   1. Evaluate the integral: $\int \frac{1}{x\sqrt{4 - x^2}} \, dx$
*   3. Evaluate the integral: $\int \frac{1}{x\sqrt{9 + x^2}} \, dx$
*   5. Evaluate the integral: $\int \frac{1}{x^2\sqrt{x^2 - 25}} \, dx$
*   7. Evaluate the integral: $\int \frac{x}{\sqrt{4 - x^2}} \, dx$
*   9. Evaluate the integral: $\int \frac{1}{(x^2 - 1)^{3/2}} \, dx$
*   10. Evaluate the integral: $\int \frac{1}{\sqrt{4x^2 - 25}} \, dx$
*   21. Evaluate the integral: $\int \frac{(4 + x^2)^2}{x^3} \, dx$
*   22. Evaluate the integral: $\int \frac{3x - 5}{\sqrt{1 - x^2}} \, dx$