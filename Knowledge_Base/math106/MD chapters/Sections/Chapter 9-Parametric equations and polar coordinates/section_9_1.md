---
source_file: "9-1.pdf"
course: MATH106
book_chapter: 9
book_section: 9.1
ksu_chapter: UNKNOWN
section_title: PARAMETRIC EQUATIONS
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: [1, 3, 5, 7, 25]
topic_tags: [parametric-equations, plane-curves, curve-orientation, projectile-motion, bezier-curves]
difficulty: UNKNOWN
in_syllabus: true
enrichment: UNKNOWN
status: draft
---

## Metadata
* **Course:** MATH106
* **Book Chapter:** 9
* **Chapter Title:** Parametric Equations and Polar Coordinates
* **Section Number:** 9.1
* **Section Title:** Parametric Equations

## Definitions
* **Definition 9.1**
  A plane curve is defined as a collection $C$ of ordered pairs $(f(t), g(t))$, where the functions $f$ and $g$ are continuous over an interval $I$[cite: 5].

* **Definition 9.2**
  Assume $C$ is a curve containing all ordered pairs $(f(t), g(t))$, where $f$ and $g$ are continuous on an interval $I$[cite: 5]. The equations
  $$x = f(t), \quad y = g(t)$$
  for $t$ within $I$ are known as the parametric equations for $C$, with $t$ serving as the parameter[cite: 5].

## Theorems
No formal boxed theorems.

## Formulas
* **Parametric Equations for Projectile Motion 9.3**
  The equations governing the motion of a projectile in a plane, starting from an initial position $(x_0, y_0)$ at time $t = 0$ with an initial horizontal velocity $h_0$ and vertical velocity $v_0$, are given by[cite: 5]:
  $$x(t) = x_0 + h_0 t$$
  $$y(t) = -\frac{1}{2}gt^2 + v_0 t + y_0$$
  where $g$ represents the magnitude of constant gravitational acceleration[cite: 5]. If the projectile is fired at an angle of elevation $\theta$ with an initial speed $s_0$, then[cite: 5]:
  $$h_0 = s_0 \cos \theta, \quad v_0 = s_0 \sin \theta$$

* **Cubic Bézier Curve Parametric Equations**
  For four given control points $P_0(p_0, q_0)$, $P_1(p_1, q_1)$, $P_2(p_2, q_2)$, and $P_3(p_3, q_3)$, the cubic Bézier curve is parameterized for $0 \le t \le 1$ by[cite: 5]:
  $$x(t) = p_0(1 - t)^3 + 3p_1(1 - t)^2 t + 3p_2(1 - t)t^2 + p_3 t^3$$
  $$y(t) = q_0(1 - t)^3 + 3q_1(1 - t)^2 t + 3q_2(1 - t)t^2 + q_3 t^3$$

## Guidelines / Methods
No formal boxed guidelines.

## Worked Examples
### Example 1
Let $C$ be the curve that has parametrization $x = 2t$, $y = t^2 - 1$ for $-1 \le t \le 2$[cite: 5]. Obtain an equation for the curve in the form $y = f(x)$[cite: 5].

**Solution**
* **Step 1:** Solve the first parametric equation for $t$ to eliminate the parameter[cite: 5].
  $$x = 2t \implies t = \frac{1}{2}x$$
* **Step 2:** Substitute this expression for $t$ into the second parametric equation[cite: 5].
  $$y = \left(\frac{1}{2}x\right)^2 - 1$$
* **Step 3:** Determine the domain by evaluating the boundaries of $t$[cite: 5]. Since $-1 \le t \le 2$ and $x = 2t$, $x$ ranges from $-2$ to $4$[cite: 5]. The curve is the segment of the parabola $y = \frac{1}{4}x^2 - 1$ connecting the points $(-2, 0)$ and $(4, 3)$[cite: 5].

### Example 2
A point moves in a plane such that its position $P(x, y)$ at time $t$ is given by $x = a \cos t$, $y = a \sin t$; $t \ge 0$, where $a > 0$[cite: 5]. Describe the motion of the point[cite: 5].

**Solution**
* **Step 1:** Eliminate the parameter by rewriting the equations and utilizing a trigonometric identity[cite: 5].
  $$\frac{x}{a} = \cos t, \quad \frac{y}{a} = \sin t$$
  $$\left(\frac{x}{a}\right)^2 + \left(\frac{y}{a}\right)^2 = \cos^2 t + \sin^2 t = 1$$
  $$x^2 + y^2 = a^2$$
* **Step 2:** The point moves along a circle $C$ of radius $a$ centered at the origin[cite: 5]. As $t$ increases from $0$, the point moves counterclockwise from $(a, 0)$, completing one full revolution every $2\pi$ units of time[cite: 5].

### Example 3
Sketch the graph of the curve $C$ parameterized by $x = -2 + t^2$, $y = 1 + 2t^2$ for $t$ in $\mathbb{R}$, and indicate the orientation[cite: 5].

**Solution**
* **Step 1:** Isolate $t^2$ from the first equation[cite: 5].
  $$t^2 = x + 2$$
* **Step 2:** Substitute into the second equation[cite: 5].
  $$y = 1 + 2(x + 2) = 2x + 5$$
* **Step 3:** Determine the domain. Because $t^2 \ge 0$, we know $x = -2 + t^2 \ge -2$ and $y = 1 + 2t^2 \ge 1$[cite: 5]. The graph is the ray of the line starting from $(-2, 1)$ extending to the right[cite: 5]. As $t$ increases from $-\infty$ to $0$, the point moves down the line toward $(-2, 1)$, and as $t$ increases from $0$ to $\infty$, the point moves back up the line[cite: 5].

### Example 5
Find the Cartesian equation for the Lissajous figure given by $x = \sin 2t$, $y = \cos t$ for $0 \le t \le 2\pi$[cite: 5].

**Solution**
* **Step 1:** Use trigonometric identities to express $x$ in terms of $\cos t$[cite: 5].
  $$x = 2 \sin t \cos t$$
  $$x^2 = 4 \sin^2 t \cos^2 t = 4(1 - \cos^2 t)\cos^2 t$$
* **Step 2:** Substitute $y = \cos t$ into the equation[cite: 5].
  $$x^2 = 4(1 - y^2)y^2$$
  $$4y^4 - 4y^2 + x^2 = 0$$
* **Step 3:** Solve for $y^2$ using the quadratic formula[cite: 5].
  $$y^2 = \frac{4 \pm \sqrt{16 - 16x^2}}{8} = \frac{1 \pm \sqrt{1 - x^2}}{2}$$
  $$y = \pm \sqrt{\frac{1 \pm \sqrt{1 - x^2}}{2}}$$

### Example 7
A pitcher throws a ball from a height of 8 ft, located 30 ft away from a 90 ft building, with initial horizontal velocity $23.5 \text{ ft/sec}$ and vertical velocity $84.8 \text{ ft/sec}$[cite: 5]. Will the ball reach the top of the building?[cite: 5]

**Solution**
* **Step 1:** Establish parametric equations for the motion[cite: 5].
  $$x(t) = 23.5t$$
  $$y(t) = -16t^2 + 84.8t + 8$$
* **Step 2:** Find the time $T$ when the ball reaches the horizontal position of the building ($x = 30$)[cite: 5].
  $$23.5T = 30 \implies T = \frac{30}{23.5} \approx 1.2766 \text{ sec}$$
* **Step 3:** Substitute $T$ into the vertical position equation to determine the height[cite: 5].
  $$y(1.2766) \approx -16(1.2766)^2 + 84.8(1.2766) + 8 \approx 90.18 \text{ ft}$$
* **Step 4:** Since $90.18 \text{ ft} > 90 \text{ ft}$, the ball will just clear the top of the building[cite: 5].

## Exercises
* **1:** Find an equation in $x$ and $y$ whose graph contains the points on the curve $C$. Sketch the graph of $C$ and indicate the orientation: $x = t - 2$, $y = 2t + 3$; $0 \le t \le 5$[cite: 5].
* **3:** Find an equation in $x$ and $y$ whose graph contains the points on the curve $C$. Sketch the graph of $C$ and indicate the orientation: $x = t^2 + 1$, $y = t^2 - 1$; $-2 \le t \le 2$[cite: 5].
* **5:** Find an equation in $x$ and $y$ whose graph contains the points on the curve $C$. Sketch the graph of $C$ and indicate the orientation: $x = 4t^2 - 5$, $y = 2t + 3$; $t$ in $\mathbb{R}$[cite: 5].
* **7:** Find an equation in $x$ and $y$ whose graph contains the points on the curve $C$. Sketch the graph of $C$ and indicate the orientation: $x = e^t$, $y = e^{-2t}$; $t$ in $\mathbb{R}$[cite: 5].
* **25:** Curves $C_1, C_2, C_3$, and $C_4$ are given parametrically, for $t$ in $\mathbb{R}$. Sketch their graphs and indicate orientations:
  $C_1: x = t^2, y = t$
  $C_2: x = t^4, y = t^2$
  $C_3: x = \sin^2 t, y = \sin t$
  $C_4: x = e^{2t}, y = -e^t$[cite: 5].