# section_7_4.md

course: MATH106
book_chapter: 7
book_section: 7.4
ksu_chapter: 3
section_title: Integrals of Rational Functions
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: [1, 2, 5, 6, 9, 11, 25]
topic_tags: [rational-functions, partial-fraction-decomposition, irreducible-quadratic]
difficulty: UNKNOWN
in_syllabus: true
enrichment: UNKNOWN
status: draft

---

# Integrals of Rational Functions

---

## Metadata

- **Course:** MATH106
- **Book:** Calculus (Swokowski)
- **Edition:** 6th
- **Chapter Number:** 7
- **Chapter Title:** Techniques of Integration
- **Section Number:** 7.4
- **Section Title:** Integrals of Rational Functions

---

## Definitions

Recall that if $q$ is a rational function, then $q(x) = f(x)/g(x)$, where $f(x)$ and $g(x)$ are polynomials.

The expression on the left side of the equation

$$\frac{1}{x - 1} + \frac{-1}{x + 1} = \frac{2}{x^2 - 1}$$

is called the **partial fraction decomposition** of $2/(x^2 - 1)$.

The sum $F_1 + F_2 + \cdots + F_r$ is the **partial fraction decomposition** of $f(x)/g(x)$, and each $F_k$ is a **partial fraction**.

---

## Theorems

No formally numbered theorems are introduced in this section.

---

## Formulas

- **Guidelines for Partial Fraction Decompositions of $f(x)/g(x)$ (7.5):**
  1. If the degree of $f(x)$ is not lower than the degree of $g(x)$, use long division to obtain the proper form.

  2. Express $g(x)$ as a product of linear factors $ax + b$ or irreducible quadratic factors $ax^2 + bx + c$, and collect repeated factors so that $g(x)$ is a product of different factors of the form $(ax + b)^n$ or $(ax^2 + bx + c)^n$ for a nonnegative integer $n$.

  3. Apply the following rules.

     **Rule a:** For each factor $(ax + b)^n$ with $n \geq 1$, the partial fraction decomposition contains a sum of $n$ partial fractions of the form

     $$\frac{A_1}{ax + b} + \frac{A_2}{(ax + b)^2} + \cdots + \frac{A_n}{(ax + b)^n},$$

     where each numerator $A_k$ is a real number.

     **Rule b:** For each factor $(ax^2 + bx + c)^n$ with $n \geq 1$ and with $ax^2 + bx + c$ irreducible, the partial fraction decomposition contains a sum of $n$ partial fractions of the form

     $$\frac{A_1 x + B_1}{ax^2 + bx + c} + \frac{A_2 x + B_2}{(ax^2 + bx + c)^2} + \cdots + \frac{A_n x + B_n}{(ax^2 + bx + c)^n},$$

     where each $A_k$ and $B_k$ is a real number.

---

## Concepts

It is theoretically possible to write any rational expression $f(x)/g(x)$ as a sum of rational expressions whose denominators involve powers of polynomials of degree not greater than two. Specifically, if $f(x)$ and $g(x)$ are polynomials and the degree of $f(x)$ is less than the degree of $g(x)$, then it can be proved that

$$\frac{f(x)}{g(x)} = F_1 + F_2 + \cdots + F_r$$

such that each term $F_k$ of the sum has one of the forms

$$\frac{A}{(ax + b)^n} \qquad \text{or} \qquad \frac{Ax + B}{(ax^2 + bx + c)^n}$$

for real numbers $A$ and $B$ and a nonnegative integer $n$, where $ax^2 + bx + c$ is **irreducible** in the sense that this quadratic polynomial has no real zeros (that is, $b^2 - 4ac < 0$). In this case, $ax^2 + bx + c$ cannot be expressed as a product of two first-degree polynomials with real coefficients.

The guidelines for finding the partial fraction decomposition of $f(x)/g(x)$ should be used only if $f(x)$ has lower degree than $g(x)$. If this is not the case, then we may use long division to arrive at the proper form. For example, given

$$\frac{x^3 - 6x^2 + 5x - 3}{x^2 - 1},$$

we obtain, by long division,

$$\frac{x^3 - 6x^2 + 5x - 3}{x^2 - 1} = x - 6 + \frac{6x - 9}{x^2 - 1}.$$

We then find the partial fraction decomposition for $(6x - 9)/(x^2 - 1)$.

To find $\int q(x) \, dx$, we integrate each of the fractions that make up the decomposition. For example,

$$\int \frac{2}{x^2 - 1} \, dx = \int \frac{1}{x - 1} \, dx + \int \frac{-1}{x + 1} \, dx$$

$$= \ln|x - 1| - \ln|x + 1| + C$$

$$= \ln\left|\frac{x - 1}{x + 1}\right| + C.$$

Another technique for finding the unknown constants $A$, $B$, and $C$ in a partial fraction decomposition is to expand the right-hand side of the equation and collect like powers of $x$, then use the fact that if two polynomials are equal, then coefficients of like powers of $x$ are the same. This is called **comparing coefficients of $x$**.

Many of the steps in the partial fraction decomposition of $f(x)/g(x)$ are straightforward algebraic manipulations that may be tedious to perform if the degree of $g$ is large. Computer algebra systems provide a useful tool for automating some of these steps in such cases.

---

## Examples

### Example 1

#### Problem

Evaluate $\displaystyle\int \frac{4x^2 + 13x - 9}{x^3 + 2x^2 - 3x} \, dx$.

#### Solution

We may factor the denominator of the integrand as follows:

$$x^3 + 2x^2 - 3x = x(x^2 + 2x - 3) = x(x + 3)(x - 1)$$

Each factor has the form stated in rule (a) of (7.5), with $n = 1$. Thus, to the factor $x$ there corresponds a partial fraction of the form $A/x$. Similarly, to the factors $x + 3$ and $x - 1$ there correspond partial fractions $B/(x + 3)$ and $C/(x - 1)$, respectively. Therefore, the partial fraction decomposition has the form

$$\frac{4x^2 + 13x - 9}{x(x + 3)(x - 1)} = \frac{A}{x} + \frac{B}{x + 3} + \frac{C}{x - 1}.$$

Multiplying by the lowest common denominator gives us

$$(*) \qquad 4x^2 + 13x - 9 = A(x + 3)(x - 1) + Bx(x - 1) + Cx(x + 3).$$

In a case such as this, in which the factors are all linear and nonrepeated, the values for $A$, $B$, and $C$ can be found by substituting values for $x$ that make the various factors zero. If we let $x = 0$ in $(*)$, then

$$-9 = -3A, \qquad \text{or} \quad A = 3.$$

Letting $x = 1$ in $(*)$ gives us

$$8 = 4C, \qquad \text{or} \quad C = 2.$$

Finally, if $x = -3$ in $(*)$, then

$$-12 = 12B, \qquad \text{or} \quad B = -1.$$

The partial fraction decomposition is, therefore,

$$\frac{4x^2 + 13x - 9}{x(x + 3)(x - 1)} = \frac{3}{x} + \frac{-1}{x + 3} + \frac{2}{x - 1}.$$

Integrating and letting $K$ denote the sum of the constants of integration, we have

$$\int \frac{4x^2 + 13x - 9}{x(x + 3)(x - 1)} \, dx = \int \frac{3}{x} \, dx + \int \frac{-1}{x + 3} \, dx + \int \frac{2}{x - 1} \, dx$$

$$= 3\ln|x| - \ln|x + 3| + 2\ln|x - 1| + K$$

$$= \ln|x^3| - \ln|x + 3| + \ln|x - 1|^2 + K$$

$$= \ln\left|\frac{x^3(x - 1)^2}{x + 3}\right| + K.$$

---

Another technique for finding $A$, $B$, and $C$ is to expand the right-hand side of $(*)$ and collect like powers of $x$ as follows:

$$4x^2 + 13x - 9 = (A + B + C)x^2 + (2A - B + 3C)x - 3A$$

We now use the fact that if two polynomials are equal, then coefficients of like powers of $x$ are the same. It is convenient to arrange our work in the following way, which we call comparing coefficients of $x$:

$$\text{coefficients of } x^2: \quad A + B + C = 4$$

$$\text{coefficients of } x: \quad 2A - B + 3C = 13$$

$$\text{constant terms:} \quad -3A = -9$$

We may show that the solution of this system of equations is $A = 3$, $B = -1$, and $C = 2$.

---

### Example 2

#### Problem

Evaluate $\displaystyle\int \frac{3x^3 - 18x^2 + 29x - 4}{(x + 1)(x - 2)^3} \, dx$.

#### Solution

By rule (a) of (7.5), there is a partial fraction of the form $A/(x + 1)$ corresponding to the factor $x + 1$ in the denominator of the integrand. For the factor $(x - 2)^3$, we apply rule (a), with $n = 3$, obtaining a sum of three partial fractions $B/(x - 2)$, $C/(x - 2)^2$, and $D/(x - 2)^3$. Consequently, the partial fraction decomposition has the form

$$\frac{3x^3 - 18x^2 + 29x - 4}{(x + 1)(x - 2)^3} = \frac{A}{x + 1} + \frac{B}{x - 2} + \frac{C}{(x - 2)^2} + \frac{D}{(x - 2)^3}.$$

Multiplying both sides by $(x + 1)(x - 2)^3$ gives us

$$(*) \qquad 3x^3 - 18x^2 + 29x - 4 = A(x - 2)^3 + B(x + 1)(x - 2)^2 + C(x + 1)(x - 2) + D(x + 1).$$

Two of the unknown constants may be determined easily. If we let $x = 2$ in $(*)$, we obtain

$$6 = 3D, \qquad \text{or} \quad D = 2.$$

Similarly, letting $x = -1$ in $(*)$ yields

$$-54 = -27A, \qquad \text{or} \quad A = 2.$$

The remaining constants may be found by comparing coefficients. Examining the right-hand side of $(*)$, we see that the coefficient of $x^3$ is $A + B$. This must equal the coefficient of $x^3$ on the left. Thus, by comparison,

$$\text{coefficients of } x^3: \quad 3 = A + B.$$

Since $A = 2$, it follows that $B = 1$.

Finally, we compare the constant terms in $(*)$ by letting $x = 0$. This gives us the following:

$$\text{constant terms:} \quad -4 = -8A + 4B - 2C + D$$

Substituting the values we have found for $A$, $B$, and $D$ into the preceding equation yields

$$-4 = -16 + 4 - 2C + 2,$$

which has the solution $C = -3$. The partial fraction decomposition is, therefore,

$$\frac{3x^3 - 18x^2 + 29x - 4}{(x + 1)(x - 2)^3} = \frac{2}{x + 1} + \frac{1}{x - 2} + \frac{-3}{(x - 2)^2} + \frac{2}{(x - 2)^3}.$$

To find the given integral, we integrate each of the partial fractions on the right side of the last equation, obtaining

$$2\ln|x + 1| + \ln|x - 2| + \frac{3}{x - 2} - \frac{1}{(x - 2)^2} + K$$

with $K$ the sum of the four constants of integration. This may be written in the form

$$\ln\left[(x + 1)^2|x - 2|\right] + \frac{3}{x - 2} - \frac{1}{(x - 2)^2} + K.$$

---

### Example 3

#### Problem

Evaluate $\displaystyle\int \frac{x^2 - x - 21}{2x^3 - x^2 + 8x - 4} \, dx$.

#### Solution

The denominator may be factored by grouping as follows:

$$2x^3 - x^2 + 8x - 4 = x^2(2x - 1) + 4(2x - 1) = (x^2 + 4)(2x - 1)$$

Applying rule (b) of (7.5) to the irreducible quadratic factor $x^2 + 4$, we see that one of the partial fractions has the form $(Ax + B)/(x^2 + 4)$. By rule (a), there is also a partial fraction $C/(2x - 1)$ corresponding to the factor $2x - 1$. Consequently,

$$\frac{x^2 - x - 21}{2x^3 - x^2 + 8x - 4} = \frac{Ax + B}{x^2 + 4} + \frac{C}{2x - 1}.$$

As in previous examples, this result leads to

$$(*) \qquad x^2 - x - 21 = (Ax + B)(2x - 1) + C(x^2 + 4).$$

We can find one constant easily. Substituting $x = \frac{1}{2}$ in $(*)$ gives us

$$-\frac{85}{4} = \frac{17}{4}C, \qquad \text{or} \quad C = -5.$$

The remaining constants may be found by comparing coefficients of $x$ in $(*)$:

$$\text{coefficients of } x^2: \quad 1 = 2A + C$$

$$\text{coefficients of } x: \quad -1 = -A + 2B$$

$$\text{constant terms:} \quad -21 = -B + 4C$$

Since $C = -5$, it follows from $1 = 2A + C$ that $A = 3$. Similarly, using the coefficients of $x$ with $A = 3$ gives us $-1 = -3 + 2B$, or $B = 1$. Thus, the partial fraction decomposition of the integrand is

$$\frac{x^2 - x - 21}{2x^3 - x^2 + 8x - 4} = \frac{3x + 1}{x^2 + 4} + \frac{-5}{2x - 1}$$

$$= \frac{3x}{x^2 + 4} + \frac{1}{x^2 + 4} - \frac{5}{2x - 1}.$$

The given integral may now be found by integrating the right side of the last equation. This gives us

$$\frac{3}{2}\ln(x^2 + 4) + \frac{1}{2}\tan^{-1}\frac{x}{2} - \frac{5}{2}\ln|2x - 1| + K.$$

---

### Example 4

#### Problem

Evaluate $\displaystyle\int \frac{5x^3 - 3x^2 + 7x - 3}{(x^2 + 1)^2} \, dx$.

#### Solution

Applying rule (b) of (7.5), with $n = 2$, yields

$$\frac{5x^3 - 3x^2 + 7x - 3}{(x^2 + 1)^2} = \frac{Ax + B}{x^2 + 1} + \frac{Cx + D}{(x^2 + 1)^2}.$$

Multiplying by the lowest common denominator $(x^2 + 1)^2$ gives us

$$5x^3 - 3x^2 + 7x - 3 = (Ax + B)(x^2 + 1) + Cx + D$$

$$5x^3 - 3x^2 + 7x - 3 = Ax^3 + Bx^2 + (A + C)x + (B + D).$$

We next compare coefficients as follows:

$$\text{coefficients of } x^3: \quad 5 = A$$

$$\text{coefficients of } x^2: \quad -3 = B$$

$$\text{coefficients of } x: \quad 7 = A + C$$

$$\text{constant terms:} \quad -3 = B + D$$

We now have $A = 5$, $B = -3$, $C = 7 - A = 2$, and $D = -3 - B = 0$; therefore,

$$\frac{5x^3 - 3x^2 + 7x - 3}{(x^2 + 1)^2} = \frac{5x - 3}{x^2 + 1} + \frac{2x}{(x^2 + 1)^2}$$

$$= \frac{5x}{x^2 + 1} - \frac{3}{x^2 + 1} + \frac{2x}{(x^2 + 1)^2}.$$

Integrating yields

$$\int \frac{5x^3 - 3x^2 + 7x - 3}{(x^2 + 1)^2} \, dx = \frac{5}{2}\ln(x^2 + 1) - 3\tan^{-1} x - \frac{1}{x^2 + 1} + K.$$

---

### Example 5

#### Problem

Use a computer algebra system to evaluate

$$\int \frac{264x^3 - 553x^2 - 310x - 543}{24x^4 - 142x^3 - 59x^2 + 267x + 90} \, dx.$$

#### Solution

We first use a CAS to help factor the denominator. The exact commands and the rules for using them depend on the particular CAS being used. In this example, we illustrate some commands available in *Theorist*®. We enter the rational function and then select the denominator. The command to _factor_ yields

$$\frac{264x^3 - 553x^2 - 310x - 543}{24x^4 - 142x^3 - 59x^2 + 267x + 90} = \frac{264x^3 - 553x^2 - 310x - 543}{24(x - 6)\left(x + \frac{5}{4}\right)\left(x - \frac{3}{2}\right)\left(x + \frac{1}{3}\right)}.$$

We see that the denominator is the product of distinct linear factors. Next, we select the entire expression on the right side of the equation and give the command to _expand_. The CAS responds with the decomposition:

$$\frac{264x^3 - 553x^2 - 310x - 543}{24(x - 6)\left(x + \frac{5}{4}\right)\left(x - \frac{3}{2}\right)\left(x + \frac{1}{3}\right)} = 7\cdot\frac{1}{x - 6} + \frac{7}{2}\cdot\frac{1}{x + \frac{5}{4}} + \frac{5}{2}\cdot\frac{1}{x - \frac{3}{2}} - 2\cdot\frac{1}{x + \frac{1}{3}}$$

We may now integrate the original fraction by integrating each of the four terms on the right:

$$\int \frac{264x^3 - 553x^2 - 310x - 543}{24x^4 - 142x^3 - 59x^2 + 267x + 90} \, dx$$

$$= 7\int \frac{dx}{x - 6} + \frac{7}{2}\int \frac{dx}{x + \frac{5}{4}} + \frac{5}{2}\int \frac{dx}{x - \frac{3}{2}} - 2\int \frac{dx}{x + \frac{1}{3}}$$

$$= 7\ln|x - 6| + \frac{7}{2}\ln\left|x + \frac{5}{4}\right| + \frac{5}{2}\ln\left|x - \frac{3}{2}\right| - 2\ln\left|x + \frac{1}{3}\right| + K$$

---

### Example 6

#### Problem

If $x$ represents the number of people in a population of constant size $N$ who have certain information, then a model of social diffusion for the rate by which $x$ changes is

$$\frac{dx}{dt} = kx(N - x)$$

for some positive constant $k$ (see Section 3.8).

(a) Find the number of people $x(t)$ who have the information at time $t$ as an explicit function of $t$.

(b) Find $\displaystyle\lim_{t \to \infty} x(t)$ and interpret the result.

#### Solution

**(a)** Beginning with the differential equation

$$\frac{dx}{dt} = kx(N - x),$$

we separate the variables and integrate to obtain

$$\int dt = \int \frac{1}{kx(N - x)} \, dx.$$

To integrate the expression on the right side of this equation, we make the partial fraction decomposition

$$\frac{1}{kx(N - x)} = \frac{1/N}{kx} + \frac{1/kN}{N - x},$$

so that

$$\int N \, dt = \int \frac{N}{kx(N - x)} \, dx$$

$$= \int \left(\frac{1}{kx} + \frac{1/k}{N - x}\right) dx$$

$$= \int \frac{1}{kx} \, dx + \int \frac{1/k}{N - x} \, dx.$$

Integrating, we have

$$Nt = \frac{1}{k}\ln|x| - \frac{1}{k}\ln|N - x| + D,$$

or

$$kNt = \ln|x| - \ln|N - x| + kD$$

for some constant $D$. Since $x$ and $N - x$ represent numbers of people, they are positive, so $\ln|x| = \ln x$ and $\ln|N - x| = \ln(N - x)$. Thus,

$$kNt = \ln x - \ln(N - x) + kD.$$

Using properties of the logarithm,

$$\ln A + \ln B = \ln(AB) \qquad \text{and} \qquad \ln A - \ln B = \ln(A/B),$$

we have

$$kNt = \ln\frac{x}{N - x} + \ln e^{kD} = \ln\frac{Cx}{N - x},$$

where the constant $C$ represents $e^{kD}$. Since $y = \ln x$ is equivalent to $x = e^y$, we can write

$$kNt = \ln\frac{Cx}{N - x} \qquad \text{as} \qquad \frac{Cx}{N - x} = e^{kNt}.$$

We now solve this equation for $x$:

$$Cx = e^{kNt}(N - x)$$

$$Cx + e^{kNt}x = Ne^{kNt}$$

$$x(C + e^{kNt}) = Ne^{kNt}$$

$$x = \frac{Ne^{kNt}}{C + e^{kNt}}$$

Thus, the solution of the differential equation gives $x(t)$, the number of people $x$ who have the information at time $t$, as

$$x(t) = \frac{Ne^{kNt}}{C + e^{kNt}}.$$

If the number of people who have the information at time $t = 0$ is $x_0$, then we can determine the value of $C$ since

$$x_0 = \frac{Ne^0}{C + e^0} = \frac{N}{C + 1}.$$

Thus,

$$C = \frac{N}{x_0} - 1 = \frac{N - x_0}{x_0},$$

and we can write $x(t)$ as

$$x(t) = \frac{Nx_0 e^{kNt}}{N - x_0 + x_0 e^{kNt}}.$$

**(b)** To determine

$$\lim_{t \to \infty} x(t) = \lim_{t \to \infty} \frac{Ne^{kNt}}{C + e^{kNt}},$$

we first divide the numerator and the denominator of the fraction by $e^{kNt}$ to obtain

$$x = \frac{N}{Ce^{-kNt} + 1},$$

so that

$$\lim_{t \to \infty} x(t) = \lim_{t \to \infty} \frac{N}{Ce^{-kNt} + 1}.$$

Since $k$ and $N$ are positive,

$$\lim_{t \to \infty} e^{-kNt} = 0$$

and hence

$$\lim_{t \to \infty} x(t) = \lim_{t \to \infty} \frac{N}{Ce^{-kNt} + 1} = \frac{N}{C \cdot 0 + 1} = N.$$

We conclude that the model predicts that eventually everyone in the population will have the information.

---

## Remarks

- The guidelines for finding the partial fraction decomposition of $f(x)/g(x)$ should be used only if $f(x)$ has lower degree than $g(x)$. If this is not the case, then we may use long division to arrive at the proper form.

- A quadratic $ax^2 + bx + c$ is **irreducible** if it has no real zeros (that is, $b^2 - 4ac < 0$). In this case, $ax^2 + bx + c$ cannot be expressed as a product of two first-degree polynomials with real coefficients.

- Two techniques for finding the unknown constants in a partial fraction decomposition are: (1) substituting values of $x$ that make various factors zero, and (2) expanding and comparing coefficients of like powers of $x$.

- The differential equation $dx/dt = kx(N - x)$ in Example 6 is called the **logistic model**. It occurs in many applications in which the growth of a population is under consideration.

---

## Figures

No figures, graphs, or diagrams appear in this section.

---

## Keywords

- Rational function
- Partial fraction decomposition
- Partial fraction
- Irreducible quadratic
- Long division
- Linear factor
- Repeated factor
- Comparing coefficients
- Logistic model
- Computer algebra system
