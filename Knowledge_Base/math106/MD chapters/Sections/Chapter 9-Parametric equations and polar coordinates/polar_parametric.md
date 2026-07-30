# ملخص الفصل التاسع (Chapter 9: Parametric & Polar Coordinates)

## 1. المعادلات البارامترية (9.1 & 9.2 Parametric Equations)
- **الميل / المشتقة الأولى:** 
  $$ \frac{dy}{dx} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}} $$
- **المشتقة الثانية:** 
  $$ \frac{d^2y}{dx^2} = \frac{\frac{d}{dt}\left(\frac{dy}{dx}\right)}{\frac{dx}{dt}} $$
- **طول القوس (Arc Length):**
  $$ L = \int_{a}^{b} \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} \, dt $$
- **مساحة السطح الدوراني (حول محور $x$):**
  $$ S = \int_{a}^{b} 2\pi y \sqrt{\left(\frac{dx}{dt}\right)^2 + \left(\frac{dy}{dt}\right)^2} \, dt $$

## 2. الإحداثيات القطبية (9.3 & 9.4 Polar Coordinates)
- **القوانين الأساسية للتحويل:**
  $$ x = r \cos \theta, \quad y = r \sin \theta $$
  $$ r^2 = x^2 + y^2, \quad \tan \theta = \frac{y}{x} $$
- **ميل المماس في القطبي:**
  $$ \frac{dy}{dx} = \frac{r' \sin \theta + r \cos \theta}{r' \cos \theta - r \sin \theta} $$
- **المساحة في القطبي (Polar Area):**
  $$ A = \frac{1}{2} \int_{\alpha}^{\beta} [r(\theta)]^2 \, d\theta $$
- **طول القوس في القطبي (Polar Arc Length):**
  $$ L = \int_{\alpha}^{\beta} \sqrt{r^2 + (r')^2} \, d\theta $$