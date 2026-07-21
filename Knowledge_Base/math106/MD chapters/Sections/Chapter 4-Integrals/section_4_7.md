---
source_file: "Section_4.7_Numerical_Integration.pdf"
course: MATH106
book_chapter: 4
book_section: 4.7
ksu_chapter: UNKNOWN
section_title: NUMERICAL INTEGRATION
doc_type: section_reference
assessment: UNKNOWN
selected_exercises: [15, 16, 17, 18, 33, 34]
topic_tags: [numerical-integration, rectangle-rules, trapezoidal-rule, simpson's-rule, error-estimates]
difficulty: UNKNOWN
in_syllabus: true
enrichment: UNKNOWN
status: draft
---

# NUMERICAL INTEGRATION

## Metadata
**Course:** MATH106
**Book:** Calculus (Swokowski)
**Edition:** 6th
**Chapter Number:** 4
**Chapter Title:** Integrals
**Section Number:** 4.7
**Section Title:** NUMERICAL INTEGRATION

## Definitions
No formal boxed definitions.

## Theorems
**Theorem 4.39**
Let $I=\int_{a}^{b}f(x)dx$ be the definite integral being approximated. If $f^{\prime}$ is continuous and if $K_{1}$ is a positive number such that $|f^{\prime}(x)|\le K_{1}$ for every x in $[a,b]$ then the error estimates for the left rectangle rule $L_{n}$ and the right rectangle rule $R_{n}$ are given by
$$|I-L_{n}|\le K_{1}\frac{(b-a)^{2}}{2n} \quad \text{and} \quad |I-R_{n}|\le K_{1}\frac{(b-a)^{2}}{2n}.$$
If $f^{\prime\prime}$ is continuous and if $K_{2}$ is a positive real number such that $|f^{\prime\prime}(x)|\le K_{2}$ for every x in $[a,b]$, then the error estimates for the midpoint rule $M_{n}$ and the trapezoidal rule $T_{n}$ are given by
$$|I-M_{n}|\le K_{2}\frac{(b-a)^{3}}{24n^{2}} \quad \text{and} \quad |I-T_{n}|\le K_{2}\frac{(b-a)^{3}}{12n^{2}}.$$
If $f^{(4)}$ is continuous and if $K_{4}$ is a positive real number such that $|f^{(4)}(x)|\le K_{4}$ for every x in $[a,b]$, then the error estimate for Simpson's rule $S_{n}$ is given by
$$|I-S_{n}|\le K_{4}\frac{(b-a)^{5}}{2880n^{4}}$$

## Formulas
**Rectangle Rules 4.36**
For a regular partition of an interval $[a,b]$ with n subintervals, each of width $\Delta x=(b-a)/n$, the definite integral $\int_{a}^{b}f(x)dx$ is approximated by
(i) the left rectangle rule:
$$L_{n}=\sum_{k=1}^{n}f(x_{k-1})\Delta x$$
(ii) the right rectangle rule:
$$R_{n}=\sum_{k=1}^{n}f(x_{k})\Delta x$$
(iii) the midpoint rule:
$$M_{n}=\sum_{k=1}^{n}f(x_{k-1/2})\Delta x$$

**Trapezoidal Rule 4.37**
For a regular partition of an interval $[a,b]$ with n subintervals, each of width $\Delta x=(b-a)/n$ the definite integral $\int_{a}^{b}f(x)dx$ is approximated by the trapezoidal rule:
$$T_{n}=\frac{1}{2}(L_{n}+R_{n})=\sum_{k=1}^{n}\frac{1}{2}[f(x_{k-1})+f(x_{k})]\Delta x$$
$$=\frac{b-a}{2n}[f(x_{0})+2f(x_{1})+2f(x_{2})+\cdot\cdot\cdot+2f(x_{n-1})+f(x_{n})]$$

**Simpson's Rule 4.38**
For a regular partition of an interval $[a,b]$ with n subintervals, each of width $\Delta x=(b-a)/n$ the definite integral $\int_{a}^{b}f(x)dx$ is approximated by Simpson's rule:
$$S_{n}=\frac{1}{3}(2M_{n}+T_{n})$$
$$=\frac{b-a}{6n}[f(x_{0})+4f(x_{1/2})+2f(x_{1})+4f(x_{3/2})$$
$$+2f(x_{2})+\cdot\cdot\cdot+2f(x_{n-1})+4f(x_{n-1/2})+f(x_{n})]$$

## Guidelines / Methods
No numbered guideline lists or method tables.

## Worked Examples
### Example 1
Approximate $\int_{1}^{2}1/x~dx$ using a regular partition with $n=4$ using
(a) the midpoint rule $M_{n}$
(b) the left rectangle rule $L_{n}$
(c) the right rectangle rule $R_{n}$
**Solution**
With $n=4$, we have $\Delta x=(b-a)/n=(2-1)/4=1/4,$ and the function f is given by $f(x)=1/x$. The endpoints of the subintervals are $x_{0}=1$, $x_{1}=\frac{5}{4}$, $x_{2}=\frac{3}{2}$, $x_{3}=\frac{7}{4}$, and $x_{4}=2$.
(a) The midpoints are $x_{1/2}=\frac{9}{8}$, $x_{3/2}=\frac{11}{8}$, $x_{5/2}=\frac{13}{8}$, and $x_{7/2}=\frac{15}{8}$. By (4.36)(iii), we obtain
$$\int_{a}^{b}f(x)dx=\int_{1}^{2}\frac{1}{x}dx\approx M_{4}=\sum_{k=1}^{4}f(x_{k-1/2})\Delta x$$
$$=\sum_{k=1}^{4}(\frac{1}{x_{k-1/2}})(\frac{1}{4})$$
$$=\frac{1}{4}\sum_{k=1}^{4}(\frac{1}{x_{k-1/2}})$$
$$=\frac{1}{4}(\frac{8}{9}+\frac{8}{11}+\frac{8}{13}+\frac{8}{15})=\frac{448}{6435}$$
$$\approx0.6912198912.$$
(b) The left-hand endpoints are 1, $\frac{5}{4}$, $\frac{3}{2}$, and $\frac{7}{4}$. By (4.36)(i),
$$\int_{1}^{2}\frac{1}{x}dx\approx L_{4}=\frac{1}{4}(1+\frac{4}{5}+\frac{2}{3}+\frac{4}{7})=\frac{319}{420}$$
$$\approx0.7595238095.$$
(c) The right-hand endpoints are $\frac{5}{4}$, $\frac{3}{2}$, $\frac{7}{4}$, and 2. By (4.36)(ii),
$$\int_{1}^{2}\frac{1}{x}dx\approx R_{4}=\frac{1}{4}(\frac{4}{5}+\frac{2}{3}+\frac{4}{7}+\frac{1}{2})$$
$$=\frac{533}{840}\approx0.6345238095$$

### Example 2
Approximate $\int_{1}^{2}1/x~dx$ using a regular partition with $n=4$, using the trapezoidal rule $T_{n}$.
**Solution**
With the results of Example 1, we have
$$T_{4}=\frac{1}{2}(L_{4}+R_{4})$$
$$=\frac{1}{2}(0.7595238095+0.6345238095)$$
$$=0.6970238095$$
Alternatively, we can compute $T_{4}$ directly from the last form of the trapezoidal rule in (4.37):
$$T_{n}=\frac{2-1}{2(4)}[f(1)+2f(\frac{5}{4})+2f(\frac{3}{2})+2f(\frac{7}{4})+f(2)]$$
$$=\frac{1}{8}[1+2(\frac{4}{5})+2(\frac{2}{3})+2(\frac{4}{7})+(\frac{1}{2})]$$
$$=\frac{1}{8}(1+\frac{8}{5}+\frac{4}{3}+\frac{8}{7}+\frac{1}{2})$$
$$=\frac{1}{8}(\frac{1171}{210})=\frac{1171}{1680}\approx0.6970238095$$

### Example 3
Approximate $\int_{1}^{2}1/x~dx$ using a regular partition with $n=4,$ using Simpson's rule $S_{n}$...
**Solution**
Using the results of Examples 1 and 2, we have
$$S_{4}=\frac{1}{3}(2M_{4}+T_{4})$$
$$\approx\frac{1}{3}[2(0.6912198912)+0.6970238095]\approx0.6931545306.$$
Alternatively, we can compute $S_{4}$ directly from the last form of Simpson's rule in (4.38):
$$S_{4}=\frac{2-1}{6(4)}[f(1)+4f(\frac{9}{8})+2f(\frac{5}{4})+4f(\frac{11}{8})+2f(\frac{3}{2})$$
$$+4f(\frac{13}{8})+2f(\frac{7}{4})+4f(\frac{15}{8})+f(2)]$$
$$=\frac{1}{24}(1+\frac{32}{9}+\frac{8}{5}+\frac{32}{11}+\frac{4}{3}+\frac{32}{13}+\frac{8}{7}+\frac{32}{15}+\frac{1}{2})$$
$$=\frac{1}{24}(\frac{35,969,064}{2,162,160})=(\frac{1,498,711}{2,162,160})\approx0.6931545307$$

### Example 4
Aerial surveys of a tract of the Green Mountain National Forest shown in Figure 4.38 measured the width of the forest (in miles) at regularly spaced intervals, $\frac{3}{10}$ mi apart. The gathered data are shown in the following table.
| x | 2.0 | 2.3 | 2.6 | 2.9 | 3.2 | 3.5 | 3.8 | 4.1 | 4.4 | 4.7 | 5.0 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| y | 9.14 | 11.82 | 13.41 | 13.72 | 12.87 | 11.27 | 9.42 | 7.81 | 6.78 | 6.49 | 6.88 |
The Forest Service estimates that, on average, there are 125 mature trees per acre. Approximate the total number of mature trees in this tract of the forest using the rules of numerical integration.
**Solution**
We use the data in the table and consider the forest area as the definite integral of the function $y=f(x)$ over the interval $[2.0, 5.0]$. For the left and right rectangle rules and for the trapezoidal rule, we can choose $n=10$ and $\Delta x=(5.0-2.0)/10=0.3$
$$R_{10}=(0.3)[\sum_{k=1}^{9}f(x_{k})+f(x_{10})]$$
$$=(0.3)[(11.82+13.41+13.72+12.87+11.27+9.42+7.81+6.78+6.49)+6.88]$$
$$=(0.3)(93.59+6.88)=30.141$$
and
$$L_{10}=R_{10}+\Delta x[f(a)-f(b)]$$
$$=30.141+(0.3)(9.14-6.88)=30.819,$$
so that
$$T_{10}=\frac{1}{2}(L_{10}+R_{10})=30.48$$
For the midpoint rule and Simpson's rule, we consider every other x-value as a midpoint so that $n=5$ and $\Delta x=0.6$ Then we compute
$$L_{5}=(9.14+13.41+12.87+9.42+6.78)(0.6)=30.972,$$
$$R_{5}=(13.41+12.87+9.42+6.78+6.88)(0.6)=29.616,$$
$$M_{5}=(11.82+13.72+11.27+7.81+6.49)(0.6)=30.666,$$
$$T_{5}=(L_{5}+R_{5})/2=30.294$$
and
$$S_{5}=(2M_{5}+T_{5})/3=30.542.$$
From these figures, we estimate the tract of forest to be about 30.5 mi². Since there are 640 acres in a square mile, the forest is about 19,520 acres in extent. With an average of 125 trees per acre, the forest contains approximately $(19,520)(125)=2,440,000$ mature trees.

### Example 5
Use the numerical integration rules to approximate the definite integral $\int_{0}^{1}[4/(1+x^{2})]dx$ for $n=2,6,18,54,$ and 162.
**Solution**
The following table displays the results of running the computer program:
| n | $L_{n}$ | $R_{n}$ | $M_{n}$ | $T_{n}$ | $S_{n}$ |
|---|---|---|---|---|---|
| 2 | 3.6 | 2.6 | 3.16235294118 | 3.1 | 3.14156862745 |
| 6 | 3.30362973314 | 2.9702963998 | 3.14390742722 | 3.13696306647 | 3.14159264031 |
| 18 | 3.19663380591 | 3.08552269480 | 3.14184985518 | 3.14107825036 | 3.14159265357 |
| 54 | 3.16005401619 | 3.12301697915 | 3.14162123155 | 3.14153549767 | 3.14159265359 |
| 162 | 3.14775914244 | 3.13541346343 | 3.14159582892 | 3.14158630293 | 3.14159265359 |

### Example 6
The definite integral $\int_{0}^{1}[4/(1+x^{2})]dx$ has a value of $\pi$.
(a) Using the results of Example 5, compute the errors for each approximation by finding the difference between $\pi$ and the approximation.
(b) Investigate the ratios of error for each successive pair of values for n.
**Solution**
(a) The following table lists the results.
| n | $L_{n}$ | $R_{n}$ | $M_{n}$ | $T_{n}$ | $S_{n}$ |
|---|---|---|---|---|---|
| 2 | $-4.584~E-1$ | $5.416~E-1$ | $-2.076~E-2$ | $4.159~E-2$ | $2.403~E-5$ |
| 6 | $-1.620~E-1$ | $1.713~E-1$ | $-2.315~E-3$ | $4.630~E-3$ | $1.328~E-8$ |
| 18 | $-5.504~E-2$ | $5.607~E-2$ | $-2.572~E-4$ | $5.144~E-4$ | $1.82~E-11$ |
| 54 | $-1.846~E-2$ | $1.858~E-2$ | $-2.858~E-5$ | $5.716~E-5$ | $3~E-13$ |
| 162 | $-6.166~E-3$ | $6.179~E-3$ | $-3.175~E-6$ | $6.351~E-6$ | $1~E-13$ |
(b) The next table shows the ratio of a column entry and the entry below it.
| $n,n+1$ | $L_{n}/L_{n+1}$ | $R_{n}/R_{n+1}$ | $M_{n}/M_{n+1}$ | $T_{n}/T_{n+1}$ | $S_{n}/S_{n+1}$ |
|---|---|---|---|---|---|
| 2, 6 | 2.83 | 3.16 | 8.97 | 8.98 | 1809 |
| 6, 18 | 2.94 | 3.06 | 9.00 | 9.00 | 729.7 |
| 18, 54 | 2.98 | 3.02 | 9.00 | 9.00 | 60.7 |
| 54, 162 | 2.99 | 3.01 | 9.00 | 9.00 | 3 |

### Example 7
Determine how large n must be in order to use the trapezoidal rule to approximate $I=\int_{1}^{3}1/x~dx$ with an error less than $10^{-3}$,
**Solution**
From Theorem (4.39), we have
$$|I-T_{n}|\le K_{2}\frac{(3-1)^{3}}{12n^{2}}=\frac{2K_{2}}{3n^{2}},$$
where $K_{2}$ is a bound on the absolute value of the second derivative of $f(x)=1/x$ on the interval $[1,3]$ Since $f^{\prime\prime}(x)=2/x^{3}$ is positive and decreasing on $[1,3]$, its maximum value is $f^{\prime\prime}(1)=2$ Therefore, we have
$|I-T_{n}|\le4/(3n^{2})$ To ensure that the error is less than $10^{-3}$, we must choose n so that
$$\frac{4}{3n^{2}}<10^{-3},$$
which is equivalent to
$$n^{2}>\frac{4000}{3} \quad \text{or} \quad n>\sqrt{\frac{4000}{3}}\approx36.5$$
Hence we should choose n to be at least 37 in order to guarantee an error less than $10^{-3}$

### Example 8
(a) Use Simpson's rule to approximate the definite integral $\int_{1}^{12}1/x~dx$ for $n=5,10,20,40$, and 80.
(b) Discuss the expected accuracy of the final result.
**Solution**
(a) We use Simpson's rule (4.38) for the integrand $f(x)=1/x$; and display the results in a table:
| n | $S_{n}$ |
|---|---|
| 5 | 2.50179046384 |
| 10 | 2.48685897261 |
| 20 | 2.48507069664 |
| 40 | 2.48491806727 |
| 80 | 2.48490738622 |
(b) Each time we double n, the error estimation in (4.39) predicts that the error in Simpson's rule will be divided by $2^{4}=16$, which means that we will add at least one correct decimal digit each time we double n. Thus, the estimate
$$\int_{1}^{12}\frac{1}{x}dx\approx2.4849$$
is correct to at least four decimal places. For the function $f(x)=1/x$ we can easily find $f^{(4)}(x)=24x^{-5}$ The largest value for this positive decreasing function on the interval $[1,12]$ is $f^{(4)}(1)=24$ Using the formal error estimate in (4.39) yields
$$|I-S_{80}|\le24\frac{(12-1)^{5}}{2880(80)^{4}}\approx3.28\times10^{-5}$$

## Exercises
*   15. (a) Approximate the definite integral using the indicated rule for the given values of n. (b) On the basis of the pattern of values, determine the expected accuracy for the approximation corresponding to the largest n. $\int_{1}^{3}\sqrt{1+x^{3}}dx;$ trapezoidal rule for $n=5,10,20$, and 40
*   16. (a) Approximate the definite integral using the indicated rule for the given values of n. (b) On the basis of the pattern of values, determine the expected accuracy for the approximation corresponding to the largest n. $\int_{0}^{5}2^{-x^{2}}dx;$ trapezoidal rule for $n=2,8,32,$ and 128
*   17. (a) Approximate the definite integral using the indicated rule for the given values of n. (b) On the basis of the pattern of values, determine the expected accuracy for the approximation corresponding to the largest n. $\int_{0}^{\pi}cos(sin~x)dx;$ Simpson's rule for $n=2,6,18,$ and 54
*   18. (a) Approximate the definite integral using the indicated rule for the given values of n. (b) On the basis of the pattern of values, determine the expected accuracy for the approximation corresponding to the largest n. $\int_{0}^{4}\frac{1}{1+x^{3}}dx;$ Simpson's rule for $n=8,16,32,$ and 64
*   33. Use Simpson's rule, with $n=4,$ to approximate the average value of f on the given interval. $f(x)=\frac{1}{x^{4}+1};$ $[0,4]$
*   34. Use Simpson's rule, with $n=4,$ to approximate the average value of f on the given interval. $f(x)=\sqrt{cos~x};$ $[-1,1]$