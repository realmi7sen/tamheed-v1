---
course: MATH106
doc_type: exam
exam_type: midterm_1
year_hijri: 1445
semester: 1
ksu_chapter:
  - unknown
book_chapters:
  - 4
  - 5
topics:
  - fundamental_theorem_of_calculus
  - substitution
  - mean_value_theorem
  - exponential_integrals
  - logarithmic_differentiation
  - inverse_trig_integrals
  - inverse_hyperbolic_integrals
exam_format: written
coordinator: Mahmoud El-ramly
coverage_verified: false
difficulty: unknown
historical_weight: unknown
language: en
status: converted
---

# Midterm 1 Exam — MATH 106 — 1445 H, Semester 1

## General Information
- **Institution**: King Saud University, Faculty of Sciences, Department of Mathematics
- **Course**: MATH 106 — Integral Calculus
- **Exam**: Midterm 1
- **Academic Year**: 1445 H, Semester 1
- **Gregorian Date**: October 2023

---

## Questions

### Question 1
(2+3+3)

a) Let $F(x) = \int_{\tan x}^{x^2} \frac{dt}{2 + t^4}$. Find $F'(x)$.

b) Use the substitution $u = x^3 + 2$ to compute $\displaystyle\int x^5 \sqrt{x^3 + 2}\, dx$.

c) Find the number $z$ in the mean value theorem for $f(x) = |x|$ on $[-1, 1]$.

### Question 2
(2+3+3)

a) Compute $\displaystyle\int (x + 1)\, 7^{x^2 + 2x}\, dx$.

b) Find the indefinite integral $\displaystyle\int \frac{x}{(x^2 + 1)\cos^2(\ln(x^2 + 1))}\, dx$.

c) If $F(x) = \tan^{-1}(\cosh(x)) + x^{x+1}$, find $F'(x)$.

### Question 3
(3+3+3)

a) Evaluate the integral $\displaystyle\int \frac{\sqrt{x^3}}{1 + x^5}\, dx$.

b) Compute $\displaystyle\int \frac{\sinh x}{\sqrt{2^{\cosh x} - 4}}\, dx$.

c) Find $\displaystyle\int \frac{1 - 2x^4}{x\sqrt{1 - x^4}}\, dx$.

---

## Model Answers

### Question 1

**a)** By the Fundamental Theorem of Calculus with variable limits:
$$F'(x) = \frac{1}{2 + (x^2)^4}\cdot 2x - \frac{1}{2 + (\tan x)^4}\cdot \sec^2 x$$
$$= \frac{2x}{2 + x^8} - \frac{\sec^2 x}{4 + \tan^4 x}$$

**b)** Let $u = x^3 + 2$, so $du = 3x^2\, dx$ and $x^3 = u - 2$.
$$\frac{1}{3}\int 3x^2 \cdot x^3(x^3 + 2)^{1/2}\, dx = \frac{1}{3}\int (u - 2)(u)^{1/2}\, du = \frac{1}{3}\int \left(u^{3/2} - 2u^{1/2}\right)\, du$$
$$= \frac{1}{3}\left[\frac{u^{5/2}}{5/2} - 2\cdot\frac{u^{3/2}}{3/2}\right] + c = \frac{1}{3}\left(\frac{2}{5}(x^3 + 2)^{5/2} - \frac{4}{3}(x^3 + 2)^{3/2}\right) + c$$

**c)** With $|x| = x$ for $x \geq 0$ and $-x$ for $x < 0$:
$$\int_{-1}^{1}|x|\, dx = \int_{-1}^{0}-x\, dx + \int_{0}^{1}x\, dx = -\frac{x^2}{2}\Big|_{-1}^{0} + \frac{x^2}{2}\Big|_{0}^{1} = \frac{1}{2} + \frac{1}{2} = 1$$
By MVT: $\int_{-1}^{1}|x|\, dx = |z|(1 - (-1))$, so $1 = |z|\cdot 2 \Rightarrow |z| = \frac{1}{2}$.

**Answer:**
$$z = \pm\frac{1}{2}, \quad \text{both in } (-1, 1)$$

### Question 2

**a)** Let $u = x^2 + 2x$, so $du = (2x + 2)\, dx = 2(x + 1)\, dx$.
$$\int (x + 1)7^{x^2 + 2x}\, dx = \frac{1}{2}\int 7^{u}\, du = \frac{1}{2}\cdot\frac{1}{\ln 7}7^{u} + c = \frac{1}{2\ln 7}7^{x^2 + 2x} + c$$

**b)** Let $u = \ln(x^2 + 1)$, so $du = \dfrac{2x}{x^2 + 1}\, dx$.
$$\frac{1}{2}\int \frac{2x}{x^2 + 1}\sec^2(\ln(x^2 + 1))\, dx = \frac{1}{2}\int \sec^2 u\, du = \frac{1}{2}\tan u + c = \frac{1}{2}\tan(\ln(x^2 + 1)) + c$$

**c)** Differentiate each term. For $\tan^{-1}(\cosh x)$:
$$\frac{d}{dx}\tan^{-1}(\cosh x) = \frac{\sinh x}{1 + \cosh^2 x}$$
For $y = x^{x+1}$, take logs: $\ln y = (x + 1)\ln x$, so
$$\frac{y'}{y} = (x + 1)\cdot\frac{1}{x} + \ln x \Rightarrow y' = x^{x+1}\left[\frac{x + 1}{x} + \ln x\right]$$

**Answer:**
$$F'(x) = \frac{\sinh x}{1 + \cosh^2 x} + x^{x+1}\left[\frac{x + 1}{x} + \ln x\right]$$

### Question 3

**a)** Rewrite $\sqrt{x^3} = x^{3/2}$. With $u = x^{5/2}$, $du = \dfrac{5}{2}x^{3/2}\, dx$:
$$\int \frac{x^{3/2}}{1 + x^5}\, dx = \frac{2}{5}\int \frac{du}{1^2 + u^2} = \frac{2}{5}\tan^{-1}(u) + c = \frac{2}{5}\tan^{-1}\left(x^{5/2}\right) + c$$

**b)** Rewrite $2^{\cosh x} = (\sqrt{2}^{\cosh x})^2$ and set $u = \sqrt{2}^{\cosh x}$, so $du = \sqrt{2}^{\cosh x}\sinh x \ln\sqrt{2}\, dx$.
$$\int \frac{\sinh x}{\sqrt{2^{\cosh x} - 4}}\, dx = \frac{1}{\ln\sqrt{2}}\int \frac{du}{u\sqrt{u^2 - 2^2}} = \frac{1}{\ln\sqrt{2}}\cdot\frac{1}{2}\sec^{-1}\left(\frac{u}{2}\right) + c$$
$$= \frac{1}{2\ln\sqrt{2}}\sec^{-1}\left(\frac{\sqrt{2}^{\cosh x}}{2}\right) + c$$

**c)** Split:
$$\int \frac{1 - 2x^4}{x\sqrt{1 - x^4}}\, dx = \int \frac{1}{x\sqrt{1 - x^4}}\, dx - 2\int \frac{x^4}{x\sqrt{1 - x^4}}\, dx$$

For the first integral, with $u = x^2$ ($du = 2x\, dx$):
$$\int \frac{1}{x\sqrt{1 - x^4}}\, dx = \frac{1}{2}\int \frac{2x}{x^2\sqrt{1^2 - (x^2)^2}}\, dx = -\frac{1}{2}\operatorname{sech}^{-1}(x^2) + c$$

*(The handwritten solution sheet develops the first term fully as above and sets up the second term $-2\int \frac{x^3}{\sqrt{1-x^4}}\,dx$; the final combined closed form is cut off at the page edge.)*

`UNREADABLE` — final combined answer for 3(c) is cut off at the bottom of the scanned solution page.
