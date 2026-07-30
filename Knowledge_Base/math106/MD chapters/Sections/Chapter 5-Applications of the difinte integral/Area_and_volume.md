# دليل تطبيقات التكامل (Chapter 5: Area, Volume, Surface Area)

## 5.1 المساحة بين منحنيين (Area between curves)
- **باستخدام شرائح رأسية ($dx$):** 
  $$ A = \int_{a}^{b} [\text{Top}(x) - \text{Bottom}(x)] \, dx $$
- **باستخدام شرائح أفقية ($dy$):** 
  $$ A = \int_{c}^{d} [\text{Right}(y) - \text{Left}(y)] \, dy $$

## 5.2 و 5.3 الحجوم الدورانية (Volumes: Disk/Washer vs Shell)
**كيف تختار الطريقة؟** القاعدة تعتمد على (محور الدوران) والتكامل بالنسبة لـ ($dx$ أو $dy$):

1. **الدوران حول محور $x$ (أو خط أفقي $y = \text{constant}$):**
   - نستخدم **Disk/Washer** إذا كاملنا بالنسبة لـ $dx$:
     $$ V = \pi \int [(\text{Outer Radius})^2 - (\text{Inner Radius})^2] \, dx $$
   - نستخدم **Shell** إذا كاملنا بالنسبة لـ $dy$:
     $$ V = 2\pi \int (\text{radius}) \cdot (\text{height}) \, dy $$

2. **الدوران حول محور $y$ (أو خط عمودي $x = \text{constant}$):**
   - نستخدم **Disk/Washer** إذا كاملنا بالنسبة لـ $dy$.
   - نستخدم **Shell** إذا كاملنا بالنسبة لـ $dx$.

> **ملاحظات لنصف القطر (radius):**
> - هو المسافة العمودية بين محور الدوران والمنحنى.
> - الدوران حول خط $y = k$ (أفقي): نصف القطر يكون $|y - k|$ أو $|f(x) - k|$.
> - الدوران حول خط $x = k$ (عمودي): نصف القطر يكون $|x - k|$ أو $|f(y) - k|$.

## 5.5 طول القوس ومساحة السطح (Arc Length & Surface Area)
- **طول القوس ($L$):**
  $$ L = \int_{a}^{b} \sqrt{1 + (f'(x))^2} \, dx $$

- **مساحة السطح الدوراني ($S$):**
  $$ S = \int_{a}^{b} 2\pi (\text{radius}) \sqrt{1 + (f'(x))^2} \, dx $$
  
  **تحديد الـ (radius) في مساحة السطح:**
  - الدوران حول محور $x \rightarrow \text{radius} = y$ (أي $f(x)$)
  - الدوران حول محور $y \rightarrow \text{radius} = x$
  - الدوران حول خط $y = k \rightarrow \text{radius} = |f(x) - k|$