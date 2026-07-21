---
source_file: "Section_6.3_The_Exponential_Function.pdf"
course: MATH106
book_chapter: 6
book_section: 6.3
ksu_chapter: UNKNOWN
section_title: THE EXPONENTIAL FUNCTION
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: [1, 3, 6, 11, 15, 31, 33]
topic_tags: [exponential-function, derivatives, optimization]
difficulty: UNKNOWN
in_syllabus: true
enrichment: UNKNOWN
status: draft
---

# THE EXPONENTIAL FUNCTION

## Metadata
**Course:** MATH106
**Book:** Calculus (Swokowski)
**Edition:** 6th
**Chapter Number:** 6
**Chapter Title:** Transcendental Functions
**Section Number:** 6.3
**Section Title:** THE EXPONENTIAL FUNCTION

## Definitions
**Definition 6.15**
The natural exponential function, denoted by exp, is the inverse of the natural logarithm function.

**Definition of e 6.16**
The letter e denotes the positive real number such that $ln~e=1$.

**Definition of $e^{x}$ 6.18**
If x is any real number, then
$$e^{x}=y \quad \text{if and only if} \quad ln~y=x$$

## Theorems
**Theorem 6.14**
To every real number x there corresponds exactly one positive real number y such that $ln~y=x$.

**Theorem 6.19**
(i) $ln~e^{x}=x$ for every x
(ii) $e^{ln~x}=x$ for every $x>0$

**Theorem 6.20**
If p and q are real numbers and r is a rational number, then
(i) $e^{p}e^{q}=e^{p+q}$
(ii) $\frac{e^{p}}{e^{q}}=e^{p-q}$
(iii) $(e^{p})^{r}=e^{pr}$

**Theorem 6.21**
$$\frac{d}{dx}(e^{x})=e^{x}$$

**Theorem 6.22**
If $u=g(x)$ and g is differentiable, then
$$\frac{d}{dx}(e^{u})=e^{u}\frac{du}{dx}$$

## Formulas
**Approximation to e 6.17**
$$e \approx 2.71828182845904523536028747135266$$

## Guidelines / Methods
No numbered guideline lists or method tables.

## Worked Examples
### Example 1
If $f(x)=x^{2}e^{x}$. find $f^{\prime}(x)$.
**Solution**
By the product rule and Theorem (6.21),
$$f^{\prime}(x)=x^{2}\frac{d}{dx}(e^{x})+e^{x}\frac{d}{dx}(x^{2})$$
$$=x^{2}e^{x}+e^{x}(2x)=xe^{x}(x+2)$$.

### Example 2
If $y=e^{\sqrt{x^{2}+1}}.$ find $dy/dx$.
**Solution**
By Theorem (6.22),
$$\frac{dy}{dx}=\frac{d}{dx}(e^{\sqrt{x^{2}+1}})=e^{\sqrt{x^{2}+1}}\frac{d}{dx}(\sqrt{x^{2}+1})$$
$$=e^{\sqrt{x^{2}+1}}\frac{d}{dx}((x^{2}+1)^{1/2})$$
$$=e^{\sqrt{x^{2}+1}}(\frac{1}{2})(x^{2}+1)^{-1/2}(2x)$$
$$=e^{\sqrt{x^{2}+1}}\cdot\frac{x}{\sqrt{x^{2}+1}}$$
$$=\frac{xe^{\sqrt{x^{2}+1}}}{\sqrt{x^{2}+1}}.$$

### Example 3
The function f defined by $f(x)=e^{-x^{2}/2}$ occurs in the branch of mathematics called probability. Find the local extrema of f, discuss concavity, find the points of inflection, and sketch the graph of f.
**Solution**
By Theorem (6.22),
$$f^{\prime}(x)=e^{-x^{2}/2}\frac{d}{dx}(-\frac{x^{2}}{2})=e^{-x^{2}/2}(-\frac{2x}{2})=-xe^{-x^{2}/2}$$
Since $e^{-x^{2}/2}$ is always positive, the only critical number of f is 0. If $x<0$ then $f^{\prime}(x)>0$ and if $x>0$, then $f^{\prime}(x)<0.$ It follows from the first derivative test that f has a local maximum at 0. The maximum value is $f(0)=e^{-0}=1$
Applying the product rule to $f^{\prime}(x)$ yields
$$f^{\prime\prime}(x)=-x\frac{d}{dx}(e^{-x^{2}/2})+e^{-x^{2}/2}\frac{d}{dx}(-x)$$
$$=-xe^{-x^{2}/2}(-2x/2)-e^{-x^{2}/2}$$
$$=e^{-x^{2}/2}(x^{2}-1)$$,
and hence the second derivative is zero at -1 and 1. If $-1<x<1,$ then $f^{\prime\prime}(x)<0$ and, by (3.18), the graph of f is concave downward in the open interval $(-1,1)$. If $x<-1$ or $x>1$, then $f^{\prime\prime}(x)>0$ and, therefore, the graph is concave upward throughout the infinite intervals $(-\infty,-1)$ and $(1,\infty)$. Consequently, $P(-1,e^{-1/2})$ and $Q(1,e^{-1/2})$ are points of inflection. From the expression
$$f(x)=\frac{1}{e^{x^{2}/2}}$$
it is evident that as x increases numerically, f(x) approaches 0. We can prove that $lim_{x\rightarrow\infty}f(x)=0$ and $lim_{x\rightarrow-\infty}f(x)=0$ that is, the x-axis is a horizontal asymptote.

### Example 4
If each cell of a tumor has two targets, then the two-target-one-hit surviving fraction is given by
$$f(x)=1-(1-e^{-kx})^{2}$$,
where k is the average size of a cell. Analyze the graph of f to determine what effect increasing the dosage x has on decreasing the surviving fraction of tumor cells.
**Solution**
First note that if $x=0$ then $f(0)=1;$ that is, if there is no dose, then all cells survive. Differentiating, we obtain
$$f^{\prime}(x)=0-2(1-e^{-kx})\frac{d}{dx}(1-e^{-kx})$$
$$=-2(1-e^{-kx})(ke^{-kx})$$
$$=-2ke^{-kx}(1-e^{-kx})$$.
Since $f^{\prime}(x)<0$ for every $x>0$ and $f^{\prime}(0)=0$, the function f is decreasing and the graph has a horizontal tangent line at the point $(0,1)$. We may verify that the second derivative is
$$f^{\prime\prime}(x)=2k^{2}e^{-kx}(1-2e^{-kx})$$,
We see that $f^{\prime\prime}(x)=0$ if $1-2e^{-kx}=0$-that is, if $e^{-kx}=\frac{1}{2}$ or, equivalently, $-kx=ln\frac{1}{2}=-ln~2$ We thus obtain
$$x=\frac{1}{k}ln~2$$ .
It can be verified that if $0\le x<(1/k)ln~2$, then $f^{\prime\prime}(x)<0$ and hence the graph is concave downward. If $x>(1/k)ln~2$, then $f^{\prime\prime}(x)>0$, and the graph is concave upward. The implication is that a point of inflection exists at x-coordinate $(1/k)ln~2$. The y-coordinate of this point is
$$f(\frac{1}{k}ln~2)=1-(1-e^{-ln~2})^{2}$$
$$=1-(1-\frac{1}{2})^{2}=\frac{3}{4}$$

## Exercises
*   1. Find $f^{\prime}(x)$ if $f(x)=e^{-5x}$
*   3. Find $f^{\prime}(x)$ if $f(x)=e^{3x^{2}}$
*   6. Find $f^{\prime}(x)$ if $f(x)=1/(e^{x}+1)$
*   11. Find $f^{\prime}(x)$ if $f(x)=e^{x}/(x^{2}+1)$
*   15. Find $f^{\prime}(x)$ if $f(x)=e^{1/x}+(1/e^{x})$
*   31. Use implicit differentiation to find $y^{\prime}$ for $e^{xy}-x^{3}+3y^{2}=11$
*   33. Use implicit differentiation to find $y^{\prime}$ for $e^{x}cot~y=xe^{2y}$