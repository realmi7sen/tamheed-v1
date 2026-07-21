---
course: MATH106
doc_type: exam
exam_type: midterm_1
year_hijri: 1446
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

# Midterm 1 Exam — MATH 106 — 1446 H, Semester 1

## General Information
- **Institution**: King Saud University, Faculty of Sciences, Department of Mathematics
- **Course**: MATH 106 — Integral Calculus
- **Exam**: Midterm 1
- **Academic Year**: 1446 H, Semester 1
- **Gregorian Date**: October 2024

---

## Questions

### Question 1
(3+2+3)

a) If $F(x) = \int_{\cos x}^{\sin x} \sqrt{1 - t^2}\, dt$, find $F'\left(\dfrac{\pi}{4}\right)$.

b) Compute the integral $\displaystyle\int \frac{1 + (\sec x)^2}{(\tan x + x)^5}\, dx$.

c) Use the trapezoid rule with $n = 4$ to approximate the integral $\displaystyle\int_{0}^{1} \frac{dx}{1 + x^2}$.

### Question 2
(3+2+3)

a) Use the substitution $u = \ln|\sec x + \tan x|$ to compute the integral $\displaystyle\int (\sec x)\ln|\sec x + \tan x|\, dx$.

b) If $y = (x^2 + 1)^{\ln x + \cos x}$, find $\dfrac{dy}{dx}$.

c) Evaluate the integral $\displaystyle\int \frac{7^{\tanh^{-1}(2x)}}{1 - 4x^2}\, dx$.

### Question 3
(3+3+3)

a) Compute the integral $\displaystyle\int \frac{1 + \ln x}{\sqrt{(x\ln x)^2 + 4}}\, dx$.

b) Evaluate $\displaystyle\int \frac{dx}{x\sqrt{9 - x^{10}}}$.

c) Find $\displaystyle\int \frac{x^4}{\sqrt{3^{x^5} - 1}}\, dx$.

---

## Model Answers

### Question 1

**a)** By the Fundamental Theorem of Calculus with variable limits:
$$F'(x) = \sqrt{1 - \sin^2 x}\cdot \cos x - \sqrt{1 - \cos^2 x}\cdot(-\sin x)$$
$$= \cos x \cdot \cos x + \sin x \cdot \sin x = \cos^2 x + \sin^2 x = 1$$

**Answer:**
$$F'\left(\frac{\pi}{4}\right) = 1$$

**b)** Let $u = x + \tan x$, so $du = (1 + \sec^2 x)\, dx$.
$$I = \int \frac{du}{u^5} = \int u^{-5}\, du = \frac{u^{-4}}{-4} + c = -\frac{1}{4u^4} + c$$

**Answer:**
$$-\frac{1}{4(\tan x + x)^4} + c$$

**c)** *(Question paper prints part c; the handwritten solution set does not include a worked trapezoid computation for this item.)*

`UNREADABLE` — worked solution for 1(c) not provided in the answer sheet.

### Question 2

**a)** Let $u = \ln|\sec x + \tan x|$, so
$$du = \frac{\sec x \tan x + \sec^2 x}{\sec x + \tan x}\, dx = \frac{\sec x(\tan x + \sec x)}{\sec x + \tan x}\, dx = \sec x\, dx$$
Then:
$$I = \int u\, du = \frac{1}{2}u^2 + c = \frac{1}{2}\left[\ln|\sec x + \tan x|\right]^2 + c$$

**b)** Take logarithms: $\ln y = (\ln x + \cos x)\ln(x^2 + 1)$.
$$\frac{y'}{y} = \left(\frac{1}{x} - \sin x\right)\ln(x^2 + 1) + (\ln x + \cos x)\cdot\frac{2x}{x^2 + 1}$$

**Answer:**
$$y' = (x^2 + 1)^{\ln x + \cos x}\left[\left(\frac{1}{x} - \sin x\right)\ln(x^2 + 1) + (\ln x + \cos x)\cdot\frac{2x}{x^2 + 1}\right]$$

**c)** Let $u = \tanh^{-1}(2x)$, so $du = \dfrac{2}{1 - 4x^2}\, dx$.
$$I = \frac{1}{2}\int 7^{u}\, du = \frac{1}{2}\left[\frac{1}{\ln 7}7^{u}\right] + c = \frac{1}{2\ln 7}7^{\tanh^{-1}(2x)} + c$$

### Question 3

**a)** Let $u = x\ln x$, so $du = (1 + \ln x)\, dx$.
$$I = \int \frac{du}{\sqrt{u^2 + 2^2}} = \sinh^{-1}\left(\frac{u}{2}\right) + c = \sinh^{-1}\left(\frac{x\ln x}{2}\right) + c$$

**b)** Rewrite by multiplying numerator and denominator to set up $u = x^5$:
$$\int \frac{dx}{x\sqrt{9 - x^{10}}} = \frac{1}{5}\int \frac{5x^4\, dx}{x^5\sqrt{3^2 - (x^5)^2}} = \frac{1}{5}\int \frac{du}{u\sqrt{3^2 - u^2}}$$
$$= \frac{1}{5}\left[-\frac{1}{3}\operatorname{sech}^{-1}\left(\frac{u}{3}\right)\right] + c = -\frac{1}{15}\operatorname{sech}^{-1}\left(\frac{x^5}{3}\right) + c$$

**c)** Let $u = 3^{x^5/2}$, so $du = 3^{x^5/2}\ln 3 \cdot \dfrac{5}{2}x^4\, dx$.
$$\int \frac{x^4}{\sqrt{3^{x^5} - 1}}\, dx = \frac{1}{\ln 3 \cdot \frac{5}{2}}\int \frac{du}{u\sqrt{u^2 - 1}} = \frac{2}{5\ln 3}\int \frac{du}{u\sqrt{u^2 - 1}}$$
$$= \frac{2}{5\ln 3}\sec^{-1}(u) + c = \frac{2}{5\ln 3}\sec^{-1}\left(3^{x^5/2}\right) + c$$
