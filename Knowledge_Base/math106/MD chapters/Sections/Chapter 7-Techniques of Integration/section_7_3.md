# section_7_3.md

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

---

## Metadata

- **Course:** MATH106
- **Book:** Calculus (Swokowski)
- **Edition:** 6th
- **Chapter Number:** 7
- **Chapter Title:** Techniques of Integration
- **Section Number:** 7.3
- **Section Title:** Trigonometric Substitutions

---

## Definitions

No formal boxed definitions are introduced in this section.

---

## Theorems

No formally numbered theorems are introduced in this section.

---

## Formulas

- **Trigonometric Substitutions (7.4):**

| Expression in integrand | Trigonometric substitution |
| ----------------------- | -------------------------- |
| $\sqrt{a^2 - x^2}$      | $x = a\sin\theta$          |
| $\sqrt{a^2 + x^2}$      | $x = a\tan\theta$          |
| $\sqrt{x^2 - a^2}$      | $x = a\sec\theta$          |

- **Substitution $x = a\sin\theta$:**

$$\sqrt{a^2 - x^2} = \sqrt{a^2 - a^2\sin^2\theta} = \sqrt{a^2(1 - \sin^2\theta)} = \sqrt{a^2\cos^2\theta} = a\cos\theta$$

- **Substitution $x = a\tan\theta$:**

$$\sqrt{a^2 + x^2} = \sqrt{a^2 + a^2\tan^2\theta} = \sqrt{a^2(1 + \tan^2\theta)} = \sqrt{a^2\sec^2\theta} = a\sec\theta$$

- **Substitution $x = a\sec\theta$:**

$$\sqrt{x^2 - a^2} = \sqrt{a^2\sec^2\theta - a^2} = \sqrt{a^2(\sec^2\theta - 1)} = \sqrt{a^2\tan^2\theta} = a\tan\theta$$

---

## Concepts

In Example 4 on p. 42, we saw how to change an expression of the form $\sqrt{a^2 - x^2}$, with $a > 0$, into a trigonometric expression without radicals, by using the trigonometric substitution $x = a\sin\theta$. We can use a similar procedure for $\sqrt{a^2 + x^2}$ and $\sqrt{x^2 - a^2}$. This technique is useful for eliminating radicals from certain types of integrands. The substitutions are listed in table (7.4).

When making a trigonometric substitution, we shall assume that $\theta$ is in the range of the corresponding inverse trigonometric function. Thus, for the substitution $x = a\sin\theta$, we have $-\pi/2 \leq \theta \leq \pi/2$. In this case, $\cos\theta \geq 0$ and

$$\sqrt{a^2 - x^2} = a\cos\theta.$$

If $\sqrt{a^2 - x^2}$ occurs in a denominator, we add the restriction $|x| \neq a$, or, equivalently, $-\pi/2 < \theta < \pi/2$.

If an integrand contains $\sqrt{a^2 + x^2}$ for $a > 0$, then, by (7.4), we use the substitution $x = a\tan\theta$ to eliminate the radical. When using this substitution, we assume that $\theta$ is in the range of the inverse tangent function—that is, $-\pi/2 < \theta < \pi/2$. In this case, $\sec\theta > 0$ and

$$\sqrt{a^2 + x^2} = a\sec\theta.$$

After substituting and evaluating the resulting trigonometric integral, it is necessary to return to the variable $x$. We can do so by using the formula $\tan\theta = x/a$ and referring to the right triangle shown in Figure 7.2.

If an integrand contains $\sqrt{x^2 - a^2}$, then using (7.4) we substitute $x = a\sec\theta$, where $\theta$ is chosen in the range of the inverse secant function—that is, either $0 \leq \theta < \pi/2$ or $\pi \leq \theta < 3\pi/2$. In this case, $\tan\theta \geq 0$ and

$$\sqrt{x^2 - a^2} = a\tan\theta.$$

Since $\sec\theta = x/a$, we may refer to the triangle in Figure 7.4 when changing from the variable $\theta$ to the variable $x$.

Trigonometric substitutions may also be used with trigonometric identities in the evaluation of definite integrals.

As shown in Example 4, we can use trigonometric substitutions to evaluate certain integrals that involve $(a^2 - x^2)^r$, $(a^2 + x^2)^r$, or $(x^2 - a^2)^r$, in cases other than $r = \frac{1}{2}$.

Although we now have additional integration techniques available, it is a good idea to keep earlier methods in mind. For example, the integral $\int (x/\sqrt{9 + x^2}) \, dx$ could be evaluated by means of the trigonometric substitution $x = 3\tan\theta$. However, it is simpler to use the algebraic substitution $u = 9 + x^2$ and $du = 2x \, dx$, for in this event the integral takes on the form $\frac{1}{2}\int u^{-1/2} \, du$, which is readily integrated by means of the power rule. The following exercises include integrals that can be evaluated using simpler techniques than trigonometric substitutions.

---

## Examples

### Example 1

#### Problem

Evaluate $\displaystyle\int \frac{1}{x^2\sqrt{16 - x^2}} \, dx$.

#### Solution

The integrand contains $\sqrt{16 - x^2}$, which is of the form $\sqrt{a^2 - x^2}$ with $a = 4$. Hence, by (7.4), we let

$$x = 4\sin\theta \qquad \text{for} \quad -\pi/2 < \theta < \pi/2.$$

It follows that

$$\sqrt{16 - x^2} = \sqrt{16 - 16\sin^2\theta} = 4\sqrt{1 - \sin^2\theta} = 4\sqrt{\cos^2\theta} = 4\cos\theta.$$

Since $x = 4\sin\theta$, we have $dx = 4\cos\theta \, d\theta$. Substituting in the given integral yields

$$\int \frac{1}{x^2\sqrt{16 - x^2}} \, dx = \int \frac{1}{(16\sin^2\theta)\,4\cos\theta} \cdot 4\cos\theta \, d\theta$$

$$= \frac{1}{16}\int \frac{1}{\sin^2\theta} \, d\theta$$

$$= \frac{1}{16}\int \csc^2\theta \, d\theta$$

$$= -\frac{1}{16}\cot\theta + C.$$

We must now return to the original variable of integration, $x$. Since $\theta = \arcsin(x/4)$, we could write $-\frac{1}{16}\cot\theta$ as $-\frac{1}{16}\cot\arcsin(x/4)$, but this is a cumbersome expression. Since the integrand contains $\sqrt{16 - x^2}$, it is preferable that the evaluated form also contain this radical. There is a simple geometric method for ensuring that it does. If $0 < \theta < \pi/2$ and $\sin\theta = x/4$, we may interpret $\theta$ as an acute angle of a right triangle having opposite side and hypotenuse of lengths $x$ and $4$, respectively (see Figure 7.1). By the Pythagorean theorem, the length of the adjacent side is $\sqrt{16 - x^2}$. Referring to the triangle, we find

$$\cot\theta = \frac{\sqrt{16 - x^2}}{x}.$$

It can be shown that the last formula is also true if $-\pi/2 < \theta < 0$. Thus, Figure 7.1 may be used if $\theta$ is either positive or negative.

Substituting $\sqrt{16 - x^2}/x$ for $\cot\theta$ in our integral evaluation gives us

$$\int \frac{1}{x^2\sqrt{16 - x^2}} \, dx = -\frac{1}{16}\cdot\frac{\sqrt{16 - x^2}}{x} + C$$

$$= -\frac{\sqrt{16 - x^2}}{16x} + C.$$

---

### Example 2

#### Problem

Evaluate $\displaystyle\int \frac{1}{\sqrt{4 + x^2}} \, dx$.

#### Solution

The denominator of the integrand has the form $\sqrt{a^2 + x^2}$ with $a = 2$. Hence, by (7.4), we make the substitution

$$x = 2\tan\theta, \qquad dx = 2\sec^2\theta \, d\theta.$$

Consequently,

$$\sqrt{4 + x^2} = \sqrt{4 + 4\tan^2\theta} = 2\sqrt{1 + \tan^2\theta} = 2\sqrt{\sec^2\theta} = 2\sec\theta$$

and

$$\int \frac{1}{\sqrt{4 + x^2}} \, dx = \int \frac{1}{2\sec\theta} \cdot 2\sec^2\theta \, d\theta$$

$$= \int \sec\theta \, d\theta$$

$$= \ln|\sec\theta + \tan\theta| + C.$$

Using $\tan\theta = x/2$, we sketch the triangle in Figure 7.3, from which we obtain

$$\sec\theta = \frac{\sqrt{4 + x^2}}{2}.$$

Hence,

$$\int \frac{1}{\sqrt{4 + x^2}} \, dx = \ln\left|\frac{\sqrt{4 + x^2}}{2} + \frac{x}{2}\right| + C.$$

The expression on the right may be written

$$\ln\left|\frac{\sqrt{4 + x^2} + x}{2}\right| + C = \ln\left|\sqrt{4 + x^2} + x\right| - \ln 2 + C.$$

Since $\sqrt{4 + x^2} + x > 0$ for every $x$, the absolute value sign is unnecessary. If we also let $D = -\ln 2 + C$, then

$$\int \frac{1}{\sqrt{4 + x^2}} \, dx = \ln\left(\sqrt{4 + x^2} + x\right) + D.$$

---

### Example 3

#### Problem

Evaluate $\displaystyle\int \frac{\sqrt{x^2 - 9}}{x} \, dx$.

#### Solution

The integrand contains $\sqrt{x^2 - 9}$, which is of the form $\sqrt{x^2 - a^2}$ with $a = 3$. Referring to (7.4), we substitute as follows:

$$x = 3\sec\theta, \qquad dx = 3\sec\theta\tan\theta \, d\theta$$

Consequently,

$$\sqrt{x^2 - 9} = \sqrt{9\sec^2\theta - 9} = 3\sqrt{\sec^2\theta - 1} = 3\sqrt{\tan^2\theta} = 3\tan\theta$$

and

$$\int \frac{\sqrt{x^2 - 9}}{x} \, dx = \int \frac{3\tan\theta}{3\sec\theta} \cdot 3\sec\theta\tan\theta \, d\theta$$

$$= 3\int \tan^2\theta \, d\theta$$

$$= 3\int (\sec^2\theta - 1) \, d\theta = 3\int \sec^2\theta \, d\theta - 3\int d\theta$$

$$= 3\tan\theta - 3\theta + C.$$

Since $\sec\theta = x/3$, we may refer to the right triangle in Figure 7.5. Using $\tan\theta = \sqrt{x^2 - 9}/3$ and $\theta = \sec^{-1}(x/3)$, we obtain

$$\int \frac{\sqrt{x^2 - 9}}{x} \, dx = 3\cdot\frac{\sqrt{x^2 - 9}}{3} - 3\sec^{-1}\left(\frac{x}{3}\right) + C$$

$$= \sqrt{x^2 - 9} - 3\sec^{-1}\left(\frac{x}{3}\right) + C.$$

---

### Example 4

#### Problem

Evaluate $\displaystyle\int \frac{(1 - x^2)^{3/2}}{x^6} \, dx$.

#### Solution

The integrand contains the expression $1 - x^2$, which is of the form $a^2 - x^2$ with $a = 1$. Using (7.4), we substitute

$$x = \sin\theta, \qquad dx = \cos\theta \, d\theta.$$

Thus, $1 - x^2 = 1 - \sin^2\theta = \cos^2\theta$, and

$$\int \frac{(1 - x^2)^{3/2}}{x^6} \, dx = \int \frac{(\cos^2\theta)^{3/2}}{\sin^6\theta}\cos\theta \, d\theta$$

$$= \int \frac{\cos^4\theta}{\sin^6\theta} \, d\theta = \int \frac{\cos^4\theta}{\sin^4\theta}\cdot\frac{1}{\sin^2\theta} \, d\theta$$

$$= \int \cot^4\theta\csc^2\theta \, d\theta$$

$$= -\tfrac{1}{5}\cot^5\theta + C.$$

To return to the variable $x$, we note that $\sin\theta = x = x/1$ and refer to the right triangle in Figure 7.6, obtaining $\cot\theta = \sqrt{1 - x^2}/x$. Hence,

$$\int \frac{(1 - x^2)^{3/2}}{x^6} \, dx = -\frac{1}{5}\left(\frac{\sqrt{1 - x^2}}{x}\right)^5 + C = -\frac{(1 - x^2)^{5/2}}{5x^5} + C.$$

---

### Example 5

#### Problem

Find the area of the region bounded by an ellipse whose major and minor axes have lengths $2a$ and $2b$, respectively.

#### Solution

By Theorem 34 (page 70), we see that an equation for the ellipse is $(x^2/a^2) + (y^2/b^2) = 1$. Solving for $y$ gives us

$$y = \pm\frac{b}{a}\sqrt{a^2 - x^2}.$$

The graph of the ellipse has the general shape shown in Figure 64 (page 69) and hence, by symmetry, it is sufficient to find the area of the region in the first quadrant and multiply the result by 4. By Theorem (4.19),

$$A = 4\int_0^a y \, dx = 4\frac{b}{a}\int_0^a \sqrt{a^2 - x^2} \, dx.$$

If we make the trigonometric substitution $x = a\sin\theta$, then

$$\sqrt{a^2 - x^2} = a\cos\theta \qquad \text{and} \qquad dx = a\cos\theta \, d\theta.$$

Since the values of $\theta$ that correspond to $x = 0$ and $x = a$ are $\theta = 0$ and $\theta = \pi/2$, respectively, we obtain

$$A = 4\frac{b}{a}\int_0^{\pi/2} a^2\cos^2\theta \, d\theta = 4ab\int_0^{\pi/2} \frac{1 + \cos 2\theta}{2} \, d\theta$$

$$= 2ab\left[\theta + \tfrac{1}{2}\sin 2\theta\right]_0^{\pi/2}$$

$$= 2ab\left[\frac{\pi}{2}\right] = \pi ab.$$

Thus, the area of an ellipse with axes of lengths $2a$ and $2b$ is $\pi ab$. As a special case, if $b = a$, the ellipse is a circle and $A = \pi a^2$.

---

## Remarks

- When using the substitution $x = a\sin\theta$, we assume $-\pi/2 \leq \theta \leq \pi/2$, so that $\cos\theta \geq 0$.

- When using the substitution $x = a\tan\theta$, we assume $-\pi/2 < \theta < \pi/2$, so that $\sec\theta > 0$.

- When using the substitution $x = a\sec\theta$, we choose $\theta$ in the range of the inverse secant function—that is, either $0 \leq \theta < \pi/2$ or $\pi \leq \theta < 3\pi/2$—so that $\tan\theta \geq 0$.

- If $\sqrt{a^2 - x^2}$ occurs in a denominator, we add the restriction $|x| \neq a$, or equivalently $-\pi/2 < \theta < \pi/2$.

- To return to the original variable $x$ after evaluating a trigonometric integral, we use a reference right triangle constructed from the substitution to express trigonometric functions of $\theta$ in terms of $x$.

- Although trigonometric substitutions are powerful, it is a good idea to keep earlier methods in mind. For example, the integral $\int (x/\sqrt{9 + x^2}) \, dx$ could be evaluated by means of the trigonometric substitution $x = 3\tan\theta$. However, it is simpler to use the algebraic substitution $u = 9 + x^2$ and $du = 2x \, dx$, for in this event the integral takes on the form $\frac{1}{2}\int u^{-1/2} \, du$, which is readily integrated by means of the power rule.

- Trigonometric substitutions can be used to evaluate integrals involving $(a^2 - x^2)^r$, $(a^2 + x^2)^r$, or $(x^2 - a^2)^r$ in cases other than $r = \frac{1}{2}$.

---

## Figures

### Figure 7.1

A right triangle with angle $\theta$, opposite side $x$, hypotenuse $4$, and adjacent side $\sqrt{16 - x^2}$. The relation $\sin\theta = \frac{x}{4}$ is labeled.

### Figure 7.2

A right triangle with angle $\theta$, opposite side $x$, adjacent side $a$, and hypotenuse $\sqrt{a^2 + x^2}$. The relation $\tan\theta = \frac{x}{a}$ is labeled.

### Figure 7.3

A right triangle with angle $\theta$, opposite side $x$, adjacent side $2$, and hypotenuse $\sqrt{4 + x^2}$. The relation $\tan\theta = \frac{x}{2}$ is labeled.

### Figure 7.4

A right triangle with angle $\theta$, hypotenuse $x$, adjacent side $a$, and opposite side $\sqrt{x^2 - a^2}$. The relation $\sec\theta = \frac{x}{a}$ is labeled.

### Figure 7.5

A right triangle with angle $\theta$, hypotenuse $x$, adjacent side $3$, and opposite side $\sqrt{x^2 - 9}$. The relation $\sec\theta = \frac{x}{3}$ is labeled.

### Figure 7.6

A right triangle with angle $\theta$, hypotenuse $1$, opposite side $x$, and adjacent side $\sqrt{1 - x^2}$. The relation $\sin\theta = x$ is labeled.

---

## Keywords

- Trigonometric substitution
- Radical elimination
- Inverse trigonometric function
- Right triangle
- Pythagorean theorem
- Definite integral
- Ellipse
- Area
- Reference triangle
