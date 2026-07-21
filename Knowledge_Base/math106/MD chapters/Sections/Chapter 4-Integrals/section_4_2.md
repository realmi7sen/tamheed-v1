---
course: MATH106
book_chapter: 4
book_section: 4.2
ksu_chapter: UNKNOWN
section_title: CHANGE OF VARIABLES IN INDEFINITE INTEGRALS
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: [1, 3, 5, 7, 9, 16, 20, 21, 27, 32, 37]
topic_tags: [change-of-variables, indefinite-integrals, method-of-substitution]
difficulty: UNKNOWN
in_syllabus: true
enrichment: UNKNOWN
status: draft
---

# CHANGE OF VARIABLES IN INDEFINITE INTEGRALS

## Metadata
**Course:** MATH106
**Book:** Calculus (Swokowski)
**Edition:** 6th
**Chapter Number:** 4
**Chapter Title:** Integrals
**Section Number:** 4.2
**Section Title:** CHANGE OF VARIABLES IN INDEFINITE INTEGRALS

## Definitions
No formal boxed definitions.

## Theorems
No formally numbered theorems.

## Formulas
No formal boxed formulas distinct from Methods.

## Guidelines / Methods
**Method of Substitution 4.7**
If F is an antiderivative of f, then
$$\int f(g(x))g^{\prime}(x)dx=F(g(x))+C$$
If $u=g(x)$ and $du=g^{\prime}(x)dx$, then
$$\int f(u)du=F(u)+C.$$

**Guidelines for Changing Variables in Indefinite Integrals 4.8**
1. Decide on a reasonable substitution $u=g(x)$.
2. Calculate $du=g^{\prime}(x)dx$.
3. Using guidelines (1) and (2), try to transform the integral into a form that involves only the variable u. If necessary, introduce a constant factor k into the integrand and compensate by multiplying the integral by $1/k$ If any part of the resulting integrand contains the variable x, use a different substitution in guideline (1).
4. Evaluate the integral obtained in guideline (3), obtaining an antiderivative involving u.
5. Replace u in the antiderivative obtained in guideline (4) by $g(x)$. The final result should contain only the variable x.

## Worked Examples
### Example 1
Evaluate $\int\sqrt{5x+7}dx.$
**Solution**
We let $u=5x+7$ and calculate du:
$$u=5x+7 \quad du=5~dx$$
Since du contains the factor 5, the integral is not in the proper form $\int f(u) du$ required by (4.7). However, we can introduce the factor 5 into the integrand, provided we also multiply by $\frac{1}{5}$ Doing so and using Theorem (4.6)(i) gives us
$$\int\sqrt{5x+7}dx=\int\sqrt{5x+7}(\frac{1}{5})5~dx$$
$$=\frac{1}{5}\int\sqrt{5x+7}5dx.$$
We now substitute and use the power rule for integration:
$$\int\sqrt{5x+7}dx=\frac{1}{5}\int\sqrt{u}du$$
$$=\frac{1}{5}\int u^{1/2}du$$
$$=\frac{1}{5}\frac{u^{3/2}}{\frac{3}{2}}+C$$
$$=\frac{2}{15}u^{3/2}+C$$
$$=\frac{2}{15}(5x+7)^{3/2}+C$$

### Example 2
Evaluate $\int cos~4x~dx$
**Solution**
We make the substitution
$$u=4x, \quad du=4~dx.$$
Since du contains the factor 4, we adjust the integrand by multiplying by 4 and compensate by multiplying the integral by $\frac{1}{4}$ before substituting:
$$\int cos~4x~dx=\frac{1}{4}\int(cos~4x)4~dx$$
$$=\frac{1}{4}\int cos~u~du$$
$$=\frac{1}{4}sin~u+C$$
$$=\frac{1}{4}sin~4x+C$$

### Example 3
Evaluate $\int(2x^{3}+1)^{7}x^{2}dx$
**Solution**
If an integrand involves an expression raised to a power, such as $(2x^{3}+1)^{7},$ we substitute u for the expression. Thus we let
$$u=2x^{3}+1, \quad du=6x^{2}dx$$
Comparing $du=6x^{2}dx$ with $x^{2}dx$ in the integral suggests that we introduce the factor 6 into the integrand. Doing so and compensating by multiplying the integral by $\frac{1}{6}$ , we obtain the following:
$$\int(2x^{3}+1)^{7}x^{2}dx=\frac{1}{6}\int(2x^{3}+1)^{7}6x^{2}dx$$
$$=\frac{1}{6}\int u^{7}du$$
$$=\frac{1}{6}(\frac{u^{8}}{8})+C$$
$$=\frac{1}{48}(2x^{3}+1)^{8}+C$$

### Example 4
Evaluate $\int x\sqrt[3]{7-6x^{2}}dx$ .
**Solution**
Note that the integrand contains the term x dx. If the factor x were missing or if x were raised to a higher power, the problem would be more complicated. For integrands that involve a radical, we often substitute for the expression under the radical sign. Thus we let
$$u=7-6x^{2}, \quad du=-12x~dx.$$
Next, we introduce the factor -12 into the integrand, compensate by multiplying the integral by $-\frac{1}{12}$ and proceed as follows:
$$\int x\sqrt[3]{7-6x^{2}}dx=-\frac{1}{12}\int\sqrt[3]{7-6x^{2}}(-12)x~dx$$
$$=-\frac{1}{12}\int\sqrt[3]{u}du=-\frac{1}{12}\int u^{1/3}du$$
$$=-\frac{1}{12}(\frac{u^{4/3}}{4/3})+C=-\frac{1}{16}u^{4/3}+C$$
$$=-\frac{1}{16}(7-6x^{2})^{4/3}+C$$

### Example 5
Evaluate $\int\frac{x^{2}-1}{(x^{3}-3x+1)^{6}}dx$
**Solution**
Let
$$u=x^{3}-3x+1, \quad du=(3x^{2}-3)dx=3(x^{2}-1)dx$$
and proceed as follows:
$$\int\frac{x^{2}-1}{(x^{3}-3x+1)^{6}}dx=\frac{1}{3}\int\frac{3(x^{2}-1)}{(x^{3}-3x+1)^{6}}dx$$
$$=\frac{1}{3}\int\frac{1}{u^{6}}du=\frac{1}{3}\int u^{-6}du$$
$$=\frac{1}{3}(\frac{u^{-5}}{-5})+C=-\frac{1}{15}(\frac{1}{u^{5}})+C$$
$$=-\frac{1}{15}\frac{1}{(x^{3}-3x+1)^{5}}+C$$

### Example 6
Evaluate $\int cos^{3}5t~sin~5t~dt$ .
**Solution**
The form of the integrand suggests that we use the power rule (2) in (4.4) with $\int u^{3}du=\frac{1}{4}u^{4}+C$ Thus we let
$$u=g(t)=cos~5t \quad du=-5~sin~5t~dt.$$
The form of du indicates that we should introduce the factor -5 into the integrand, multiply the integral by $-\frac{1}{5}$ and then integrate as follows:
$$\int cos^{3}5t~sin~5t~dt=-\frac{1}{5}\int cos^{3}5t(-5~sin~5t)dt$$
$$=-\frac{1}{5}\int u^{3}du$$
$$=-\frac{1}{5}(\frac{u^{4}}{4})+C$$
$$=-\frac{1}{20}cos^{4}5t+C$$

### Example 7
Studies have shown that the rate at which students learn new vocabulary words in a foreign language decreases as the size of the known vocabulary increases. If W(t) is the number of words known after t days and the rate of change of W is modeled by the differential equation
$$W^{\prime}(t)=\frac{8200}{W(t)} \quad \text{for } 0\le t\le365,$$
(a) find W as an explicit function of t, if the student knows 400 words at time $t=0$
(b) find the number of words known after 1 day and 2 days
**Solution**
(a) From the differential equation, we have
$$W(t)W^{\prime}(t)=8200 \quad \text{for } 0\le t\le365.$$
Since the expressions on each side of the equation are identical on an interval [0, 365], the indefinite integrals of the functions they represent will be identical. Thus, we have
$$\int W(t)W^{\prime}(t)dt=\int8200~dt.$$
We make the substitution
$$u=W(t)$$
$$du=W^{\prime}(t)dt$$
on the left-hand side of this equation, obtaining
$$\int u~du=\int8200~dt$$
so that
$$\frac{u^{2}}{2}=8200t+C.$$
Changing back to our original variables, we have
$$\frac{[W(t)]^{2}}{2}=8200t+C$$
Evaluating at $t=0$ (with $W(0)=400)$ yields
$$\frac{400^{2}}{2}=8200(0)+C=0+C=C,$$
so $C=80,000.$
Hence,
$$\frac{[W(t)]^{2}}{2}=8200t+80,000.$$
This result gives us
$$[W(t)]^{2}=16,400t+160,000$$
and
$$W(t)=\sqrt{16,400t+160,000}=20\sqrt{41t+400}.$$
Thus the number of words $W(t)$ known after t days is $20\sqrt{41t+400}$

(b) After 1 day of additional study, the number of words the student knows is given by
$$W(1)=20\sqrt{41+400}=20\sqrt{441}=(20)(21)=420$$ .
After 2 days, the number of words is
$$W(2)=20\sqrt{482}\approx439.$$
In this model of learning, the student masters an additional 20 words on the first day, but only 19 more words on the second day.

## Exercises
*   1. $\int x(2x^{2}+3)^{40}dx;$ $u=2x^{2}+3$
*   3. $\int x^{2}\sqrt[3]{3x^{3}+7}dx;$ $u=3x^{3}+7$
*   5. $\int\frac{(1+\sqrt{x})^{3}}{\sqrt{x}}dx;$ $u=1+\sqrt{x}$
*   7. $\int\sqrt{x}cos\sqrt{x^{3}}dx;$ $u=x^{3/2}$
*   9. $\int\sqrt{3x-2}dx$
*   16. $\int v\sqrt{9-v^{2}}dv$
*   20. $\int(3-s^{3})^{2}s~ds$
*   21. $\int\frac{(\sqrt{x}+3)^{4}}{\sqrt{x}}dx$
*   27. $\int cos(4x-3)dx$
*   32. $\int\frac{sin~2x}{\sqrt{1-cos~2x}}dx$
*   37. $\int\frac{sin~x}{cos^{4}x}dx$