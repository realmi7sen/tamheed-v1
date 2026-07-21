---
course: MATH106
doc_type: exam
exam_type: midterm_1
year_hijri: 1439
semester: summer
ksu_chapter:
  - unknown
book_chapters:
  - 4
  - 5
topics:
  - antiderivatives
  - summation_formulas
  - riemann_sums
  - integral_mean_value_theorem
  - fundamental_theorem_of_calculus
  - logarithmic_differentiation
  - inverse_hyperbolic_derivatives
  - substitution
  - inverse_trig_integrals
exam_format: written
coordinator: unknown
coverage_verified: false
difficulty: unknown
historical_weight: unknown
language: en
status: converted
---

# First Midterm Exam — MATH 106 — 1439 H, Summer Semester

## General Information
- **Institution**: King Saud University, College of Science, Department of Mathematics
- **Course**: MATH 106 — Integral Calculus
- **Exam**: First Midterm
- **Academic Year**: 1438–39 H, Summer Semester
- **Gregorian Date**: Monday, July 9, 2018
- **Duration**: 7:00 – 8:30 pm
- **Total Marks**: 25

---

## Questions

### Question 1
(4 Marks: 2 + 2)

a) Determine the function $f(x)$ given that $f'(x) = 8x^3 + 6x^2 + 4x + 5$, and $f(1) = 14$.

b) Find the value of the constant $c$ such that $\displaystyle\sum_{k=1}^{6}\left(k^2 + 2k + 7c\right) = 217$.

### Question 2
(3 Marks: 2 + 1)

Let $R$ be the region under the graph of $f(x) = 2x + 3$ on the interval $[0, 4]$. Let $P$ be the regular partition of $[0, 4]$ into $n$ subintervals.

a) Find the Riemann sum if $c_i = \dfrac{4i}{n}$, $\ i = 1, 2, \cdots, n$.

b) Compute the area of the region $R$ by using the Riemann sum in part (a).

### Question 3
(4 Marks: 2 + 2)

a) Find the value of $c$ that satisfies the Integral Mean Value Theorem for the function $f(x) = 3x^2 - 2x + 3$ on $[-1, 3]$.

b) If $F(x) = \displaystyle\int_{\cos x}^{1 + \sin x} \sqrt{2 + t}\, dt$, then find $F'(0)$.

### Question 4
(5 Marks: 1 + 2 + 2)

Differentiate the following functions:

1. $y = 2^{\pi + \sin x}$

2. $y = (1 + x^2)^{\tan x}$

3. $y = \ln\left(\cosh^{-1} x\right)$

### Question 5
(9 Marks: 1 + 2 + 2 + 2 + 2)

Evaluate the following integrals:

1. $\displaystyle\int \left(x^{2/3} - 4x^{-1/5} + 4\right)\, dx$

2. $\displaystyle\int_{2}^{4} \frac{1}{9 - 2x}\, dx$

3. $\displaystyle\int \frac{e^{\sqrt{y}}}{\sqrt{y}}\, dy$

4. $\displaystyle\int 3^{\cos x^2}\, x\sin x^2\, dx$

5. $\displaystyle\int \frac{\sec(x + 2)\tan(x + 2)}{4 + \sec^2(x + 2)}\, dx$

---

## Model Answers

### Question 1

**a)**
$$f(x) = \int f'(x)\, dx = \int 8x^3 + 6x^2 + 4x + 5\, dx = 2x^4 + 2x^3 + 2x^2 + 5x + C$$
Using $f(1) = 14$: $\ 14 = 2 + 2 + 2 + 5 + C \Rightarrow C = 3$.
$$f(x) = 2x^4 + 2x^3 + 2x^2 + 5x + 3$$

**b)** Using $\sum_{k=1}^{6}k^2 = \dfrac{6(7)(13)}{6}$, $\sum_{k=1}^{6}2k = 2\cdot\dfrac{6(7)}{2}$, $\sum_{k=1}^{6}7c = 7c(6)$:
$$91 + 42 + 42c = 217 \Rightarrow 42c = 84 \Rightarrow c = 2$$

### Question 2

**a)** With $\Delta x_i = \dfrac{b - a}{n} = \dfrac{4}{n}$ and $c_i = \dfrac{4i}{n}$:
$$\text{Riemann sum} = \sum_{i=1}^{n} f(c_i)\Delta x_i = \frac{4}{n}\sum_{i=1}^{n}\left(2\cdot\frac{4i}{n} + 3\right) = \frac{4}{n}\sum_{i=1}^{n}\left(\frac{8i}{n} + 3\right)$$
$$= \frac{4}{n}\left[\frac{8}{n}\cdot\frac{n(n+1)}{2} + 3n\right] = \frac{16(n+1)}{n} + 12$$

**b)**
$$\text{Area} = \lim_{n \to \infty}\left[\frac{16(n+1)}{n} + 12\right] = \lim_{n \to \infty}\left[16 + \frac{16}{n} + 12\right] = 28$$

### Question 3

**a)** By the Integral MVT: $f(c) = \dfrac{1}{b - a}\displaystyle\int_{a}^{b} f(x)\, dx$.
$$f(c) = \frac{1}{4}\int_{-1}^{3}(3x^2 - 2x + 3)\, dx = \frac{1}{4}\left[x^3 - x^2 + 3x\right]_{-1}^{3} = \frac{1}{4}(27 - (-5)) = 8$$
So $3c^2 - 2c + 3 = 8 \Rightarrow 3c^2 - 2c - 5 = 0 \Rightarrow c = -1$ or $c = \dfrac{5}{3}$.

**Answer:** $c = \dfrac{5}{3} \in (-1, 3)$ (reject $c = -1$, endpoint).

**b)** By the FTC with variable limits:
$$F'(x) = \sqrt{2 + 1 + \sin x}\cdot\cos x - \sqrt{2 + \cos x}\cdot(-\sin x)$$
$$F'(0) = \sqrt{3} - 0 = \sqrt{3}$$

### Question 4

**1.**
$$y' = \cos x \cdot 2^{\pi + \sin x}\ln 2$$

**2.** $\ln y = \tan x \ln(1 + x^2)$, so
$$\frac{y'}{y} = \tan x\cdot\frac{2x}{1 + x^2} + \sec^2 x \ln(1 + x^2)$$
$$y' = \left[\frac{2x\tan x}{1 + x^2} + \sec^2 x \ln(1 + x^2)\right](1 + x^2)^{\tan x}$$

**3.**
$$y' = \frac{1}{\cosh^{-1} x}\cdot\frac{1}{\sqrt{x^2 - 1}} = \frac{1}{\sqrt{x^2 - 1}\,\cosh^{-1} x}$$

### Question 5

**1.**
$$\int \left(x^{2/3} - 4x^{-1/5} + 4\right)\, dx = \frac{3}{5}x^{5/3} - 5x^{4/5} + 4x + C$$

**2.** Let $u = 9 - 2x$, $du = -2\, dx$; bounds $x = 2 \to u = 5$, $x = 4 \to u = 1$.
$$\int_{2}^{4} \frac{1}{9 - 2x}\, dx = -\frac{1}{2}\left[\ln|u|\right]_{5}^{1} = -\frac{1}{2}[\ln 1 - \ln 5] = \frac{1}{2}\ln 5$$

**3.** Let $u = \sqrt{y}$, $2\, du = \dfrac{dy}{\sqrt{y}}$.
$$\int \frac{e^{\sqrt{y}}}{\sqrt{y}}\, dy = \int 2e^u\, du = 2e^u + C = 2e^{\sqrt{y}} + C$$

**4.** Let $u = \cos x^2$, $du = -2x\sin(x^2)\, dx$, so $\dfrac{du}{-2} = x\sin(x^2)\, dx$.
$$\int 3^{\cos x^2}x\sin x^2\, dx = \int 3^{u}\frac{du}{-2} = -\frac{1}{2}\frac{3^{u}}{\ln 3} + C = -\frac{1}{2\ln 3}3^{\cos(x^2)} + C$$

**5.** Let $u = \sec(x + 2)$, $du = \sec(x + 2)\tan(x + 2)\, dx$.
$$\int \frac{\sec(x + 2)\tan(x + 2)}{4 + \sec^2(x + 2)}\, dx = \int \frac{du}{4 + u^2} = \frac{1}{2}\tan^{-1}\left(\frac{u}{2}\right) + C = \frac{1}{2}\tan^{-1}\left(\frac{\sec(x + 2)}{2}\right) + C$$
