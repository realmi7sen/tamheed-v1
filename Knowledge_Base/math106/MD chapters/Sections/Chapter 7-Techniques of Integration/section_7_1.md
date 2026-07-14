# section_7_1.md

course: MATH106
book_chapter: 7
book_section: 7.1
ksu_chapter: 3
section_title: Integration by Parts
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: [1, 2, 7, 11, 12, 13, 16, 17, 31]
topic_tags: [integration-by-parts, reduction-formula, product-rule]
difficulty: UNKNOWN
in_syllabus: true
enrichment: UNKNOWN
status: draft

---

# Integration by Parts

---

## Metadata

- **Course:** MATH106
- **Book:** Calculus (Swokowski)
- **Edition:** 6th
- **Chapter Number:** 7
- **Chapter Title:** Techniques of Integration
- **Section Number:** 7.1
- **Section Title:** Integration by Parts

---

## Definitions

No formal boxed definitions are introduced in this section.

---

## Theorems

### Integration by Parts Formula (7.1)

If $u = f(x)$ and $v = g(x)$ and if $f'$ and $g'$ are continuous, then

$$\int u \, dv = uv - \int v \, du.$$

---

## Proofs

### Proof of Formula (7.1)

By the product rule,

$$\frac{d}{dx}(f(x)g(x)) = f(x)g'(x) + g(x)f'(x),$$

or, equivalently,

$$f(x)g'(x) = \frac{d}{dx}(f(x)g(x)) - g(x)f'(x).$$

Integrating both sides of the preceding equation gives us

$$\int f(x)g'(x) \, dx = \int \frac{d}{dx}(f(x)g(x)) \, dx - \int g(x)f'(x) \, dx.$$

By Theorem (4.5)(i), the first integral on the right side is $f(x)g(x) + C$. Because another constant of integration is obtained from the second integral, we may omit $C$ in the formula—that is,

$$\int f(x)g'(x) \, dx = f(x)g(x) - \int g(x)f'(x) \, dx.$$

Since $dv = g'(x) \, dx$ and $du = f'(x) \, dx$, we may write the preceding formula as in (7.1). $\blacksquare$

---

## Formulas

- **Integration by Parts:**

$$\int u \, dv = uv - \int v \, du$$

- **Reduction Formula for $\int \sin^n x \, dx$:**

$$\int \sin^n x \, dx = -\frac{1}{n}\cos x \sin^{n-1} x + \frac{n-1}{n}\int \sin^{n-2} x \, dx$$

---

## Concepts

When applying Formula (7.1) to an integral, we begin by letting one part of the integrand correspond to $dv$. The expression we choose for $dv$ must include the differential $dx$. After selecting $dv$, we designate the remaining part of the integrand by $u$ and then find $du$. Since this process involves splitting the integrand into two parts, the use of (7.1) is referred to as **integrating by parts**. A proper choice for $dv$ is crucial. We generally let $dv$ equal the most complicated part of the integrand that can be readily integrated.

It takes considerable practice to become proficient in making a suitable choice for $dv$.

Sometimes it is necessary to use integration by parts more than once in the same problem.

Integration by parts may sometimes be employed to obtain **reduction formulas** for integrals. We can use such formulas to write an integral involving powers of an expression in terms of integrals that involve lower powers of the expression.

---

## Examples

### Example 1

#### Problem

Evaluate $\displaystyle\int x e^{2x} \, dx$.

#### Solution

The following list contains all possible choices for $dv$:

$$dx, \quad x \, dx, \quad e^{2x} \, dx, \quad xe^{2x} \, dx$$

The most complicated of these expressions that can be readily integrated is $e^{2x} \, dx$. Thus, we let

$$dv = e^{2x} \, dx.$$

The remaining part of the integrand is $u$—that is, $u = x$. To find $v$, we integrate $dv$, obtaining $v = \frac{1}{2}e^{2x}$. Note that a constant of integration is not added at this stage of the solution. (In Exercise 51, you are asked to prove that if a constant is added to $v$, the same final result is obtained.) If $u = x$, then $du = dx$. For ease of reference, let us display these expressions as follows:

$$dv = e^{2x} \, dx \qquad u = x$$

$$v = \tfrac{1}{2}e^{2x} \qquad du = dx$$

Substituting these expressions in Formula (7.1)—that is, integrating by parts—we obtain

$$\int xe^{2x} \, dx = x\left(\tfrac{1}{2}e^{2x}\right) - \int \tfrac{1}{2}e^{2x} \, dx.$$

We may find the integral on the right side as in Section 6.4. This gives us

$$\int xe^{2x} \, dx = \tfrac{1}{2}xe^{2x} - \tfrac{1}{4}e^{2x} + C.$$

---

To illustrate, if we had chosen $dv = x \, dx$ in Example 1, then it would have been necessary to let $u = e^{2x}$, giving us

$$dv = x \, dx \qquad u = e^{2x}$$

$$v = \tfrac{1}{2}x^2 \qquad du = 2e^{2x} \, dx.$$

Integrating by parts, we obtain

$$\int xe^{2x} \, dx = \tfrac{1}{2}x^2 e^{2x} - \int x^2 e^{2x} \, dx.$$

Since the exponent associated with $x$ has increased, the integral on the right is more complicated than the given integral. This indicates that we have made an incorrect choice for $dv$.

---

### Example 2

#### Problem

Evaluate

(a) $\displaystyle\int x \sec^2 x \, dx$ $\qquad$ (b) $\displaystyle\int_0^{\pi/3} x \sec^2 x \, dx$

#### Solution

**(a)** The possible choices for $dv$ are

$$dx, \quad x \, dx, \quad \sec x \, dx, \quad x \sec x \, dx, \quad \sec^2 x \, dx, \quad x \sec^2 x \, dx.$$

The most complicated of these expressions that can be readily integrated is $\sec^2 x \, dx$. Thus, we let

$$dv = \sec^2 x \, dx \qquad u = x$$

$$v = \tan x \qquad du = dx.$$

Integrating by parts gives us

$$\int x \sec^2 x \, dx = x \tan x - \int \tan x \, dx$$

$$= x \tan x + \ln|\cos x| + C.$$

**(b)** The indefinite integral obtained in part (a) is an antiderivative of $x \sec^2 x$. Using the fundamental theorem of calculus (and dropping the constant of integration $C$), we obtain

$$\int_0^{\pi/3} x \sec^2 x \, dx = \Big[x \tan x + \ln|\cos x|\Big]_0^{\pi/3}$$

$$= \left(\frac{\pi}{3}\tan\frac{\pi}{3} + \ln\left|\cos\frac{\pi}{3}\right|\right) - (0 + \ln 1)$$

$$= \left(\frac{\pi}{3}\sqrt{3} + \ln\frac{1}{2}\right) - (0 + 0)$$

$$= \frac{\pi}{3}\sqrt{3} - \ln 2 \approx 1.12.$$

---

If, in Example 2, we had chosen $dv = x \, dx$ and $u = \sec^2 x$, then the integration by parts formula (7.1) would have led to a more complicated integral. (Verify this fact.)

---

### Example 3

#### Problem

Evaluate $\displaystyle\int \ln x \, dx$.

#### Solution

Let

$$dv = dx \qquad u = \ln x$$

$$v = x \qquad du = \frac{1}{x} \, dx$$

and integrate by parts as follows:

$$\int \ln x \, dx = (\ln x)x - \int (x)\frac{1}{x} \, dx$$

$$= x \ln x - \int dx$$

$$= x \ln x - x + C$$

---

### Example 4

#### Problem

Evaluate $\displaystyle\int x^2 e^{2x} \, dx$.

#### Solution

Let

$$dv = e^{2x} \, dx \qquad u = x^2$$

$$v = \tfrac{1}{2}e^{2x} \qquad du = 2x \, dx$$

and integrate by parts as follows:

$$\int x^2 e^{2x} \, dx = x^2\left(\tfrac{1}{2}e^{2x}\right) - \int \left(\tfrac{1}{2}e^{2x}\right)2x \, dx$$

$$= \tfrac{1}{2}x^2 e^{2x} - \int xe^{2x} \, dx$$

To evaluate the integral on the right side of the last equation, we must again integrate by parts. Proceeding exactly as in Example 1 leads to

$$\int x^2 e^{2x} \, dx = \tfrac{1}{2}x^2 e^{2x} - \tfrac{1}{2}xe^{2x} + \tfrac{1}{4}e^{2x} + C.$$

---

### Example 5

#### Problem

Evaluate $\displaystyle\int e^x \cos x \, dx$.

#### Solution

We could either let $dv = \cos x \, dx$ or let $dv = e^x \, dx$, since each of these expressions is readily integrable. Let us choose

$$dv = \cos x \, dx \qquad u = e^x$$

$$v = \sin x \qquad du = e^x \, dx$$

and integrate by parts as follows:

$$\int e^x \cos x \, dx = e^x \sin x - \int (\sin x)e^x \, dx$$

$$(1) \qquad \int e^x \cos x \, dx = e^x \sin x - \int e^x \sin x \, dx$$

We next apply integration by parts to the integral on the right side of equation (1). Since we chose a trigonometric form for $dv$ in the first integration by parts, we shall also choose a trigonometric form for the second. Letting

$$dv = \sin x \, dx \qquad u = e^x$$

$$v = -\cos x \qquad du = e^x \, dx$$

and integrating by parts, we have

$$\int e^x \sin x \, dx = e^x(-\cos x) - \int (-\cos x)e^x \, dx$$

$$(2) \qquad \int e^x \sin x \, dx = -e^x \cos x + \int e^x \cos x \, dx.$$

If we now use equation (2) to substitute on the right side of equation (1), we obtain

$$\int e^x \cos x \, dx = e^x \sin x - \left[-e^x \cos x + \int e^x \cos x \, dx\right],$$

or

$$\int e^x \cos x \, dx = e^x \sin x + e^x \cos x - \int e^x \cos x \, dx.$$

Adding $\displaystyle\int e^x \cos x \, dx$ to both sides of the last equation gives us

$$2\int e^x \cos x \, dx = e^x(\sin x + \cos x).$$

Finally, dividing both sides by 2 and adding the constant of integration yields

$$\int e^x \cos x \, dx = \tfrac{1}{2}e^x(\sin x + \cos x) + C.$$

We could have evaluated the given integral by using $dv = e^x \, dx$ for both the first and second applications of the integration by parts formula.

---

### Incorrect Substitution Warning (Example 5 continued)

We must choose substitutions carefully when evaluating an integral of the type given in Example 5. To illustrate, suppose that in the evaluation of the integral on the right in equation (1) of the solution we had used

$$dv = e^x \, dx \qquad u = \sin x$$

$$v = e^x \qquad du = \cos x \, dx.$$

Integration by parts then leads to

$$\int e^x \sin x \, dx = (\sin x)e^x - \int e^x \cos x \, dx$$

$$= e^x \sin x - \int e^x \cos x \, dx.$$

If we now substitute in equation (1), we obtain

$$\int e^x \cos x \, dx = e^x \sin x - \left[e^x \sin x - \int e^x \cos x \, dx\right],$$

which reduces to

$$\int e^x \cos x \, dx = \int e^x \cos x \, dx.$$

Although this is a true statement, it is not an evaluation of the given integral.

---

### Example 6

#### Problem

Evaluate $\displaystyle\int \sec^3 x \, dx$.

#### Solution

The possible choices for $dv$ are

$$dx, \quad \sec x \, dx, \quad \sec^2 x \, dx, \quad \sec^3 x \, dx.$$

The most complicated of these expressions that can be readily integrated is $\sec^2 x \, dx$. Thus, we let

$$dv = \sec^2 x \, dx \qquad u = \sec x$$

$$v = \tan x \qquad du = \sec x \tan x \, dx$$

and integrate by parts as follows:

$$\int \sec^3 x \, dx = \sec x \tan x - \int \sec x \tan^2 x \, dx$$

Instead of applying another integration by parts, let us change the form of the integral on the right by using the identity $1 + \tan^2 x = \sec^2 x$. This gives us

$$\int \sec^3 x \, dx = \sec x \tan x - \int \sec x(\sec^2 x - 1) \, dx,$$

or

$$\int \sec^3 x \, dx = \sec x \tan x - \int \sec^3 x \, dx + \int \sec x \, dx.$$

Adding $\displaystyle\int \sec^3 x \, dx$ to both sides of the last equation gives us

$$2\int \sec^3 x \, dx = \sec x \tan x + \int \sec x \, dx.$$

If we now evaluate $\displaystyle\int \sec x \, dx$ and divide both sides of the resulting equation by 2 (and then add the constant of integration), we obtain

$$\int \sec^3 x \, dx = \tfrac{1}{2}\sec x \tan x + \tfrac{1}{2}\ln|\sec x + \tan x| + C.$$

---

### Example 7

#### Problem

Find a reduction formula for $\displaystyle\int \sin^n x \, dx$.

#### Solution

Let

$$dv = \sin x \, dx \qquad u = \sin^{n-1} x$$

$$v = -\cos x \qquad du = (n-1)\sin^{n-2} x \cos x \, dx$$

and integrate by parts as follows:

$$\int \sin^n x \, dx = -\cos x \sin^{n-1} x + (n-1)\int \sin^{n-2} x \cos^2 x \, dx$$

Since $\cos^2 x = 1 - \sin^2 x$, we may write

$$\int \sin^n x \, dx = -\cos x \sin^{n-1} x + (n-1)\int \sin^{n-2} x \, dx - (n-1)\int \sin^n x \, dx.$$

Consequently,

$$\int \sin^n x \, dx + (n-1)\int \sin^n x \, dx = -\cos x \sin^{n-1} x + (n-1)\int \sin^{n-2} x \, dx.$$

The left side of the last equation reduces to $n\displaystyle\int \sin^n x \, dx$. Dividing both sides by $n$, we obtain

$$\int \sin^n x \, dx = -\frac{1}{n}\cos x \sin^{n-1} x + \frac{n-1}{n}\int \sin^{n-2} x \, dx.$$

---

### Example 8

#### Problem

Use the reduction formula in Example 7 to evaluate $\displaystyle\int \sin^4 x \, dx$.

#### Solution

Using the formula with $n = 4$ gives us

$$\int \sin^4 x \, dx = -\tfrac{1}{4}\cos x \sin^3 x + \tfrac{3}{4}\int \sin^2 x \, dx.$$

Applying the reduction formula, with $n = 2$, to the integral on the right, we have

$$\int \sin^2 x \, dx = -\tfrac{1}{2}\cos x \sin x + \tfrac{1}{2}\int dx = -\tfrac{1}{2}\cos x \sin x + \tfrac{1}{2}x + C.$$

Consequently,

$$\int \sin^4 x \, dx = -\tfrac{1}{4}\cos x \sin^3 x - \tfrac{3}{8}\cos x \sin x + \tfrac{3}{8}x + D$$

with $D = \frac{3}{4}C$.

---

## Remarks

- When choosing $dv$, the expression must include the differential $dx$.

- A proper choice for $dv$ is crucial. We generally let $dv$ equal the most complicated part of the integrand that can be readily integrated.

- When a constant of integration is added to $v$ after integrating $dv$, the same final result is obtained (see Exercise 51).

- If the wrong choice of $dv$ is made, the resulting integral on the right side may be more complicated than the original, indicating an incorrect choice (as shown in Example 1's alternate approach).

- When applying integration by parts twice to integrals of the form $\int e^x \cos x \, dx$ or $\int e^x \sin x \, dx$, one must be consistent: if a trigonometric form is chosen for $dv$ in the first application, a trigonometric form should also be chosen for $dv$ in the second application. Mixing choices (e.g., trigonometric for the first and exponential for the second) leads to a tautological identity that does not evaluate the integral.

- By repeated applications of the reduction formula in Example 7, we can find $\int \sin^n x \, dx$ for any positive integer $n$, because these reductions end with either $\int \sin x \, dx$ or $\int dx$, and each of these can be evaluated easily.

---

## Figures

No figures, graphs, or diagrams appear in this section.

---

## Keywords

- Integration by parts
- Product rule
- Reduction formula
- Integrating by parts
- Antiderivative
- Fundamental theorem of calculus
- Trigonometric integrals
- Exponential integrals
- Logarithmic integrals
