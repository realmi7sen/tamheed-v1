# ملخص الفصل السادس (Chapter 6: Transcendental Functions & L'Hopital)

## 1. الدوال اللوغاريتمية والأسية (6.2 - 6.5)
- **اللوغاريتم الطبيعي:**
  $$ \frac{d}{dx} (\ln|x|) = \frac{1}{x} \quad \implies \quad \int \frac{1}{x} \, dx = \ln|x| + C $$
- **الدالة الأسية الطبيعية:**
  $$ \frac{d}{dx} (e^x) = e^x \quad \implies \quad \int e^x \, dx = e^x + C $$
- **الدالة الأسية العامة:**
  $$ \frac{d}{dx} (a^x) = a^x \ln(a) \quad \implies \quad \int a^x \, dx = \frac{a^x}{\ln(a)} + C $$
- **قاعدة اللوغاريتم في التكامل:** 
  $$ \int \frac{f'(x)}{f(x)} \, dx = \ln|f(x)| + C $$

## 2. الدوال المثلثية العكسية (6.7)
- $$ \int \frac{1}{\sqrt{a^2 - x^2}} \, dx = \arcsin\left(\frac{x}{a}\right) + C $$
- $$ \int \frac{1}{a^2 + x^2} \, dx = \frac{1}{a} \arctan\left(\frac{x}{a}\right) + C $$
- $$ \int \frac{1}{x \sqrt{x^2 - a^2}} \, dx = \frac{1}{a} \text{arcsec}\left(\frac{x}{a}\right) + C $$

## 3. الدوال الزائدية (Hyperbolic Functions 6.8)
- $$ \frac{d}{dx} (\sinh x) = \cosh x \quad \implies \quad \int \cosh x \, dx = \sinh x + C $$
- $$ \frac{d}{dx} (\cosh x) = \sinh x \quad \implies \quad \int \sinh x \, dx = \cosh x + C $$
- $$ \frac{d}{dx} (\tanh x) = \text{sech}^2 x \quad \implies \quad \int \text{sech}^2 x \, dx = \tanh x + C $$
- **المتطابقة الأساسية:** 
  $$ \cosh^2(x) - \sinh^2(x) = 1 $$

## 4. قاعدة لوبيتال (L'Hopital's Rule 6.9)
**متى نستخدمها؟** إذا كانت النهاية تعطي حالة عدم تعيين (Indeterminate form) مثل $\frac{0}{0}$ أو $\frac{\infty}{\infty}$.
- **القاعدة:** نشتق البسط لوحده، ونشتق المقام لوحده، ثم نعوض مرة أخرى:
  $$ \lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)} $$
> **ملاحظة:** إذا ظهرت حالات مثل $0 \cdot \infty$ أو $\infty - \infty$، يجب تبسيطها جبرياً أولاً إلى كسر $\frac{0}{0}$ أو $\frac{\infty}{\infty}$ قبل استخدام القاعدة.