---
course: MATH106
book_chapter: 7
book_section: 7.4
ksu_chapter: 3
section_title: Integrals of Rational Functions
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: [1, 2, 5, 6, 9, 11, 25]
topic_tags: [rational-functions, partial-fraction-decomposition, irreducible-quadratic]
difficulty: UNKNOWN
in_syllabus: true
enrichment: UNKNOWN
status: draft
---

# Integrals of Rational Functions

## Metadata
**Course:** MATH106
**Book:** Calculus (Swokowski)
**Edition:** 6th
**Chapter Number:** 7
**Chapter Title:** Techniques of Integration
**Section Number:** 7.4
**Section Title:** Integrals of Rational Functions

## Definitions
A rational function is $q(x) = f(x)/g(x)$, where $f(x)$ and $g(x)$ are polynomials.

The expression $\frac{1}{x - 1} + \frac{-1}{x + 1} = \frac{2}{x^2 - 1}$ shows the **partial fraction decomposition** of $2/(x^2 - 1)$. In general, the sum $F_1 + F_2 + \cdots + F_r$ is called the partial fraction decomposition of $f(x)/g(x)$, and each $F_k$ is a partial fraction.

A quadratic $ax^2 + bx + c$ is **irreducible** if $b^2 - 4ac < 0$ — it cannot be factored into two real linear factors.

## Theorems
No formally numbered theorems are introduced in this section.

## Formulas
If $f(x)$ and $g(x)$ are polynomials with $\deg f < \deg g$, then
$$\frac{f(x)}{g(x)} = F_1 + F_2 + \cdots + F_r$$
where each $F_k$ has the form $\frac{A}{(ax + b)^n}$ or $\frac{Ax + B}{(ax^2 + bx + c)^n}$ with $ax^2 + bx + c$ irreducible.

## Guidelines / Methods
**Guidelines for Partial Fraction Decomposition of $f(x)/g(x)$ (7.5):**
1. If $\deg f \geq \deg g$: use long division first to obtain a proper fraction.
2. Factor $g(x)$ into linear factors $(ax + b)$ and irreducible quadratics $(ax^2 + bx + c)$, collecting repeats as $(ax+b)^n$ or $(ax^2+bx+c)^n$.
3. Apply the following rules:

**Rule (a):** For each factor $(ax + b)^n$ with $n \geq 1$, the decomposition contains:
$$\frac{A_1}{ax + b} + \frac{A_2}{(ax + b)^2} + \cdots + \frac{A_n}{(ax + b)^n}.$$

**Rule (b):** For each factor $(ax^2 + bx + c)^n$ with $n \geq 1$ and quadratic irreducible, the decomposition contains:
$$\frac{A_1 x + B_1}{ax^2 + bx + c} + \frac{A_2 x + B_2}{(ax^2 + bx + c)^2} + \cdots + \frac{A_n x + B_n}{(ax^2 + bx + c)^n}.$$

To find unknown constants: (1) substitute values of $x$ that make factors zero, or (2) expand and compare coefficients of like powers of $x$.

## Worked Examples
### Example 1
Evaluate $\int \frac{4x^2 + 13x - 9}{x^3 + 2x^2 - 3x} \, dx$.
**Solution**
Factor: $x^3 + 2x^2 - 3x = x(x + 3)(x - 1)$. By rule (a):
$$\frac{4x^2 + 13x - 9}{x(x + 3)(x - 1)} = \frac{A}{x} + \frac{B}{x + 3} + \frac{C}{x - 1}.$$
Multiplying by the LCD:
$$(*) \quad 4x^2 + 13x - 9 = A(x + 3)(x - 1) + Bx(x - 1) + Cx(x + 3).$$
Setting $x = 0$: $-9 = -3A$, so $A = 3$. Setting $x = 1$: $8 = 4C$, so $C = 2$. Setting $x = -3$: $-12 = 12B$, so $B = -1$. Then:
$$\int \frac{4x^2 + 13x - 9}{x(x + 3)(x - 1)} \, dx = 3\ln|x| - \ln|x + 3| + 2\ln|x - 1| + K = \ln\left|\frac{x^3(x - 1)^2}{x + 3}\right| + K.$$

### Example 2
Evaluate $\int \frac{3x^3 - 18x^2 + 29x - 4}{(x + 1)(x - 2)^3} \, dx$.
**Solution**
By rule (a) with $n = 3$ on $(x - 2)^3$:
$$\frac{3x^3 - 18x^2 + 29x - 4}{(x + 1)(x - 2)^3} = \frac{A}{x + 1} + \frac{B}{x - 2} + \frac{C}{(x - 2)^2} + \frac{D}{(x - 2)^3}.$$
Multiplying by the LCD:
$$(*) \quad 3x^3 - 18x^2 + 29x - 4 = A(x - 2)^3 + B(x + 1)(x - 2)^2 + C(x + 1)(x - 2) + D(x + 1).$$
$x = 2$: $6 = 3D$, so $D = 2$. $x = -1$: $-54 = -27A$, so $A = 2$. Comparing coefficients of $x^3$: $3 = A + B$, giving $B = 1$. From constant terms ($x = 0$): $-4 = -8A + 4B - 2C + D = -16 + 4 - 2C + 2$, so $C = -3$. Therefore:
$$\int = 2\ln|x + 1| + \ln|x - 2| + \frac{3}{x - 2} - \frac{1}{(x - 2)^2} + K.$$

### Example 3
Evaluate $\int \frac{x^2 - x - 21}{2x^3 - x^2 + 8x - 4} \, dx$.
**Solution**
Factor by grouping: $2x^3 - x^2 + 8x - 4 = x^2(2x - 1) + 4(2x - 1) = (x^2 + 4)(2x - 1)$. By rules (a) and (b):
$$\frac{x^2 - x - 21}{(x^2 + 4)(2x - 1)} = \frac{Ax + B}{x^2 + 4} + \frac{C}{2x - 1}.$$
Multiplying by the LCD gives $x^2 - x - 21 = (Ax + B)(2x - 1) + C(x^2 + 4)$. Setting $x = 1/2$: $C = -5$. Comparing $x^2$-coefficients: $1 = 2A + C$, so $A = 3$. Comparing $x$-coefficients: $-1 = -A + 2B$, so $B = 1$. Then:
$$\int = \frac{3}{2}\ln(x^2 + 4) + \frac{1}{2}\tan^{-1}\frac{x}{2} - \frac{5}{2}\ln|2x - 1| + K.$$

### Example 4
Evaluate $\int \frac{5x^3 - 3x^2 + 7x - 3}{(x^2 + 1)^2} \, dx$.
**Solution**
By rule (b) with $n = 2$:
$$\frac{5x^3 - 3x^2 + 7x - 3}{(x^2 + 1)^2} = \frac{Ax + B}{x^2 + 1} + \frac{Cx + D}{(x^2 + 1)^2}.$$
Expanding: $5x^3 - 3x^2 + 7x - 3 = Ax^3 + Bx^2 + (A + C)x + (B + D)$. Comparing coefficients: $A = 5$, $B = -3$, $C = 2$, $D = 0$. Then:
$$\int = \frac{5}{2}\ln(x^2 + 1) - 3\tan^{-1} x - \frac{1}{x^2 + 1} + K.$$

### Example 5 (CAS-assisted)
Evaluate $\int \frac{264x^3 - 553x^2 - 310x - 543}{24x^4 - 142x^3 - 59x^2 + 267x + 90} \, dx$ using a computer algebra system.
**Solution**
A CAS factors the denominator as $24(x - 6)(x + \tfrac{5}{4})(x - \tfrac{3}{2})(x + \tfrac{1}{3})$ and computes the decomposition:
$$= \frac{7}{x - 6} + \frac{7/2}{x + 5/4} + \frac{5/2}{x - 3/2} - \frac{2}{x + 1/3}.$$
Integrating each term:
$$\int = 7\ln|x - 6| + \tfrac{7}{2}\ln\left|x + \tfrac{5}{4}\right| + \tfrac{5}{2}\ln\left|x - \tfrac{3}{2}\right| - 2\ln\left|x + \tfrac{1}{3}\right| + K.$$

### Example 6 (Logistic Model)
If $dx/dt = kx(N - x)$ with $k, N > 0$: (a) find $x(t)$ explicitly, (b) find $\lim_{t \to \infty} x(t)$.
**Solution**
(a) Separating variables: $\int dt = \int \frac{1}{kx(N - x)} \, dx$. Partial fractions: $\frac{1}{kx(N - x)} = \frac{1/(kN)}{x} + \frac{1/(kN)}{N - x}$. Integrating:
$$Nt = \frac{1}{k}\ln x - \frac{1}{k}\ln(N - x) + D,$$
$$kNt = \ln\frac{Cx}{N - x}, \qquad \frac{Cx}{N - x} = e^{kNt}.$$
Solving for $x$ and using $x(0) = x_0$, $C = (N - x_0)/x_0$:
$$x(t) = \frac{Nx_0 e^{kNt}}{N - x_0 + x_0 e^{kNt}}.$$
(b) Dividing numerator and denominator by $e^{kNt}$: $x = N/(Ce^{-kNt} + 1)$. As $t \to \infty$, $e^{-kNt} \to 0$, so $\lim_{t \to \infty} x(t) = N$ — eventually everyone in the population has the information.

## Exercises
*   1. Evaluate the integral: $\int \frac{5x - 12}{x(x - 4)} \, dx$
*   2. Evaluate the integral: $\int \frac{x + 34}{(x - 6)(x + 2)} \, dx$
*   5. Evaluate the integral: $\int \frac{6x - 11}{(x - 1)^2} \, dx$
*   6. Evaluate the integral: $\int \frac{-19x^2 + 50x - 25}{x^2(3x - 5)} \, dx$
*   9. Evaluate the integral: $\int \frac{5x^2 - 10x - 8}{x^3 - 4x} \, dx$
*   11. Evaluate the integral: $\int \frac{2x^2 - 25x - 33}{(x + 1)^2(x - 5)} \, dx$
*   25. Evaluate the integral: $\int \frac{x^6 - x^3 + 1}{x^4 + 9x^2} \, dx$