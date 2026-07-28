---
source_file: "5-1.pdf"
course: MATH106
book_chapter: 5
book_section: 5.1
ksu_chapter: UNKNOWN
section_title: AREA
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: [5, 6, 9, 10, 11, 12, 14, 27, 28, 31]
topic_tags: [area-between-curves, definite-integral, limits-of-sums, geometry]
difficulty: UNKNOWN
in_syllabus: true
enrichment: UNKNOWN
status: draft
---

## Metadata
* **Course:** MATH106
* **Book Chapter:** 5
* **Chapter Title:** Applications of the Definite Integral
* **Section Number:** 5.1
* **Section Title:** Area

## Definitions
No formal boxed definitions.[cite: 1]

## Theorems
* **Theorem 5.1**
  If functions $f$ and $g$ are continuous such that $f(x) \ge g(x)$ for every $x$ in $[a, b]$, then the area $A$ of the region bounded by the graphs of $f$, $g$, $x = a$, and $x = b$ is given by[cite: 1]
  $$A = \int_{a}^{b} [f(x) - g(x)] dx$$

* **Corollary 5.2**
  The area $A$ is the limit of the Riemann sums of the differences between the functions evaluated at sample points $w_k$[cite: 1]:
  $$A = \lim_{||P||\to 0} \sum_k [f(w_k) - g(w_k)] \Delta x_k = \int_{a}^{b} [f(x) - g(x)] dx$$

## Formulas
* **Area of an $R_x$ region (vertical rectangles):**
  $$A = \int_{a}^{b} [f(x) - g(x)] dx$$[cite: 1]
* **Area of an $R_y$ region (horizontal rectangles):**
  $$A = \int_{c}^{d} [f(y) - g(y)] dy$$[cite: 1]
* **Area between intersecting graphs on $[a, b]$ with crossover at $c$:**
  $$A = A_1 + A_2 = \int_{a}^{c} [f(x) - g(x)] dx + \int_{c}^{b} [g(x) - f(x)] dx$$[cite: 1]

## Guidelines / Methods
* **Guidelines for Finding the Area of an $R_x$ Region 5.3**[cite: 1]
  1. Sketch the region, labeling the upper boundary $y = f(x)$ and the lower boundary $y = g(x)$.[cite: 1] Find the smallest value $x = a$ and the largest value $x = b$ for points $(x, y)$ in the region.[cite: 1]
  2. Sketch a typical vertical rectangle and label its width $dx$.[cite: 1]
  3. Express the area of the rectangle in guideline (2) as $[f(x) - g(x)] dx$.[cite: 1]
  4. Apply the limit of sums operator $\int_a^b$ to the expression in guideline (3) and evaluate the integral.[cite: 1]

* **Guidelines for Finding the Area of an $R_y$ Region 5.4**[cite: 1]
  1. Sketch the region, labeling the right boundary $x = f(y)$ and the left boundary $x = g(y)$.[cite: 1] Find the smallest value $y = c$ and the largest value $y = d$ for points $(x, y)$ in the region.[cite: 1]
  2. Sketch a typical horizontal rectangle and label its width $dy$.[cite: 1]
  3. Express the area of the rectangle in guideline (2) as $[f(y) - g(y)] dy$.[cite: 1]
  4. Apply the limit of sums operator $\int_c^d$ to the expression in guideline (3) and evaluate the integral.[cite: 1]

## Worked Examples
### Example 1
Find the area of the region bounded by the graphs of the equations $y = x^2$ and $y = \sqrt{x}$[cite: 1].

**Solution**
* **Step 1:** Solve equations simultaneously to find intersections: $x^2 = \sqrt{x}$ gives points $(0,0)$ and $(1,1)$[cite: 1]. 
* **Step 2:** The upper boundary is $y = \sqrt{x}$ and the lower boundary is $y = x^2$. The length of the typical vertical rectangle is $\sqrt{x} - x^2$ and width is $dx$[cite: 1].
* **Step 3:** Evaluate the definite integral from $a=0$ to $b=1$[cite: 1]:
  $$A = \int_{0}^{1} (\sqrt{x} - x^2) dx = \int_{0}^{1} (x^{1/2} - x^2) dx$$
  $$= \left[ \frac{x^{3/2}}{3/2} - \frac{x^3}{3} \right]_0^1 = \frac{2}{3} - \frac{1}{3} = \frac{1}{3}$$[cite: 1]

### Example 2
Find the area of the region bounded by the graphs of $y + x^2 = 6$ and $y + 2x - 3 = 0$[cite: 1].

**Solution**
* **Step 1:** Write as functions of $x$: upper boundary $y = 6 - x^2$ and lower boundary $y = 3 - 2x$[cite: 1].
* **Step 2:** Equate to find bounds: $6 - x^2 = 3 - 2x$ yields intersection points $(-1,5)$ and $(3,-3)$[cite: 1].
* **Step 3:** Setup and evaluate the integral[cite: 1]:
  $$A = \int_{-1}^{3} [(6 - x^2) - (3 - 2x)] dx = \int_{-1}^{3} (3 - x^2 + 2x) dx$$
  $$= \left[ 3x - \frac{x^3}{3} + x^2 \right]_{-1}^3 = \left[ 9 - \frac{27}{3} + 9 \right] - \left[ -3 - \left(-\frac{1}{3}\right) + 1 \right] = \frac{32}{3}$$[cite: 1]

### Example 3
Find the area of the region $R$ bounded by the graphs of $y - x = 6$, $y - x^3 = 0$, and $2y + x = 0$[cite: 1].

**Solution**
* **Step 1:** Divide the region into two $R_x$ regions because the lower boundary consists of two different graphs[cite: 1].
* **Step 2:** For region $R_1$ (from $x=-4$ to $x=0$), the upper boundary is $y = x + 6$ and lower is $y = -\frac{1}{2}x$[cite: 1].
  $$A_1 = \int_{-4}^{0} \left[ (x + 6) - \left(-\frac{1}{2}x\right) \right] dx = \int_{-4}^{0} \left( \frac{3}{2}x + 6 \right) dx = \left[ \frac{3}{4}x^2 + 6x \right]_{-4}^0 = 12$$[cite: 1]
* **Step 3:** For region $R_2$ (from $x=0$ to $x=2$), the upper boundary is $y = x + 6$ and lower is $y = x^3$[cite: 1].
  $$A_2 = \int_{0}^{2} [(x + 6) - x^3] dx = \left[ \frac{x^2}{2} + 6x - \frac{x^4}{4} \right]_0^2 = 10$$[cite: 1]
* **Step 4:** Total Area $A = A_1 + A_2 = 12 + 10 = 22$[cite: 1].

### Example 4
Find the area of the region bounded by the graphs of the equations $2y^2 = x + 4$ and $y^2 = x$[cite: 1].

**Solution**
* **Step 1:** Solve for $x$ in terms of $y$: Right boundary $x = y^2$, Left boundary $x = 2y^2 - 4$[cite: 1].
* **Step 2:** Intersections occur at $y = -2$ and $y = 2$[cite: 1].
* **Step 3:** Use horizontal rectangles (Guideline 5.4) and symmetry across the x-axis[cite: 1]:
  $$A = \int_{-2}^{2} [y^2 - (2y^2 - 4)] dy = 2 \int_{0}^{2} (4 - y^2) dy$$
  $$= 2 \left[ 4y - \frac{y^3}{3} \right]_0^2 = 2 \left( 8 - \frac{8}{3} \right) = \frac{32}{3}$$[cite: 1]

### Example 5
For the region bounded by $y = \cos(0.3x^2)$ and $y = x^2 + 0.6x - 2$, set up an integral and approximate the area[cite: 1].

**Solution**
* **Step 1:** Intersections are approximately at $a \approx -1.899686$ and $b \approx 1.408265$[cite: 1].
* **Step 2:** Setup integral[cite: 1]:
  $$A \approx \int_{-1.899686}^{1.408265} [\cos(0.3x^2) - x^2 - 0.6x + 2] dx$$
* **Step 3:** Using numerical approximations, $A \approx 6.9354268$[cite: 1].

### Example 6
If net investment flow is $I(t) = 4 - t^2 + 2t$ (millions of dollars per time unit), find the capital formation during the time interval $[1, 2]$[cite: 1].

**Solution**
* **Step 1:** Integrate the net investment flow[cite: 1]:
  $$\int_{1}^{2} (4 - t^2 + 2t) dt = \left[ 4t - \frac{t^3}{3} + t^2 \right]_1^2$$
  $$= \left[ 8 - \frac{8}{3} + 4 \right] - \left[ 4 - \frac{1}{3} + 1 \right] = 4\frac{2}{3}$$[cite: 1]
* **Answer:** The capital accumulation is about $4.67$ million dollars[cite: 1].

### Example 7
For net investment flows $I_1(t) = 4 - t^2 + 2t$ and $I_2(t) = 4 - t$, find the time interval where $I_1 \ge I_2$ and the excess capital accumulated[cite: 1].

**Solution**
* **Step 1:** Find intersection points by setting $4 - t^2 + 2t = 4 - t \Rightarrow 3t - t^2 = 0 \Rightarrow t=0, t=3$[cite: 1]. Thus interval is $[0, 3]$[cite: 1].
* **Step 2:** Find the difference in accumulation[cite: 1]:
  $$\int_{0}^{3} [I_1(t) - I_2(t)] dt = \int_{0}^{3} (3t - t^2) dt = \left[ \frac{3t^2}{2} - \frac{t^3}{3} \right]_0^3 = \frac{27}{2} - \frac{27}{3} = \frac{9}{2}$$[cite: 1]

## Exercises
* **5:** Sketch the region bounded by the graphs of the equations and find its area: $y = x^2$; $y = 4x$[cite: 1].
* **6:** Sketch the region bounded by the graphs of the equations and find its area: $x + y = 3$; $y + x^2 = 3$[cite: 1].
* **9:** Sketch the region bounded by the graphs of the equations and find its area: $y = 1/x^2$; $y = -x^2$; $x = 1$; $x = 2$[cite: 1].
* **10:** Sketch the region bounded by the graphs of the equations and find its area: $y = x^3$; $y = x^2$[cite: 1].
* **11:** Sketch the region bounded by the graphs of the equations and find its area: $y^2 = -x$; $x - y = 4$; $y = -1$; $y = 2$[cite: 1].
* **12:** Sketch the region bounded by the graphs of the equations and find its area: $x = y^2$; $y - x = 2$; $y = -2$; $y = 3$[cite: 1].
* **14:** Sketch the region bounded by the graphs of the equations and find its area: $x = y^2$; $x - y = 2$[cite: 1].
* **27:** Set up sums of integrals that can be used to find the area of the region bounded by the graphs of the equations by integrating with respect to (a) x and (b) y: $y = \sqrt{x}$; $y = -x$; $x = 1$; $x = 4$[cite: 1].
* **28:** Set up sums of integrals that can be used to find the area of the region bounded by the graphs of the equations by integrating with respect to (a) x and (b) y: $y = 1 - x^2$; $y = x - 1$[cite: 1].
* **31:** Find the area of the region between the graphs of $f$ and $g$ if $x$ is restricted to the given interval: $f(x) = 6 - 3x^2$; $g(x) = 3x$; $[0, 2]$[cite: 1].