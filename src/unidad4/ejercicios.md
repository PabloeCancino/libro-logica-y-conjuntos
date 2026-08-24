# Ejercicios de la Unidad 4

---

## 📝 Bloque A: Métodos de Demostración Formal

1. Demuestre por **prueba directa** que si \\(a, b \in \mathbb{Z}\\) son enteros impares, entonces su producto \\(a \cdot b\\) es un entero impar.

2. Demuestre por **contraposición** que si \\(3n + 2\\) es un número entero impar, entonces \\(n\\) es un número entero impar.

3. Demuestre por **reducción al absurdo** (contradicción) que \\(\log\_2(3)\\) es un número irracional.

4. Demuestre por **casos exhaustivos** que para todo entero \\(n \in \mathbb{Z}\\), el número \\(n^3 - n\\) es divisible por 3.

---

## 📝 Bloque B: Principio de Inducción Matemática

5. Demuestre por inducción matemática que para todo \\(n \ge 1\\):
   - a) \\(\sum\_{i=1}^n i^2 = 1^2 + 2^2 + \dots + n^2 = \frac{n(n+1)(2n+1)}{6}\\)
   - b) \\(\sum\_{i=1}^n i^3 = 1^3 + 2^3 + \dots + n^3 = \left[\frac{n(n+1)}{2}\right]^2\\)
   - c) \\(\sum\_{i=0}^n 2^i = 1 + 2 + 4 + \dots + 2^n = 2^{n+1} - 1\\)
   - d) \\(n^3 + 2n\\) es divisible por 3 para todo \\(n \in \mathbb{N}\\).
   - e) \\(2^n > n^2\\) para todo entero \\(n \ge 5\\).

---

## 📝 Bloque C: Relaciones de Equivalencia y de Orden

6. Sea \\(R\\) la relación sobre \\(\mathbb{Z} \times (\mathbb{Z} \setminus \{0\})\\) definida por:

\\[
(a, b) \, R \, (c, d) \;\iff\; a \cdot d = b \cdot c
\\]

   - a) Demuestre que \\(R\\) es una relación de equivalencia (Propiedades Reflexiva, Simétrica y Transitiva).
   - b) Describa la clase de equivalencia \\([(1, 2)]\\). ¿Qué conjunto numérico fundamental se construye mediante este conjunto cociente?

7. Sea \\(A = \{1, 2, 3, 4, 6, 12\}\\) ordenado mediante la relación de divisibilidad \\(a \mid b\\).
   - a) Dibuje el diagrama de Hasse correspondiente.
   - b) Identifique los elementos minimales, maximales, el mínimo y el máximo de \\(A\\) (si existen).

---

## 📝 Bloque D: Funciones y Cardinalidad Infinita

8. Para cada una de las siguientes funciones, determine si es inyectiva, sobreyectiva o biyectiva. Si es biyectiva, determine su función inversa \\(f^{-1}\\):
   - a) \\(f: \mathbb{R} \to \mathbb{R}\\), \\(f(x) = 3x - 5\\)
   - b) \\(g: \mathbb{R} \to \mathbb{R}\\), \\(g(x) = x^2 - 1\\)
   - c) \\(h: [0, \infty) \to [0, \infty)\\), \\(h(x) = x^2\\)
   - d) \\(k: \mathbb{Z} \to \mathbb{N}\\), dada por \\(k(n) = 2n\\) si \\(n > 0\\), y \\(k(n) = 2(-n) + 1\\) si \\(n \le 0\\).

9. Demuestre el **Teorema de Cantor**: Para todo conjunto \\(A\\), no existe ninguna función sobreyectiva \\(f: A \to \mathcal{P}(A)\\).  
*(Sugerencia: Considere el conjunto diagonal \\(D = \{x \in A \mid x \notin f(x)\} \in \mathcal{P}(A)\\) y suponga que existe \\(d \in A\\) tal que \\(f(d) = D\\))*.

---

## 💡 Soluciones y Guías Seleccionadas

> **Solución al Ejercicio 3 (Irracionalidad de \\(\log\_2(3)\\)):**  
> Supongamos por contradicción que \\(\log\_2(3) \in \mathbb{Q}\\).  
> Como \\(3 > 1\\) y \\(2 > 1\\), \\(\log\_2(3) > 0\\). Por tanto existen enteros positivos \\(p, q \in \mathbb{N}\\) tales que:  
> \\[
> \log_2(3) \;=\; \frac{p}{q}
> \\]  
> Por la definición de logaritmo:  
> \\[
> 2^{p/q} = 3 \implies 2^p = 3^q
> \\]  
> Como \\(p \ge 1\\), el miembro izquierdo \\(2^p\\) es un número entero **par**.  
> Como \\(q \ge 1\\), el miembro derecho \\(3^q\\) es producto de impares y por ende es un número **impar**.  
> Esto genera la contradicción lógica \\(\text{par} = \text{impar}\\) (\\(\bot\\)).  
> Por lo tanto, \\(\log\_2(3)\\) es un número **irracional**. \\(\blacksquare\\)

> **Solución al Ejercicio 9 (Teorema de Cantor):**  
> Sea \\(f: A \to \mathcal{P}(A)\\) una función arbitraria.  
> Definamos el conjunto \\(D = \{x \in A \mid x \notin f(x)\}\\). Claramente \\(D \subseteq A\\), luego \\(D \in \mathcal{P}(A)\\).  
> Supongamos por reducción al absurdo que \\(f\\) es sobreyectiva.  
> Entonces debe existir un elemento \\(d \in A\\) tal que \\(f(d) = D\\).  
> Analicemos si \\(d \in D\\):  
> * Si \\(d \in D\\), por la definición de \\(D\\) se tiene que \\(d \notin f(d) = D\\) (Contradicción).  
> * Si \\(d \notin D\\), entonces \\(d \notin f(d)\\), por lo que \\(d\\) cumple la condición para pertenecer a \\(D\\), es decir, \\(d \in D\\) (Contradicción).  
> En ambos casos se arriba a \\(d \in D \iff d \notin D\\) (\\(\bot\\)).  
> Por tanto, \\(f\\) no puede ser sobreyectiva, demostrando que \\(|A| < |\mathcal{P}(A)|\\) para todo conjunto \\(A\\). \\(\blacksquare\\)