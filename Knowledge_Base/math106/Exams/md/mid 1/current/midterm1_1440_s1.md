---
course: MATH106
doc_type: exam
exam_type: midterm_1
year_hijri: 1440
semester: 1
ksu_chapter:
  - unknown
book_chapters:
  - 4
  - 5
topics:
  - fundamental_theorem_of_calculus
  - riemann_sums
  - simpsons_rule
  - substitution
  - logarithmic_differentiation
  - inverse_trig_integrals
  - inverse_hyperbolic_integrals
  - exponential_integrals
exam_format: written
coordinator: unknown
coverage_verified: false
difficulty: unknown
historical_weight: unknown
language: en
status: converted
notes: "Questions RECONSTRUCTED from a solutions-only sheet (Semester I, 1439-1440). No original question paper was uploaded. Question wording is inferred from the worked solutions; the source OCR was partly degraded, so verify integrands and bounds against an original paper before treating as authoritative."
---

# First Examination — MATH 106 — 1440 H, Semester 1 (Reconstructed from Solutions)

## General Information
- **Institution**: King Saud University, Department of Mathematics
- **Course**: MATH 106 — Integral Calculus
- **Exam**: First Examination (Midterm 1)
- **Academic Year**: 1439–1440 H, Semester 1 (filename 40-2)
- **Note**: Reconstructed from the official solution sheet; original question paper not provided.

---

## Questions

> ⚠️ Reconstructed from the model-answer sheet. Each item is inferred from its worked solution.

### Exercise 1

a) If $f(x) = \ln(2x)$ and $g(x) = \displaystyle\int_{1}^{4x^2} (1 + t^2)^{10}\, dt$, and $F(x) = f(x)\, g(x)$, find $F'\left(\dfrac{1}{2}\right)$.

b) Use Riemann sums to compute $\displaystyle\int_{0}^{2} 3x^2\, dx$.

c) Use Simpson's rule with the given nodes to approximate $\displaystyle\int_{0}^{\pi} \sin^4(x)\, dx$.

### Exercise 2

a) Find $f'(x)$ if $f(x) = \log_2(\sin^{-1}(x))$.

b) Evaluate the integral $\displaystyle\int \frac{4^{-\ln x}}{x}\, dx$.

c) Use logarithmic differentiation to find $y'$ if $y = \dfrac{e^{2x^2}\ln x}{(x - 1)^{3/2}}$ *(equivalently $y = e^{2x^2\ln x}(x-1)^{3/2}$ as written in the solution)*.

### Exercise 3

a) Evaluate the integral $\displaystyle\int \frac{2x + 3}{\sqrt{4 - x^2}}\, dx$.

b) Evaluate the integral $\displaystyle\int \frac{e^{x/2}}{7 + e^x}\, dx$.

c) Compute the integral $\displaystyle\int \frac{\sin(x)}{\sqrt{e^{\cos(x)} - 1}}\, dx$.

---

## Model Answers

### Exercise 1

**a)** With $f = \ln(2x)$ and $g(x) = \displaystyle\int_{1}^{4x^2}(1 + t^2)^{10}\, dt$: since $f\left(\tfrac{1}{2}\right) = 0$ and $g\left(\tfrac{1}{2}\right) = 0$,
$$F'\left(\tfrac{1}{2}\right) = 0.$$
In general:
$$F'(x) = \frac{1}{x}\int_{1}^{4x^2}(1 + t^2)^{10}\, dt + 8x\ln(2x)(1 + 16x^4)^{10}$$

**b)**
$$\int_{0}^{2} 3x^2\, dx = \lim_{n \to +\infty}\frac{3\cdot 2}{n}\sum_{k=1}^{n}\frac{4k^2}{n^2} = \lim_{n \to +\infty} 24\left(\frac{n(n+1)(2n+1)}{6n^3}\right) = 8$$

**c)** With $f(x) = \sin^4(x)$ on nodes $0, \tfrac{\pi}{4}, \tfrac{\pi}{2}, \tfrac{3\pi}{4}, \pi$ and Simpson weights $(1, 4, 2, 4, 1)$:
$$\int_{0}^{\pi}\sin^4(x)\, dx \approx \frac{3\pi}{8}$$

### Exercise 2

**a)**
$$f'(x) = \frac{1}{(\ln 2)(\sin^{-1}(x))\sqrt{1 - x^2}}$$

**b)** With $t = -\ln(x)$:
$$\int \frac{4^{-\ln(x)}}{x}\, dx = -\int 4^{t}\, dt = -\frac{4^{-\ln(x)}}{\ln 4} + c$$

**c)** With $y = e^{2x^2\ln(x)}(x - 1)^{3/2}$, so $\ln(y) = 2x^2\ln(x) + \tfrac{3}{2}\ln(x - 1)$:
$$\frac{y'}{y} = 4x\ln(x) + 2x + \frac{3}{2(x - 1)}$$
$$y' = \left(4x\ln(x) + 2x + \frac{3}{2(x - 1)}\right)y$$

### Exercise 3

**a)**
$$\int \frac{2x + 3}{\sqrt{4 - x^2}}\, dx = \int \frac{2x}{\sqrt{4 - x^2}}\, dx + 3\int \frac{dx}{\sqrt{4 - x^2}} = -2\sqrt{4 - x^2} + 3\sin^{-1}\left(\frac{x}{2}\right) + c$$

**b)** With $t = e^{x/2}$:
$$\int \frac{e^{x/2}}{7 + e^x}\, dx = 2\int \frac{dt}{7 + t^2} = \frac{2}{\sqrt{7}}\tan^{-1}\left(\frac{e^{x/2}}{\sqrt{7}}\right) + c$$

**c)** With $t = \cos(x)$, then $u^2 = e^t - 1$:
$$\int \frac{\sin(x)}{\sqrt{e^{\cos(x)} - 1}}\, dx = -\int \frac{dt}{\sqrt{e^t - 1}} = -\int \frac{2\, du}{1 + u^2} = -2\tan^{-1}\left(\sqrt{e^{\cos(x)} - 1}\right) + c$$
Equivalently, with $t = e^{\frac{1}{2}\cos(x)}$:
$$= -2\int \frac{dt}{t\sqrt{t^2 - 1}} = -2\sec^{-1}\left(e^{\frac{1}{2}\cos(x)}\right) + c$$
