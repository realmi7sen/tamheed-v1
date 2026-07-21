---
source_file: "Section_6.2_Natural_Logarithm.pdf" #[cite: 9]
course: MATH106
book_chapter: 6
book_section: 6.2
ksu_chapter: UNKNOWN
section_title: THE NATURAL LOGARITHM FUNCTION
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: [3, 5, 9, 11, 32, 35, 39, 41, 42]
topic_tags: [natural-logarithm, logarithmic-differentiation, derivatives]
difficulty: UNKNOWN
in_syllabus: true
enrichment: UNKNOWN
status: draft
---

# THE NATURAL LOGARITHM FUNCTION

## Metadata
**Course:** MATH106
**Book:** Calculus (Swokowski)
**Edition:** 6th
**Chapter Number:** 6
**Chapter Title:** Transcendental Functions
**Section Number:** 6.2
**Section Title:** THE NATURAL LOGARITHM FUNCTION

## Definitions
**Definition 6.9**
The natural logarithm function, denoted by ln, is defined by
$$ln~x=\int_{1}^{x}\frac{1}{t}dt$$
for every $x>0$.

## Theorems
**Theorem 6.10**
$$\frac{d}{dx}(ln~x)=\frac{1}{x}$$

**Theorem 6.11**
If $u=g(x)$ and g is differentiable, then
(i) $\frac{d}{dx}(ln~u)=\frac{1}{u}\frac{du}{dx}$ if $u>0$
(ii) $\frac{d}{dx}(ln|u|)=\frac{1}{u}\frac{du}{dx}$ if $u\ne0$

**Laws of Natural Logarithms 6.12**
If $p>0$ and $q>0,$ then
(i) $ln~pq=ln~p+ln~q$
(ii) $ln\frac{p}{q}=ln~p-ln~q$
(iii) $ln~p^{r}=r~ln~p$ for every rational number r

## Formulas
No formal boxed formulas distinct from Theorems and Methods.

## Guidelines / Methods
**Guidelines for Logarithmic Differentiation 6.13**
1. $y=f(x)$ Given
2. $ln~y=ln~f(x)$ Take natural logarithms and simplify
3. $\frac{d}{dx}(ln~y)=\frac{d}{dx}(ln~f(x))$ Differentiate implicitly
4. $\frac{1}{y}\frac{dy}{dx}=\frac{d}{dx}(ln~f(x))$ By Theorem (6.11)
5. $\frac{dy}{dx}=f(x)\frac{d}{dx}(ln~f(x))$ Multiply by $y=f(x)$

## Worked Examples
### Example 1
If $f(x)=ln(x^{2}-6)$, find $f^{\prime}(x)$.
**Solution**
Letting $u=x^{2}-6$ in Theorem (6.11)(i) yields
$$f^{\prime}(x)=\frac{d}{dx}(ln(x^{2}-6))=\frac{1}{x^{2}-6}\frac{d}{dx}(x^{2}-6)=\frac{2x}{x^{2}-6}$$

### Example 2
If $y=ln\sqrt{x+1},$ find $dy/dx$.
**Solution**
Letting $u=\sqrt{x+1}$ in Theorem (6.11)(i) gives us
$$\frac{dy}{dx}=\frac{d}{dx}(ln\sqrt{x+1})$$
$$=\frac{1}{\sqrt{x+1}}\frac{d}{dx}(\sqrt{x+1})=\frac{1}{\sqrt{x+1}}\cdot\frac{1}{2}(x+1)^{-1/2}$$
$$=\frac{1}{\sqrt{x+1}}\cdot\frac{1}{2}\frac{1}{\sqrt{x+1}}=\frac{1}{2(x+1)}.$$

### Example 3
If $f(x)=ln|4+5x-2x^{3}|$, find $f^{\prime}(x)$
**Solution**
Using Theorem (6.11)(ii) with $u=4+5x-2x^{3}$ yields
$$f^{\prime}(x)=\frac{d}{dx}(ln|4+5x-2x^{3}|)$$
$$=\frac{1}{4+5x-2x^{3}}\frac{d}{dx}(4+5x-2x^{3})=\frac{5-6x^{2}}{4+5x-2x^{3}}$$

### Example 4
If $f(x)=ln[\sqrt{6x-1}(4x+5)^{3}]$ find $f^{\prime}(x)$
**Solution**
We first write $\sqrt{6x-1}=(6x-1)^{1/2}$ and then use laws of logarithms (i) and (iii):
$$f(x)=ln[(6x-1)^{1/2}(4x+5)^{3}]$$
$$=ln(6x-1)^{1/2}+ln(4x+5)^{3}$$
$$=\frac{1}{2}ln(6x-1)+3~ln(4x+5)$$
By Theorem (6.11),
$$f^{\prime}(x)=(\frac{1}{2}\cdot\frac{1}{6x-1}\cdot6)+(3\cdot\frac{1}{4x+5}\cdot4)$$
$$=\frac{3}{6x-1}+\frac{12}{4x+5}$$
$$=\frac{84x+3}{(6x-1)(4x+5)}.$$

### Example 5
If $y=ln\sqrt[3]{\frac{x^{2}-1}{x^{2}+1}},$ find $\frac{dy}{dx}$
**Solution**
We first use laws of logarithms to change the form of y as follows:
$$y=ln(\frac{x^{2}-1}{x^{2}+1})^{1/3}=\frac{1}{3}ln(\frac{x^{2}-1}{x^{2}+1})$$
$$=\frac{1}{3}[ln(x^{2}-1)-ln(x^{2}+1)]$$
Next we use Theorem (6.11) to obtain
$$\frac{dy}{dx}=\frac{1}{3}(\frac{1}{x^{2}-1}\cdot2x-\frac{1}{x^{2}+1}\cdot2x)$$
$$=\frac{2x}{3}(\frac{1}{x^{2}-1}-\frac{1}{x^{2}+1})$$
$$=\frac{2x}{3}[\frac{2}{(x^{2}-1)(x^{2}+1)}]=\frac{4x}{3(x^{2}-1)(x^{2}+1)}.$$

### Example 6
If $y=\frac{(5x-4)^{3}}{\sqrt{2x+1}},$ use logarithmic differentiation to find $dy/dx$.
**Solution**
As in guideline (2), we begin by taking the natural logarithm of each side, obtaining
$$ln~y=ln(5x-4)^{3}-ln\sqrt{2x+1}$$
$$=3~ln(5x-4)-\frac{1}{2}ln(2x+1).$$
Applying guidelines (3) and (4), we differentiate implicitly with respect to x and then use Theorem (6.8) to obtain
$$\frac{1}{y}\frac{dy}{dx}=(3\cdot\frac{1}{5x-4}\cdot5)-(\frac{1}{2}\cdot\frac{1}{2x+1}\cdot2)$$
$$=\frac{25x+19}{(5x-4)(2x+1)}$$
Finally, as in guideline (5), we multiply both sides of the last equation by y (that is, by $(5x-4)^{3}/\sqrt{2x+1})$ to get
$$\frac{dy}{dx}=\frac{25x+19}{(5x-4)(2x+1)}\cdot\frac{(5x-4)^{3}}{\sqrt{2x+1}}$$
$$=\frac{(25x+19)(5x-4)^{2}}{(2x+1)^{3/2}}.$$

### Example 7
The Count model is an empirically based formula that can be used to predict the height of a preschooler. If $h(x)$ denotes the height (in centimeters) at age x (in years) $\frac{1}{4}\le x\le6,$ then $h(x)$ can be approximated by
$$h(x)=70.228+5.104x+9.222~ln~x.$$
(a) Predict the height and rate of growth when a child reaches age 2.
(b) When is the rate of growth largest?
**Solution**
(a) The height at age 2 is approximately
$$h(2)=70.228+5.104(2)+9.222~ln~2\approx86.8$$ cm.
The rate of change of h with respect to x is
$$h^{\prime}(x)=5.104+9.222(\frac{1}{x})$$
Letting $x=2$ gives us
$$h^{\prime}(2)=5.104+9.222(\frac{1}{2})=9.715$$.
Hence the rate of growth on the child's second birthday is about $9.7$ cm/yr.
(b) To determine the maximum value of the rate of growth $h^{\prime}(x)$ we first find the critical numbers of $h^{\prime}$. Differentiating $h^{\prime}(x)$, we obtain
$$h^{\prime\prime}(x)=9.222(-\frac{1}{x^{2}})=-\frac{9.222}{x^{2}}.$$
Since $h^{\prime\prime}(x)$ is negative for every x in $[\frac{1}{4}, 6]$, $h^{\prime}$ has no critical numbers in $(\frac{1}{4},6)$. It follows from Theorem (3.15) that $h^{\prime}$ is decreasing on $[\frac{1}{4},6]$. Consequently, the maximum value of $h^{\prime}(x)$ occurs at $x=\frac{1}{4}$ that is, the rate of growth is largest at the age of 3 months.

## Exercises
*   3. Find $f^{\prime}(x)$ if $f(x)=ln(3x^{2}-2x+1)$
*   5. Find $f^{\prime}(x)$ if $f(x)=ln|3-2x|$
*   9. Find $f^{\prime}(x)$ if $f(x)=ln\sqrt{7-2x^{3}}$
*   11. Find $f^{\prime}(x)$ if $f(x)=x~ln~x$
*   32. Find $f^{\prime}(x)$ if $f(x)=ln|sin~x|$
*   35. Use implicit differentiation to find $y^{\prime}$ for $3y-x^{2}+ln~xy=2$
*   39. Use logarithmic differentiation to find $dy/dx$ for $y=(5x+2)^{3}(6x+1)^{2}$
*   41. Use logarithmic differentiation to find $dy/dx$ for $y=\sqrt{4x+7}(x-5)^{3}$
*   42. Use logarithmic differentiation to find $dy/dx$ for $y=\sqrt{(3x^{2}+2)\sqrt{6x-7}}$