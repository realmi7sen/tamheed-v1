---
source_file: "Section_6.5_General_Exponential_and_Logarithmic_Functions.pdf"
course: MATH106
book_chapter: 6
book_section: 6.5
ksu_chapter: UNKNOWN
section_title: GENERAL EXPONENTIAL AND LOGARITHMIC FUNCTIONS
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: [1, 5, 15, 17, 23, 29, 37, 39, 41, 43]
topic_tags: [exponential-functions, logarithmic-functions, derivatives, integrals, power-rule]
difficulty: UNKNOWN
in_syllabus: true
enrichment: UNKNOWN
status: draft
---

# GENERAL EXPONENTIAL AND LOGARITHMIC FUNCTIONS

## Metadata
**Course:** MATH106
**Book:** Calculus (Swokowski)
**Edition:** 6th
**Chapter Number:** 6
**Chapter Title:** Transcendental Functions
**Section Number:** 6.5
**Section Title:** GENERAL EXPONENTIAL AND LOGARITHMIC FUNCTIONS

## Definitions
**Definition of $a^{x}$ 6.26**
$$a^{x}=e^{x~ln~a}$$
for every $a>0$ and every real number x.

**Definition of $log_{a}x$ 6.30**
If $a\ne1$ and $f(x)=a^{x}$, then f is a one-to-one function. Its inverse function is denoted by $log_{a}$ and is called the logarithmic function with base a. Another way of stating this relationship is as follows.
$$y=log_{a}x \quad \text{if and only if} \quad x=a^{y}$$

## Theorems
**Laws of Exponents 6.27**
Let $a>0$ and $b>0$ If u and v are any real numbers, then
(i) $a^{u}a^{v}=a^{u+v}$
(ii) $(a^{u})^{v}=a^{uv}$
(iii) $(ab)^{u}=a^{u}b^{u}$
(iv) $\frac{a^{u}}{a^{v}}=a^{u-v}$
(v) $(\frac{a}{b})^{u}=\frac{a^{u}}{b^{u}}$

**Theorem 6.28**
(i) $\frac{d}{dx}(a^{x})=a^{x}ln~a$
(ii) $\frac{d}{dx}(a^{u})=(a^{u}ln~a)\frac{du}{dx}$

**Theorem 6.29**
(i) $\int a^{x}dx=(\frac{1}{ln~a})a^{x}+C$
(ii) $\int a^{u}du=(\frac{1}{ln~a})a^{u}+C$

**Theorem 6.31**
(i) $\frac{d}{dx}(log_{a}x)=\frac{d}{dx}(\frac{ln~x}{ln~a})=\frac{1}{ln~a}\cdot\frac{1}{x}$
(ii) $\frac{d}{dx}(log_{a}|u|)=\frac{d}{dx}(\frac{ln|u|}{ln~a})=\frac{1}{ln~a}\cdot\frac{1}{u}\frac{du}{dx}$

**Theorem 6.32**
(i) $lim_{h\rightarrow0}(1+h)^{1/h}=e$
(ii) $lim_{n\rightarrow\infty}(1+\frac{1}{n})^{n}=e$

## Formulas
$$log_{a}x=\frac{ln~x}{ln~a}$$

## Guidelines / Methods
No numbered guideline lists or method tables.

## Worked Examples
### Example 1
Find $y^{\prime}$ if $y=(x^{2}+1)^{10}+10^{x^{2}+1}$
**Solution**
Using the power rule for functions and Theorem (6.28), we obtain
$$y^{\prime}=10(x^{2}+1)^{9}(2x)+(10^{x^{2}+1}ln~10)(2x)$$
$$=20x[(x^{2}+1)^{9}+10^{x^{2}}ln~10]$$

### Example 2
Evaluate:
(a) $\int3^{x}dx$
(b) $\int x3^{(x^{2})}dx$
**Solution**
(a) Using (i) of Theorem (6.29) yields
$$\int3^{x}dx=(\frac{1}{ln~3})3^{x}+C.$$
(b) To use (ii) of Theorem (6.29), we make the substitution
$$u=x^{2} \quad du=2x~dx$$
and proceed as follows:
$$\int x3^{(x^{2})}dx=\frac{1}{2}\int3^{(x^{2})}(2x)dx=\frac{1}{2}\int3^{u}du$$
$$=\frac{1}{2}(\frac{1}{ln~3})3^{u}+C=(\frac{1}{2~ln~3})3^{(x^{2})}+C$$

### Example 3
An important problem in oceanography is determining the light intensity at different ocean depths. The Beer-Lambert law states that at a depth x (in meters), the light intensity $I(x)$ (in $calories/cm^{2}/sec)$ is given by $I(x)=I_{0}a^{x}$ where $I_{0}$ and a are positive constants.
(a) What is the light intensity at the surface?
(b) Find the rate of change of the light intensity with respect to depth at a depth x.
(c) If $a=0.4$ and $I_{0}=10$ find the average light intensity between the surface and a depth of 5 meters.
(d) Show that $I(x)=I_{0}e^{kx}$ for some constant k.
**Solution**
(a) At the surface, $x=0$ and
$$I(0)=I_{0}a^{0}=I_{0}.$$
Hence the light intensity at the surface is $I_{0}$.
(b) The rate of change of $I(x)$ with respect to x is $I^{\prime}(x)$. Thus,
$$I^{\prime}(x)=I_{0}(a^{x}ln~a)=(ln~a)(I_{0}a^{x})=(ln~a)I(x).$$
Hence the rate of change $I^{\prime}(x)$ at depth x is directly proportional to $I(x)$, and the constant of proportionality is $ln~a$.
(c) If $I(x)=10(0.4)^{x},$ then, by Definition (4.29), the average value of I on the interval $[0, 5]$ is
$$I_{av}=\frac{1}{5-0}\int_{0}^{5}10(0.4)^{x}dx=2\int_{0}^{5}(0.4)^{x}dx$$
$$=2[\frac{1}{ln(0.4)}(0.4)^{x}]_{0}^{5}=\frac{2}{ln(0.4)}[(0.4)^{5}-(0.4)^{0}]$$
$$=\frac{-1.97952}{ln(0.4)}\approx2.16.$$
(d) Using Definition (6.26) yields
$$I(x)=I_{0}a^{x}=I_{0}e^{x~ln~a}=I_{0}e^{kx}$$,
where $k=ln~a.$

### Example 4
If $f(x)=log(2x+5)^{2/3},$
(a) find $f^{\prime}(x)$
(b) graph both the function f and the line tangent to its graph at $x=-0.6$
**Solution**
(a) We express the function in terms of natural logarithms to make differentiating easier. We first write $f(x)=log(2x+5)^{2/3}$. The law $log~u^{r}=r~log~u$ is true only if $u>0;$ however, since $(2x+5)^{2/3}=|2x+5|^{2/3}$ we may proceed as follows:
$$f(x)=log(2x+5)^{2/3}$$
$$=log|2x+5|^{2/3}$$
$$=\frac{2}{3}log|2x+5|$$
$$=\frac{2}{3}\frac{ln|2x+5|}{ln~10}$$
Differentiating yields
$$f^{\prime}(x)=\frac{2}{3}\cdot\frac{1}{ln~10}\cdot\frac{1}{2x+5}(2)=\frac{4}{3(2x+5)ln~10}$$
(b) We begin by using a graphing utility to plot the function $f(x)=log(2x+5)^{2/3}$. To graph the tangent line, we must first find an equation for it using the point-slope formula. Since
$$f(-0.6)=\frac{2}{3}log~3.8\approx0.386522$$,
the point of tangency is $(-0.6, 0.386522)$. The slope of the tangent line is the value of the derivative $f^{\prime}$ at $x=-0.6$ From part (a), we have
$$f^{\prime}(-0.6)=\frac{4}{11.4~ln~10}\approx0.152384$$
Thus, an equation for the line tangent to the graph at $x=-0.6$ is approximately $y=0.386522+0.152384(x+0.6).$

### Example 5
If $y=x^{x}$ and $x>0$.
(a) find $dy/dx$
(b) graph both the function and its derivative
**Solution**
(a) Since the exponent in $x^{x}$ is a variable, the power rule may not be used. Similarly, Theorem (6.28) is not applicable, since the base a is not a fixed real number. However, by Definition (6.26), $x^{x}=e^{x~ln~x}$ for every $x>0$ and hence
$$\frac{d}{dx}(x^{x})=\frac{d}{dx}(e^{x~ln~x})$$
$$=e^{x~ln~x}\frac{d}{dx}(x~ln~x)$$
$$=e^{x~ln~x}[x(\frac{1}{x})+(1)ln~x]=x^{x}(1+ln~x)$$.
Another way of solving this problem is to use the method of logarithmic differentiation. We take the natural logarithm of both sides of the equation $y=x^{x}$ and then differentiate implicitly as follows:
$$ln~y=ln~x^{x}=x~ln~x$$
$$\frac{d}{dx}(ln~y)=\frac{d}{dx}(x~ln~x)$$
$$\frac{1}{y}\frac{dy}{dx}=1+ln~x$$
$$\frac{dy}{dx}=y(1+ln~x)=x^{x}(1+ln~x)$$
(b) We use a graphing utility to plot its graph and the graph of its derivative. When $x=0$ the expression $x^{x}$ becomes the undefined algebraic expression $0^{0}$, but from the graph it appears that the function $f(x)=x^{x}$ approaches 1 as x approaches 0 from the right. If we examine the graph of the derivative $f^{\prime}$ we see that it is negative for $0<x<a$ and positive for $x>a.$ We can determine the value of a by examining the sign of $f^{\prime}(x)$ Since $x^{x}>0$, $f^{\prime}(x)<0$ if $1+ln~x<0$ or, equivalently, $x<e^{-1}$ Hence, $a=e^{-1}\approx0.37$ Thus, the function $f(x)=x^{x}$ decreases to an absolute minimum at $x=a$ and then increases for $x>a$. It also appears from the graph of the derivative that it is unbounded in the negative direction as $x\rightarrow0^{+},$ so the function $f(x)=x^{x}$ is not differentiable at $x=0.$

## Exercises
*   1. Find $f^{\prime}(x)$ if $f(x)=7^{x}$
*   5. Find $f^{\prime}(x)$ if $f(x)=log(x^{4}+3x^{2}+1)$
*   15. Find $f^{\prime}(x)$ if $f(x)=log~ln~x$
*   17. Find $f^{\prime}(x)$ if $f(x)=x^{e}+e^{x}$
*   23. Find $f^{\prime}(x)$ if (a) $f(x)=e^{x}$ (b) $f(x)=x^{5}$ (c) $f(x)=x^{\sqrt{5}}$ (d) $f(x)=(\sqrt{5})^{x}$ (e) $f(x)=x^{(x^{2})}$
*   29. Evaluate the integral. (a) $\int7^{x}dx$ (b) $\int_{-2}^{1}7^{x}dx$
*   37. Evaluate the integral. $\int\frac{2^{x}}{2^{x}+1}dx$
*   39. Evaluate the integral. $\int\frac{1}{x~log~x}dx$
*   41. Evaluate the integral. $\int3^{cos~x}sin~x~dx$
*   43. Evaluate the integral. (a) $\int\pi^{\pi}dx$ (b) $\int x^{4}dx$ (c) $\int x^{\pi}dx$ (d) $\int\pi^{x}dx$