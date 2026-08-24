# 4.2 Prueba por Contradicción, por Casos, Existencia y Unicidad

Continuando con las técnicas formales de demostración matemática, abordamos los métodos de reducción al absurdo, el método por casos exhaustivos y las pruebas de proposiciones existenciales.

---

## 1. Demostración por Contradicción (Reducción al Absurdo)

El método de **demostración por contradicción** (*Reductio ad Absurdum*) es una de las herramientas más potentes del razonamiento deductivo. Se basa en la tautología:

\\[
(\neg P \implies \bot) \;\implies\; P
\\]

donde \\(\bot\\) representa una contradicción lógica explícita (una afirmación del tipo \\(R \land \neg R\\)).

> **Estructura de la Prueba por Contradicción:**  
> 1. Para demostrar que una proposición \\(P\\) es verdadera, se formula la **suposición por contradicción** de que \\(P\\) es **Falsa** (es decir, que \\(\neg P\\) es verdadera).
> 2. Si el teorema a demostrar es una implicación \\(P \implies Q\\), negar la implicación equivale a asumir que:
> \\[
> P \quad \text{es Verdadera} \qquad \text{y} \qquad Q \quad \text{es Falsa (\neg Q es Verdadera)}
> \\]
> 3. A partir de estas premisas de trabajo se deduce lógicamente una **contradicción flagrante \\(\bot\\)** (por ejemplo, que un número es simultáneamente par e impar, que \\(0 = 1\\), o que contradice una hipótesis inicial o axioma).
> 4. Dado que en la lógica clásica las contradicciones son imposibles, la suposición de que \\(\neg P\\) era verdadera resulta insostenible. Se concluye que \\(P\\) es **Verdadera**. \\(\blacksquare\\)

### Ejemplo Clásico 1: La Irracionalidad de \\(\sqrt{2}\\) (Demostración de Euclides)

> **Teorema 4.3:**  
> El número \\(\sqrt{2}\\) es irracional (\\(\sqrt{2} \notin \mathbb{Q}\\)).

*Demostración por Contradicción:*
1. **Suposición por reducción al absurdo:** Supongamos que \\(\sqrt{2}\\) **es un número racional** (\\(\sqrt{2} \in \mathbb{Q}\\)).
2. Por definición de número racional, existen enteros \\(a, b \in \mathbb{Z}\\) con \\(b \neq 0\\) tales que:

\\[
\sqrt{2} \;=\; \frac{a}{b}
\\]

3. Sin pérdida de generalidad, podemos asumir que la fracción \\(\frac{a}{b}\\) está en su **forma irreducible**, es decir, que \\(a\\) y \\(b\\) son **coprimos** (su máximo común divisor es \\(\gcd(a, b) = 1\\); no comparten factores primos comunes).
4. Elevando ambos miembros al cuadrado:

\\[
2 \;=\; \frac{a^2}{b^2} \implies a^2 \;=\; 2b^2
\\]

5. Como \\(b \in \mathbb{Z}\\), \\(a^2\\) es un múltiplo de 2, luego \\(a^2\\) es **par**.
6. Por el Teorema 4.2 demostrado previamente, si \\(a^2\\) es par, entonces **\\(a\\) es par**.
7. Por tanto, existe un entero \\(k \in \mathbb{Z}\\) tal que \\(a = 2k\\).
8. Sustituyendo \\(a = 2k\\) en la ecuación del paso 4:

\\[
(2k)^2 \;=\; 2b^2 \implies 4k^2 \;=\; 2b^2 \implies b^2 \;=\; 2k^2
\\]

9. De aquí se deduce que \\(b^2\\) es par, y por el Teorema 4.2, **\\(b\\) también es par**.
10. **La Contradicción:** Hemos deducido que tanto \\(a\\) como \\(b\\) son pares (ambos son divisibles entre 2). Esto significa que \\(2 \mid \gcd(a, b)\\), lo cual contradice directamente la hipótesis fundamental de que \\(\gcd(a, b) = 1\\) (que la fracción era irreducible).
11. Esta contradicción demuestra que la suposición inicial de que \\(\sqrt{2} \in \mathbb{Q}\\) es falsa. Por lo tanto, \\(\sqrt{2}\\) es **irracional**. \\(\blacksquare\\)

---

## 2. Demostración por Casos Exhaustivos

La **demostración por casos** se fundamenta en la regla del dilema constructivo. Se utiliza cuando el dominio de la hipótesis puede descomponerse en un número finito de casos \\(C\_1, C\_2, \dots, C\_k\\) que cubren la totalidad de las posibilidades (es decir, \\(C\_1 \lor C\_2 \lor \dots \lor C\_k \equiv \top\\)):

\\[
\frac{(C\_1 \lor \dots \lor C\_k), \quad C\_1 \implies Q, \quad \dots, \quad C\_k \implies Q}{\therefore Q}
\\]

### Ejemplo:
> **Teorema 4.4:**  
> Para todo entero \\(n \in \mathbb{Z}\\), el producto \\(n(n+1)\\) es un número par.

*Demostración por Casos:*  
Por el algoritmo de la división, todo entero \\(n\\) es par o impar (casos exhaustivos):
* **Caso 1 (\\(n\\) es par):** Existe \\(k \in \mathbb{Z}\\) con \\(n = 2k\\).  
  Entonces \\(n(n+1) = 2k(2k+1) = 2[k(2k+1)]\\), que es claramente par.
* **Caso 2 (\\(n\\) es impar):** Existe \\(k \in \mathbb{Z}\\) con \\(n = 2k+1\\).  
  Entonces \\(n+1 = 2k+2 = 2(k+1)\\).  
  Luego \\(n(n+1) = (2k+1) \cdot 2(k+1) = 2[(2k+1)(k+1)]\\), que también es par.
* Como ambos casos son exhaustivos y en ambos se concluye la paridad, el teorema queda demostrado para todo \\(n \in \mathbb{Z}\\). \\(\blacksquare\\)

---

## 3. Demostraciones de Existencia y Unicidad

### A. Pruebas de Existencia (\\(\exists x \, P(x)\\))
1. **Prueba Constructiva:** Se exhibe explícitamente un elemento testigo \\(x\_0\\) y se verifica algebraicamente que satisface \\(P(x\_0)\\).
2. **Prueba No Constructiva:** Se demuestra la existencia mediante contradicción o mediante teoremas de existencia global (como el Teorema del Valor Intermedio), sin calcular explícitamente el valor del testigo.

### B. Pruebas de Unicidad (\\(\exists! x \, P(x)\\))
Para probar que existe un **único** elemento que cumple \\(P(x)\\):
1. **Paso 1 (Existencia):** Se prueba que existe al menos un elemento \\(x\\) con \\(P(x)\\).
2. **Paso 2 (Unicidad):** Se asume que existen dos elementos \\(x\_1\\) y \\(x\_2\\) que cumplen la propiedad (\\(P(x\_1) \land P(x\_2)\\)), y mediante deducciones formales se demuestra rigurosamente que:

\\[
x\_1 \;=\; x\_2
\\]