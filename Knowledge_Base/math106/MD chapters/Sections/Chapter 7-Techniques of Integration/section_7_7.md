---
course: MATH106
book_chapter: 7
book_section: 7.7
ksu_chapter: 3
section_title: Improper Integrals
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: [1, 2, 4, 7, 13, 14, 15, 17]
topic_tags: [improper-integral, infinite-limits, discontinuous-integrand]
difficulty: UNKNOWN
in_syllabus: true
enrichment: UNKNOWN
status: draft
---

# Improper Integrals

## Metadata
**Course:** MATH106
**Book:** Calculus (Swokowski)
**Edition:** 6th
**Chapter Number:** 7
**Chapter Title:** Techniques of Integration
**Section Number:** 7.7
**Section Title:** Improper Integrals

## Definitions
**Definition (7.7) — Improper Integrals with Infinite Limits**
(i) If $f$ is continuous on $[a, \infty)$: $\int_a^{\infty} f(x) \, dx = \lim_{t \to \infty} \int_a^t f(x) \, dx$, provided the limit exists.
(ii) If $f$ is continuous on $(-\infty, a]$: $\int_{-\infty}^a f(x) \, dx = \lim_{t \to -\infty} \int_t^a f(x) \, dx$, provided the limit exists.

**Definition (7.8) — Both Limits Infinite**
Let $f$ be continuous everywhere. For any real number $a$:
$$\int_{-\infty}^{\infty} f(x) \, dx = \int_{-\infty}^a f(x) \, dx + \int_a^{\infty} f(x) \, dx,$$
provided **both** improper integrals on the right converge. If either diverges, the whole thing diverges. This is not the same as $\lim_{t \to \infty}\int_{-t}^t f(x)\,dx$ (consider $f(x) = x$).

**Definition (7.9) — Discontinuous Integrand**
(i) If $f$ is continuous on $[a, b)$ and discontinuous at $b$: $\int_a^b f(x) \, dx = \lim_{t \to b^-} \int_a^t f(x) \, dx$, provided the limit exists.
(ii) If $f$ is continuous on $(a, b]$ and discontinuous at $a$: $\int_a^b f(x) \, dx = \lim_{t \to a^+} \int_t^b f(x) \, dx$, provided the limit exists.

**Definition (7.10) — Discontinuity Inside the Interval**
If $f$ has a discontinuity at $c \in (a, b)$ but is continuous elsewhere on $[a, b]$:
$$\int_a^b f(x) \, dx = \int_a^c f(x) \, dx + \int_c^b f(x) \, dx,$$
provided **both** improper integrals on the right converge. If either diverges, the whole diverges.

**Terminology:** an improper integral **converges** if its defining limit exists (the value = that limit). Otherwise it **diverges**.

## Theorems
No formally numbered theorems are introduced in this section.

## Formulas
No new standalone formulas beyond the definitions above.

## Guidelines / Methods
**Critical warning:** the Fundamental Theorem of Calculus cannot be applied to an integral whose integrand has a discontinuity inside the interval. Applying it anyway can produce absurd answers (see Example 10 below). Always check the integrand for discontinuities on the interval of integration first.

**Strategy summary:**
- Infinite limit → replace $\infty$ with $t$, take $\lim_{t \to \infty}$.
- Discontinuity at endpoint → replace that endpoint with $t$, take one-sided limit approaching the endpoint.
- Discontinuity in the interior → split at the discontinuity, treat as two improper integrals; the whole converges only if both pieces do.
- Combined case (discontinuity + infinite limit) → split into pieces where each piece has only one issue.

## Worked Examples
### Example 1
Determine convergence: (a) $\int_2^{\infty} \frac{1}{(x-1)^2} \, dx$, (b) $\int_2^{\infty} \frac{1}{x-1} \, dx$.
**Solution**
(a) $\int_2^{\infty} \frac{dx}{(x-1)^2} = \lim_{t \to \infty} \left[\frac{-1}{x-1}\right]_2^t = \lim_{t \to \infty}\left(\frac{-1}{t-1} + 1\right) = 1$. **Converges to 1.**
(b) $\int_2^{\infty} \frac{dx}{x-1} = \lim_{t \to \infty} [\ln(x-1)]_2^t = \lim_{t \to \infty} \ln(t-1) = \infty$. **Diverges.**

Interesting note: revolving the region under $y = 1/(x-1)$ (which has infinite area for $x \geq 2$) about the $x$-axis gives a solid of finite volume $\pi$ — computed via $\int_2^{\infty} \pi/(x-1)^2 \, dx = \pi$.

### Example 2
Find the area under $y = e^x$ to the left of $x = 1$.
**Solution**
$$\int_{-\infty}^1 e^x \, dx = \lim_{t \to -\infty} [e^x]_t^1 = \lim_{t \to -\infty}(e - e^t) = e.$$

### Example 3
Evaluate $\int_{-\infty}^{\infty} \frac{1}{1+x^2} \, dx$.
**Solution**
Split at $a = 0$ (Definition 7.8):
$$\int_0^{\infty} \frac{dx}{1+x^2} = \lim_{t \to \infty} [\arctan x]_0^t = \frac{\pi}{2}.$$
By symmetry $\int_{-\infty}^0 \frac{dx}{1+x^2} = \frac{\pi}{2}$. **Total: $\pi$** — an area of $\pi$ square units under the bell curve.

### Example 4
Find the work to project a 100-lb object from Earth's surface (radius 4000 mi) to a point outside Earth's gravitational field.
**Solution**
Gravitational force at distance $x$ from Earth's center: $f(x) = k/x^2$. At the surface: $100 = k/(4000)^2$, so $k = 16 \times 10^8$. Then:
$$W = \int_{4000}^{\infty} \frac{16 \times 10^8}{x^2} \, dx = 16 \times 10^8 \lim_{t \to \infty}\left[-\frac{1}{x}\right]_{4000}^t = \frac{16 \times 10^8}{4000} = 4 \times 10^5 \text{ mi-lb}.$$
Converting: $W \approx 2.1 \times 10^9$ ft-lb ≈ 2 billion ft-lb.

### Example 5
Estimate $\int_{-\infty}^{\infty} e^{-x^2} \, dx$ numerically (Gaussian integral — no elementary antiderivative).
**Solution**
By symmetry, $= 2\int_0^{\infty} e^{-x^2} \, dx$. Compute $\int_0^t e^{-x^2}\,dx$ for growing $t$ using Simpson's rule:

$t = 1$: 0.7468; $t = 2$: 0.8821; $t = 3$: 0.8862; $t = 4$: 0.88623; $t = 5,6,7$: 0.886226925453.

Values stabilize, so $\int_0^{\infty} e^{-x^2} \, dx \approx 0.886226925453$, giving $\int_{-\infty}^{\infty} e^{-x^2} \, dx \approx 1.7725$. (Exact value: $\sqrt{\pi}$.)

### Example 6
Bound the error $\int_7^{\infty} e^{-x^2} \, dx$ by comparison.
**Solution**
For $x > 1$: $0 < e^{-x^2} < xe^{-x^2}$. So:
$$\int_7^{\infty} e^{-x^2} \, dx < \int_7^{\infty} xe^{-x^2} \, dx = \lim_{s \to \infty}\left[-\tfrac{1}{2}e^{-x^2}\right]_7^s = \tfrac{1}{2}e^{-49} \approx 2.62 \times 10^{-22}.$$
Negligible — this validates truncating Example 5's integral at $t = 7$.

### Example 7
A gas well produces at rate $W(t) = 750e^{-0.1t} - 450e^{-0.3t}$ thousand ft³/yr. Total lifetime production?
**Solution**
$$\int_0^{\infty} W(t) \, dt = \lim_{N \to \infty}\left[\frac{750}{-0.1}e^{-0.1t} - \frac{450}{-0.3}e^{-0.3t}\right]_0^N = 0 - (-7500 + 1500) = 6000.$$
**6 million cubic feet total.**

### Example 8
Evaluate $\int_0^3 \frac{1}{\sqrt{3-x}} \, dx$.
**Solution**
Integrand has infinite discontinuity at $x = 3$. By Definition (7.9)(i):
$$\lim_{t \to 3^-} \int_0^t \frac{dx}{\sqrt{3-x}} = \lim_{t \to 3^-}[-2\sqrt{3-x}]_0^t = \lim_{t \to 3^-}(-2\sqrt{3-t} + 2\sqrt{3}) = 2\sqrt{3}.$$

### Example 9
Convergence of $\int_0^1 \frac{1}{x} \, dx$?
**Solution**
Discontinuity at $x = 0$. By (7.9)(ii):
$$\lim_{t \to 0^+} \int_t^1 \frac{dx}{x} = \lim_{t \to 0^+}(0 - \ln t) = \infty.$$
**Diverges.**

### Example 10
Convergence of $\int_0^4 \frac{1}{(x-3)^2} \, dx$?
**Solution**
Discontinuity at $x = 3 \in (0, 4)$. By Definition (7.10):
$$\int_0^4 = \int_0^3 + \int_3^4.$$
Both must converge. Check the first:
$$\int_0^3 \frac{dx}{(x-3)^2} = \lim_{t \to 3^-}\left[\frac{-1}{x-3}\right]_0^t = \lim_{t \to 3^-}\left(\frac{-1}{t-3} - \tfrac{1}{3}\right) = \infty.$$
**Diverges** (no need to check the second).

**Warning demonstrated:** blindly applying FTC would give $\left[\frac{-1}{x-3}\right]_0^4 = -1 - \tfrac{1}{3} = -\tfrac{4}{3}$ — impossible, since the integrand $(x-3)^{-2}$ is never negative. Never apply FTC across a discontinuity.

### Example 11
Show the period of an oscillating weight is $T = 2\int_{-c}^c \frac{1}{v(y)} \, dy$, where $v(y)$ is velocity at position $y$.
**Solution**
Partition $[-c, c]$. For subinterval $[y_{k-1}, y_k]$, distance $\Delta y_k \approx v(w_k)\Delta t_k$, so $\Delta t_k \approx \Delta y_k / v(w_k)$. Summing over both halves of one full oscillation and taking the limit:
$$T = 2\sum_k \Delta t_k \approx 2\sum_k \frac{\Delta y_k}{v(w_k)} \to 2\int_{-c}^c \frac{1}{v(y)} \, dy.$$
The integral is improper because $v(c) = v(-c) = 0$ (velocity vanishes at the turning points).

## Exercises
*   1. Determine whether the integral converges or diverges, and if it converges, find its value: $\int_1^{\infty} \frac{1}{x^{4/3}} \, dx$
*   2. Determine whether the integral converges or diverges, and if it converges, find its value: $\int_{-\infty}^0 \frac{1}{(x - 1)^3} \, dx$
*   4. Determine whether the integral converges or diverges, and if it converges, find its value: $\int_0^{\infty} \frac{x}{1 + x^2} \, dx$
*   7. Determine whether the integral converges or diverges, and if it converges, find its value: $\int_0^{\infty} e^{-2x} \, dx$
*   13. Determine whether the integral converges or diverges, and if it converges, find its value: $\int_0^{\infty} \frac{\cos x}{1 + \sin^2 x} \, dx$
*   14. Determine whether the integral converges or diverges, and if it converges, find its value: $\int_{-\infty}^2 \frac{1}{x^2 + 4} \, dx$
*   15. Determine whether the integral converges or diverges, and if it converges, find its value: $\int_{-\infty}^{\infty} xe^{-x^2} \, dx$
*   17. Determine whether the integral converges or diverges, and if it converges, find its value: $\int_1^{\infty} \frac{\ln x}{x} \, dx$