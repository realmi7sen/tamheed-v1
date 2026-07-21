---
course: MATH106
doc_type: exam
exam_type: midterm_1
year_hijri: 1447
semester: 1
ksu_chapter:
  - unknown
book_chapters:
  - 4
  - 5
topics:
  - fundamental_theorem_of_calculus
  - substitution
  - trapezoid_rule
  - mean_value_theorem
  - logarithmic_differentiation
  - inverse_hyperbolic_integrals
  - inverse_trig_integrals
exam_format: written
coordinator: unknown
coverage_verified: false
difficulty: unknown
historical_weight: unknown
language: en
status: converted
---

# Midterm 1 Exam — MATH 106 — 1447 H, Semester 1

## General Information
- **Institution**: King Saud University, Faculty of Sciences, Department of Mathematics
- **Course**: MATH 106 — Integral Calculus
- **Exam**: Midterm 1
- **Academic Year**: 1447 H, Semester 1
- **Gregorian Date**: October 2025

---

## Questions

### Question 1
(2+3+3)

a) If $F(x) = \int_{2x}^{x^2} \sqrt{1 + t^6}\, dt$, find $F'(x)$.

b) Compute the integral $\displaystyle\int \frac{dx}{(x \ln x)(\ln(\ln x))}$.

c) Use the trapezoid formula with $n = 5$ to approximate the integral $\displaystyle\int_{0}^{5} \frac{dx}{1 + x}$.

### Question 2
(3+2+3)

a) Find the number $c$ in the mean value theorem for $f(x) = -3\sqrt{2x - 6}$ on $[3, 5]$.

b) If $y = \sqrt{(x^2 + 1)^3 \sqrt{5x + 4}}$, find $\dfrac{dy}{dx}$.

c) Evaluate the integral $\displaystyle\int \frac{x + \cosh^{-1} x}{\sqrt{(x - 1)(x + 1)}}\, dx$.

### Question 3
(3+3+3)

a) Compute the integral $\displaystyle\int \frac{x\, dx}{\sqrt{1 - 4x^4}}$.

b) Evaluate $\displaystyle\int \frac{dx}{x\sqrt{x^8 - 16}}$.

c) Find $\displaystyle\int \frac{dx}{\sec x \sqrt{9\sin^2 x - \sin^4 x}}$, $\ 0 < x < \dfrac{\pi}{2}$.

---

## Model Answers

### Question 1

**a)**
$$F'(x) = 2x\sqrt{1 + x^{12}} - 2\sqrt{1 + 16^{}x^6}$$

(By the Fundamental Theorem of Calculus with variable limits: differentiate the upper limit $x^2$ and lower limit $2x$.)

**b)**

**Step 1 — Substitute $u = \ln x$**
$$\int \frac{dx}{x \ln x \, \ln(\ln x)} = \int \frac{du}{u \ln u}$$

**Step 2 — Substitute $t = \ln u$**
$$= \int \frac{dt}{t} = \ln |t| + c$$

**Answer:**
$$\ln|\ln(\ln x)| + c$$

**c)**

Nodes with $x_k = k$, $f(x_k) = \dfrac{1}{1 + x_k}$ for $k = 0, 1, 2, 3, 4, 5$; trapezoid weights $(1, 2, 2, 2, 2, 1)$.

The weighted sum evaluates to approximately $3.7333$, and with $\Delta x = 1$:
$$\int_{0}^{5} \frac{dx}{1 + x} \approx \frac{1}{2}(3.7333) \approx 1.8666$$

### Question 2

**a)**
$$-3\int_{3}^{5} \sqrt{2x - 6}\, dx = -8$$

Setting $f(c)(5 - 3) = -8$ and solving:
$$c = \frac{35}{9}$$

**b)**

**Step 1 — Take logarithms**
$$\ln y = \frac{3}{2}\ln(x^2 + 1) + \frac{1}{4}\ln(5x + 4)$$

**Step 2 — Differentiate**
$$y' = y\left(\frac{3x}{x^2 + 1} + \frac{5}{4(5x + 4)}\right)$$

**Answer:**
$$y' = \sqrt{(x^2+1)^3\sqrt{5x+4}}\left(\frac{3x}{x^2 + 1} + \frac{5}{4(5x + 4)}\right)$$

**c)**

Split the integral. For the first part:
$$\int \frac{x}{\sqrt{(x-1)(x+1)}}\, dx = \int \frac{x}{\sqrt{x^2 - 1}}\, dx = \sqrt{x^2 - 1} + c$$

For the second part, with $u = \cosh^{-1} x$:
$$\int \frac{\cosh^{-1} x}{\sqrt{(x-1)(x+1)}}\, dx = \int u\, du = \frac{1}{2}\left(\cosh^{-1} x\right)^2 + c$$

**Answer:**
$$\sqrt{x^2 - 1} + \frac{1}{2}\left(\cosh^{-1} x\right)^2 + c$$

### Question 3

**a)**

With $t = 2x^2$:
$$\int \frac{x\, dx}{\sqrt{1 - 4x^4}} = \frac{1}{4}\int \frac{dt}{\sqrt{1 - t^2}} = \frac{1}{4}\sin^{-1}(2x^2) + c$$

**b)**

With $u = x^4$ (so $4u = x^4$ in the printed working):
$$\int \frac{dx}{x\sqrt{x^8 - 16}} = \frac{1}{16}\int \frac{du}{u\sqrt{u^2 - 1}} = \frac{1}{16}\sec^{-1}\left(\frac{x^4}{4}\right) + c$$

**c)**

Rewrite:
$$\int \frac{dx}{\sec x \sqrt{9\sin^2 x - \sin^4 x}} = \int \frac{\cos x\, dx}{\sin x \sqrt{9 - \sin^2 x}}$$

With $u = \sin x$ (printed as $3u = \sin x$):
$$= \frac{1}{3}\int \frac{du}{u\sqrt{1 - u^2}} = -\frac{1}{3}\operatorname{sech}^{-1}\left(\frac{\sin x}{3}\right) + c$$
