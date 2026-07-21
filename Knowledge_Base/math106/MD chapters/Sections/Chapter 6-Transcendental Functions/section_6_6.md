---
source_file: "Section_6.6_Separable_Differential_Equations.pdf" #[cite: 13]
course: MATH106
book_chapter: 6
book_section: 6.6
ksu_chapter: UNKNOWN
section_title: SEPARABLE DIFFERENTIAL EQUATIONS AND LAWS OF GROWTH AND DECAY
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: []
topic_tags: [separable-differential-equations, exponential-growth, exponential-decay, newton's-law-of-cooling]
difficulty: UNKNOWN
in_syllabus: false
enrichment: UNKNOWN
status: draft
---

# SEPARABLE DIFFERENTIAL EQUATIONS AND LAWS OF GROWTH AND DECAY

## Metadata
**Course:** MATH106
**Book:** Calculus (Swokowski)
**Edition:** 6th
**Chapter Number:** 6
**Chapter Title:** Transcendental Functions
**Section Number:** 6.6
**Section Title:** SEPARABLE DIFFERENTIAL EQUATIONS AND LAWS OF GROWTH AND DECAY

## Definitions
No formal boxed definitions.

## Theorems
**Theorem 6.33**
Let y be a differentiable function of t such that $y>0$ for every t, and let $y_{0}$ be the value of y at $t=0$ If $dy/dt=cy$ for some constant c, then
$$y=y_{0}e^{ct}$$

## Formulas
No formal boxed formulas distinct from Theorems and Methods.

## Guidelines / Methods
No numbered guideline lists or method tables.

## Worked Examples
### Example 1
The number of bacteria in a culture increases from 600 to 1800 in 2 hr. Assuming that the rate of increase is directly proportional to the number of bacteria present, find
(a) a formula for the number of bacteria at time t
(b) the number of bacteria at the end of 4 hr
**Solution**
(a) Let $y=q(t)$ denote the number of bacteria after t hours. Thus, $y_{0}=q(0)=600$ and $q(2)=1800.$ By hypothesis,
$$\frac{dy}{dt}=cy$$ .
Following exactly the same steps used in the proof of Theorem (6.33), we obtain
$$y=y_{0}e^{ct}=600e^{ct}$$
Since $y=1800$ when $t=2$, we obtain the following equivalent equations:
$$1800=600e^{2c} \quad 3=e^{2c}$$
$$e^{c}=3^{1/2}$$
Substituting for $e^{c}$ in $y=600e^{ct}$ gives us
$$y=600(3^{1/2})^{t}, \quad \text{or} \quad y=600(3)^{t/2}$$
(b) Letting $t=4$ in $y=600(3)^{t/2}$ yields
$$y=600(3)^{4/2}=600(9)=5400.$$

### Example 2
Radium decays exponentially and has a half-life of approximately 1600 yr that is, given any quantity, one half of it will disintegrate in 1600 yr.
(a) Find a formula for the amount y remaining from 50 mg of pure radium after t years.
(b) When will the amount remaining be 20 mg?
**Solution**
(a) If we let $y=q(t),$ then
$$y_{0}=q(0)=50 \quad \text{and} \quad q(1600)=\frac{1}{2}(50)=25$$.
Since $dy/dt=cy$ for some c, it follows from Theorem (6.33) that
$$y=50e^{ct}$$
Since $y=25$ when $t=1600,$
$$25=50e^{1600c} \quad \text{or} \quad e^{1600c}=\frac{1}{2}$$
Hence,
$$e^{c}=(\frac{1}{2})^{1/1600}=2^{-1/1600}$$
Substituting for $e^{c}$ in $y=50e^{ct}$ gives us
$$y=50(2^{-1/1600})^{t} \quad \text{or} \quad y=50(2)^{-t/1600}$$
(b) Using $y=50(2)^{-t/1600}$, we see that the value of t at which $y=20$ is a solution of the equation
$$20=50(2)^{-t/1600} \quad \text{or} \quad 2^{t/1600}=\frac{5}{2}$$
Taking the natural logarithm of each side, we obtain
$$\frac{t}{1600}ln~2=ln\frac{5}{2}$$
or
$$t=\frac{1600~ln\frac{5}{2}}{ln~2}\approx2115 \text{ yr}.$$

### Example 3
According to Newton's law of cooling, the rate at which an object cools is directly proportional to the difference in temperature between the object and the surrounding medium. If an object cools from 125 °F to 100°F in half an hour when surrounded by air at a temperature of 75°F, find its temperature at the end of the next half hour.
**Solution**
Let y denote the temperature of the object after t hours of cooling. Since the temperature of the surrounding medium is $75^{\circ}$, the difference in temperature is $y-75$, and therefore, by Newton's law of cooling,
$$\frac{dy}{dt}=c(y-75)$$
for some constant c. We separate variables and integrate as follows:
$$\frac{1}{y-75}dy=c~dt$$
$$\int\frac{1}{y-75}dy=\int c~dt$$
$$ln(y-75)=ct+b$$
for some constant b. The last equation is equivalent to
$$y-75=e^{ct+b}=e^{b}e^{ct}$$
Since $y=125$ when $t=0$.
$$125-75=e^{b}e^{0}=e^{b}$$.
or $e^{b}=50$.
Hence,
$$y-75=50e^{ct}$$,
or $y=50e^{ct}+75$
Using the fact that $y=100$ when $t=\frac{1}{2}$ leads to the following equivalent equations:
$$100=50e^{c/2}+75 \quad e^{c/2}=\frac{25}{50}=\frac{1}{2}, \quad e^{c}=\frac{1}{4}$$
Substituting $\frac{1}{4}$ for $e^{c}$ in $y=50e^{ct}+75$ gives us a formula for the temperature after t hours:
$$y=50(\frac{1}{4})^{t}+75$$
In particular, if $t=1$,
$$y=50(\frac{1}{4})+75=87.5^{\circ}\text{F}$$.

### Example 4
Discuss and sketch the graph of the Gompertz growth function G.
$$G(t)=ke^{(-Ae^{-Bt})}$$
**Solution**
We first observe that the y-intercept is $G(0)=ke^{-A}$ and that $G(t)>0$ for every t. Differentiating twice, we obtain
$$G^{\prime}(t)=ke^{(-Ae^{-Bt})}(-Ae^{-Bt})^{\prime}$$
$$=ABke^{(-Bt-Ae^{-Bt})}$$
$$G^{\prime\prime}(t)=ABke^{(-Bt-Ae^{-Bt})}(-Bt-Ae^{-Bt})^{\prime}$$
$$=ABk(-B+ABe^{-Bt})e^{-Bt-Ae^{-Bt}}.$$
Since $G^{\prime}(t)>0$ for every t, the function G is increasing on $[0,\infty)$. The second derivative $G^{\prime\prime}(t)$ is zero if
$$-B+ABe^{-Bt}=0, \quad \text{or} \quad e^{Bt}=A$$
Solving the last equation for t gives us $t=(1/B)ln~A$, which is a critical number for the function G'. We can also show that
$$lim_{t\rightarrow\infty}G^{\prime}(t)=0 \quad \text{and} \quad lim_{t\rightarrow\infty}G(t)=k$$ .
Hence, as t increases without bound, the rate of growth approaches 0 and the graph of G has a horizontal asymptote $y=k$. The point P on the graph, corresponding to $t=(1/B)ln~A$, is a point of inflection, and the concavity changes from upward to downward at P.

### Example 5
When uranium disintegrates into lead, one step in the process is the radioactive decay of radium into radon gas. Radon gas enters homes by diffusing through the soil into basements, where it presents a health hazard if inhaled. If a quantity Q of radium is present initially, then the amount of radon gas present after t years is given by
$$A(t)=\frac{c_{1}Q}{c_{2}-c_{1}}(e^{-c_{1}t}-e^{-c_{2}t}),$$
where $c_{1}=\frac{1}{1600}ln~2$ and $c_{2}=\frac{1}{0.0105}ln~2$ are the decay constants for radium and radon gas, respectively.
(a) Find the amount of radon gas present initially and after an extended period of time.
(b) Use a graphing utility to graph A(t).
(c) Determine the maximum amount $A_{M}$ of radon gas and when that amount is reached.
(d) After the maximum amount $A_{M}$ has been reached, estimate how long it would take the radon gas to decrease to 90% of the maximum.
**Solution**
(a) The initial amount of radon gas is
$$A(0)=\frac{c_{1}Q}{c_{2}-c_{1}}(e^{0}-e^{0})=0.$$
If we let t increase without bound, then
$$lim_{t\rightarrow\infty}A(t)=\frac{c_{1}Q}{c_{2}-c_{1}}lim_{t\rightarrow\infty}(e^{-c_{1}t}-e^{-c_{2}t})$$
$$=\frac{c_{1}Q}{c_{2}-c_{1}}(0-0)=0$$ .
Hence, over a long period of time, the amount of radon gas decreases to 0.
(b) We use a graphing utility to obtain a graph of A(t). It appears that the radon gas rises fairly quickly to its maximum level and then levels off or perhaps decreases very, very slowly.
(c) To find the critical numbers of A, we differentiate, obtaining
$$A^{\prime}(t)=\frac{c_{1}Q}{c_{2}-c_{1}}(-c_{1}e^{-c_{1}t}+c_{2}e^{-c_{2}t})$$
Thus, $A^{\prime}(t)=0$ if
$$c_{1}e^{-c_{1}t}=c_{2}e^{-c_{2}t} \quad \text{or} \quad e^{(c_{2}-c_{1})t}=\frac{c_{2}}{c_{1}}$$
It follows that
$$(c_{2}-c_{1})t=ln\frac{c_{2}}{c_{1}}$$
or
$$t=\frac{ln(c_{2}/c_{1})}{c_{2}-c_{1}}$$
This value of t yields the maximum value of A. Substituting this value for t into the function, we find that the maximum value is
$$A_{M}=A(\frac{ln(c_{2}/c_{1})}{c_{2}-c_{1}})=(\frac{c_{1}}{c_{2}})^{c_{2}/(c_{2}-c_{1})}Q$$
For the given values of the constants $c_{1}$ and $c_{2}$ these two numbers are approximately
$$t_{M}\approx0.181~years\approx66\text{ days} \quad \text{and} \quad A_{M}\approx(6.562)10^{-6}Q$$.
(d) To find the value $t_{1}>t_{M}$ that yields $A(t_{1})=0.90A_{M}$ we first divide both sides by Q so that we can work numerically. Using a computational device, we find that the solution to
$$\frac{c_{1}}{c_{2}-c_{1}}(e^{-c_{1}t_{1}}-e^{-c_{2}t_{1}})=(0.9)(6.562)10^{-6}Q$$
for the given values of $c_{1}$ and $c_{2}$ is $t_{1}\approx243$ years.

## Exercises
No exercises assigned for this section.