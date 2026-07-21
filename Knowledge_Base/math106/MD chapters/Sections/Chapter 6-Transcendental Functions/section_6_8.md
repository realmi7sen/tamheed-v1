---
source_file: "Section_6.8_Hyperbolic_and_Inverse_Hyperbolic_Functions.pdf"
course: MATH106
book_chapter: 6
book_section: 6.8
ksu_chapter: UNKNOWN
section_title: HYPERBOLIC AND INVERSE HYPERBOLIC FUNCTIONS
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: [19, 20, 21, 28, 29, 61, 63, 65, 67, 73, 74, 75, 79, 80]
topic_tags: [hyperbolic-functions, inverse-hyperbolic-functions, derivatives, integrals]
difficulty: UNKNOWN
in_syllabus: true
enrichment: UNKNOWN
status: draft
---

# HYPERBOLIC AND INVERSE HYPERBOLIC FUNCTIONS

## Metadata
**Course:** MATH106
**Book:** Calculus (Swokowski)
**Edition:** 6th
**Chapter Number:** 6
**Chapter Title:** Transcendental Functions
**Section Number:** 6.8
**Section Title:** HYPERBOLIC AND INVERSE HYPERBOLIC FUNCTIONS

## Definitions
**Definition 6.41**
The hyperbolic sine function, denoted by sinh, and the hyperbolic cosine function, denoted by cosh, are defined by
$$sinh~x=\frac{e^{x}-e^{-x}}{2} \quad \text{and} \quad cosh~x=\frac{e^{x}+e^{-x}}{2}$$
for every real number x.

**Definition 6.43**
(i) $tanh~x=\frac{sinh~x}{cosh~x}=\frac{e^{x}-e^{-x}}{e^{x}+e^{-x}}$
(ii) $coth~x=\frac{cosh~x}{sinh~x}=\frac{e^{x}+e^{-x}}{e^{x}-e^{-x}}, x\ne0$
(iii) $sech~x=\frac{1}{cosh~x}=\frac{2}{e^{x}+e^{-x}}$
(iv) $csch~x=\frac{1}{sinh~x}=\frac{2}{e^{x}-e^{-x}}, x\ne0$

## Theorems
**Theorem 6.42**
$$cosh^{2}x-sinh^{2}x=1$$

**Theorem 6.44**
(i) $1-tanh^{2}x=sech^{2}x$
(ii) $coth^{2}x-1=csch^{2}x$

**Theorem 6.45**
(i) $\frac{d}{dx}(sinh~u)=cosh~u\frac{du}{dx}$
(ii) $\frac{d}{dx}(cosh~u)=sinh~u\frac{du}{dx}$
(iii) $\frac{d}{dx}(tanh~u)=sech^{2}u\frac{du}{dx}$
(iv) $\frac{d}{dx}(coth~u)=-csch^{2}u\frac{du}{dx}$
(v) $\frac{d}{dx}(sech~u)=-sech~u~tanh~u\frac{du}{dx}$
(vi) $\frac{d}{dx}(csch~u)=-csch~u~coth~u\frac{du}{dx}$

**Theorem 6.46**
(i) $\int sinh~u~du=cosh~u+C$
(ii) $\int cosh~u~du=sinh~u+C$
(iii) $\int sech^{2}u~du=tanh~u+C$
(iv) $\int csch^{2}u~du=-coth~u+C$
(v) $\int sech~u~tanh~u~du=-sech~u+C$
(vi) $\int csch~u~coth~u~du=-csch~u+C$

**Theorem 6.47**
(i) $sinh^{-1}x=ln(x+\sqrt{x^{2}+1})$
(ii) $cosh^{-1}x=ln(x+\sqrt{x^{2}-1}), x\ge1$
(iii) $tanh^{-1}x=\frac{1}{2}ln\frac{1+x}{1-x}, |x|<1$
(iv) $sech^{-1}x=ln\frac{1+\sqrt{1-x^{2}}}{x}, 0<x\le1$

**Theorem 6.48**
(i) $\frac{d}{dx}(sinh^{-1}u)=\frac{1}{\sqrt{u^{2}+1}}\frac{du}{dx}$
(ii) $\frac{d}{dx}(cosh^{-1}u)=\frac{1}{\sqrt{u^{2}-1}}\frac{du}{dx}, u>1$
(iii) $\frac{d}{dx}(tanh^{-1}u)=\frac{1}{1-u^{2}}\frac{du}{dx}, |u|<1$
(iv) $\frac{d}{dx}(sech^{-1}u)=\frac{-1}{u\sqrt{1-u^{2}}}\frac{du}{dx}, 0<u<1$

**Theorem 6.49**
(i) $\int\frac{1}{\sqrt{a^{2}+u^{2}}}du=sinh^{-1}\frac{u}{a}+C, a>0$
(ii) $\int\frac{1}{\sqrt{u^{2}-a^{2}}}du=cosh^{-1}\frac{u}{a}+C, 0<a<u$
(iii) $\int\frac{1}{a^{2}-u^{2}}du=\frac{1}{a}tanh^{-1}\frac{u}{a}+C, |u|<a$
(iv) $\int\frac{1}{u\sqrt{a^{2}-u^{2}}}du=-\frac{1}{a}sech^{-1}\frac{|u|}{a}+C, 0<|u|<a$

## Formulas
No formal boxed formulas distinct from Theorems.

## Guidelines / Methods
No numbered guideline lists or method tables.

## Worked Examples
### Example 1
If $f(x)=cosh(x^{2}+1)$ find $f^{\prime}(x)$.
**Solution**
Applying Theorem (6.45)(i), with $u=x^{2}+1$, we obtain
$$f^{\prime}(x)=sinh(x^{2}+1)\cdot\frac{d}{dx}(x^{2}+1)=2x~sinh(x^{2}+1).$$

### Example 5
Evaluate $\int\frac{1}{\sqrt{25+9x^{2}}}dx.$
**Solution**
We may express the integral as in Theorem (6.49)(i), by using the substitution
$$u=3x, \quad du=3~dx.$$
Since du contains the factor 3, we adjust the integrand by multiplying by 3 and then compensate by multiplying the integral by $\frac{1}{3}$ before substituting:
$$\int\frac{1}{\sqrt{25+9x^{2}}}dx=\frac{1}{3}\int\frac{1}{\sqrt{5^{2}+(3x)^{2}}}3dx$$
$$=\frac{1}{3}\int\frac{1}{\sqrt{5^{2}+u^{2}}}du$$
$$=\frac{1}{3}sinh^{-1}\frac{u}{5}+C$$
$$=\frac{1}{3}sinh^{-1}\frac{3x}{5}+C$$

### Example 6
Evaluate $\int\frac{e^{x}}{16-e^{2x}}dx.$
**Solution**
Substituting $u=e^{x}$, $du=e^{x}dx$ and applying Theorem (6.49)(iii) with $a=4$, we have
$$\int\frac{e^{x}}{16-e^{2x}}dx=\int\frac{1}{4^{2}-(e^{x})^{2}}e^{x}dx$$
$$=\int\frac{1}{4^{2}-u^{2}}du$$
$$=\frac{1}{4}tanh^{-1}\frac{u}{4}+C$$
$$=\frac{1}{4}tanh^{-1}\frac{e^{x}}{4}+C, \quad |u|<a \text{ (that is, } e^{x}<4).$$

## Exercises
*   19. Evaluate: $\int x^{2}cosh(x^{3})dx$
*   20. Evaluate: $\int\frac{1}{sech~7x}dx$
*   21. Evaluate: $\int\frac{sinh\sqrt{x}}{\sqrt{x}}dx$
*   28. Evaluate: $\int sinh~x~sech^{2}x~dx$
*   29. Evaluate: $\int cosh~x~csch^{2}x~dx$
*   61. Find $f^{\prime}(x)$ if $f(x)=sinh^{-1}5x$
*   63. Find $f^{\prime}(x)$ if $f(x)=cosh^{-1}\sqrt{x}$
*   65. Find $f^{\prime}(x)$ if $f(x)=tanh^{-1}(-4x)$
*   67. Find $f^{\prime}(x)$ if $f(x)=sech^{-1}x^{2}$
*   73. Evaluate: $\int\frac{1}{\sqrt{81+16x^{2}}}dx$
*   74. Evaluate: $\int\frac{1}{\sqrt{16x^{2}-9}}dx$
*   75. Evaluate: $\int\frac{1}{49-4x^{2}}dx$
*   79. Evaluate: $\int\frac{1}{x\sqrt{9-x^{4}}}dx$
*   80. Evaluate: $\int\frac{sin~x}{\sqrt{1+cos^{2}x}}dx$