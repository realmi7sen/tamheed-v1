---
course: MATH106
book_chapter: 4
book_section: 4.1
ksu_chapter: UNKNOWN
section_title: ANTIDERIVATIVES, INDEFINITE INTEGRALS, AND SIMPLE DIFFERENTIAL EQUATIONS
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: [1, 5, 7, 11, 14, 15, 17, 23, 27, 29, 35, 41, 43, 49]
topic_tags: [antiderivatives, indefinite-integrals, differential-equations]
difficulty: UNKNOWN
in_syllabus: true
enrichment: UNKNOWN
status: draft
---

# ANTIDERIVATIVES, INDEFINITE INTEGRALS, AND SIMPLE DIFFERENTIAL EQUATIONS

## Metadata
**Course:** MATH106
**Book:** Calculus (Swokowski)
**Edition:** 6th
**Chapter Number:** 4
**Chapter Title:** Integrals
**Section Number:** 4.1
**Section Title:** ANTIDERIVATIVES, INDEFINITE INTEGRALS, AND SIMPLE DIFFERENTIAL EQUATIONS

## Definitions
**Definition 4.1**
A function F is an antiderivative of the function f on an interval l if $F^{\prime}(x)=f(x)$ for every x in l.

**Definition 4.3**
The notation $\int f(x)dx=F(x)+C,$ where $F^{\prime}(x)=f(x)$ and C is an arbitrary constant, denotes the family of all antiderivatives of f(x) on an interval l.

## Theorems
**Theorem 4.2**
Let F be an antiderivative of f on an interval l. If G is any antiderivative of f on l, then $G(x)=F(x)+C$ for some constant C and every x in l.

**Theorem 4.5**
(i) $\int\frac{d}{dx}(f(x))dx=f(x)+C$
(ii) $\frac{d}{dx}(\int f(x)dx)=f(x)$

**Theorem 4.6**
(i) $\int cf(x)dx=c\int f(x)dx$ for any nonzero constant c
(ii) $\int[f(x)+g(x)]dx=\int f(x)dx+\int g(x)dx$
(iii) $\int[f(x)-g(x)]dx=\int f(x)dx-\int g(x)dx$

## Formulas
**Brief Table of Indefinite Integrals 4.4**
(1) $\int1~dx=\int dx=x+C$
(2) $\int x^{r}dx=\frac{x^{r+1}}{r+1}+C$ ($r\ne-1$)
(3) $\int cos~x~dx=sin~x+C$
(4) $\int sin~x~dx=-cos~x+C$
(5) $\int sec^{2}x~dx=tan~x+C$
(6) $\int csc^{2}xdx=-cot~x+C$
(7) $\int sec~x~tan~x~dx=sec~x+C$
(8) $\int csc~x~cot~x~dx=-csc~x+C$

## Guidelines / Methods
No formal boxed or numbered guidelines.

## Worked Examples
### Example 1
Verify Theorem (4.5) for the special case $f(x)=x^{2}$.
**Solution**
(i) If we first differentiate $x^{2}$ and then integrate,
$$\int\frac{d}{dx}(x^{2})dx=\int2x~dx=x^{2}+C.$$
(ii) If we first integrate $x^{2}$ and then differentiate,
$$\frac{d}{dx}(\int x^{2}dx)=\frac{d}{dx}(\frac{x^{3}}{3}+C)=x^{2}.$$

### Example 2
Evaluate $\int(5x^{3}+2~cos~x)dx.$
**Solution**
We first use (ii) and (i) of Theorem (4.6) and then formulas from (4.4):
$$\int(5x^{3}+2~cos~x)dx=\int5x^{3}dx+\int2~cos~x~dx$$
$$=5\int x^{3}dx+2\int cos~xdx$$
$$=5(\frac{x^{4}}{4}+C_{1})+2(sin~x+C_{2})$$
$$=\frac{5}{4}x^{4}+5C_{1}+2~sin~x+2C_{2}$$
$$=\frac{5}{4}x^{4}+2~sin~x+C$$
where $C=5C_{1}+2C_{2}$.

### Example 3
Evaluate $\int(8t^{3}-6\sqrt{t}+\frac{1}{t^{3}})dt.$
**Solution**
First we find an antiderivative for each of the three terms in the integrand and then add an arbitrary constant C. We rewrite $\sqrt{t}$ as $t^{1/2}$ and $1/t^{3}$ as $t^{-3}$ and then use the power rule for integration:
$$\int(8t^{3}-6\sqrt{t}+\frac{1}{t^{3}})dt=\int(8t^{3}-6t^{1/2}+t^{-3})dt$$
$$=8\cdot\frac{t^{4}}{4}-6\cdot\frac{t^{3/2}}{\frac{3}{2}}+\frac{t^{-2}}{-2}+C$$
$$=2t^{4}-4t^{3/2}-\frac{1}{2t^{2}}+C$$

### Example 4
Evaluate $\int\frac{(x^{2}-1)^{2}}{x^{2}}dx.$
**Solution**
First we change the form of the integrand, because the degree of the numerator is greater than or equal to the degree of the denominator. We then find an antiderivative for each term, adding an arbitrary constant C after the last integration:
$$\int\frac{(x^{2}-1)^{2}}{x^{2}}dx=\int\frac{x^{4}-2x^{2}+1}{x^{2}}dx$$
$$=\int(x^{2}-2+x^{-2})dx$$
$$=\frac{x^{3}}{3}-2x+\frac{x^{-1}}{-1}+C$$
$$=\frac{1}{3}x^{3}-2x-\frac{1}{x}+C$$

### Example 5
Evaluate $\int\frac{1}{cos~u~cot~u}du$
**Solution**
We use trigonometric identities to change the integrand and then apply Formula (7) from Table (4.4):
$$\int\frac{1}{cos~u~cot~u}du=\int sec~u~tan~u~du$$
$$=sec~u+C$$

### Example 6
Solve the differential equation $f^{\prime}(x)=6x^{2}+x-5$ subject to the initial condition $f(0)=2$
**Solution**
We proceed as follows:
$$f^{\prime}(x)=6x^{2}+x-5$$
$$\int f^{\prime}(x)dx=\int(6x^{2}+x-5)dx$$
$$f(x)=2x^{3}+\frac{1}{2}x^{2}-5x+C$$
for some number C. Letting $x=0$ and using the given initial condition $f(0)=2$ gives us
$$f(0)=0+0-0+C \quad \text{or} \quad 2=C$$
Hence the solution f of the differential equation with the initial condition $f(0)=2$ is
$$f(x)=2x^{3}+\frac{1}{2}x^{2}-5x+2$$

### Example 7
Solve the differential equation $f^{\prime\prime}(x)=5~cos~x+2~sin~x$ subject to the initial conditions $f(0)=3$ and $f^{\prime}(0)=4$
**Solution**
We proceed as follows:
$$f^{\prime\prime}(x)=5~cos~x+2~sin~x$$
$$\int f^{\prime\prime}(x)dx=\int(5~cos~x+2~sin~x)dx$$
$$f^{\prime}(x)=5~sin~x-2~cos~x+C$$
Letting $x=0$ and using the initial condition $f^{\prime}(0)=4$ gives us
$$f^{\prime}(0)=5~sin~0-2~cos~0+C$$
$$4=0-2\cdot1+C \quad \text{or} \quad C=6$$
Thus,
$$f^{\prime}(x)=5~sin~x-2~cos~x+6$$
We integrate a second time:
$$\int f^{\prime}(x)dx=\int(5~sin~x-2~cos~x+6)dx$$
$$f(x)=-5~cos~x-2~sin~x+6x+D$$
Letting $x=0$ and using the initial condition $f(0)=3$, we find that
$$f(0)=-5~cos~0-2~sin~0+6\cdot0+D$$
$$3=-5-0+0+D,$$
or $D=8$.
Therefore, the solution of the differential equation with the given initial condition is
$$f(x)=-5~cos~x-2~sin~x+6x+8$$.

### Example 8
A particle moving along a coordinate line at time $t=0$ is at a position 3 cm from the origin and traveling at a velocity of 7 cm/sec. If the acceleration of the particle is given by $a(t)=2-2(t+1)^{-3}$, find the velocity and the position of the particle as functions of t.
**Solution**
Since the velocity $v(t)=\int v^{\prime}(t)dt=\int a(t)dt,$ we have
$$v(t)=\int[2-2(t+1)^{-3}]dt$$
$$=2t+(t+1)^{-2}+C$$
for some number C. Substituting 0 for t and using the fact that $v(0)=7$ gives us $7=0+1+C$ or $C=6$. Consequently,
$$v(t)=2t+(t+1)^{-2}+6.$$
Since $s^{\prime}(t)=v(t)$ we obtain
$$s^{\prime}(t)=2t+(t+1)^{-2}+6$$
$$\int s^{\prime}(t)dt=\int[2t+(t+1)^{-2}+6]dt$$
$$s(t)=t^{2}-(t+1)^{-1}+6t+D$$
for some number D. Using the fact that $s(0)=3$ gives $3=0-1+0+D$ or $D=4$. Thus, the position of the particle from the origin at time t is given by
$$s(t)=t^{2}-(t+1)^{-1}+6t+4$$ cm,
and the particle travels at a velocity of
$$v(t)=2t+(t+1)^{-2}+6$$ cm/sec.

### Example 9
A manufacturer finds that the marginal cost (in dollars) associated with the production of x units of a photocopier component is given by $30-0.02x$. If the cost of producing one unit is $35, find the cost function and the cost of producing 100 units.
**Solution**
If C is the cost function, then the marginal cost is the rate of change of C with respect to x-that is,
$$C^{\prime}(x)=30-0.02x$$.
Hence
$$\int C^{\prime}(x)dx=\int(30-0.02x)dx$$
and
$$C(x)=30x-0.01x^{2}+K$$
for some K. Letting $x=1$ and using $C(1)=35,$ we obtain
$$35=30-0.01+K \quad \text{or} \quad K=5.01$$
Consequently,
$$C(x)=30x-0.01x^{2}+5.01$$
In particular, the cost of producing 100 units is
$$C(100)=3000-100+5.01$$
$$=\$2905.01$$.

## Exercises
*   1. $\int(4x+3)dx$
*   5. $\int(\frac{1}{z^{3}}-\frac{3}{z^{2}})dz$
*   7. $\int(3\sqrt{u}+\frac{1}{\sqrt{u}})du$
*   11. $\int(3x-1)^{2}dx$
*   14. $\int(2x-5)(3x+1)dx$
*   15. $\int\frac{8x-5}{\sqrt[2]{x}}dx$
*   17. $\int\frac{x^{3}-1}{x-1}dx$
*   23. $\int\frac{7}{csc~x}dx$
*   27. $\int\frac{sec~t}{cos~t}dt$
*   29. $\int(csc~v~cot~v~sev~v)dv$
*   35. $\int\frac{d}{dx}(\sqrt{x^{2}+4})dx$
*   41. Show that $\int x^{2}dx\ne x\int x~dx.$
*   43. $\int a^{2}dx$
*   49. $f^{\prime}(x)=12x^{2}-6x+1$; $f(1)=5$