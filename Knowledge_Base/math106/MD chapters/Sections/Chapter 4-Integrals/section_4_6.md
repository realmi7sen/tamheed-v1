---
course: MATH106
book_chapter: 4
book_section: 4.6
ksu_chapter: UNKNOWN
section_title: THE FUNDAMENTAL THEOREM OF CALCULUS
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: [1, 7, 8, 9, 11, 12, 13, 15, 17, 21, 29, 32, 36, 45, 47]
topic_tags: [fundamental-theorem-of-calculus, definite-integrals, antiderivatives, mean-value-theorem]
difficulty: UNKNOWN
in_syllabus: true
enrichment: UNKNOWN
status: draft
---

# THE FUNDAMENTAL THEOREM OF CALCULUS

## Metadata
**Course:** MATH106
**Book:** Calculus (Swokowski)
**Edition:** 6th
**Chapter Number:** 4
**Chapter Title:** Integrals
**Section Number:** 4.6
**Section Title:** THE FUNDAMENTAL THEOREM OF CALCULUS

## Definitions
No formal boxed definitions.

## Theorems
**Fundamental Theorem of Calculus 4.30**
Suppose f is continuous on a closed interval $[a,b]$.
Part I If the function G is defined by
$$G(x)=\int_{a}^{x}f(t)dt$$
for every x in $[a,b]$, then G is an antiderivative of f on $[a,b]$.
Part II If F is any antiderivative of f on $[a,b]$, then
$$\int_{a}^{b}f(x)dx=F(b)-F(a).$$

**Corollary 4.31**
If f is continuous on $[a,b]$ and F is any antiderivative of f, then
$$\int_{a}^{b}f(x)dx=F(x)]_{a}^{b}=F(b)-F(a).$$

**Theorem 4.32**
$$\int_{a}^{b}f(x)dx=[\int f(x)dx]_{a}^{b}$$

**Theorem 4.33**
If $u=g(x)$ then $\int_{a}^{b}f(g(x))g^{\prime}(x)dx=\int_{g(a)}^{g(b)}f(u)du.$

**Theorem 4.34**
Let f be continuous on $[-a,a]$
(i) If f is an even function,
$$\int_{-a}^{a}f(x)dx=2\int_{0}^{a}f(x)dx.$$
(ii) If f is an odd function,
$$\int_{-a}^{a}f(x)dx=0.$$

**Theorem 4.35**
Let f be continuous on $[a,b]$. If $a\le c\le b$, then for every x in $[a,b]$,
$$\frac{d}{dx}\int_{c}^{x}f(t)dt=f(x).$$

## Formulas
No formal boxed formulas distinct from Theorems and Methods.

## Guidelines / Methods
No numbered guideline lists or method tables.

## Worked Examples
### Example 1
Evaluate $\int_{-2}^{3}(6x^{2}-5)dx$.
**Solution**
An antiderivative of $6x^{2}-5$ is $F(x)=2x^{3}-5x$. Applying Corollary (4.31), we get
$$\int_{-2}^{3}(6x^{2}-5)dx=[2x^{3}-5x]_{-2}^{3}$$
$$=[2(3)^{3}-5(3)]-[2(-2)^{3}-5(-2)]$$
$$=[54-15]-[-16+10]=45.$$

### Example 2
Find the area A of the region between the graph of $y=sin~x$ and the x-axis from $x=0$ to $x=\pi$.
**Solution**
Applying Theorems (4.19) and (4.32) gives us the following:
$$A=\int_{0}^{\pi}sin~x~dx=[\int sin~x~dx]_{0}^{\pi}$$
$$=[-cos~x]_{0}^{\pi}$$
$$=-cos~\pi-(-cos~0)$$
$$=-(-1)+1=2$$

### Example 3
Evaluate $\int_{-1}^{2}(x^{3}+1)^{2}dx$
**Solution**
We first square the integrand and then apply the power rule to each term as follows:
$$\int_{-1}^{2}(x^{3}+1)^{2}dx=\int_{-1}^{2}(x^{6}+2x^{3}+1)dx$$
$$=[\frac{x^{7}}{7}+2\cdot\frac{x^{4}}{4}+x]_{-1}^{2}$$
$$=[\frac{2^{7}}{7}+2\cdot\frac{2^{4}}{4}+2]-[\frac{(-1)^{7}}{7}+2\frac{(-1)^{4}}{4}+(-1)]$$
$$=\frac{405}{14}$$

### Example 4
Evaluate $\int_{1}^{4}(5x-2\sqrt{x}+\frac{32}{x^{3}})dx.$
**Solution**
We begin by changing the form of the integrand so that the power rule may be applied to each term. Thus,
$$\int_{1}^{4}(5x-2x^{1/2}+32x^{-3})dx=[5(\frac{x^{2}}{2})-2(\frac{x^{3/2}}{3/2})+32(\frac{x^{-2}}{-2})]_{1}^{4}$$
$$=[\frac{5}{2}x^{2}-\frac{4}{3}x^{3/2}-\frac{16}{x^{2}}]_{1}^{4}$$
$$=[\frac{5}{2}(4)^{2}-\frac{4}{3}(4)^{3/2}-\frac{16}{4^{2}}]-[\frac{5}{2}-\frac{4}{3}-16]$$
$$=\frac{259}{6}$$

### Example 5
Evaluate $\int_{2}^{10}\frac{3}{\sqrt{5x-1}}dx.$
**Solution**
Let us begin by writing the integral as
$$3\int_{2}^{10}\frac{1}{\sqrt{5x-1}}dx.$$
The expression $\sqrt{5x-1}$ in the integrand suggests the following substitution:
$$u=5x-1 \quad du=5~dx$$
The form of du indicates that we should introduce the factor 5 into the integrand and then compensate by multiplying the integral by $\frac{1}{5},$ as follows:
$$3\int_{2}^{10}\frac{1}{\sqrt{5x-1}}dx=\frac{3}{5}\int_{2}^{10}\frac{1}{\sqrt{5x-1}}5dx$$
We next calculate the values of $u=5x-1$ that correspond to the limits of integration $x=2$ and $x=10$
(i) If $x=2,$ then $u=5(2)-1=9$
(ii) If $x=10$, then $u=5(10)-1=49$
Substituting in the integrand and changing the limits of integration as in Theorem (4.33) gives us
$$3\int_{2}^{10}\frac{1}{\sqrt{5x-1}}dx=\frac{3}{5}\int_{2}^{10}\frac{1}{\sqrt{5x-1}}5dx$$
$$=\frac{3}{5}\int_{9}^{49}\frac{1}{\sqrt{u}}du=\frac{3}{5}\int_{9}^{49}u^{-1/2}du$$
$$=[(\frac{3}{5})\frac{u^{1/2}}{1/2}]_{9}^{49}=\frac{6}{5}[49^{1/2}-9^{1/2}]=\frac{24}{5}.$$

### Example 6
Evaluate $\int_{0}^{\pi/4}(1+sin~2x)^{3}cos~2x~dx$ .
**Solution**
The integrand suggests the power rule $\int_{a}^{b}u^{3}du=[\frac{1}{4}u^{4}]_{a}^{b}$ Thus, we let
$$u=1+sin~2x \quad du=2~cos~2x~dx.$$
The form of du indicates that we should introduce the factor 2 into the integrand and multiply the integral by $\frac{1}{2}$ , as follows:
$$\int_{0}^{\pi/4}(1+sin~2x)^{3}cos~2x~dx=\frac{1}{2}\int_{0}^{\pi/4}(1+sin~2x)^{3}2~cos~2x~dx.$$
We next calculate the values of $u=1+sin~2x$ that correspond to the limits of integration $x=0$ and $x=\pi/4$:
(i) If $x=0$ then $u=1+sin~0=1+0=1$
(ii) If $x=\frac{\pi}{4}$ then $u=1+sin\frac{\pi}{2}=1+1=2$
Substituting in the integrand and changing the limits of integration gives us
$$\int_{0}^{\pi/4}(1+sin~2x)^{3}cos~2x~dx=\frac{1}{2}\int_{1}^{2}u^{3}du$$
$$=\frac{1}{2}[\frac{u^{4}}{4}]_{1}^{2}=\frac{1}{8}[16-1]=\frac{15}{8}.$$

### Example 7
Evaluate
(a) $\int_{-1}^{1}(x^{4}+3x^{2}+1)dx$
(b) $\int_{-1}^{1}(x^{5}+3x^{3}+x)dx$
(c) $\int_{-5}^{5}(2x^{3}+3x^{2}+7x)dx$
**Solution**
(a) Since the integrand determines an even function, we may apply Theorem (4.34)(i):
$$\int_{-1}^{1}(x^{4}+3x^{2}+1)dx=2\int_{0}^{1}(x^{4}+3x^{2}+1)dx$$
$$=2[\frac{x^{5}}{5}+x^{3}+x]_{0}^{1}=\frac{22}{5}$$
(b) The integrand is odd, so we apply Theorem (4.34)(ii):
$$\int_{-1}^{1}(x^{5}+3x^{3}+x)dx=0$$
(c) The function given by $2x^{3}+7x$ is odd but the function given by $3x^{2}$ is even, so we apply Theorem (4.34)(ii) and (i):
$$\int_{-5}^{5}(2x^{3}+3x^{2}+7x)dx=\int_{-5}^{5}(2x^{3}+7x)dx+\int_{-5}^{5}3x^{2}dx$$
$$=0+2\int_{0}^{5}3x^{2}dx$$
$$=2[x^{3}]_{0}^{5}=250$$

### Example 8
If $G(x)=\int_{1}^{x}\frac{1}{t}dt$ and $x>0,$ find $G^{\prime}(x)$.
**Solution**
We apply Theorem (4.35) with $c=1$ and $f(x)=1/x$ If we choose a and b such that $0\le a\le1\le b$ then f is continuous on $[a,b]$ Hence, by Theorem (4.35), for every x in $[a,b]$
$$G^{\prime}(x)=\frac{d}{dx}\int_{1}^{x}\frac{1}{t}dt=\frac{1}{x}$$

### Example 9
Suppose that a point P moving on a coordinate line has a continuous velocity function v. Show that the average value of v on $[a,b]$ equals the average velocity during the time interval $[a,b]$.
**Solution**
By Definition (4.29) with $f=v,$
$$v_{av}=\frac{1}{b-a}\int_{a}^{b}v(t)dt.$$
If s is the position function of P, then $s^{\prime}(t)=v(t)$- that is, $s(t)$ is an antiderivative of $v(t)$. Hence, by the fundamental theorem of calculus,
$$\int_{a}^{b}v(t)dt=\int_{a}^{b}s^{\prime}(t)dt=s(t)]_{a}^{b}=s(b)-s(a).$$
Substituting in the formula for $v_{av}$ give us
$$v_{av}=\frac{s(b)-s(a)}{b-a}.$$
which is the average velocity of P on $[a,b]$ (see Definition 2.2).

## Exercises
*   1. $\int_{1}^{4}(x^{2}-4x-3)dx$
*   7. $\int_{1}^{2}\frac{5}{x^{6}}dx$
*   8. $\int_{1}^{4}\sqrt{16x^{5}}dx$
*   9. $\int_{4}^{9}\frac{t-3}{\sqrt{t}}dt$
*   11. It will follow from the results in Section 4.6 that $\int_{1}^{4}x^{2}dx=21$ and $\int_{1}^{4}x~dx=\frac{15}{2}$. Verify the inequality without evaluating the integrals. $\int_{1}^{2}(3x^{2}+4)dx\ge\int_{1}^{2}(2x^{2}+5)dx$
*   12. Verify the inequality without evaluating the integrals. $\int_{1}^{4}(2x+2)dx\le\int_{1}^{4}(3x+1)dx$
*   13. $\int_{-1}^{0}(2x+3)^{2}dx$
*   15. $\int_{3}^{2}\frac{x^{2}-1}{x-1}dx$
*   17. Express as one integral. $\int_{5}^{1}f(x)dx+\int_{-3}^{5}f(x)dx$
*   21. $\int_{-3}^{6}|x-4|dx$
*   29. $\int_{1}^{4}\frac{1}{\sqrt{x}(\sqrt{x}+1)^{3}}dx$
*   32. $\int_{0}^{\pi/2}3~sin(\frac{1}{2}x)dx$
*   36. $\int_{0}^{\pi/3}\frac{sin~x}{cos^{2}x}dx$
*   45. Find the derivative without integrating. $\frac{d}{dx}\int_{0}^{3}\sqrt{x^{2}+16}dx$
*   47. Find the derivative without integrating. $\frac{d}{dx}\int_{0}^{x}\frac{1}{t+1}dt$