---
source_file: "Section_4.4_The_Definite_Integral.pdf"
course: MATH106
book_chapter: 4
book_section: 4.4
ksu_chapter: UNKNOWN
section_title: THE DEFINITE INTEGRAL
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: [1, 5, 10, 11, 15, 16, 19, 20, 31, 33, 37]
topic_tags: [definite-integral, riemann-sum, partitions, area, limits]
difficulty: UNKNOWN
in_syllabus: true
enrichment: UNKNOWN
status: draft
---

# THE DEFINITE INTEGRAL

## Metadata
**Course:** MATH106
**Book:** Calculus (Swokowski)
**Edition:** 6th
**Chapter Number:** 4
**Chapter Title:** Integrals
**Section Number:** 4.4
**Section Title:** THE DEFINITE INTEGRAL

## Definitions
**Definition 4.14**
Let f be defined on a closed interval $[a,b]$, and let P be a partition of $[a,b]$. A Riemann sum of f (or $f(x)$) for P is any expression $R_{P}$ of the form
$$R_{P}=\sum_{k=1}^{n}f(w_{k})\Delta x_{k}$$
where $w_{k}$ is in $[x_{k-1},x_{k}]$ and $k=1,2,...,n.$

**Definition 4.15**
Let f be defined on a closed interval $[a,b]$, and let L be a real number. The statement
$$lim_{||P||\rightarrow0}\sum_{k}f(w_{k})\Delta x_{k}=L$$
means that for every $\epsilon>0$, there is a $\delta>0$ such that if P is a partition of $[a,b]$ with $||P||<\delta$, then
$$|\sum_{k}f(w_{k})\Delta x_{k}-L|<\epsilon$$
for any choice of numbers $w_{k}$ in the subintervals $[x_{k-1},x_{k}]$ of P. The number L is a limit of (Riemann) sums.

**Definition 4.16**
Let f be defined on a closed interval $[a,b]$. The definite integral of f from a to b, denoted by $\int_{a}^{b}f(x)dx$, is
$$\int_{a}^{b}f(x)dx=lim_{||P||\rightarrow0}\sum_{k}f(w_{k})\Delta x_{k},$$
provided the limit exists.

**Definition 4.17**
If $c>d$, then
$$\int_{c}^{d}f(x)dx=-\int_{d}^{c}f(x)dx.$$

**Definition 4.18**
If $f(a)$ exists, then
$$\int_{a}^{a}f(x)dx\equiv0.$$

## Theorems
**Theorem 4.19**
If f is integrable and $f(x)\ge0$ for every x in $[a,b]$, then the area A of the region under the graph of f from a to b is
$$A=\int_{a}^{b}f(x)dx.$$

**Theorem 4.20**
If f is continuous on $[a,b]$ then f is integrable on $[a,b].$

## Formulas
No formal boxed formulas distinct from Methods.

## Guidelines / Methods
**Endpoint and Midpoint Approximations for Definite Integrals**
For a regular partition where $\Delta x=(b-a)/n$:
*   **Left endpoint approximation ($L_n$):** Let $w_{k}=x_{k-1}$
    $$\int_{a}^{b}f(x)dx\approx L_{n}=\sum_{k=1}^{n}f(x_{k-1})\Delta x$$
*   **Right endpoint approximation ($R_n$):** Let $w_{k}=x_{k}$
    $$\int_{a}^{b}f(x)dx\approx R_{n}=\sum_{k=1}^{n}f(x_{k})\Delta x$$
*   **Midpoint approximation ($M_n$):** Let $w_{k}=(x_{k-1}+x_{k})/2$
    $$\int_{a}^{b}f(x)dx\approx M_{n}=\sum_{k=1}^{n}f(\frac{x_{k-1}+x_{k}}{2})\Delta x$$

## Worked Examples
### Example 1
The numbers $\{1, 1.7, 2.2, 3.3, 4.1, 4.5, 5, 6\}$ determine a partition P of the interval $[1,6]$. Find the lengths $\Delta x_{1}, ..., \Delta x_{n}$ of the subintervals in P and the norm of the partition.
**Solution**
The lengths $\Delta x_{k}$ of the subintervals are found by subtracting successive numbers in P. Thus,
$\Delta x_{1}=0.7$, $\Delta x_{2}=0.5$, $\Delta x_{3}=1.1$, $\Delta x_{4}=0.8$, $\Delta x_{5}=0.4$, $\Delta x_{6}=0.5$, $\Delta x_{7}=1.0$.
The norm of P is the largest of these numbers. Hence,
$$||P||=\Delta x_{3}=1.1.$$

### Example 2
Let $f(x)=8-\frac{1}{2}x^{2}$, and let P be the partition of $[0,6]$ into the five subintervals determined by
$x_{0}=0$, $x_{1}=1.5$, $x_{2}=2.5$, $x_{3}=4.5$, $x_{4}=5$, $x_{5}=6$
Find the norm of the partition and the Riemann sum $R_{P}$ if
$w_{1}=1$, $w_{2}=2$, $w_{3}=3.5$, $w_{4}=5$, $w_{5}=5.5$
**Solution**
The lengths of the subintervals are:
$\Delta x_{1}=1.5$, $\Delta x_{2}=1$, $\Delta x_{3}=2$, $\Delta x_{4}=0.5$, $\Delta x_{5}=1.$
The norm $||P||$ of the partition is $\Delta x_{3}$ or 2.
Using Definition (4.14) with $n=5$ we have
$$R_{P}=\sum_{k=1}^{5}f(w_{k})\Delta x_{k}$$
$$=f(w_{1})\Delta x_{1}+f(w_{2})\Delta x_{2}+f(w_{3})\Delta x_{3}+f(w_{4})\Delta x_{4}+f(w_{5})\Delta x_{5}$$
$$=f(1)(1.5)+f(2)(1)+f(3.5)(2)+f(5)(0.5)+f(5.5)(1)$$
$$=(7.5)(1.5)+(6)(1)+(1.875)(2)+(-4.5)(0.5)+(-7.125)(1)$$
$$=11.625$$

### Example 3
Express the following limit of sums as a definite integral on the interval $[3,8]$
$$lim_{||P||\rightarrow0}\sum_{k=1}^{n}(5w_{k}^{3}+\sqrt{w_{k}}-4~sin~w_{k})\Delta x_{k}$$
where $w_{k}$ and $\Delta x_{k}$ are as in Definition (4.15).
**Solution**
The given limit of sums has the form stated in Definition (4.16), with
$$f(x)=5x^{3}+\sqrt{x}-4~sin~x$$
Hence the limit can be expressed as the definite integral
$$\int_{3}^{8}(5x^{3}+\sqrt{x}-4~sin~x)dx.$$

### Example 4
Use midpoint approximations with $n=10, 20, 40$ and 80 to estimate $\int_{0}^{\pi}cos(x^{2})dx$.
**Solution**
For a regular partition, $\Delta x=(\pi-0)/n=\pi/n$, so that $x_{k}=k\pi/n$. Thus,
$$\frac{x_{k-1}+x_{k}}{2}=\frac{\frac{(k-1)\pi}{n}+\frac{k\pi}{n}}{2}=\frac{k\pi+k\pi-\pi}{2n}=\frac{2k\pi-\pi}{2n}=\frac{k\pi}{n}-\frac{\pi}{2n}.$$
With $f(x)=cos(x^{2})$, we have
$$f(\frac{x_{k-1}+x_{k}}{2})=cos(\frac{k\pi}{n}-\frac{\pi}{2n})^{2}.$$
We use a calculator to compute the desired summations for the midpoint approximations:
$$\int_{0}^{\pi}cos(x^{2})dx\approx M_{n}=\sum_{k=1}^{n}[cos(\frac{k\pi}{n}-\frac{\pi}{2n})^{2}]\frac{\pi}{n}$$
$M_{10}\approx0.553751825506$
$M_{20}\approx0.562860413669$
$M_{40}\approx0.564995257214$
$M_{80}\approx0.565519579069$

### Example 5
Evaluate $\int_{-2}^{4}(\frac{1}{2}x+3)dx$.
**Solution**
If $f(x)=\frac{1}{2}x+3$ then the graph of f is a line. By Theorem (4.19), the value of the integral is numerically equal to the area of the region under this line from $x=-2$ to $x=4$. The region is a trapezoid with bases parallel to the y-axis of lengths 2 and 5 and altitude on the x-axis of length 6. Using the formula for the area of a trapezoid, we obtain
$$\int_{-2}^{4}(\frac{1}{2}x+3)dx=\frac{1}{2}(2+5)6=21.$$

### Example 6
Evaluate $\int_{-4}^{4}\sqrt{16-x^{2}}dx$
**Solution**
If $f(x)=\sqrt{16-x^{2}}$ then the graph of f is a semicircle. By Theorem (4.19), the value of the integral is numerically equal to the area of the region under this semicircle from $x=-4$ to $x=4$. Hence,
$$\int_{-4}^{4}\sqrt{16-x^{2}}dx=\frac{1}{2}\cdot\pi(4)^{2}=8\pi.$$

### Example 7
Evaluate
(a) $\int_{4}^{-4}\sqrt{16-x^{2}}dx$
(b) $\int_{4}^{4}\sqrt{16-x^{2}}dx$
**Solution**
(a) Using Definition (4.17) and Example 6, we have
$$\int_{4}^{-4}\sqrt{16-x^{2}}dx=-\int_{-4}^{4}\sqrt{16-x^{2}}dx=-8\pi.$$
(b) By Definition (4.18),
$$\int_{4}^{4}\sqrt{16-x^{2}}dx=0.$$

## Exercises
*   1. The given numbers determine a partition P of an interval. (a) Find the length of each subinterval of P. (b) Find the norm $||P||$ of the partition. $\{0, 1.1, 2.6, 3.7, 4.1, 5\}$
*   5. Find the Riemann sum $R$ for the given function f on the indicated partition P by choosing on each subinterval of P (a) the left-hand endpoint, (b) the right-hand endpoint, and (c) the midpoint. $f(x)=2x+3$; $P=\{1,3,4,5\}$
*   10. Find the Riemann sum $R$ for the given function f on the indicated partition P by choosing on each subinterval of P (a) the left-hand endpoint, (b) the right-hand endpoint, and (c) the midpoint. $f(x)=\sqrt{x}$, $P=\{1,3,4,9,12,16\}$, $n=5$
*   11. Find the Riemann sum $R$ for the given function f on the indicated interval with a regular partition P of size n by choosing on each subinterval of P (a) the left-hand endpoint, (b) the right-hand endpoint, and (c) the midpoint. $f(x)=x^{3}$; $[-2,6]$, $n=32$
*   15. Use Definition (4.16) to express each limit as a definite integral on the given interval $[a,b]$. $lim_{||P||\rightarrow0}\sum_{k=1}^{n}(3w_{k}^{2}-2w_{k}+5)\Delta x_{k}$; $[-1,2]$
*   16. Use Definition (4.16) to express each limit as a definite integral on the given interval $[a,b]$. $lim_{||P||\rightarrow0}\sum_{k=1}^{n}\pi(w_{k}^{2}-4)\Delta x_{k}$; $[2,3]$
*   19. Given $\int_{1}^{4}\sqrt{x}dx=\frac{14}{3}$, evaluate the integral. $\int_{4}^{1}\sqrt{x}dx$
*   20. Given $\int_{1}^{4}\sqrt{x}dx=\frac{14}{3}$, evaluate the integral. $\int_{1}^{4}\sqrt{t}dt$
*   31. Evaluate the definite integral by regarding it as the area under the graph of a function. $\int_{-3}^{2}(2x+6)dx$
*   33. Evaluate the definite integral by regarding it as the area under the graph of a function. $\int_{-1}^{4}|x|dx$
*   37. Evaluate the definite integral by regarding it as the area under the graph of a function. $\int_{-2}^{2}(3+\sqrt{4-x^{2}})dx$