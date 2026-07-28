---
source_file: "9-3.pdf"
course: MATH106
book_chapter: 9
book_section: 9.3
ksu_chapter: UNKNOWN
section_title: POLAR COORDINATES
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: [1, 2, 3, 5, 7, 9, 27, 31, 33, 37, 38, 51, 53, 59]
topic_tags: [polar-coordinates, polar-equations, symmetry, tangent-lines, curves]
difficulty: UNKNOWN
in_syllabus: true
enrichment: UNKNOWN
status: draft
---

## Metadata
* **Course:** MATH106
* **Book Chapter:** 9
* **Chapter Title:** Parametric Equations and Polar Coordinates
* **Section Number:** 9.3
* **Section Title:** Polar Coordinates

## Definitions
* **Polar Coordinate System:** A system for specifying points in a plane using a fixed reference point $O$ called the pole (or origin), and a directed half-line starting from $O$ called the polar axis[cite: 7].
* **Polar Coordinates:** An ordered pair $(r, \theta)$ representing a point $P$, where $r = d(O, P)$ is the directed distance from the pole, and $\theta$ is the measure of the angle determined by the polar axis and the line segment $OP$[cite: 7]. $\theta$ is positive for counterclockwise rotation and negative for clockwise rotation[cite: 7].
* **Polar Equation:** An equation expressed in terms of the variables $r$ and $\theta$[cite: 7].
* **Graph of a Polar Equation:** The collection of all points in the $r\theta$-plane corresponding to the solutions $(r, \theta)$ of the polar equation[cite: 7].

## Theorems
* **Theorem 9.11**
  The slope $m$ of the tangent line to the graph of $r = f(\theta)$ at the point $P(r, \theta)$ is[cite: 7]:
  $$m = \frac{\frac{dr}{d\theta} \sin \theta + r \cos \theta}{\frac{dr}{d\theta} \cos \theta - r \sin \theta}$$

## Formulas
* **Relationships between Rectangular and Polar Coordinates 9.9**
  When a rectangular $xy$-plane is superimposed on an $r\theta$-plane so that the positive x-axis coincides with the polar axis, the rectangular coordinates $(x, y)$ and polar coordinates $(r, \theta)$ of a point $P$ are related by[cite: 7]:
  (i) $x = r \cos \theta$, $y = r \sin \theta$[cite: 7]
  (ii) $r^2 = x^2 + y^2$, $\tan \theta = y/x$ (if $x \ne 0$)[cite: 7]

## Guidelines / Methods
* **Tests for Symmetry 9.10**
  1. The graph of $r = f(\theta)$ is symmetric with respect to the polar axis if substituting $-\theta$ for $\theta$ yields an equivalent equation[cite: 7].
  2. The graph of $r = f(\theta)$ is symmetric with respect to the vertical line $\theta = \pi/2$ if substituting either $\pi - \theta$ for $\theta$, or substituting $-r$ for $r$ and $-\theta$ for $\theta$, yields an equivalent equation[cite: 7].
  3. The graph of $r = f(\theta)$ is symmetric with respect to the pole (origin) if substituting either $-r$ for $r$, or $\pi + \theta$ for $\theta$, yields an equivalent equation[cite: 7].

## Worked Examples
### Example 1
Sketch the graph of the polar equation $r = 4 \sin \theta$[cite: 7].

**Solution**
* **Step 1:** Create a table of values for $\theta$ from $0$ to $\pi$ to find corresponding $r$ values[cite: 7]. For instance, $r=0$ at $\theta=0$, $r=2$ at $\theta=\pi/6$, and $r=4$ at $\theta=\pi/2$[cite: 7].
* **Step 2:** Plot these points in the $r\theta$-plane[cite: 7]. The plotted points form a circle of radius 2[cite: 7].
* **Step 3:** Note that as $\theta$ increases from $\pi$ to $2\pi$, the same points are retraced due to the periodicity of the sine function[cite: 7].

### Example 2
Sketch the graph of the polar equation $r = 2 + 2 \cos \theta$[cite: 7].

**Solution**
* **Step 1:** Analyze the behavior of the cosine function[cite: 7]. As $\theta$ varies from $0$ to $\pi$, $\cos \theta$ decreases from $1$ to $-1$, meaning $r$ decreases from $4$ to $0$[cite: 7]. 
* **Step 2:** Plot points for $0 \le \theta \le \pi$ to sketch the upper half of the graph[cite: 7].
* **Step 3:** As $\theta$ increases from $\pi$ to $2\pi$, $r$ increases back from $0$ to $4$, completing the lower half of the graph[cite: 7]. The resulting heart-shaped graph is called a cardioid[cite: 7].

### Example 3
Sketch the graph of the polar equation $r = 2 + 4 \cos \theta$[cite: 7].

**Solution**
* **Step 1:** Tabulate coordinates for $0 \le \theta \le \pi$[cite: 7]. Note that $r = 0$ at $\theta = 2\pi/3$[cite: 7].
* **Step 2:** For $2\pi/3 < \theta \le \pi$, the values of $r$ are negative, which generates the lower half of a small inner loop[cite: 7].
* **Step 3:** Let $\theta$ range from $\pi$ to $2\pi$ to trace the upper half of the small loop and the lower half of the large outer loop[cite: 7]. The shape is a limaçon with an inner loop[cite: 7].

### Example 4
Sketch the graph of the polar equation $r = a \sin 2\theta$ for $a > 0$[cite: 7].

**Solution**
* **Step 1:** As $\theta$ increases from $0$ to $\pi/4$, $2\theta$ goes from $0$ to $\pi/2$, so $r$ increases from $0$ to $a$[cite: 7]. As $\theta$ continues from $\pi/4$ to $\pi/2$, $r$ decreases from $a$ back to $0$[cite: 7]. This forms a loop in the first quadrant[cite: 7].
* **Step 2:** For $\pi/2 \le \theta \le \pi$, $r$ is negative, causing the points to be traced in the fourth quadrant, forming a second loop[cite: 7].
* **Step 3:** Extending $\theta$ through $2\pi$ generates loops in the third and second quadrants, creating a four-leafed rose[cite: 7].

### Example 5
Sketch the graph of the polar equation $r = \theta$ for $\theta \ge 0$[cite: 7].

**Solution**
* **Step 1:** The graph consists of points $(c, c)$ for $c \ge 0$[cite: 7].
* **Step 2:** As $\theta$ increases, $r$ increases at an identical rate[cite: 7].
* **Step 3:** This traces a spiral (the spiral of Archimedes) that winds counterclockwise around the origin[cite: 7].

### Example 6
Find an equation in $x$ and $y$ that has the same graph as the polar equation $r = a \sin \theta$, with $a \ne 0$. Sketch the graph[cite: 7].

**Solution**
* **Step 1:** Multiply both sides of the polar equation by $r$ to obtain $r^2 = a r \sin \theta$[cite: 7].
* **Step 2:** Substitute the rectangular relationships $r^2 = x^2 + y^2$ and $y = r \sin \theta$[cite: 7]:
  $$x^2 + y^2 = ay$$
* **Step 3:** Rearrange and complete the square in $y$[cite: 7]:
  $$x^2 + y^2 - ay + \left(\frac{a}{2}\right)^2 = \left(\frac{a}{2}\right)^2$$
  $$x^2 + \left(y - \frac{a}{2}\right)^2 = \left(\frac{a}{2}\right)^2$$
* **Step 4:** This represents a circle centered at $(0, a/2)$ with radius $|a|/2$[cite: 7].

### Example 7
Find a polar equation for the hyperbola given by $x^2 - y^2 = 16$[cite: 7].

**Solution**
* **Step 1:** Substitute the relationships $x = r \cos \theta$ and $y = r \sin \theta$[cite: 7]:
  $$(r \cos \theta)^2 - (r \sin \theta)^2 = 16$$
* **Step 2:** Factor out $r^2$[cite: 7]:
  $$r^2 (\cos^2 \theta - \sin^2 \theta) = 16$$
* **Step 3:** Apply the double-angle identity for cosine[cite: 7]:
  $$r^2 \cos 2\theta = 16$$
* **Step 4:** Solve for $r^2$[cite: 7]:
  $$r^2 = \frac{16}{\cos 2\theta} \quad \text{or} \quad r^2 = 16 \sec 2\theta$$

### Example 8
Find a polar equation of an arbitrary line[cite: 7].

**Solution**
* **Step 1:** Start with the standard linear equation $ax + by = c$[cite: 7].
* **Step 2:** Substitute $x = r \cos \theta$ and $y = r \sin \theta$[cite: 7]:
  $$a(r \cos \theta) + b(r \sin \theta) = c$$
* **Step 3:** Factor out $r$ and solve[cite: 7]:
  $$r(a \cos \theta + b \sin \theta) = c$$
  $$r = \frac{c}{a \cos \theta + b \sin \theta}$$

### Example 9
For the cardioid $r = 2 + 2 \cos \theta$ with $0 \le \theta < 2\pi$, find (a) the slope of the tangent line at $\theta = \pi/6$, (b) the points at which the tangent line is horizontal, and (c) the points at which the tangent line is vertical[cite: 7].

**Solution**
* **Step 1 (a):** Use Theorem 9.11 to find the slope $m$[cite: 7]:
  $$m = \frac{(-2 \sin \theta)\sin \theta + (2 + 2 \cos \theta)\cos \theta}{(-2 \sin \theta)\cos \theta - (2 + 2 \cos \theta)\sin \theta}$$
  $$m = \frac{2(\cos^2 \theta - \sin^2 \theta) + 2 \cos \theta}{-2(2 \sin \theta \cos \theta) - 2 \sin \theta} = -\frac{\cos 2\theta + \cos \theta}{\sin 2\theta + \sin \theta}$$
  Evaluate at $\theta = \pi/6$[cite: 7]:
  $$m = -\frac{\cos(\pi/3) + \cos(\pi/6)}{\sin(\pi/3) + \sin(\pi/6)} = -\frac{1/2 + \sqrt{3}/2}{\sqrt{3}/2 + 1/2} = -1$$
* **Step 2 (b):** Set the numerator equal to zero to find horizontal tangents[cite: 7]:
  $$\cos 2\theta + \cos \theta = 0 \implies (2 \cos \theta - 1)(\cos \theta + 1) = 0$$
  This yields $\theta = \pi/3, 5\pi/3$ giving points $(3, \pi/3)$ and $(3, 5\pi/3)$[cite: 7]. When $\cos \theta = -1$, $\theta = \pi$. At the pole $(0, \pi)$, evaluating $m = \tan \pi = 0$ confirms a horizontal tangent[cite: 7].
* **Step 3 (c):** Set the denominator equal to zero for vertical tangents[cite: 7]:
  $$\sin 2\theta + \sin \theta = 0 \implies \sin \theta(2 \cos \theta + 1) = 0$$
  This yields $\theta = 0, 2\pi/3, 4\pi/3$, giving points $(4, 0), (1, 2\pi/3)$, and $(1, 4\pi/3)$ where vertical tangents occur[cite: 7].

## Exercises
* **1:** Sketch the graph of the polar equation: $r = 5$[cite: 7].
* **2:** Sketch the graph of the polar equation: $\theta = -\pi/6$[cite: 7].
* **3:** Sketch the graph of the polar equation: $r = 3 \cos \theta$[cite: 7].
* **5:** Sketch the graph of the polar equation: $r = 4 - 4 \sin \theta$[cite: 7].
* **7:** Sketch the graph of the polar equation: $r = 2 + 4 \sin \theta$[cite: 7].
* **9:** Sketch the graph of the polar equation: $r = -2 \sin \theta$[cite: 7].
* **27:** Find a polar equation that has the same graph as the equation in $x$ and $y$: $x = -3$[cite: 7].
* **31:** Find a polar equation that has the same graph as the equation in $x$ and $y$: $2y = -x$[cite: 7].
* **33:** Find a polar equation that has the same graph as the equation in $x$ and $y$: $y^2 - x^2 = 4$[cite: 7].
* **37:** Find an equation in $x$ and $y$ that has the same graph as the polar equation and use it to help sketch the graph in an $xy$-plane: $r \cos \theta = 5$[cite: 7].
* **38:** Find an equation in $x$ and $y$ that has the same graph as the polar equation and use it to help sketch the graph in an $xy$-plane: $r \sin \theta = -2$[cite: 7].
* **51:** Find the slope of the tangent line to the graph of the polar equation at the point corresponding to the given value of $\theta$: $r = 2 \cos \theta; \theta = \pi/3$[cite: 7].
* **53:** Find the slope of the tangent line to the graph of the polar equation at the point corresponding to the given value of $\theta$: $r = 5 + 3 \sin \theta; \theta = \pi/4$[cite: 7].
* **59:** Find the slope of the tangent line to the graph of the polar equation at the point corresponding to the given value of $\theta$: $r = 2^\theta; \theta = \pi$[cite: 7].