# section_7_5.md

course: MATH106
book_chapter: 7
book_section: 7.5
ksu_chapter: 3
section_title: Quadratic Expressions and Miscellaneous Substitutions
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: [1, 3, 5, 6, 10, 12, 25, 26, 27, 28, 32, 47, 48, 49, 50]
topic_tags: [completing-the-square, miscellaneous-substitution, half-angle-substitution]
difficulty: UNKNOWN
in_syllabus: true
enrichment: UNKNOWN
status: draft

---

# Quadratic Expressions and Miscellaneous Substitutions

---

## Metadata

- **Course:** MATH106
- **Book:** Calculus (Swokowski)
- **Edition:** 6th
- **Chapter Number:** 7
- **Chapter Title:** Techniques of Integration
- **Section Number:** 7.5
- **Section Title:** Quadratic Expressions and Miscellaneous Substitutions

---

## Definitions

No formal boxed definitions are introduced in this section.

---

## Theorems

### Theorem (7.6)

If an integrand is a rational expression in $\sin x$ and $\cos x$, the following substitutions will produce a rational expression in $u$:

$$\sin x = \frac{2u}{1 + u^2}, \qquad \cos x = \frac{1 - u^2}{1 + u^2}, \qquad dx = \frac{2}{1 + u^2} \, du,$$

where $u = \tan\dfrac{x}{2}$ for $-\pi < x < \pi$.

---

## Formulas

- **Completing the square:**

$$ax^2 + bx + c = a\left(x^2 + \frac{b}{a}x\right) + c = a\left(x + \frac{b}{2a}\right)^2 + c - \frac{b^2}{4a}$$

- **Half-angle identities used in Theorem (7.6):**

$$\cos\frac{x}{2} = \frac{1}{\sec(x/2)} = \frac{1}{\sqrt{1 + \tan^2(x/2)}} = \frac{1}{\sqrt{1 + u^2}}$$

$$\sin\frac{x}{2} = \tan\frac{x}{2}\cos\frac{x}{2} = \frac{u}{\sqrt{1 + u^2}}$$

$$\sin x = 2\sin\frac{x}{2}\cos\frac{x}{2} = \frac{2u}{1 + u^2}$$

$$\cos x = 1 - 2\sin^2\frac{x}{2} = 1 - \frac{2u^2}{1 + u^2} = \frac{1 - u^2}{1 + u^2}$$

$$dx = \frac{2}{1 + u^2} \, du$$

---

## Concepts

### Integrals Involving Quadratic Expressions

In this section, we study some additional techniques for finding antiderivatives. We first examine integrands that involve quadratic expressions, and then we consider a variety of integrals that can be handled by substitutions.

Partial fraction decompositions may lead to integrands containing an irreducible quadratic expression $ax^2 + bx + c$. If $b \neq 0$, it is sometimes necessary to complete the square as follows:

$$ax^2 + bx + c = a\left(x^2 + \frac{b}{a}x\right) + c = a\left(x + \frac{b}{2a}\right)^2 + c - \frac{b^2}{4a}$$

The substitution $u = x + b/(2a)$ may then lead to an integrable form.

We may also use the technique of completing the square if a quadratic expression appears under a radical sign. In the next example, we make a trigonometric substitution after completing the square.

### Miscellaneous Substitutions

We now consider substitutions that are useful for evaluating certain types of integrals. The first example illustrates that if an integral contains an expression of the form $\sqrt[n]{f(x)}$, then one of the substitutions $u = \sqrt[n]{f(x)}$ or $u = f(x)$ may simplify the evaluation.

If an integrand is a rational expression in $\sin x$ and $\cos x$, then the substitution

$$u = \tan\frac{x}{2} \qquad \text{for} \quad -\pi < x < \pi$$

will transform the integrand into a rational (algebraic) expression in $u$. To prove this, first note that

$$\cos\frac{x}{2} = \frac{1}{\sec(x/2)} = \frac{1}{\sqrt{1 + \tan^2(x/2)}} = \frac{1}{\sqrt{1 + u^2}}$$

$$\sin\frac{x}{2} = \tan\frac{x}{2}\cos\frac{x}{2} = \frac{u}{\sqrt{1 + u^2}}.$$

Consequently,

$$\sin x = 2\sin\frac{x}{2}\cos\frac{x}{2} = \frac{2u}{1 + u^2}$$

$$\cos x = 1 - 2\sin^2\frac{x}{2} = 1 - \frac{2u^2}{1 + u^2} = \frac{1 - u^2}{1 + u^2}.$$

Moreover, since $x/2 = \tan^{-1} u$, we have $x = 2\tan^{-1} u$, and, therefore,

$$dx = \frac{2}{1 + u^2} \, du.$$

Theorem (7.6) may be used for any integrand that is a rational expression in $\sin x$ and $\cos x$. However, it is also important to consider simpler substitutions, as illustrated in Example 6.

The evaluation of an integral may well involve the application of several techniques in succession. John Bernoulli's solution of the _brachistochrone problem_, for example, requires an algebraic substitution, a trigonometric substitution, and the use of several trigonometric identities. In 1696, Bernoulli published this problem as a challenge to other mathematicians: Find among all smooth curves lying in a vertical plane and connecting a given higher point $P_0$ to a given lower point $P_1$, the curve along which a particle will slide in the shortest possible time.

In Figure 7.8, we have set up a coordinate system with the higher point $P_0$ at the origin and with the positive direction of the $y$-axis downward. Figure 7.8 also shows a curve joining the points. Such a curve occurs in planning the design of a ski jump, for example. Bernoulli wished to find explicitly an expression for the function $y = f(x)$ whose graph is the curve of fastest descent from $P_0$ to $P_1$. Assuming that gravity is the only force acting on the particle, Bernoulli used ideas from optics, mechanics, and calculus to discover that the function $f$ must satisfy the differential equation

$$y\left[1 + \left(\frac{dy}{dx}\right)^2\right] = c$$

for some constant $c$. We may rewrite this equation as

$$\left[1 + \left(\frac{dy}{dx}\right)^2\right] = \frac{c}{y}$$

or, equivalently,

$$\left(\frac{dy}{dx}\right)^2 = \frac{c}{y} - 1 = \frac{c - y}{y},$$

so that

$$\frac{dy}{dx} = \sqrt{\frac{c - y}{y}},$$

where we have chosen the positive square root, since in our coordinate system $y$ increases as $x$ increases, making $dy/dx > 0$. Since the right side of this differential equation is a function only of the variable $y$, we separate the variables and obtain

$$\int dx = \int \sqrt{\frac{y}{c - y}} \, dy,$$

so that

$$x = \int \sqrt{\frac{y}{c - y}} \, dy.$$

To carry out the integration of the right side, we first make the algebraic substitution $u = \sqrt{y/(c - y)}$, so that $u^2 = y/(c - y)$, which gives $y = cu^2/(1 + u^2)$ and, with differentiation, $dy = [2cu/(1 + u^2)^2] \, du$. Thus,

$$x = \int \sqrt{\frac{y}{c - y}} \, dy = \int u \cdot \frac{2cu}{(1 + u^2)^2} \, du = \int \frac{2cu^2}{(1 + u^2)^2} \, du.$$

To evaluate the last integral, we make the trigonometric substitution $u = \tan\phi$, $du = \sec^2\phi \, d\phi$. Thus, the integrand becomes

$$\frac{2cu^2}{(1 + u^2)^2} = \frac{2c\tan^2\phi}{(1 + \tan^2\phi)^2} = \frac{2c\tan^2\phi}{(\sec^2\phi)^2}$$

so that

$$x = \int \frac{2cu^2}{(1 + u^2)^2} \, du = \int \frac{2c\tan^2\phi}{(\sec^2\phi)^2}\sec^2\phi \, d\phi = \int 2c\sin^2\phi \, d\phi.$$

Our final substitution is to use a variation of the double-angle formula for the cosine, $2\sin^2\phi = 1 - \cos 2\phi$, obtaining

$$x = c\int (1 - \cos 2\phi) \, d\phi.$$

Integration yields

$$x = \frac{c}{2}(2\phi - \sin 2\phi) + D$$

for some constant $D$. Substituting $\phi = 0$ into this equation, we see that $D$ is equal to the value of $x$ when $\phi = 0$. At $\phi = 0$, $u = \tan 0 = 0$ and hence $y = cu^2/(1 + u^2) = 0$. But when $y = 0$, we also have $x = 0$ because the point $P_0(0, 0)$ lies on the curve. Thus, $D = 0$.

Using $u = \tan\phi$ gives us a formula for $y$:

$$y = \frac{cu^2}{1 + u^2} = \frac{c\tan^2\phi}{1 + \tan^2\phi} = \frac{c\tan^2\phi}{\sec^2\phi} = c\sin^2\phi = \frac{c}{2}(1 - \cos 2\phi)$$

As a final simplification, we let $a = c/2$ and $\theta = 2\phi$. The curve of fastest descent is then described by the set of points $P(x, y)$, where $x$ and $y$ are given by a pair of equations:

$$x = a(\theta - \sin\theta), \qquad y = a(1 - \cos\theta)$$

Here we have described the curve by giving separate equations for the $x$- and $y$-coordinates in terms of a third variable, $\theta$. This description is called a **parametric representation** of a curve; we will study such representations in more detail in Chapter 9. In this case, we may regard $\theta$ as representing time. At $\theta = 0$, $x = 0$ and $y = 0$, and the particle is at the point $P_0$. As $\theta$ increases, the particle moves down the curve toward the point $P_1$.

---

## Examples

### Example 1

#### Problem

Evaluate $\displaystyle\int \frac{2x - 1}{x^2 - 6x + 13} \, dx$.

#### Solution

Note that the quadratic expression $x^2 - 6x + 13$ is irreducible, since $b^2 - 4ac = -16 < 0$. We complete the square as follows:

$$x^2 - 6x + 13 = (x^2 - 6x \qquad) + 13$$

$$= (x^2 - 6x + 9) + 13 - 9 = (x - 3)^2 + 4$$

Thus,

$$\int \frac{2x - 1}{x^2 - 6x + 13} \, dx = \int \frac{2x - 1}{(x - 3)^2 + 4} \, dx.$$

We now make the substitution

$$u = x - 3, \quad x = u + 3, \quad dx = du.$$

Thus,

$$\int \frac{2x - 1}{x^2 - 6x + 13} \, dx = \int \frac{2(u + 3) - 1}{u^2 + 4} \, du$$

$$= \int \frac{2u + 5}{u^2 + 4} \, du$$

$$= \int \frac{2u}{u^2 + 4} \, du + 5\int \frac{1}{u^2 + 4} \, du$$

$$= \ln(u^2 + 4) + \frac{5}{2}\tan^{-1}\frac{u}{2} + C$$

$$= \ln(x^2 - 6x + 13) + \frac{5}{2}\tan^{-1}\frac{x - 3}{2} + C.$$

---

### Example 2

#### Problem

Evaluate $\displaystyle\int \frac{1}{\sqrt{x^2 + 8x + 25}} \, dx$.

#### Solution

We complete the square for the quadratic expression as follows:

$$x^2 + 8x + 25 = (x^2 + 8x \qquad) + 25$$

$$= (x^2 + 8x + 16) + 25 - 16$$

$$= (x + 4)^2 + 9$$

Thus,

$$\int \frac{1}{\sqrt{x^2 + 8x + 25}} \, dx = \int \frac{1}{\sqrt{(x + 4)^2 + 9}} \, dx.$$

If we make the trigonometric substitution

$$x + 4 = 3\tan\theta, \qquad dx = 3\sec^2\theta \, d\theta,$$

then

$$\sqrt{(x + 4)^2 + 9} = \sqrt{9\tan^2\theta + 9} = 3\sqrt{\tan^2\theta + 1} = 3\sec\theta$$

and

$$\int \frac{1}{\sqrt{x^2 + 8x + 25}} \, dx = \int \frac{1}{3\sec\theta} 3\sec^2\theta \, d\theta$$

$$= \int \sec\theta \, d\theta$$

$$= \ln|\sec\theta + \tan\theta| + C.$$

To return to the variable $x$, we use the triangle in Figure 7.7, obtaining

$$\int \frac{1}{\sqrt{x^2 + 8x + 25}} \, dx = \ln\left|\frac{\sqrt{x^2 + 8x + 25}}{3} + \frac{x + 4}{3}\right| + C$$

$$= \ln\left|\sqrt{x^2 + 8x + 25} + x + 4\right| - \ln|3| + C$$

$$= \ln\left|\sqrt{x^2 + 8x + 25} + x + 4\right| + K$$

with $K = C - \ln 3$.

---

### Example 3

#### Problem

Evaluate $\displaystyle\int \frac{x^3}{\sqrt[3]{x^2 + 4}} \, dx$.

#### Solution

**Solution 1.** The substitution $u = \sqrt[3]{x^2 + 4}$ leads to the following equivalent equations:

$$u = \sqrt[3]{x^2 + 4}, \qquad u^3 = x^2 + 4, \qquad x^2 = u^3 - 4$$

Taking the differential of each side of the last equation, we obtain

$$2x \, dx = 3u^2 \, du, \qquad \text{or} \quad x \, dx = \tfrac{3}{2}u^2 \, du.$$

We now substitute as follows:

$$\int \frac{x^3}{\sqrt[3]{x^2 + 4}} \, dx = \int \frac{x^2}{\sqrt[3]{x^2 + 4}} \cdot x \, dx$$

$$= \int \frac{u^3 - 4}{u} \cdot \tfrac{3}{2}u^2 \, du = \tfrac{3}{2}\int (u^4 - 4u) \, du$$

$$= \tfrac{3}{2}\left(\tfrac{1}{5}u^5 - 2u^2\right) + C = \tfrac{3}{10}u^2(u^3 - 10) + C$$

$$= \tfrac{3}{10}(x^2 + 4)^{2/3}(x^2 - 6) + C$$

**Solution 2.** If we substitute $u$ for the expression _underneath_ the radical, then

$$u = x^2 + 4, \qquad \text{or} \quad x^2 = u - 4$$

and

$$2x \, dx = du, \qquad \text{or} \quad x \, dx = \tfrac{1}{2} \, du.$$

In this case, we may write

$$\int \frac{x^3}{\sqrt[3]{x^2 + 4}} \, dx = \int \frac{x^2}{\sqrt[3]{x^2 + 4}} \cdot x \, dx$$

$$= \int \frac{u - 4}{u^{1/3}} \cdot \tfrac{1}{2} \, du = \tfrac{1}{2}\int (u^{2/3} - 4u^{-1/3}) \, du$$

$$= \tfrac{1}{2}\left(\tfrac{3}{5}u^{5/3} - 6u^{2/3}\right) + C = \tfrac{3}{10}u^{2/3}(u - 10) + C$$

$$= \tfrac{3}{10}(x^2 + 4)^{2/3}(x^2 - 6) + C.$$

---

### Example 4

#### Problem

Evaluate $\displaystyle\int \frac{1}{\sqrt{x} + \sqrt[3]{x}} \, dx$.

#### Solution

To obtain a substitution that will eliminate the two radicals $\sqrt{x} = x^{1/2}$ and $\sqrt[3]{x} = x^{1/3}$, we use $u = x^{1/n}$, where $n$ is the least common denominator of $\frac{1}{2}$ and $\frac{1}{3}$. Thus, we let

$$u = x^{1/6}, \qquad \text{or, equivalently,} \quad x = u^6.$$

Hence,

$$dx = 6u^5 \, du, \qquad x^{1/2} = (u^6)^{1/2} = u^3, \qquad x^{1/3} = (u^6)^{1/3} = u^2$$

and, therefore,

$$\int \frac{1}{\sqrt{x} + \sqrt[3]{x}} \, dx = \int \frac{1}{u^3 + u^2} 6u^5 \, du = 6\int \frac{u^3}{u + 1} \, du.$$

By long division,

$$\frac{u^3}{u + 1} = u^2 - u + 1 - \frac{1}{u + 1}.$$

Consequently,

$$\int \frac{1}{\sqrt{x} + \sqrt[3]{x}} \, dx = 6\int \left(u^2 - u + 1 - \frac{1}{u + 1}\right) du$$

$$= 6\left(\tfrac{1}{3}u^3 - \tfrac{1}{2}u^2 + u - \ln|u + 1|\right) + C$$

$$= 2\sqrt{x} - 3\sqrt[3]{x} + 6\sqrt[6]{x} - 6\ln(\sqrt[6]{x} + 1) + C.$$

---

### Example 5

#### Problem

Evaluate $\displaystyle\int \frac{1}{4\sin x - 3\cos x} \, dx$.

#### Solution

Applying Theorem (7.6) and simplifying the integrand yields

$$\int \frac{1}{4\sin x - 3\cos x} \, dx = \int \frac{1}{4\left(\dfrac{2u}{1 + u^2}\right) - 3\left(\dfrac{1 - u^2}{1 + u^2}\right)} \cdot \frac{2}{1 + u^2} \, du$$

$$= \int \frac{2}{8u - 3(1 - u^2)} \, du$$

$$= 2\int \frac{1}{3u^2 + 8u - 3} \, du.$$

Using partial fractions, we have

$$\frac{1}{3u^2 + 8u - 3} = \frac{1}{10}\left(\frac{3}{3u - 1} - \frac{1}{u + 3}\right)$$

and hence

$$\int \frac{1}{4\sin x - 3\cos x} \, dx = \frac{1}{5}\int \left(\frac{3}{3u - 1} - \frac{1}{u + 3}\right) du$$

$$= \frac{1}{5}(\ln|3u - 1| - \ln|u + 3|) + C$$

$$= \frac{1}{5}\ln\left|\frac{3u - 1}{u + 3}\right| + C$$

$$= \frac{1}{5}\ln\left|\frac{3\tan(x/2) - 1}{\tan(x/2) + 3}\right| + C.$$

---

### Example 6

#### Problem

Evaluate $\displaystyle\int \frac{\cos x}{1 + \sin^2 x} \, dx$.

#### Solution

We could use the formulas in Theorem (7.6) to change the integrand into a rational expression in $u$. The following substitution is simpler:

$$u = \sin x, \qquad du = \cos x \, dx$$

Thus,

$$\int \frac{\cos x}{1 + \sin^2 x} \, dx = \int \frac{1}{1 + u^2} \, du$$

$$= \arctan u + C$$

$$= \arctan \sin x + C.$$

---

## Remarks

- The guidelines for finding the partial fraction decomposition of $f(x)/g(x)$ should be used only if $f(x)$ has lower degree than $g(x)$. Completing the square is sometimes necessary when the decomposition leads to irreducible quadratic expressions.

- If an integral contains an expression of the form $\sqrt[n]{f(x)}$, then one of the substitutions $u = \sqrt[n]{f(x)}$ or $u = f(x)$ may simplify the evaluation.

- Theorem (7.6) may be used for any integrand that is a rational expression in $\sin x$ and $\cos x$. However, it is also important to consider simpler substitutions.

- The curve of fastest descent (brachistochrone) is described parametrically by $x = a(\theta - \sin\theta)$ and $y = a(1 - \cos\theta)$. This description is called a **parametric representation** of a curve.

---

## Figures

### Figure 7.7

A right triangle with angle $\theta$, opposite side $x + 4$, adjacent side $3$, and hypotenuse $\sqrt{(x + 4)^2 + 9}$. The relation $\tan\theta = \frac{x + 4}{3}$ is labeled.

### Figure 7.8

A coordinate system with point $P_0$ at the origin and the positive $y$-axis directed downward. A smooth curve descends from $P_0$ to a lower point $P_1$. The horizontal axis is labeled $x$ and the vertical axis is labeled $y$.

---

## Keywords

- Completing the square
- Irreducible quadratic
- Trigonometric substitution
- Miscellaneous substitution
- Rational expression in sine and cosine
- Half-angle substitution
- Brachistochrone problem
- Parametric representation
- Partial fractions
- Radical substitution
