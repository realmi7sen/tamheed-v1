---
source_file: "Section_6.7_Inverse_Trigonometric_Functions.pdf"
course: MATH106
book_chapter: 6
book_section: 6.7
ksu_chapter: UNKNOWN
section_title: INVERSE TRIGONOMETRIC FUNCTIONS
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: [31, 33, 37, 43, 51, 52, 56, 57, 60, 61, 62]
topic_tags: [inverse-trigonometric-functions, derivatives, integrals, arc-length]
difficulty: UNKNOWN
in_syllabus: true
enrichment: UNKNOWN
status: draft
---

# INVERSE TRIGONOMETRIC FUNCTIONS

## Metadata
**Course:** MATH106
**Book:** Calculus (Swokowski)
**Edition:** 6th
**Chapter Number:** 6
**Chapter Title:** Transcendental Functions
**Section Number:** 6.7
**Section Title:** INVERSE TRIGONOMETRIC FUNCTIONS

## Definitions
**Definition 6.34**
The inverse sine function, denoted $sin^{-1}$, is defined by
$$y=sin^{-1}x \quad \text{if and only if} \quad x=sin~y$$
for $-1\le x\le1$ and $-\pi/2\le y\le\pi/2$.

The inverse cosine function, denoted $cos^{-1}$, is defined by
$$y=cos^{-1}x \quad \text{if and only if} \quad x=cos~y$$
for $-1\le x\le1$ and $0\le y\le\pi$.

**Definition 6.35**
The inverse tangent function, or arctangent function, denoted by $tan^{-1}$ or arctan, is defined by
$$y=tan^{-1}x=arctan~x \quad \text{if and only if} \quad x=tan~y$$
for every x and $-\pi/2<y<\pi/2$.

**Definition 6.37**
The inverse secant function, or arcsecant function, denoted by $sec^{-1}$ or arcsec, is defined by
$$y=sec^{-1}x=arcsec~x \quad \text{if and only if} \quad x=sec~y$$
for $|x|\ge1$ and y in $[0,\pi/2)$ or in $[\pi,3\pi/2)$.

## Theorems
**Properties of Inverse Trigonometric Functions 6.36**
(i) $sin(sin^{-1}x)=sin(arcsin~x)=x$ if $-1\le x\le1$
(ii) $sin^{-1}(sin~x)=arcsin(sin~x)=x$ if $-\pi/2\le x\le\pi/2$
(iii) $cos(cos^{-1}x)=cos(arccos~x)=x$ if $-1\le x\le1$
(iv) $cos^{-1}(cos~x)=arccos(cos~x)=x$ if $0\le x\le\pi$
(v) $tan(tan^{-1}x)=tan(arctan~x)=x$ for every x
(vi) $tan^{-1}(tan~x)=arctan(tan~x)=x$ if $-\pi/2<x<\pi/2$

**Theorem 6.38**
(i) $\frac{d}{dx}(sin^{-1}u)=\frac{1}{\sqrt{1-u^{2}}}\frac{du}{dx}$
(ii) $\frac{d}{dx}(cos^{-1}u)=-\frac{1}{\sqrt{1-u^{2}}}\frac{du}{dx}$
(iii) $\frac{d}{dx}(tan^{-1}u)=\frac{1}{1+u^{2}}\frac{du}{dx}$
(iv) $\frac{d}{dx}(sec^{-1}u)=\frac{1}{u\sqrt{u^{2}-1}}\frac{du}{dx}$

**Theorem 6.39**
(i) $\int\frac{1}{\sqrt{a^{2}-u^{2}}}du=sin^{-1}\frac{u}{a}+C$
(ii) $\int\frac{1}{a^{2}+u^{2}}du=\frac{1}{a}tan^{-1}\frac{u}{a}+C$
(iii) $\int\frac{1}{u\sqrt{u^{2}-a^{2}}}du=\frac{1}{a}sec^{-1}\frac{u}{a}+C$

**Integrals of Inverse Trigonometric Functions 6.40**
(i) $\int sin^{-1}u~du=u~sin^{-1}u+\sqrt{1-u^{2}}+C$
(ii) $\int cos^{-1}u~du=u~cos^{-1}u-\sqrt{1-u^{2}}+C$
(iii) $\int tan^{-1}u~du=u~tan^{-1}u-\frac{1}{2}ln(1+u^{2})+C$
(iv) $\int sec^{-1}u~du=u~sec^{-1}u-ln|u+\sqrt{u^{2}-1}|+C$

## Formulas
No formal boxed formulas distinct from Theorems and Methods.

## Guidelines / Methods
No numbered guideline lists or method tables.

## Worked Examples
### Example 1
Find the exact value of $sec(arctan\frac{2}{3})$.
**Solution**
If we let $y=arctan\frac{2}{3}$, then $tan~y=\frac{2}{3}$ We wish to find $sec~y$. Since $-\pi/2<arctan~x<\pi/2$ for every x and $tan~y>0,$ it follows that $0<y<\pi/2$. Thus, we may regard y as the radian measure of an angle of a right triangle such that $tan~y=\frac{2}{3}$. By the Pythagorean theorem, the hypotenuse is $\sqrt{3^{2}+2^{2}}=\sqrt{13}.$ Referring to the triangle, we obtain
$$sec(arctan\frac{2}{3})=sec~y=\frac{\sqrt{13}}{3}.$$

### Example 2
Use a calculator to approximate arcsec(-14.3).
**Solution**
From the graph of the inverse secant function, we see that arcsec(-14.3) will lie between $\pi$ and $3\pi/2$ If we let $y=arcsec(-14.3)$, then $sec~y=-14.3$ and $cos~y=-(1/14.3)$. Since the range of the inverse cosine function is $[0,\pi]$ with $\pi/2<arccos~x\le\pi$ when $x<0$, a calculator provides the approximation
$$\tilde{y}=cos^{-1}(-1/14.3)\approx1.64078352.$$
To find the desired answer in the interval $(\pi,3\pi/2)$ we treat $\tilde{y}$ as a reference angle and compute the answer as $y=\pi+(\pi-\tilde{y})\approx4.64240179$

### Example 3
If $-1\le x\le1$ rewrite $cos(sin^{-1}x)$ as an algebraic expression in x.
**Solution**
Let $y=sin^{-1}x$, or, equivalently, $sin~y=x$
We wish to express $cos~y$ in terms of x. Since $-\pi/2\le y\le\pi/2$ it follows that $cos~y\ge0,$ and hence
$$cos~y=\sqrt{1-sin^{2}y}=\sqrt{1-x^{2}},$$
Consequently, $cos(sin^{-1}x)=\sqrt{1-x^{2}}$

### Example 4
A rocket is fired directly upward with initial velocity 0 and burns fuel at a rate that produces a constant acceleration of $50\text{ ft/sec}^{2}$ for $0\le t\le5$ with time in seconds. An observer 400 ft from the launching pad visually follows the flight of the rocket.
(a) Express the angle of elevation $\theta$ of the rocket as a function of t.
(b) The observer perceives the rocket to be rising fastest when $d\theta/dt$ is largest. Determine the height of the rocket at the moment of perceived maximum velocity.
**Solution**
(a) Let $s(t)$ denote the height of the rocket at time t. The fact that the acceleration is always 50 gives us the differential equation $s^{\prime\prime}(t)=50$ subject to the initial conditions $s^{\prime}(0)=0$ and $s(0)=0$. Integrating with respect to t, we obtain
$$s^{\prime}(t)=50t.$$
Integrating again, we have
$$s(t)=25t^{2}.$$
We find
$$tan~\theta=\frac{25t^{2}}{400}=\frac{t^{2}}{16} \quad \text{or} \quad \theta=arctan\frac{t^{2}}{16}$$
(b) By Theorem (6.38), the rate of change of $\theta$ with respect to t is
$$\frac{d\theta}{dt}=\frac{1}{1+(t^{2}/16)^{2}}(\frac{2t}{16})=\frac{32t}{256+t^{4}}.$$
Since we wish to find the maximum value of $d\theta/dt$, we begin by finding the critical numbers of $d\theta/dt$. Using the quotient rule, we obtain
$$\frac{d^{2}\theta}{dt^{2}}=\frac{32(256-3t^{4})}{(256+t^{4})^{2}}.$$
Considering $d^{2}\theta/dt^{2}=0$ gives us the critical number $t=\sqrt[4]{256/3}$. It follows that $d\theta/dt$ has a maximum value at $t=\sqrt[4]{256/3}\approx3.04$ sec. The height of the rocket at this time is
$$s(\sqrt[4]{256/3})=25(\sqrt[4]{256/3})^{2}=25\sqrt{256/3}\approx230.9\text{ ft}.$$

### Example 5
Evaluate $\int_{0}^{1}\frac{4}{1+x^{2}}dx.$
**Solution**
Using (6.39)(ii), we have
$$\int_{0}^{1}\frac{4}{1+x^{2}}dx=4\int_{0}^{1}\frac{1}{1+x^{2}}dx$$
$$=4[arctan~x]_{0}^{1}$$
$$=4(arctan~1-arctan~0)$$
$$=4(\frac{\pi}{4}-0)=\pi.$$

### Example 6
Evaluate $\int\frac{e^{2x}}{\sqrt{1-e^{4x}}}dx.$
**Solution**
The integral may be written as in Theorem (6.39)(i) by letting $a=1$ and using the substitution
$$u=e^{2x} \quad du=2e^{2x}dx.$$
We introduce a factor 2 in the integrand and proceed as follows:
$$\int\frac{e^{2x}}{\sqrt{1-e^{4x}}}dx=\frac{1}{2}\int\frac{1}{\sqrt{1-(e^{2x})^{2}}}2e^{2x}dx$$
$$=\frac{1}{2}\int\frac{1}{\sqrt{1-u^{2}}}du$$
$$=\frac{1}{2}sin^{-1}u+C$$
$$=\frac{1}{2}sin^{-1}e^{2x}+C$$

### Example 7
Evaluate $\int\frac{x^{2}}{5+x^{6}}dx.$
**Solution**
The integral may be written as in Theorem (6.39)(ii) by letting $a^{2}=5$ and using the substitution
$$u=x^{3} \quad du=3x^{2}dx$$
We introduce a factor 3 in the integrand and proceed as follows:
$$\int\frac{x^{2}}{5+x^{6}}dx=\frac{1}{3}\int\frac{1}{5+(x^{3})^{2}}3x^{2}dx$$
$$=\frac{1}{3}\int\frac{1}{(\sqrt{5})^{2}+u^{2}}du$$
$$=\frac{1}{3}\cdot\frac{1}{\sqrt{5}}tan^{-1}\frac{u}{\sqrt{5}}+C$$
$$=\frac{\sqrt{5}}{15}tan^{-1}\frac{x^{3}}{\sqrt{5}}+C$$

### Example 8
Evaluate $\int\frac{1}{x\sqrt{x^{4}-9}}dx.$
**Solution**
The integral may be written as in Theorem (6.39)(iii) by letting $a^{2}=9$ and using the substitution
$$u=x^{2} \quad du=2x~dx.$$
We introduce 2x in the integrand by multiplying the numerator and the denominator by 2x and then proceed as follows:
$$\int\frac{1}{x\sqrt{x^{4}-9}}dx=\int\frac{1}{2x\cdot x\sqrt{(x^{2})^{2}-3^{2}}}2x~dx$$
$$=\frac{1}{2}\int\frac{1}{u\sqrt{u^{2}-3^{2}}}du$$
$$=\frac{1}{2}\cdot\frac{1}{3}sec^{-1}\frac{u}{3}+C$$
$$=\frac{1}{6}sec^{-1}\frac{x^{2}}{3}+C$$

### Example 9
Approximate the arc length of the graph of the function $f(x)=arcsec~x$ from $x=2$ to $x=3$ to four decimal places.
**Solution**
From the definition (5.14) of arc length, we know that the arc length of this graph is
$$\int_{2}^{3}\sqrt{1+[f^{\prime}(x)]^{2}}dx$$.
If $f(x)=arcsec~x$, then by Theorem (6.38)(iv), $f^{\prime}(x)=1/(x\sqrt{x^{2}-1})$ so
$$1+[f^{\prime}(x)]^{2}=1+\frac{1}{x^{2}(x^{2}-1)}$$
and the arc length is
$$\int_{2}^{3}\sqrt{1+\frac{1}{x^{2}(x^{2}-1)}}dx.$$
We evaluate this definite integral numerically by using Simpson's rule, obtaining 1.01783 as an approximation. Thus to four decimal places, the arc length is 1.0178.

### Example 10
(a) Find $f^{\prime}(x)$ if $f(x)=x~arcsin~x$.
(b) Use the result of part (a) to find $\int arcsin~x~dx$.
**Solution**
(a) By the product rule (2.19),
$$f^{\prime}(x)=(x~arcsin~x)^{\prime}$$
$$=(x)^{\prime}(arcsin~x)+(x)(arcsin~x)^{\prime}$$
$$=1~arcsin~x+x\frac{1}{\sqrt{1-x^{2}}}$$
$$=arcsin~x+\frac{x}{\sqrt{1-x^{2}}}.$$
(b) From part (a), we have
$$arcsin~x=(x~arcsin~x)^{\prime}-\frac{x}{\sqrt{1-x^{2}}}$$
Integrating each side of this equation with respect to x gives
$$\int arcsin~x~dx=\int[(x~arcsin~x)^{\prime}-\frac{x}{\sqrt{1-x^{2}}}]dx$$
$$=\int(x~arcsin~x)^{\prime}dx-\int\frac{x}{\sqrt{1-x^{2}}}dx$$
$$=x~arcsin~x+\sqrt{1-x^{2}}+C$$.

## Exercises
*   31. Find $f^{\prime}(x)$ if $f(x)=sin^{-1}\sqrt{x}$
*   33. Find $f^{\prime}(x)$ if $f(x)=tan^{-1}(3x-5)$
*   37. Find $f^{\prime}(x)$ if $f(x)=ln~arctan(x^{2})$
*   43. Find $f^{\prime}(x)$ if $f(x)=3^{arcsin(x^{3})}$
*   51. Evaluate the integral. (a) $\int\frac{1}{x^{2}+16}dx$ (b) $\int_{0}^{4}\frac{1}{x^{2}+16}dx$
*   52. Evaluate the integral. (a) $\int\frac{e^{x}}{1+e^{2x}}dx$ (b) $\int_{0}^{1}\frac{e^{x}}{1+e^{2x}}dx$
*   56. Evaluate the integral. $\int\frac{cos~x}{\sqrt{9-sin^{2}x}}dx$
*   57. Evaluate the integral. $\int\frac{e^{x}}{\sqrt{15-e^{2x}}}dx$
*   60. Evaluate the integral. $\int\frac{1}{x\sqrt{x^{6}-4}}dx$
*   61. Evaluate the integral. $\int\frac{1}{\sqrt{e^{2x}-25}}dx$
*   62. Evaluate the integral. $\int\frac{1}{x\sqrt{x-1}}dx$