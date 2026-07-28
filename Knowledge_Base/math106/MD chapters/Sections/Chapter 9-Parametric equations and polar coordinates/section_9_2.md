---
source_file: "9-2.pdf"
course: MATH106
book_chapter: 9
book_section: 9.2
ksu_chapter: UNKNOWN
section_title: ARC LENGTH AND SURFACE AREA
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: [1, 3, 5, 9, 11, 13, 21, 23, 29, 31]
topic_tags: [parametric-equations, arc-length, surface-area, derivative, second-derivative]
difficulty: UNKNOWN
in_syllabus: true
enrichment: UNKNOWN
status: draft
---

## Metadata
* **Course:** MATH106
* **Book Chapter:** 9
* **Chapter Title:** Parametric Equations and Polar Coordinates
* **Section Number:** 9.2
* **Section Title:** Arc Length and Surface Area

## Definitions
No formal boxed definitions.[cite: 6]

## Theorems
* **Theorem 9.4**
  If a smooth curve $C$ is given parametrically by $x = f(t)$, $y = g(t)$, then the slope $dy/dx$ of the tangent line to $C$ at $P(x, y)$ is[cite: 6]
  $$\frac{dy}{dx} = \frac{dy/dt}{dx/dt}$$
  provided $\frac{dx}{dt} \ne 0$[cite: 6].

* **Theorem 9.6**
  If a smooth curve $C$ is given parametrically by $x = f(t)$, $y = g(t)$, $a \le t \le b$, and if $C$ does not intersect itself, except possibly for $t = a$ and $t = b$, then the length $L$ of $C$ is[cite: 6]
  $$L = \int_{a}^{b} \sqrt{[f'(t)]^2 + [g'(t)]^2} dt = \int_{a}^{b} \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} dt$$[cite: 6]

* **Theorem 9.8**
  Let a smooth curve $C$ be given by $x = f(t)$, $y = g(t)$, $a \le t \le b$, and suppose $C$ does not intersect itself, except possibly at the points corresponding to $t = a$ and $t = b$[cite: 6]. If $g(t) \ge 0$ throughout $[a, b]$, then the area $S$ of the surface of revolution obtained by revolving $C$ about the x-axis is[cite: 6]
  $$S = \int_{t=a}^{t=b} 2\pi y \, ds = \int_{a}^{b} 2\pi g(t) \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} dt$$[cite: 6]

## Formulas
* **Second Derivative in Parametric Form 9.5**
  If a curve $C$ is parameterized by $x = f(t), y = g(t)$, and $y'$ is a differentiable function of $t$, the second derivative is[cite: 6]:
  $$\frac{d^2y}{dx^2} = \frac{d}{dx}(y') = \frac{dy'/dt}{dx/dt}$$[cite: 6]

* **Parametric Differential of Arc Length 9.7**
  $$ds = \sqrt{(dx)^2 + (dy)^2} = \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} dt$$[cite: 6]

* **Surface Area for Revolution about the y-axis**
  If the curve $C$ is revolved about the y-axis and $x = f(t) \ge 0$ for $a \le t \le b$, then[cite: 6]:
  $$S = \int_{t=a}^{t=b} 2\pi x \, ds = \int_{a}^{b} 2\pi f(t) \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} dt$$[cite: 6]

## Guidelines / Methods
No formal boxed guidelines.[cite: 6]

## Worked Examples
### Example 1
Let $C$ be the curve with parametrization $x = 2t$, $y = t^2 - 1$ for $-1 \le t \le 2$[cite: 6]. Find the slopes of the tangent line and normal line to $C$ at $P(x, y)$[cite: 6].

**Solution**
* **Step 1:** Apply Theorem (9.4) to find the slope of the tangent line[cite: 6].
  $$\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{2t}{2} = t$$[cite: 6]
* **Step 2:** The slope of the normal line is the negative reciprocal of the tangent line's slope[cite: 6].
  $$\text{Normal slope } = -\frac{1}{t}, \text{ provided } t \ne 0$$[cite: 6]

### Example 2
Let $C$ be the curve with parametrization $x = t^3 - 3t$, $y = t^2 - 5t - 1$ for $t$ in $\mathbb{R}$[cite: 6].
(a) Find an equation of the tangent line to $C$ at the point corresponding to $t = 2$[cite: 6].
(b) For what values of $t$ is the tangent line horizontal or vertical?[cite: 6]

**Solution**
* **Step 1 (a):** Find the coordinates of the point at $t=2$[cite: 6].
  $$x(2) = 2^3 - 3(2) = 2, \quad y(2) = 2^2 - 5(2) - 1 = -7$$[cite: 6]
  The point is $(2, -7)$[cite: 6].
* **Step 2 (a):** Use Theorem (9.4) to find the slope[cite: 6].
  $$\frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{2t - 5}{3t^2 - 3}$$[cite: 6]
  $$m = \left. \frac{dy}{dx} \right|_{t=2} = \frac{2(2) - 5}{3(2^2) - 3} = -\frac{1}{9}$$[cite: 6]
* **Step 3 (a):** Use the point-slope form to find the equation of the line[cite: 6].
  $$y + 7 = -\frac{1}{9}(x - 2) \implies x + 9y = -61$$[cite: 6]
* **Step 4 (b):** The tangent line is horizontal when $\frac{dy}{dx} = 0$, meaning the numerator is $0$[cite: 6].
  $$2t - 5 = 0 \implies t = \frac{5}{2}$$[cite: 6]
* **Step 5 (b):** The tangent line is vertical when the denominator is $0$ (and numerator is non-zero)[cite: 6].
  $$3t^2 - 3 = 0 \implies t = 1 \text{ and } t = -1$$[cite: 6]

### Example 3
Let $C$ be the curve with parametrization $x = e^{-t}$, $y = e^{2t}$ for $t$ in $\mathbb{R}$[cite: 6]. Use formulas (9.4) and (9.5) to find $dy/dx$ and $d^2y/dx^2$[cite: 6].

**Solution**
* **Step 1:** Find $dy/dx$ using Theorem (9.4)[cite: 6].
  $$y' = \frac{dy}{dx} = \frac{dy/dt}{dx/dt} = \frac{2e^{2t}}{-e^{-t}} = -2e^{3t}$$[cite: 6]
* **Step 2:** Find $d^2y/dx^2$ using formula (9.5)[cite: 6].
  $$\frac{d^2y}{dx^2} = \frac{dy'/dt}{dx/dt} = \frac{-6e^{3t}}{-e^{-t}} = 6e^{4t}$$[cite: 6]
* **Step 3:** Since $d^2y/dx^2 = 6e^{4t} > 0$ for every $t$, the curve $C$ is concave upward at every point[cite: 6].

### Example 4
Find the length of one arch of the cycloid that has the parametrization $x = t - \sin t, y = 1 - \cos t$ for $t$ in $\mathbb{R}$[cite: 6].

**Solution**
* **Step 1:** One arch corresponds to the interval $t = 0$ to $t = 2\pi$[cite: 6]. Apply Theorem (9.6)[cite: 6].
  $$L = \int_{0}^{2\pi} \sqrt{(1 - \cos t)^2 + (\sin t)^2} dt = \int_{0}^{2\pi} \sqrt{1 - 2\cos t + \cos^2 t + \sin^2 t} dt$$[cite: 6]
* **Step 2:** Simplify the integrand using $\cos^2 t + \sin^2 t = 1$[cite: 6].
  $$L = \int_{0}^{2\pi} \sqrt{2 - 2\cos t} dt = \int_{0}^{2\pi} \sqrt{2} \sqrt{1 - \cos t} dt$$[cite: 6]
* **Step 3:** Use the half-angle formula $1 - \cos t = 2\sin^2\left(\frac{1}{2}t\right)$[cite: 6].
  $$L = \int_{0}^{2\pi} \sqrt{2} \sqrt{2\sin^2\left(\frac{1}{2}t\right)} dt = \int_{0}^{2\pi} 2 \left| \sin\left(\frac{1}{2}t\right) \right| dt$$[cite: 6]
* **Step 4:** Evaluate the integral. Since $\sin(\frac{1}{2}t) \ge 0$ for $0 \le t \le 2\pi$, the absolute value can be removed[cite: 6].
  $$L = 2 \int_{0}^{2\pi} \sin\left(\frac{1}{2}t\right) dt = -4\left[\cos\left(\frac{1}{2}t\right)\right]_0^{2\pi} = -4(-1 - 1) = 8$$[cite: 6]

### Example 5
Verify that the surface area of a sphere of radius $a$ is $4\pi a^2$[cite: 6].

**Solution**
* **Step 1:** Parameterize the upper half of the circle $x^2 + y^2 = a^2$[cite: 6].
  $$x = a \cos t, \quad y = a \sin t; \quad 0 \le t \le \pi$$[cite: 6]
* **Step 2:** Apply Theorem (9.8)[cite: 6].
  $$S = \int_{0}^{\pi} 2\pi (a \sin t) \sqrt{(-a \sin t)^2 + (a \cos t)^2} dt$$[cite: 6]
* **Step 3:** Simplify the radical using $\sin^2 t + \cos^2 t = 1$[cite: 6].
  $$\sqrt{a^2 \sin^2 t + a^2 \cos^2 t} = \sqrt{a^2} = a$$[cite: 6]
* **Step 4:** Evaluate the integral[cite: 6].
  $$S = \int_{0}^{\pi} 2\pi a^2 \sin t dt = 2\pi a^2 [-\cos t]_0^\pi = -2\pi a^2 (-1 - 1) = 4\pi a^2$$[cite: 6]

## Exercises
* **1:** Find the slopes of the tangent line and the normal line at the point on the curve that corresponds to $t = 1$: $x = t^2 + 1, y = t^2 - 1$; $-2 \le t \le 2$[cite: 6].
* **3:** Find the slopes of the tangent line and the normal line at the point on the curve that corresponds to $t = 1$: $x = 4t^2 - 5, y = 2t + 3$; $t$ in $\mathbb{R}$[cite: 6].
* **5:** Find the slopes of the tangent line and the normal line at the point on the curve that corresponds to $t = 1$: $x = e^t, y = e^{-2t}$; $t$ in $\mathbb{R}$[cite: 6].
* **9:** Let $C$ be the curve with the given parametrization, for $t$ in $\mathbb{R}$. Find the points on $C$ at which the slope of the tangent line is $m$: $x = -t^3, y = -6t^2 - 18t$; $m = 2$[cite: 6].
* **11:** (a) Find the points on the curve $C$ at which the tangent line is either horizontal or vertical. (b) Find $d^2y/dx^2$. (c) Sketch the graph of $C$: $x = 4t^2, y = t^3 - 12t$; $t$ in $\mathbb{R}$[cite: 6].
* **13:** (a) Find the points on the curve $C$ at which the tangent line is either horizontal or vertical. (b) Find $d^2y/dx^2$. (c) Sketch the graph of $C$: $x = t^3 + 1, y = t^2 - 2t$; $t$ in $\mathbb{R}$[cite: 6].
* **21:** Find the length of the curve: $x = 5t^2, y = 2t^3$; $0 \le t \le 1$[cite: 6].
* **23:** Find the length of the curve: $x = e^t \cos t, y = e^t \sin t$; $0 \le t \le \pi/2$[cite: 6].
* **29:** Find the area of the surface generated by revolving the curve about the x-axis: $x = t^2, y = 2t$; $0 \le t \le 4$[cite: 6].
* **31:** Find the area of the surface generated by revolving the curve about the x-axis: $x = t^2, y = t - \frac{1}{3}t^3$; $0 \le t \le 1$[cite: 6].