---
course: MATH106
doc_type: exam
exam_type: midterm_1
year_hijri: 1443
semester: 1
ksu_chapter:
  - unknown
book_chapters:
  - 4
  - 5
topics:
  - simpsons_rule
  - substitution
  - logarithmic_differentiation
  - inverse_trig_integrals
  - inverse_hyperbolic_integrals
  - integration_by_parts
  - trigonometric_integrals
  - trig_substitution
  - partial_fractions
  - limits
exam_format: written
coordinator: unknown
coverage_verified: false
difficulty: unknown
historical_weight: unknown
language: en
status: converted
notes: "Questions RECONSTRUCTED from a solutions-only sheet (1442-1443). No original question paper was available. Question wording is inferred from the worked solutions and may differ slightly from the printed exam. Verify before treating as authoritative."
---

# Midterm Exam — MATH 106 — 1442–1443 H, Semester 1 (Reconstructed from Solutions)

## General Information
- **Institution**: King Saud University, Department of Mathematics
- **Course**: MATH 106 — Integral Calculus
- **Exam**: Midterm (first examination)
- **Academic Year**: 1442–1443 H, Semester 1
- **Note**: Reconstructed from the official solution sheet; original question paper not provided.

---

## Questions

> ⚠️ These questions were reconstructed by reading the model-answer sheet. Each is inferred from the corresponding worked solution.

### Question 1
1. Use Simpson's rule with $n = 4$ to approximate the integral $\displaystyle\int_{1}^{3} f(x)\, dx$ from the given table of values, where $S_4 = \dfrac{3 - 1}{12}\left(f(1) + 4f\left(\tfrac{3}{2}\right) + 2f(2) + 4f\left(\tfrac{5}{2}\right) + f(3)\right)$.

2. Evaluate the integral $\displaystyle\int \frac{\left(1 - \frac{1}{x^2}\right)^5}{x^3}\, dx$.

3. Use logarithmic differentiation to find $y'$ if $y = \sqrt{x}\cdot\sqrt[3]{x + 2}\cdot\sqrt[5]{x - 1}$.

4. Evaluate the integral $\displaystyle\int \frac{(\sec x)^2}{\sqrt{4 - (\tan x)^2}}\, dx$.

5. Evaluate the integral $\displaystyle\int \frac{dx}{\sqrt{e^{2x} - 1}}$.

6. Compute the integral $\displaystyle\int \frac{dx}{x\sqrt{1 - x^5}}$.

7. Find $\displaystyle\lim_{x \to 0} \frac{\cos x - 1 + \frac{x^2}{2}}{x^4}$.

### Question 2
8. Evaluate the integral $\displaystyle\int (\ln x)^2\, dx$.

9. Evaluate the integral $\displaystyle\int (\tan x)^5 (\sec x)^3\, dx$.

10. Evaluate the integral $\displaystyle\int \frac{x^2}{\sqrt{9 - x^2}}\, dx$.

11. Evaluate the integral $\displaystyle\int \frac{x^2 + 8x + 10}{x^2 + 6x + 11}\, dx$.

---

## Model Answers

### Question 1

**1.** Simpson's rule:
$$S_4 = \frac{3 - 1}{12}\left(f(1) + 4f\left(\tfrac{3}{2}\right) + 2f(2) + 4f\left(\tfrac{5}{2}\right) + f(3)\right) \approx 4.505$$

**2.** With $t = 1 - \dfrac{1}{x^2}$:
$$\int \frac{\left(1 - \frac{1}{x^2}\right)^5}{x^3}\, dx = \frac{1}{2}\int t^5\, dt = \frac{1}{12}\left(1 - \frac{1}{x^2}\right)^6 + c$$

**3.** $\ln y = \dfrac{1}{2}\ln x + \dfrac{1}{3}\ln(x + 2) + \dfrac{1}{5}\ln(x - 1)$.
$$\frac{y'}{y} = \frac{1}{2x} + \frac{1}{3(x + 2)} + \frac{1}{5(x - 1)}$$
$$y' = \left(\frac{1}{2x} + \frac{1}{3(x + 2)} + \frac{1}{5(x - 1)}\right)\sqrt{x}\cdot\sqrt[3]{x + 2}\cdot\sqrt[5]{x - 1}$$

**4.** With $t = \tan x$:
$$\int \frac{(\sec x)^2}{\sqrt{4 - (\tan x)^2}}\, dx = \int \frac{dt}{\sqrt{4 - t^2}} = \sin^{-1}\left(\frac{t}{2}\right) + c = \sin^{-1}\left(\frac{\tan x}{2}\right) + c$$

**5.** With $t = e^x$:
$$\int \frac{dx}{\sqrt{e^{2x} - 1}} = \int \frac{dt}{t\sqrt{t^2 - 1}} = \sec^{-1}(e^x) + c$$

**6.** With $t = x^5$:
$$\int \frac{dx}{x\sqrt{1 - x^5}} = \frac{2}{5}\int \frac{dt}{t\sqrt{1 - t^2}} = -\frac{2}{5}\operatorname{sech}^{-1}\left(x^{5/2}\right) + c$$

**7.** By repeated L'Hôpital / Taylor:
$$\lim_{x \to 0} \frac{\cos x - 1 + \frac{x^2}{2}}{x^4} = \lim_{x \to 0}\frac{-\sin x + x}{4x^3} = \lim_{x \to 0}\frac{-\cos x + 1}{12x^2} = \lim_{x \to 0}\frac{\sin x}{24x} = \frac{1}{24}$$

### Question 2

**8.** By parts with $u = (\ln x)^2$, $v' = 1$:
$$\int (\ln x)^2\, dx = x(\ln x)^2 - 2\int \ln x\, dx = x(\ln x)^2 - 2x\ln x + 2x + c$$

**9.** With $t = \sec x$:
$$\int (\tan x)^5 (\sec x)^3\, dx = \int (t^2 - 1)^2 t^2\, dt = \frac{1}{7}\sec^7 x - \frac{2}{5}\sec^5 x + \frac{1}{3}\sec^3 x + c$$

**10.** With $x = 3\sin\theta$:
$$\int \frac{x^2}{\sqrt{9 - x^2}}\, dx = 9\int \sin^2\theta\, d\theta = \frac{9}{2}\int (1 - \cos 2\theta)\, d\theta = \frac{9}{2}(\theta - \sin\theta\cos\theta) + c$$
$$= \frac{9}{2}\left(\sin^{-1}\left(\frac{x}{3}\right) - \frac{1}{9}x\sqrt{9 - x^2}\right) + c$$

**11.** Polynomial division gives $\dfrac{x^2 + 8x + 10}{x^2 + 6x + 11} = 1 + \dfrac{2x - 1}{x^2 + 6x + 11}$.
$$\int \frac{x^2 + 8x + 10}{x^2 + 6x + 11}\, dx = \int 1 + \frac{2x + 6}{x^2 + 6x + 11}\, dx - \int \frac{7}{(x + 3)^2 + 2}\, dx$$
$$= x + \ln\left(x^2 + 6x + 11\right) - \frac{7}{\sqrt{2}}\tan^{-1}\left(\frac{x + 3}{\sqrt{2}}\right) + c$$
