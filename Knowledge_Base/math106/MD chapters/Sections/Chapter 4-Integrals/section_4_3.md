---
course: MATH106
book_chapter: 4
book_section: 4.3
ksu_chapter: UNKNOWN
section_title: SUMMATION NOTATION AND AREA
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: [1, 2, 3, 5, 6, 9, 12, 27, 37]
topic_tags: [summation-notation, area, limits, rectangles]
difficulty: UNKNOWN
in_syllabus: true
enrichment: UNKNOWN
status: draft
---

# SUMMATION NOTATION AND AREA

## Metadata
**Course:** MATH106
**Book:** Calculus (Swokowski)
**Edition:** 6th
**Chapter Number:** 4
**Chapter Title:** Integrals
**Section Number:** 4.3
**Section Title:** SUMMATION NOTATION AND AREA

## Definitions
**Summation Notation 4.9**
Given a collection of numbers $\{a_{1},a_{2},...,a_{n}\}$, the symbol $\sum_{k=1}^{n}a_{k}$ represents their sum as follows.
$$\sum_{k=1}^{n}a_{k}=a_{1}+a_{2}+a_{3}+\cdot\cdot\cdot+a_{n}$$

**Definition 4.13**
Let f be continuous and nonnegative on $[a,b].$ Let A be a real number, and let $f(u_{k})$ be the minimum value of f on $[x_{k-1},x_{k}]$ The notation
$$A=lim_{\Delta x\rightarrow0}\sum_{k=1}^{n}f(u_{k})\Delta x$$
means that for every $\epsilon>0$, there is a $\delta>0$ such that if $0<\Delta x<\delta$, then
$$A-\sum_{k=1}^{n}f(u_{k})\Delta x<\epsilon,$$

## Theorems
**Theorem 4.10**
If $a_{k}=c$ for every k, then
$$\sum_{k=1}^{n}c=nc$$

**Theorem 4.11**
If n is any positive integer and $\{a_{1},a_{2},...,a_{n}\}$ and $\{b_{1},b_{2},...,b_{n}\}$ are sets of real numbers, then
(i) $\sum_{k=1}^{n}(a_{k}+b_{k})=\sum_{k=1}^{n}a_{k}+\sum_{k=1}^{n}b_{k}$
(ii) $\sum_{k=1}^{n}ca_{k}=c(\sum_{k=1}^{n}a_{k}),$ for every real number c
(iii) $\sum_{k=1}^{n}(a_{k}-b_{k})=\sum_{k=1}^{n}a_{k}-\sum_{k=1}^{n}b_{k}$

**Theorem 4.12**
(i) $\sum_{k=1}^{n}k=1+2+\cdot\cdot\cdot+n=\frac{n(n+1)}{2}$
(ii) $\sum_{k=1}^{n}k^{2}=1^{2}+2^{2}+\cdot\cdot\cdot+n^{2}=\frac{n(n+1)(2n+1)}{6}$
(iii) $\sum_{k=1}^{n}k^{3}=1^{3}+2^{3}+\cdot\cdot\cdot+n^{3}=[\frac{n(n+1)}{2}]^{2}$

## Formulas
No formal boxed or numbered formulas.

## Guidelines / Methods
No numbered guideline lists or method tables.

## Worked Examples
### Example 1
Evaluate $\sum_{k=1}^{4}k^{2}(k-3).$
**Solution**
Comparing the sum with (4.9), we have $a_{k}=k^{2}(k-3)$ and $n=4.$ To find the sum, we substitute 1, 2, 3, and 4 for k and add the resulting terms. Thus,
$$\sum_{k=1}^{4}k^{2}(k-3)=1^{2}(1-3)+2^{2}(2-3)+3^{2}(3-3)+4^{2}(4-3)$$
$$=(-2)+(-4)+0+16=10$$

### Example 2
Evaluate $\sum_{k=0}^{3}\frac{2^{k}}{(k+1)}$
**Solution**
$$\sum_{k=0}^{3}\frac{2^{k}}{(k+1)}=\frac{2^{0}}{(0+1)}+\frac{2^{1}}{(1+1)}+\frac{2^{2}}{(2+1)}+\frac{2^{3}}{(3+1)}$$
$$=1+1+\frac{4}{3}+2=\frac{16}{3}$$

### Example 3
Evaluate $\sum_{k=1}^{100}k$ and $\sum_{k=1}^{20}k^{2}$
**Solution**
Using (i) and (ii) of Theorem (4.12), we obtain
$$\sum_{k=1}^{100}k=1+2+\cdot\cdot\cdot+100=\frac{100(101)}{2}=5050$$
and
$$\sum_{k=1}^{20}k^{2}=1^{2}+2^{2}+\cdot\cdot\cdot+20^{2}=\frac{20(21)(41)}{6}=2870.$$

### Example 4
Express $\sum_{k=1}^{n}(k^{2}-4k+3)$ in terms of n.
**Solution**
We use Theorems (4.11), (4.12), and (4.10):
$$\sum_{k=1}^{n}(k^{2}-4k+3)=\sum_{k=1}^{n}k^{2}-4\sum_{k=1}^{n}k+\sum_{k=1}^{n}3$$
$$=\frac{n(n+1)(2n+1)}{6}-4\frac{n(n+1)}{2}+3n$$
$$=\frac{1}{3}n^{3}-\frac{3}{2}n^{2}+\frac{7}{6}n$$

### Example 5
Let $f(x)=\sqrt{x}$, and let R be the region under the graph of f from 1 to 5. Approximate the area A of R using
(a) an inscribed rectangular polygon with $\Delta x=0.1$
(b) a circumscribed rectangular polygon with $\Delta x=0.1$
**Solution**
With $\Delta x=0.1=1/10,$ the interval $[1,5]$ is divided into 40 subintervals. Since $x_{0}=1$ and $x_{n}=5$ with $n=40,$ we have $x_{k}=1+k\Delta x=1+k/10$
(a) Since f is increasing on the interval $[1,5]$, we obtain inscribed rectangles by selecting $u_{k}=x_{k-1}$ the left-hand endpoint of each subinterval $[x_{k-1},x_{k}]$. Thus,
$$u_{k}=1+\frac{k-1}{10}$$
and
$$f(u_{k})=\sqrt{1+\frac{k-1}{10}}.$$
Using a computational device to sum the 40 terms, we find that the inscribed rectangular polygon has area
$$A_{IP}=\sum_{k=1}^{40}\sqrt{1+\frac{k-1}{10}}(\frac{1}{10})\approx6.72485958283$$ .
(b) We obtain circumscribed rectangles over $[1,5]$ by selecting $u_{k}=x_{k}$ the right-hand endpoint of each subinterval $[x_{k-1},x_{k}]$ Hence, the area of the circumscribed rectangular polygon is
$$A_{CP}=\sum_{k=1}^{40}\sqrt{1+\frac{k}{10}}(\frac{1}{10})\approx6.84846638058$$
Thus, we can conclude that the area A satisfies
$$6.72485958283<A<6.84846638058.$$

### Example 6
One side of a farmer's field is bordered by a straight stretch of highway. The opposite side is bordered by a river whose path traces a curve that is modeled by the function $f(x)=16-x^{2}$. The farmer measures the side of the field along the highway, placing markers at every $\frac{1}{2}$ km for a total of 3 km, as shown in Figure 4.6. Approximate the area A of the field using
(a) an inscribed rectangular polygon with $\Delta x=\frac{1}{2}$
(b) a circumscribed rectangular polygon with $\Delta x=\frac{1}{2}$
**Solution**
(a) We model the farmer's field by graphing the function $f(x)=16-x^{2}$ and considering the area of the region under the graph from 0 to 3 on the x-axis, which is the side of the field measured in units of $\frac{1}{2}$ km. Note that f is decreasing on $[0,3]$, and hence the minimum value $f(u_{k})$ on the kth subinterval occurs at the right-hand endpoint of the subinterval. Since there are six rectangles to consider, the formula for $A_{IP}$ is
$$A_{IP}=\sum_{k=1}^{6}f(u_{k})\Delta x$$
$$=f(\frac{1}{2})\cdot\frac{1}{2}+f(1)\cdot\frac{1}{2}+f(\frac{3}{2})\cdot\frac{1}{2}+f(2)\cdot\frac{1}{2}+f(\frac{5}{2})\cdot\frac{1}{2}+f(3)\cdot\frac{1}{2}$$
$$=\frac{63}{4}\cdot\frac{1}{2}+15\cdot\frac{1}{2}+\frac{55}{4}\cdot\frac{1}{2}+12\cdot\frac{1}{2}+\frac{39}{4}\cdot\frac{1}{2}+7\cdot\frac{1}{2}$$
$$=\frac{295}{8}=36.625$$
Using inscribed rectangles, we find that the area of the field is approximately 36.6 km²
(b) Since f is decreasing on $[0,3]$, the maximum value $f(v_{k})$ occurs at the left-hand endpoint of the kth subinterval. Hence,
$$A_{CP}=\sum_{k=1}^{6}f(v_{k})\Delta x$$
$$=f(0)\cdot\frac{1}{2}+f(\frac{1}{2})\cdot\frac{1}{2}+f(1)\cdot\frac{1}{2}+f(\frac{3}{2})\cdot\frac{1}{2}+f(2)\cdot\frac{1}{2}+f(\frac{5}{2})\cdot\frac{1}{2}$$
$$=16\cdot\frac{1}{2}+\frac{63}{4}\cdot\frac{1}{2}+15\cdot\frac{1}{2}+\frac{55}{4}\cdot\frac{1}{2}+12\cdot\frac{1}{2}+\frac{39}{4}\cdot\frac{1}{2}$$
$$=\frac{329}{8}=41.125$$.
Using circumscribed rectangles, we find that the area of the field is approximately 41.1 km².

### Example 7
Referring to Example 6, determine the area of the farmer's field, which is the area of the region under the graph of f from 0 to 3.
**Solution**
If the interval $[0,3]$ is divided into n equal subintervals, then the length $\Delta x$ of each subinterval is $3/n$. Employing the notation used in Figure 4.4, with $a=0$ and $b=3$ we have
$$x_{0}=0, \quad x_{1}=\Delta x, \quad x_{2}=2\Delta x, \quad \dots$$
$$x_{k}=k\Delta x, \quad \dots, \quad x_{n}=n\Delta x=3$$
Since $\Delta x=3/n$,
$$x_{k}=k\Delta x=k\frac{3}{n}=\frac{3k}{n}$$
Since f is decreasing on $[0,3]$, the number $u_{k}$ in $[x_{k-1},x_{k}]$ at which f takes on its minimum value is always the right-hand endpoint $x_{k}$ of the subinterval; that is, $u_{k}=x_{k}=3k/n$. Thus,
$$f(u_{k})=f(\frac{3k}{n})=16-(\frac{3k}{n})^{2}=16-\frac{9k^{2}}{n^{2}},$$
and the summation in Definition (4.13) is
$$\sum_{k=1}^{n}f(u_{k})\Delta x=\sum_{k=1}^{n}[(16-\frac{9k^{2}}{n^{2}})\cdot\frac{3}{n}]$$
$$=\frac{3}{n}\sum_{k=1}^{n}(16-\frac{9k^{2}}{n^{2}})$$
where the last equality follows from (ii) of Theorem (4.11). We next use Theorems (4.11), (4.10), and (4.12) to obtain
$$\sum_{k=1}^{n}f(u_{k})\Delta x=\frac{3}{n}(\sum_{k=1}^{n}16-\frac{9}{n^{2}}\sum_{k=1}^{n}k^{2})$$
$$=\frac{3}{n}[n\cdot16-\frac{9}{n^{2}}\frac{n(n+1)(2n+1)}{6}]$$
$$=48-\frac{9}{2}\frac{(n+1)(2n+1)}{n^{2}}.$$
To find the area of the region, we let $\Delta x$ approach 0. Since $\Delta x=3/n$, we can accomplish this by letting n increase without bound. Assuming that we can replace $\Delta x\rightarrow0$ by $n\rightarrow\infty$, we obtain
$$lim_{\Delta x\rightarrow0}\sum_{k=1}^{n}f(u_{k})\Delta x=lim_{n\rightarrow\infty}[48-\frac{9}{2}\frac{(n+1)(2n+1)}{n^{2}}]$$
$$=48-\frac{9}{2}\cdot2=39.$$
Thus the area of the region under the graph of f from 0 to 3 is 39, which means that the area of the farmer's field is 39 km².

### Example 8
If $f(x)=x^{3}$ find the area under the graph of f from 0 to b for any $b>0$
**Solution**
Subdividing the interval $[0,b]$ into n equal parts, we obtain a circumscribed rectangular polygon such that $\Delta x=b/n$ and $x_{k}=k~\Delta x$. Since f is an increasing function, the maximum value $f(v_{k})$ in the interval $[x_{k-1},x_{k}]$ occurs at the right-hand endpoint-that is,
$$v_{k}=x_{k}=k\Delta x=k\frac{b}{n}=\frac{bk}{n}$$
The sum of the areas of the circumscribed rectangles is
$$\sum_{k=1}^{n}f(v_{k})\Delta x=\sum_{k=1}^{n}[(\frac{bk}{n})^{3}\cdot\frac{b}{n}]=\sum_{k=1}^{n}\frac{b^{4}}{n^{4}}k^{3}$$
$$=\frac{b^{4}}{n^{4}}\sum_{k=1}^{n}k^{3}=\frac{b^{4}}{n^{4}}[\frac{n(n+1)}{2}]^{2}$$
$$=\frac{b^{4}}{4}\cdot\frac{n^{2}(n+1)^{2}}{n^{4}},$$
where we have used Theorem (4.12)(iii). If we let $\Delta x$ approach 0, then n increases without bound and the expression involving n approaches 1. It follows that the area under the graph is
$$lim_{\Delta x\rightarrow0}\sum_{k=1}^{n}f(v_{k})\Delta x=\frac{b^{4}}{4}.$$

### Example 9
If $f(x)=x^{3}$ find the area A of the region under the graph of f from $\frac{1}{2}$ to 2.
**Solution**
If we let $A_{1}$ = area under the graph of f from 0 to $\frac{1}{2}$ and $A_{2}$ = area under the graph of f from 0 to 2, the area A can be found by subtracting $A_{1}$ from $A_{2}$:
$$A=A_{2}-A_{1}$$
In Example 8, we found that the area under the graph of $y=x^{3}$ from 0 to b is $\frac{1}{4}b^{4}$. Hence, using $b=\frac{1}{2}$ for $A_{1}$, and $b=2$ for $A_{2}$ yields
$$A=\frac{2^{4}}{4}-\frac{(\frac{1}{2})^{4}}{4}=4-\frac{1}{64}\approx3.98.$$

## Exercises
*   1. $\sum_{j=1}^{4}(j^{2}+1)$
*   2. $\sum_{j=1}^{4}(2^{j}+1)$
*   3. $\sum_{k=0}^{5}k(k-1)$
*   5. $\sum_{n=1}^{10}\{1+(-1)^{n}\}$
*   6. $\sum_{n=1}^{4}(-1)^{n}(\frac{1}{n})$
*   9. $\sum_{k=1}^{n}(k^{2}+3k+5)$
*   12. $\sum_{k=1}^{n}(3k^{3}+k)$
*   27. UNREADABLE (Exercise not included in provided source document)
*   37. UNREADABLE (Exercise not included in provided source document)