# section_7_7.md

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

---

## Metadata

- **Course:** MATH106
- **Book:** Calculus (Swokowski)
- **Edition:** 6th
- **Chapter Number:** 7
- **Chapter Title:** Techniques of Integration
- **Section Number:** 7.7
- **Section Title:** Improper Integrals

---

## Definitions

### Definition (7.7)

**(i)** If $f$ is continuous on $[a, \infty)$, then

$$\int_a^{\infty} f(x) \, dx = \lim_{t \to \infty} \int_a^t f(x) \, dx,$$

provided the limit exists.

**(ii)** If $f$ is continuous on $(-\infty, a]$, then

$$\int_{-\infty}^a f(x) \, dx = \lim_{t \to -\infty} \int_t^a f(x) \, dx,$$

provided the limit exists.

### Definition (7.8)

Let $f$ be continuous for every $x$. If $a$ is any real number, then

$$\int_{-\infty}^{\infty} f(x) \, dx = \int_{-\infty}^a f(x) \, dx + \int_a^{\infty} f(x) \, dx,$$

provided both of the improper integrals on the right converge.

### Definition (7.9)

**(i)** If $f$ is continuous on $[a, b)$ and discontinuous at $b$, then

$$\int_a^b f(x) \, dx = \lim_{t \to b^-} \int_a^t f(x) \, dx,$$

provided the limit exists.

**(ii)** If $f$ is continuous on $(a, b]$ and discontinuous at $a$, then

$$\int_a^b f(x) \, dx = \lim_{t \to a^+} \int_t^b f(x) \, dx,$$

provided the limit exists.

### Definition (7.10)

If $f$ has a discontinuity at a number $c$ in the open interval $(a, b)$ but is continuous elsewhere on $[a, b]$, then

$$\int_a^b f(x) \, dx = \int_a^c f(x) \, dx + \int_c^b f(x) \, dx,$$

provided _both_ of the improper integrals on the right converge. If both converge, then the value of the improper integral $\int_a^b f(x) \, dx$ is the sum of the two values.

---

## Theorems

No formally numbered theorems are introduced in this section.

---

## Formulas

No new standalone formulas are introduced in this section beyond the definitions above.

---

## Concepts

### Integrals with Infinite Limits of Integration

In our work with definite integrals of the form $\int_a^b f(x) \, dx$, we have considered almost exclusively _proper integrals_—that is, situations in which the function $f$ is continuous on a closed interval $[a, b]$ of finite length. In this section, we extend the definite integral to cases where the interval may be of infinite length or where the function $f$ has isolated discontinuities on the interval.

Suppose that a function $f$ is continuous and nonnegative on an infinite interval $[a, \infty)$ and $\lim_{x \to \infty} f(x) = 0$. If $t > a$, then the area $A(t)$ under the graph of $f$ from $a$ to $t$, as illustrated in Figure 7.9, is

$$A(t) = \int_a^t f(x) \, dx.$$

If $\lim_{t \to \infty} A(t)$ exists, then the limit may be interpreted as the area of the region that lies under the graph of $f$, over the $x$-axis, and to the right of $x = a$, as illustrated in Figure 7.10. The symbol $\int_a^{\infty} f(x) \, dx$ is used to denote this number. If $\lim_{t \to \infty} A(t) = \infty$, we cannot assign an area to this (unbounded) region.

Part (i) of Definition (7.7) generalizes the preceding remarks to the case where $f(x)$ may be negative for some $x$ in $[a, \infty)$.

If $f(x) \geq 0$ for every $x$, then the limit in Definition (7.7)(ii) may be regarded as the area under the graph of $f$, over the $x$-axis, and to the _left_ of $x = a$ (see Figure 7.11).

The expressions in Definition (7.7) are **improper integrals**. They differ from definite integrals in that one of the limits of integration is not a real number. An improper integral is said to **converge** if the limit exists, and the limit is the **value** of the improper integral. If the limit does not exist, the improper integral **diverges**.

Definition (7.7) is useful in many applications. In Example 4, we shall use an improper integral to calculate the work required to project an object from the surface of the earth to a point outside of the earth's gravitational field. Another important application occurs in the investigation of infinite series.

An improper integral may have _two_ infinite limits of integration, as in Definition (7.8).

If either of the integrals on the right in Definition (7.8) diverges, then $\int_{-\infty}^{\infty} f(x) \, dx$ is said to **diverge**. It can be shown that (7.8) does not depend on the choice of the real number $a$. It can also be shown that $\int_{-\infty}^{\infty} f(x) \, dx$ is not necessarily the same as $\lim_{t \to \infty} \int_{-t}^t f(x) \, dx$ (consider $f(x) = x$).

We now consider a physical application of an improper integral. If $a$ and $b$ are the coordinates of two points $A$ and $B$ on a coordinate line $l$ (see Figure 7.16) and if $f(x)$ is the force acting at the point $P$ with coordinate $x$, then, by Definition (5.21), the work done as $P$ moves from $A$ to $B$ is given by

$$W = \int_a^b f(x) \, dx.$$

In similar fashion, the improper integral $\int_a^{\infty} f(x) \, dx$ may be used to define the work done as $P$ moves indefinitely to the right (in applications, we use the terminology $P$ _moves to infinity_). For example, if $f(x)$ is the force of attraction between a particle fixed at point $A$ and a (movable) particle at $P$ and if $c > a$, then $\int_c^{\infty} f(x) \, dx$ represents the work required to move $P$ from the point with coordinate $c$ to infinity.

In applications, we frequently encounter integrals for which there exist no antiderivatives that can be expressed in simple terms involving standard functions we have studied. The indefinite integral $\int e^{-x^2} \, dx$ is an example. If one of these integrals occurs as a definite integral, then we must use numerical integration techniques for evaluation. The next example illustrates how we may use such techniques for an improper integral.

In Example 5, we estimated $\int_0^{\infty} e^{-x^2} \, dx$ by a numerical approximation of $\int_0^7 e^{-x^2} \, dx$. With this approach, we ignored the contribution to the improper integral due to $\int_7^{\infty} e^{-x^2} \, dx$. By comparing our integral to one whose antiderivative we _can_ find, we can estimate the error made by using this approach.

In economics, improper integrals often occur when considering the entire _future_ amount of a quantity whose rate of flow is known as a function of time. For example, if the revenue flow from sales of a particular item is estimated to be $R(t)$ dollars per time unit at time $t$, with $t = 0$ corresponding to the present, then the entire future revenue from sales is given by $\int_0^{\infty} R(t) \, dt$. Since $t$ is the variable of integration, we can modify Definition (7.7) as follows: $\int_0^{\infty} R(t) \, dt = \lim_{N \to \infty} \int_0^N R(t) \, dt$.

### Integrals with Discontinuous Integrands

If a function $f$ is continuous on a closed interval $[a, b]$, then, by Theorem (4.20), the definite integral $\int_a^b f(x) \, dx$ exists. If $f$ has an infinite discontinuity at some number in the interval, it may still be possible to assign a value to the integral. Suppose, for example, that $f$ is continuous and nonnegative on the half-open interval $[a, b)$ and $\lim_{x \to b^-} f(x) = \infty$. If $a < t < b$, then the area $A(t)$ under the graph of $f$ from $a$ to $t$ (see Figure 7.19) is

$$A(t) = \int_a^t f(x) \, dx.$$

If $\lim_{t \to b^-} A(t)$ exists, then the limit may be interpreted as the area of the unbounded region that lies under the graph of $f$, over the $x$-axis, and between $x = a$ and $x = b$. We shall denote this number by $\int_a^b f(x) \, dx$.

For the situation illustrated in Figure 7.20, $\lim_{x \to a^+} f(x) = \infty$, and we define $\int_a^b f(x) \, dx$ as the limit of $\int_t^b f(x) \, dx$ as $t \to a^+$.

As in the preceding section, the integrals defined in (7.9) are referred to as _improper integrals_ and they _converge_ if the limits exist. The limits are called the _values_ of the improper integrals. If the limits do not exist, the improper integrals _diverge_.

The graph of a function satisfying the conditions of Definition (7.10) is sketched in Figure 7.21.

A definition similar to (7.10) is used if $f$ has any finite number of discontinuities in $(a, b)$. For example, suppose $f$ has discontinuities at $c_1$ and $c_2$, with $c_1 < c_2$, but is continuous elsewhere on $[a, b]$. One possibility is illustrated in Figure 7.22. In this case, we choose a number $k$ between $c_1$ and $c_2$ and express $\int_a^b f(x) \, dx$ as a sum of four improper integrals over the intervals $[a, c_1]$, $[c_1, k]$, $[k, c_2]$, and $[c_2, b]$, respectively. By definition, $\int_a^b f(x) \, dx$ converges if and only if each of the four improper integrals in the sum converges. We can show that this definition is independent of the number $k$.

Finally, if $f$ is continuous on $(a, b)$ but has infinite discontinuities at $a$ and $b$, then we again define $\int_a^b f(x) \, dx$ by means of (7.10).

It is important to note that the fundamental theorem of calculus cannot be applied to the integral in Example 10, since the function given by the integrand is not continuous on $[0, 4]$. If we had (incorrectly) applied the fundamental theorem, we would have obtained

$$\left[\frac{-1}{x - 3}\right]_0^4 = -1 - \frac{1}{3} = -\frac{4}{3}.$$

This result is obviously incorrect, since the integrand is never negative.

An improper integral may have both a discontinuity in the integrand and an infinite limit of integration. Integrals of this type may be investigated by expressing them as sums of improper integrals, each of which has _one_ of the forms previously defined. As an illustration, since the integrand of $\int_0^{\infty} (1/\sqrt{x}) \, dx$ is discontinuous at $x = 0$, we choose any number greater than 0—say, 1—and write

$$\int_0^{\infty} \frac{1}{\sqrt{x}} \, dx = \int_0^1 \frac{1}{\sqrt{x}} \, dx + \int_1^{\infty} \frac{1}{\sqrt{x}} \, dx.$$

We can show that the first integral on the right side of the equation converges and the second diverges. Hence (by definition) the given integral diverges.

Improper integrals of the types considered in this section occur in physical applications. Figure 7.23 is a schematic drawing of a spring with an attached weight that is oscillating between points with coordinates $-c$ and $c$ on a coordinate line $y$ (the $y$-axis has been positioned at the right for clarity). The **period** $T$ is the time required for one complete oscillation—that is, _twice_ the time required for the weight to cover the interval $[-c, c]$.

---

## Examples

### Example 1

#### Problem

Determine whether the integral converges or diverges, and if it converges, find its value.

(a) $\displaystyle\int_2^{\infty} \frac{1}{(x - 1)^2} \, dx$ $\qquad$ (b) $\displaystyle\int_2^{\infty} \frac{1}{x - 1} \, dx$

#### Solution

**(a)** By Definition (7.7)(i),

$$\int_2^{\infty} \frac{1}{(x - 1)^2} \, dx = \lim_{t \to \infty} \int_2^t \frac{1}{(x - 1)^2} \, dx = \lim_{t \to \infty} \left[\frac{-1}{x - 1}\right]_2^t$$

$$= \lim_{t \to \infty} \left(\frac{-1}{t - 1} + \frac{1}{2 - 1}\right) = 0 + 1 = 1.$$

Thus, the integral converges and has the value 1.

**(b)** By Definition (7.7)(i),

$$\int_2^{\infty} \frac{1}{x - 1} \, dx = \lim_{t \to \infty} \int_2^t \frac{1}{x - 1} \, dx$$

$$= \lim_{t \to \infty} \Big[\ln(x - 1)\Big]_2^t$$

$$= \lim_{t \to \infty} [\ln(t - 1) - \ln(2 - 1)]$$

$$= \lim_{t \to \infty} \ln(t - 1) = \infty.$$

Since the limit does not exist, the improper integral diverges.

---

The graphs of the two functions given by the integrands in Example 1, together with the (unbounded) regions that lie under the graphs for $x \geq 2$, are sketched in Figures 7.12 and 7.13. Note that although the graphs have the same general shape for $x \geq 2$, we may assign an area to the region under the graph shown in Figure 7.12, but not to that shown in Figure 7.13.

The graph in Figure 7.13 has an interesting property. If we revolve the region under the graph of $y = 1/(x - 1)$ about the $x$-axis, we obtain an unbounded solid of revolution. We may regard the improper integral

$$\int_2^{\infty} \pi \frac{1}{(x - 1)^2} \, dx$$

as the volume of this solid. By Example 1(a), the value of this improper integral is $\pi$. This gives us the curious fact that although we cannot assign an area to the region in Figure 7.13, the volume of the solid of revolution generated by the region is finite.

---

### Example 2

#### Problem

Assign an area to the region that lies under the graph of $y = e^x$, over the $x$-axis, and to the left of $x = 1$.

#### Solution

The region bounded by the graphs of $y = e^x$, $y = 0$, $x = 1$, and $x = t$, for $t < 1$, is sketched in Figure 7.14. The area of the unbounded region to the left of $x = 1$ is

$$\int_{-\infty}^1 e^x \, dx = \lim_{t \to -\infty} \int_t^1 e^x \, dx = \lim_{t \to -\infty} \Big[e^x\Big]_t^1$$

$$= \lim_{t \to -\infty} (e - e^t) = e - 0 = e.$$

---

### Example 3

#### Problem

(a) Evaluate $\displaystyle\int_{-\infty}^{\infty} \frac{1}{1 + x^2} \, dx$.

(b) Sketch the graph of $f(x) = 1/(1 + x^2)$ and interpret the integral in part (a) as an area.

#### Solution

**(a)** Using Definition (7.8), with $a = 0$, yields

$$\int_{-\infty}^{\infty} \frac{1}{1 + x^2} \, dx = \int_{-\infty}^0 \frac{1}{1 + x^2} \, dx + \int_0^{\infty} \frac{1}{1 + x^2} \, dx.$$

Next, applying Definition (7.7)(i), we have

$$\int_0^{\infty} \frac{1}{1 + x^2} \, dx = \lim_{t \to \infty} \int_0^t \frac{1}{1 + x^2} \, dx = \lim_{t \to \infty} \Big[\arctan x\Big]_0^t$$

$$= \lim_{t \to \infty} (\arctan t - \arctan 0) = \frac{\pi}{2} - 0 = \frac{\pi}{2}.$$

Similarly, we may show, by using Definition (7.7)(ii), that

$$\int_{-\infty}^0 \frac{1}{1 + x^2} \, dx = \frac{\pi}{2}.$$

Consequently, the given improper integral converges and has the value $(\pi/2) + (\pi/2) = \pi$.

**(b)** The graph of $y = 1/(1 + x^2)$ is sketched in Figure 7.15. As in our previous discussion, the unbounded region that lies under the graph and above the $x$-axis may be assigned an area of $\pi$ square units.

---

### Example 4

#### Problem

Let $l$ be a coordinate line with origin $O$ at the center of the earth, as shown in Figure 7.17. The gravitational force exerted at a point on $l$ that is a distance $x$ from $O$ is given by $f(x) = k/x^2$, for some constant $k$. Using 4000 mi as the radius of the earth, find the work required to project an object weighing 100 lb along $l$, from the surface to a point outside of the earth's gravitational field.

#### Solution

Theoretically, there is _always_ a gravitational force $f(x)$ acting on the object; however, we may think of projecting the object from the surface to infinity. From the preceding discussion, we wish to find

$$W = \int_{4000}^{\infty} f(x) \, dx.$$

By definition, $f(x) = k/x^2$ is the weight of an object that is a distance $x$ from $O$, and hence

$$100 = f(4000) = \frac{k}{(4000)^2},$$

or, equivalently,

$$k = 100(4000)^2 = 10^2 \cdot 16 \cdot 10^6 = 16 \cdot 10^8.$$

Thus,

$$f(x) = (16 \cdot 10^8)\frac{1}{x^2}$$

and the required work is

$$W = \int_{4000}^{\infty} (16 \cdot 10^8)\frac{1}{x^2} \, dx = 16 \cdot 10^8 \lim_{t \to \infty} \int_{4000}^t \frac{1}{x^2} \, dx$$

$$= 16 \cdot 10^8 \lim_{t \to \infty} \left[-\frac{1}{x}\right]_{4000}^t = 16 \cdot 10^8 \lim_{t \to \infty} \left(-\frac{1}{t} + \frac{1}{4000}\right)$$

$$= \frac{16 \cdot 10^8}{4000} = 4 \cdot 10^5 \text{ mi-lb.}$$

In terms of foot-pounds,

$$W = 5280 \cdot 4 \cdot 10^5 \approx (2.1)10^9 \text{ ft-lb},$$

or approximately 2 billion ft-lb.

---

### Example 5

#### Problem

The improper integral $\int_{-\infty}^{\infty} e^{-x^2} \, dx$ occurs frequently in the study of probability and statistics. Estimate the value of this integral using Simpson's rule.

#### Solution

The function $f(x) = e^{-x^2}$ has the property that $f(-x) = f(x)$. Hence, the graph of $y = f(x)$ is symmetric about the $y$-axis (see Figure 7.18). Thus,

$$\int_{-\infty}^{\infty} e^{-x^2} \, dx = 2\int_0^{\infty} e^{-x^2} \, dx.$$

Since

$$\int_0^{\infty} e^{-x^2} \, dx = \lim_{t \to \infty} \int_0^t e^{-x^2} \, dx,$$

we estimate the improper integral by numerical integration of $\int_0^t e^{-x^2} \, dx$ for successively larger values of $t$. Using Simpson's rule with $\Delta x = 0.01$, we obtain the values listed in the following table:

| $t$ | $\int_0^t e^{-x^2} \, dx$ |
| --- | ------------------------- |
| 1   | 0.746824132818            |
| 2   | 0.882081390760            |
| 3   | 0.886207348259            |
| 4   | 0.886226911790            |
| 5   | 0.886226925451            |
| 6   | 0.886226925453            |
| 7   | 0.886226925453            |

The numerical values in the table appear to converge rather rapidly for relatively small values of $t$. This result is consistent with Figure 7.18, which shows the graph of $f(x) = e^{-x^2}$ quickly approaching 0 as $x$ moves away from 0.

It appears then that $\int_0^{\infty} e^{-x^2} \, dx \approx 0.886226925453$. Thus, our final estimate is $\int_{-\infty}^{\infty} e^{-x^2} \, dx \approx 2(0.886226925453) = 1.772453850906$. In Chapter 9, we shall determine that the exact value of the improper integral is $\sqrt{\pi} \approx 1.772453850906$.

---

### Example 6

#### Problem

Obtain an upper bound for $\int_7^{\infty} e^{-x^2} \, dx$ by comparing this improper integral to $\int_7^{\infty} xe^{-x^2} \, dx$.

#### Solution

For $x > 1$, we have $0 < e^{-x^2} < xe^{-x^2}$. Hence,

$$\int_7^{\infty} e^{-x^2} \, dx < \int_7^{\infty} xe^{-x^2} \, dx = \lim_{s \to \infty} \int_7^s xe^{-x^2} \, dx$$

$$= \lim_{s \to \infty} \left(-\tfrac{1}{2}e^{-x^2}\right)\Big|_7^s = \tfrac{1}{2}e^{-t^2}.$$

Thus, the error made by ignoring $\int_7^{\infty} e^{-x^2} \, dx$ is less than $\frac{1}{2}e^{-49}$, or about 2.621E−22.

---

### Example 7

#### Problem

In assessing the potential revenue or profit from a mineral or energy source, economists must estimate the total amount of the resource that can be recovered from the site. Mining engineers determine that $t$ years from now, a newly opened natural gas well will produce gas at a rate of

$$W(t) = 750e^{-0.1t} - 450e^{-0.3t}$$

thousand cubic feet per year. Estimate the total amount of gas that this well could produce.

#### Solution

We wish to estimate the entire future production of the well if it continues to pump indefinitely. This amount is given by

$$\int_0^{\infty} W(t) \, dt$$

$$= \int_0^{\infty} (750e^{-0.1t} - 450e^{-0.3t}) \, dt$$

$$= \lim_{N \to \infty} \int_0^N (750e^{-0.1t} - 450e^{-0.3t}) \, dt$$

$$= \lim_{N \to \infty} \left[\frac{750}{-0.1}e^{-0.1t} - \frac{450}{-0.3}e^{-0.3t}\right]_{t=0}^{t=N}$$

$$= \lim_{N \to \infty} \left[\frac{750}{-0.1}e^{-0.1N} - \frac{450}{-0.3}e^{-0.3N} - \left(\frac{750}{-0.1}e^0 - \frac{450}{-0.3}e^0\right)\right]$$

$$= \lim_{N \to \infty} \left[\frac{750}{(-0.1)e^{0.1N}} - \frac{450}{(-0.3)e^{0.3N}} - (-7500 + 1500)\right]$$

$$= 0 - 0 - (-6000) = 6000.$$

Thus, we estimate that this well will produce $(6000)(1000) = 6$ million cubic feet of natural gas.

---

### Example 8

#### Problem

Evaluate $\displaystyle\int_0^3 \frac{1}{\sqrt{3 - x}} \, dx$.

#### Solution

Since the integrand has an infinite discontinuity at the number $x = 3$, we apply Definition (7.9)(i) as follows:

$$\int_0^3 \frac{1}{\sqrt{3 - x}} \, dx = \lim_{t \to 3^-} \int_0^t \frac{1}{\sqrt{3 - x}} \, dx$$

$$= \lim_{t \to 3^-} \Big[-2\sqrt{3 - x}\Big]_0^t$$

$$= \lim_{t \to 3^-} (-2\sqrt{3 - t} + 2\sqrt{3})$$

$$= 0 + 2\sqrt{3} = 2\sqrt{3}$$

---

### Example 9

#### Problem

Determine whether the improper integral $\displaystyle\int_0^1 \frac{1}{x} \, dx$ converges or diverges.

#### Solution

The integrand is undefined at $x = 0$. Applying (7.9)(ii) gives us

$$\int_0^1 \frac{1}{x} \, dx = \lim_{t \to 0^+} \int_t^1 \frac{1}{x} \, dx = \lim_{t \to 0^+} \Big[\ln x\Big]_t^1 = \lim_{t \to 0^+} (0 - \ln t) = \infty.$$

Since the limit does not exist, the improper integral diverges.

---

### Example 10

#### Problem

Determine whether the improper integral

$$\int_0^4 \frac{1}{(x - 3)^2} \, dx$$

converges or diverges.

#### Solution

The integrand is undefined at $x = 3$. Since this number is in the interval $(0, 4)$, we use Definition (7.10) with $c = 3$:

$$\int_0^4 \frac{1}{(x - 3)^2} \, dx = \int_0^3 \frac{1}{(x - 3)^2} \, dx + \int_3^4 \frac{1}{(x - 3)^2} \, dx$$

For the integral on the left to converge, _both_ integrals on the right must converge. Equivalently, the integral on the left diverges if either of the integrals on the right diverges. Applying Definition (7.9)(i) to the first integral on the right gives us

$$\int_0^3 \frac{1}{(x - 3)^2} \, dx = \lim_{t \to 3^-} \int_0^t \frac{1}{(x - 3)^2} \, dx = \lim_{t \to 3^-} \left[\frac{-1}{x - 3}\right]_0^t$$

$$= \lim_{t \to 3^-} \left(\frac{-1}{t - 3} - \frac{1}{3}\right) = \infty.$$

Thus, the given improper integral diverges.

---

It is important to note that the fundamental theorem of calculus cannot be applied to the integral in Example 10, since the function given by the integrand is not continuous on $[0, 4]$. If we had (incorrectly) applied the fundamental theorem, we would have obtained

$$\left[\frac{-1}{x - 3}\right]_0^4 = -1 - \frac{1}{3} = -\frac{4}{3}.$$

This result is obviously incorrect, since the integrand is never negative.

---

### Example 11

#### Problem

Let $v(y)$ denote the velocity of the weight in Figure 7.23 when it is at the point with coordinate $y$ in $[-c, c]$. Show that the period $T$ is given by

$$T = 2\int_{-c}^c \frac{1}{v(y)} \, dy.$$

#### Solution

Let us partition $[-c, c]$ in the usual way, and let $\Delta y_k = y_k - y_{k-1}$ denote the distance that the weight travels during the time interval $\Delta t_k$. If $w_k$ is any number in the subinterval $[y_{k-1}, y_k]$, then $v(w_k)$ is the velocity of the weight when it is at the point with coordinate $w_k$. If the norm of the partition is small and if we assume that $v$ is a continuous function, then the distance $\Delta y_k$ may be approximated by the product $v(w_k)\Delta t_k$; that is,

$$\Delta y_k \approx v(w_k)\Delta t_k.$$

Hence, the time required for the weight to cover the distance $\Delta y_k$ may be approximated by

$$\Delta t_k \approx \frac{1}{v(w_k)}\Delta y_k$$

and, therefore,

$$T = 2\sum_k \Delta t_k \approx 2\sum_k \frac{1}{v(w_k)}\Delta y_k.$$

By considering the limit of the sums on the right and using the definition of definite integral, we conclude that

$$T = 2\int_{-c}^c \frac{1}{v(y)} \, dy.$$

Note that $v(c) = 0$ and $v(-c) = 0$, so the integral is improper.

---

## Remarks

- The graphs of $y = 1/(x-1)^2$ and $y = 1/(x-1)$ both have the same general shape for $x \geq 2$, but we may assign an area to the region under the first graph and not the second. Moreover, the volume of the solid of revolution obtained by revolving the region under $y = 1/(x-1)$ about the $x$-axis is finite ($\pi$), even though the area of the region is infinite.

- $\int_{-\infty}^{\infty} f(x) \, dx$ is not necessarily the same as $\lim_{t \to \infty} \int_{-t}^t f(x) \, dx$ (consider $f(x) = x$).

- The fundamental theorem of calculus cannot be applied if the integrand has a discontinuity in the interval of integration. Doing so may produce an incorrect result.

- An improper integral may have both a discontinuity in the integrand and an infinite limit of integration.

---

## Figures

### Figure 7.9

Graph of a nonnegative continuous function $y = f(x)$ on $[a, t]$ with the area $\int_a^t f(x) \, dx$ shaded beneath the curve, above the $x$-axis.

### Figure 7.10

Graph of a nonnegative continuous function $y = f(x)$ on $[a, \infty)$ with the unbounded region $\int_a^{\infty} f(x) \, dx$ shaded beneath the curve, above the $x$-axis, with $t \to \infty$ indicated.

### Figure 7.11

Graph of a nonnegative continuous function $y = f(x)$ on $(-\infty, a]$ with the unbounded region $\int_{-\infty}^a f(x) \, dx$ shaded beneath the curve, with $t \to -\infty$ indicated.

### Figure 7.12

Graph of $y = \frac{1}{(x-1)^2}$ with a vertical asymptote at $x = 1$ and the shaded region under the curve for $x \geq 2$.

### Figure 7.13

Graph of $y = \frac{1}{x-1}$ with a vertical asymptote at $x = 1$ and the shaded region under the curve for $x \geq 2$.

### Figure 7.14

Graph of $y = e^x$ with the shaded region under the curve to the left of $x = 1$, bounded by $y = 0$ and $x = t$ for $t < 1$.

### Figure 7.15

Graph of $y = \frac{1}{1+x^2}$ showing a bell-shaped curve symmetric about the $y$-axis with maximum value $1$ at $x = 0$, and the entire unbounded region under the curve shaded.

### Figure 7.16

A coordinate line $l$ with points $A$ and $B$ at coordinates $a$ and $b$, respectively, and a movable point $P$ at coordinate $x$.

### Figure 7.17

An illustration of the Earth with a coordinate line $l$ extending outward from its center $O$.

### Figure 7.18

Graph of $f(x) = e^{-x^2}$ showing a bell-shaped curve symmetric about the $y$-axis with $y = f(x)$ labeled.

### Figure 7.19

Graph of a nonnegative continuous function $y = f(x)$ on $[a, b)$ with $\lim_{x \to b^-} f(x) = \infty$, showing the shaded area $\int_a^t f(x) \, dx$ for $a < t < b$, with a vertical asymptote at $x = b$.

### Figure 7.20

Graph of a nonnegative continuous function $y = f(x)$ on $(a, b]$ with $\lim_{x \to a^+} f(x) = \infty$, showing the shaded area $\int_t^b f(x) \, dx$ for $a < t < b$, with a vertical asymptote at $x = a$.

### Figure 7.21

Graph of a function with a vertical asymptote at an interior point $c$ in the interval $(a, b)$, with the curve going to infinity at $x = c$.

### Figure 7.22

Graph of a function with vertical asymptotes at two interior points $c_1$ and $c_2$ in the interval $(a, b)$, with a point $k$ chosen between $c_1$ and $c_2$.

### Figure 7.23

A schematic drawing of a vertical spring with an attached weight oscillating between positions $-c$ and $c$ on a coordinate line $y$, with the equilibrium position at $0$.

---

## Keywords

- Improper integral
- Proper integral
- Convergent integral
- Divergent integral
- Infinite limits of integration
- Discontinuous integrand
- Infinite discontinuity
- Value of an improper integral
- Work
- Gravitational force
- Numerical integration
- Simpson's rule
- Period of oscillation
- Revenue flow
- Gaussian integral
