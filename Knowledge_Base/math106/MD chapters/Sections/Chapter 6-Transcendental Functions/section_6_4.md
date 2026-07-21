---
source_file: "Section_6.4_Integration.pdf" #[cite: 11]
course: MATH106
book_chapter: 6
book_section: 6.4
ksu_chapter: UNKNOWN
section_title: INTEGRATION USING NATURAL LOGARITHM AND EXPONENTIAL FUNCTIONS
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: [1, 3, 6, 11, 15, 18, 19, 30, 31]
topic_tags: [integration, natural-logarithm, exponential-function, integration-by-substitution]
difficulty: UNKNOWN
in_syllabus: true
enrichment: UNKNOWN
status: draft
---

# INTEGRATION USING NATURAL LOGARITHM AND EXPONENTIAL FUNCTIONS

## Metadata
**Course:** MATH106
**Book:** Calculus (Swokowski)
**Edition:** 6th
**Chapter Number:** 6
**Chapter Title:** Transcendental Functions
**Section Number:** 6.4
**Section Title:** INTEGRATION USING NATURAL LOGARITHM AND EXPONENTIAL FUNCTIONS

## Definitions
No formal boxed definitions.

## Theorems
**Theorem 6.23**
If $u=g(x)\ne0$ and g is differentiable, then
$$\int\frac{1}{u}du=ln|u|+C$$

**Theorem 6.24**
If $u=g(x)$ and g is differentiable, then
$$\int e^{u}du=e^{u}+C.$$

**Theorem 6.25**
(i) $\int tan~u~du=-ln|cos~u|+C$
(ii) $\int cot~u~du=ln|sin~u|+C$
(iii) $\int sec~u~du=ln|sec~u+tan~u|+C$
(iv) $\int csc~u~du=ln|csc~u-cot~u|+C$

## Formulas
No formal boxed formulas distinct from Theorems and Methods.

## Guidelines / Methods
No numbered guideline lists or method tables.

## Worked Examples
### Example 1
Evaluate $\int\frac{x}{3x^{2}-5}dx.$
**Solution**
Rewriting the integral as
$$\int\frac{x}{3x^{2}-5}dx=\int\frac{1}{3x^{2}-5}x~dx$$
suggests that we use Theorem (6.23) with $u=3x^{2}-5$. Thus, we make the substitution
$$u=3x^{2}-5 \quad du=6x~dx$$.
Introducing a factor 6 in the integrand and using Theorem (6.23) yields
$$\int\frac{x}{3x^{2}-5}dx=\frac{1}{6}\int\frac{1}{3x^{2}-5}6x~dx=\frac{1}{6}\int\frac{1}{u}du$$
$$=\frac{1}{6}ln|u|+C=\frac{1}{6}ln|3x^{2}-5|+C$$.

### Example 2
Evaluate $\int_{2}^{4}\frac{1}{9-2x}dx$
**Solution**
One method of evaluation consists of using an indefinite integral to find an antiderivative of $1/(9-2x)$. We let
$$u=9-2x, \quad du=-2~dx$$
and proceed as follows:
$$\int\frac{1}{9-2x}dx=-\frac{1}{2}\int\frac{1}{9-2x}(-2)dx$$
$$=-\frac{1}{2}\int\frac{1}{u}du=-\frac{1}{2}ln|u|+C$$
$$=-\frac{1}{2}ln|9-2x|+C$$
Applying the fundamental theorem of calculus yields
$$\int_{2}^{4}\frac{1}{9-2x}dx=-\frac{1}{2}[ln|9-2x|]_{2}^{4}$$
$$=-\frac{1}{2}(ln~1-ln~5)=\frac{1}{2}ln~5$$
Another method is to use the same substitution in the definite integral and change the limits of integration. Since $u=9-2x.$ we obtain the following:
(i) If $x=2$ then $u=5$.
(ii) If $x=4$ then $u=1$.
Thus,
$$\int_{2}^{4}\frac{1}{9-2x}dx=-\frac{1}{2}\int_{2}^{4}\frac{1}{9-2x}(-2)dx$$
$$=-\frac{1}{2}\int_{5}^{1}\frac{1}{u}du=-\frac{1}{2}[ln|u|]_{5}^{1}$$
$$=-\frac{1}{2}(ln~1-ln~5)=\frac{1}{2}ln~5.$$

### Example 3
Evaluate $\int\frac{\sqrt{ln~x}}{x}dx.$
**Solution**
Two possible substitutions are $u=\sqrt{ln~x}$ and $u=ln~x.$ If we use
$$u=ln~x,$$
then
$$du=\frac{1}{x}dx,$$
$$\int\frac{\sqrt{ln~x}}{x}dx=\int\sqrt{ln~x}\cdot\frac{1}{x}dx=\int u^{1/2}du=\frac{u^{3/2}}{3/2}+C$$
$$=\frac{2}{3}(ln~x)^{3/2}+C$$

### Example 4
Evaluate:
(a) $\int\frac{e^{3/x}}{x^{2}}dx$
(b) $\int_{1}^{2}\frac{e^{3/x}}{x^{2}}dx$
**Solution**
(a) Rewriting the integral as
$$\int\frac{e^{3/x}}{x^{2}}dx=\int e^{3/x}\frac{1}{x^{2}}dx$$
suggests that we use Theorem (6.24) with $u=3/x.$ Thus, we make the substitution
$$u=\frac{3}{x}, \quad du=-\frac{3}{x^{2}}dx.$$
The integrand may be written in the form of Theorem (6.24) by introducing the factor -3. Doing this and compensating by multiplying the integral by $-\frac{1}{3},$ we obtain
$$\int\frac{e^{3/x}}{x^{2}}dx=-\frac{1}{3}\int e^{3/x}(-\frac{3}{x^{2}})dx$$
$$=-\frac{1}{3}\int e^{u}du$$
$$=-\frac{1}{3}e^{u}+C$$
$$=-\frac{1}{3}e^{3/x}+C$$
(b) Using the antiderivative found in part (a) and applying the fundamental theorem of calculus yields
$$\int_{1}^{2}\frac{e^{3/x}}{x^{2}}dx=-\frac{1}{3}[e^{3/x}]_{1}^{2}$$
$$=-\frac{1}{3}(e^{3/2}-e^{3})\approx5.2$$.
We can also evaluate the integral by using the method of substitution. As in part (a), we let $u=3/x$, $du=(-3/x^{2})dx$, and we note that if $x=1$ then $u=3$, and if $x=2$, then $u=\frac{3}{2}$ Consequently,
$$\int_{1}^{2}\frac{e^{3/x}}{x^{2}}dx=-\frac{1}{3}\int_{1}^{2}e^{3/x}(-\frac{3}{x^{2}})dx$$
$$=-\frac{1}{3}\int_{3}^{3/2}e^{u}du$$
$$=-\frac{1}{3}[e^{u}]_{3}^{3/2}=-\frac{1}{3}(e^{3/2}-e^{3})\approx5.2.$$

### Example 5
Solve the differential equation
$$\frac{dy}{dx}=3e^{2x}+6e^{-3x}$$
subject to the initial condition $y=4$ if $x=0$.
**Solution**
We may multiply both sides of the equation by dx and then integrate as follows:
$$dy=(3e^{2x}+6e^{-3x})dx$$
$$\int dy=\int(3e^{2x}+6e^{-3x})dx=3\int e^{2x}dx+6\int e^{-3x}dx$$
$$y=3(\frac{1}{2})e^{2x}+6(-\frac{1}{3})e^{-3x}+C$$
$$=\frac{3}{2}e^{2x}-2e^{-3x}+C$$
Using the initial condition $y=4$ if $x=0$ gives us
$$4=\frac{3}{2}e^{0}-2e^{0}+C=\frac{3}{2}-2+C$$.
Hence, $C=4-\frac{3}{2}+2=\frac{9}{2}$ and the solution of the differential equation is
$$y=\frac{3}{2}e^{2x}-2e^{-3x}+\frac{9}{2}$$.

### Example 6
Find the area of the region bounded by the graphs of the equations $y=e^{x}$ $y=\sqrt{x},$ $x=0,$ and $x=1$.
**Solution**
As usual, we list the following:
width of rectangle: dx
length of rectangle: $e^{x}-\sqrt{x}$
area of rectangle: $(e^{x}-\sqrt{x})dx$
We next take a limit of sums of these rectangular areas by applying the operator $\int_{0}^{1}$
$$\int_{0}^{1}(e^{x}-\sqrt{x})dx=\int_{0}^{1}(e^{x}-x^{1/2})dx$$
$$=[e^{x}-\frac{2}{3}x^{3/2}]_{0}^{1}=e-\frac{5}{3}\approx1.05$$

### Example 7
Evaluate $\int x~cot~x^{2}dx$ .
**Solution**
To obtain the form of $cot~u~du$, we make the substitution
$$u=x^{2} \quad du=2x~dx$$.
We next introduce the factor 2 in the integrand as follows:
$$\int x~cot~x^{2}dx=\frac{1}{2}\int(cot~x^{2})2x~dx$$
Since $u=x^{2}$ and $du=2x~dx$,
$$\int x~cot~x^{2}dx=\frac{1}{2}\int cot~u~du=\frac{1}{2}ln|sin~u|+C$$
$$=\frac{1}{2}ln|sin~x^{2}|+C$$

### Example 8
Evaluate $\int_{0}^{\pi/2}tan\frac{x}{2}dx.$
**Solution**
We make the substitution
$$u=\frac{x}{2} \quad du=\frac{1}{2}dx$$
and note that $u=0$ if $x=0$, and $u=\pi/4$ if $x=\pi/2$. Thus,
$$\int_{0}^{\pi/2}tan\frac{x}{2}dx=2\int_{0}^{\pi/2}tan\frac{x}{2}\cdot\frac{1}{2}dx$$
$$=2\int_{0}^{\pi/4}tan~u~du=2[ln~sec~u]_{0}^{\pi/4}$$
In this case, we may drop the absolute value sign given in Theorem (6.25)(iii), because $sec~u$ is positive if u is between 0 and $\pi/4$ Since $ln~sec(\pi/4)=ln\sqrt{2}=\frac{1}{2}ln~2$ and $ln~sec~0=ln~1=0,$ it follows that
$$\int_{0}^{\pi/2}tan\frac{x}{2}dx=2\cdot\frac{1}{2}ln~2=ln~2\approx0.69.$$

### Example 9
Evaluate $\int e^{2x}sec~e^{2x}dx.$
**Solution**
We let
$$u=e^{2x} \quad du=2e^{2x}dx$$
and proceed as follows:
$$\int e^{2x}sec~e^{2x}dx=\frac{1}{2}\int(sec~e^{2x})2e^{2x}dx$$
$$=\frac{1}{2}\int sec~u~du$$
$$=\frac{1}{2}ln|sec~u+tan~u|+C$$
$$=\frac{1}{2}ln|sec~e^{2x}+tan~e^{2x}|+C$$

### Example 10
Evaluate $\int(csc~x-1)^{2}dx$
**Solution**
$$\int(csc~x-1)^{2}dx=\int(csc^{2}x-2~csc~x+1)dx$$
$$=\int csc^{2}x~dx-2\int csc~x~dx+\int dx$$
$$=-cot~x-2~ln|csc~x-cot~x|+x+C$$

## Exercises
*   1. (a) $\int\frac{1}{2x+7}dx$ (b) $\int_{-2}^{1}\frac{1}{2x+7}dx$
*   3. (a) $\int\frac{4x}{x^{2}-9}dx$ (b) $\int_{1}^{2}\frac{4x}{x^{2}-9}dx$
*   6. (a) $\int x^{2}e^{3x^{3}}dx$ (b) $\int_{1}^{2}x^{2}e^{3x^{3}}dx$
*   11. $\int\frac{x-2}{x^{2}-4x+9}dx$
*   15. $\int\frac{ln~x}{x}dx$
*   18. $\int\frac{e^{\sqrt{x}}}{\sqrt{x}}dx$
*   19. $\int\frac{3~sin~x}{1+2~cos~x}dx$
*   30. $\int e^{cos~x}sin~x~dx$
*   31. $\int\frac{cos^{2}x}{sin~x}dx$