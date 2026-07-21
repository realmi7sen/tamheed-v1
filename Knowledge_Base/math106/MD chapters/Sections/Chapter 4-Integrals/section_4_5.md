---
source_file: "Section_4.5_Properties_of_the_Definite_Integral.pdf"[cite: 6]
course: MATH106
book_chapter: 4
book_section: 4.5
ksu_chapter: UNKNOWN
section_title: PROPERTIES OF THE DEFINITE INTEGRAL
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: [7, 10, 11, 15, 17, 22, 23, 25, 29, 34]
topic_tags: [definite-integral, properties-of-integrals, mean-value-theorem, average-value]
difficulty: UNKNOWN
in_syllabus: true
enrichment: UNKNOWN
status: draft
---

# PROPERTIES OF THE DEFINITE INTEGRAL

## Metadata
**Course:** MATH106
**Book:** Calculus (Swokowski)
**Edition:** 6th
**Chapter Number:** 4
**Chapter Title:** Integrals
**Section Number:** 4.5
**Section Title:** PROPERTIES OF THE DEFINITE INTEGRAL

## Definitions
**Definition 4.29**
Let f be continuous on $[a,b]$. The average value $f_{av}$ of f on $[a,b]$ is
$$f_{av}=\frac{1}{b-a}\int_{a}^{b}f(x)dx.$$

## Theorems
**Theorem 4.21**
If c is a real number, then
$$\int_{a}^{b}c~dx=c(b-a).$$

**Theorem 4.22**
If f is integrable on $[a,b]$ and c is any real number, then cf is integrable on $[a,b]$ and
$$\int_{a}^{b}cf(x)dx=c\int_{a}^{b}f(x)dx.$$

**Theorem 4.23**
If f and g are integrable on $[a,b]$ then $f+g$ and $f-g$ are integrable on $[a,b]$ and
(i) $\int_{a}^{b}[f(x)+g(x)]dx=\int_{a}^{b}f(x)dx+\int_{a}^{b}g(x)dx$
(ii) $\int_{a}^{b}[f(x)-g(x)]dx=\int_{a}^{b}f(x)dx-\int_{a}^{b}g(x)dx$

**Theorem 4.24**
If $a<c<b$ and if f is integrable on both $[a,c]$ and $[c,b],$ then f is integrable on $[a,b]$ and
$$\int_{a}^{b}f(x)dx=\int_{a}^{c}f(x)dx+\int_{c}^{b}f(x)dx$$

**Theorem 4.25**
If f is integrable on a closed interval and if a, b, and c are any three numbers in the interval, then
$$\int_{a}^{b}f(x)dx=\int_{a}^{c}f(x)dx+\int_{c}^{b}f(x)dx.$$

**Theorem 4.26**
If f is integrable on $[a,b]$ and $f(x)\ge0$ for every x in $[a,b]$, then
$$\int_{a}^{b}f(x)dx\ge0.$$

**Corollary 4.27**
If f and g are integrable on $[a,b]$ and $f(x)\ge g(x)$ for every x in $[a,b],$ then
$$\int_{a}^{b}f(x)dx\ge\int_{a}^{b}g(x)dx.$$

**Mean Value Theorem for Definite Integrals 4.28**
If f is continuous on a closed interval $[a,b]$, then there is a number z in the open interval $(a,b)$ such that
$$\int_{a}^{b}f(x)dx=f(z)(b-a).$$

## Formulas
No formal boxed formulas distinct from Theorems and Definitions.

## Guidelines / Methods
No numbered guideline lists or method tables.

## Worked Examples
### Example 1
Evaluate $\int_{-2}^{3}7dx$
**Solution**
Using Theorem (4.21) yields
$$\int_{-2}^{3}7dx=7[3-(-2)]=7(5)=35$$

### Example 2
It will follow from the results in Section 4.6 that $\int_{0}^{2}x^{3}dx=4$ and $\int_{0}^{2}x~dx=2.$ Use these facts to evaluate $\int_{0}^{2}(5x^{3}-3x+6)dx$.
**Solution**
We may proceed as follows:
$$\int_{0}^{2}(5x^{3}-3x+6)dx=\int_{0}^{2}5x^{3}dx-\int_{0}^{2}3x~dx+\int_{0}^{2}6~dx$$
$$=5\int_{0}^{2}x^{3}dx-3\int_{0}^{2}x~dx+6(2-0)$$
$$=5(4)-3(2)+12=26$$

### Example 3
Express as one integral:
$$\int_{2}^{7}f(x)dx-\int_{5}^{7}f(x)dx$$
**Solution**
First we interchange the limits of the second integral using Definition (4.17) and then use Theorem (4.25) with $a=2$, $b=5,$ and $c=7$
$$\int_{2}^{7}f(x)dx-\int_{5}^{7}f(x)dx=\int_{2}^{7}f(x)dx+\int_{7}^{5}f(x)dx$$
$$=\int_{2}^{5}f(x)dx$$
As an alternative solution, by recognizing that
$$\int_{2}^{7}f(x)dx=\int_{2}^{5}f(x)dx+\int_{5}^{7}f(x)dx$$
the previous result immediately follows.

### Example 4
Show that $\int_{-1}^{2}(x^{2}+2)dx\ge\int_{-1}^{2}(x-1)dx.$
**Solution**
Since
$$x^{2}+2\ge x-1$$
for every x in $[-1,2]$, the conclusion follows from Corollary (4.27).

### Example 5
It will follow from the results of Section 4.6 that $\int_{0}^{3}x^{2}dx=9$ Find a number z that satisfies the conclusion of the mean value theorem (4.28) for this definite integral.
**Solution**
By the mean value theorem, there is a number z between 0 and 3 such that
$$\int_{0}^{3}x^{2}dx=f(z)(3-0)=z^{2}(3).$$
This result implies that
$$9=3z^{2} \quad \text{or} \quad z^{2}=3.$$
The solutions of the last equation are $z=\pm\sqrt{3};$ however, $-\sqrt{3}$ is not in $[0,3]$ The number $z=\sqrt{3}$ satisfies the conclusion of the theorem.

### Example 6
Given $\int_{0}^{3}x^{2}dx=9,$ find the average value of f on $[0,3]$
**Solution**
By Definition (4.29), with $a=0$, $b=3$ and $f(x)=x^{2}$
$$f_{av}=\frac{1}{3-0}\int_{0}^{3}x^{2}dx=\frac{1}{3}\cdot9=3$$ .
In the interval $[0,3]$, the function values $f(x)=x^{2}$ range from $f(0)=0$ to $f(3)=9$ Note that the function f takes on its average value 3 at the number $z=\sqrt{3}$

## Exercises
*   7. UNREADABLE (Exercise not included in provided source document)
*   10. UNREADABLE (Exercise not included in provided source document)
*   11. UNREADABLE (Exercise not included in provided source document)
*   15. UNREADABLE (Exercise not included in provided source document)
*   17. UNREADABLE (Exercise not included in provided source document)
*   22. UNREADABLE (Exercise not included in provided source document)
*   23. UNREADABLE (Exercise not included in provided source document)
*   25. UNREADABLE (Exercise not included in provided source document)
*   29. UNREADABLE (Exercise not included in provided source document)
*   34. UNREADABLE (Exercise not included in provided source document)