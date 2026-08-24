# 4.1 Métodos de Demostración Directa y por Contraposición

Una **demostración matemática** es un argumento deductivo riguroso que establece la verdad irrefutable de una proposición matemática (teorema, lema o corolario) a partir de un conjunto de axiomas, definiciones previamente establecidas y teoremas demostrados con anterioridad.

La inmensa mayoría de los enunciados matemáticos tienen la forma condicional universal:

\\[
(\forall x \in U) [P(x) \implies Q(x)]
\\]

donde \\(P(x)\\) es la **hipótesis** y \\(Q(x)\\) es la **conclusión** o **tesis**.

---

## 1. El Método de Demostración Directa

El método de **demostración directa** es la técnica más intuitiva y natural. Se fundamenta en la regla de inferencia *Modus Ponens*:

> **Estructura de la Demostración Directa:**  
> 1. **Paso 1 (Hipótesis):** Se asume explícitamente que la hipótesis \\(P\\) es **Verdadera**.
> 2. **Paso 2 (Cadena Deductiva):** Utilizando definiciones axiomáticas, identidades algebraicas y teoremas previos, se deduce una cadena finita de implicaciones válidas:
> \\[
> P \implies P_1 \implies P_2 \implies \dots \implies P_k \implies Q
> \\]
> 3. **Paso 3 (Conclusión):** Se arriba formalmente a la verdad de \\(Q\\).  
> Por el Teorema de la Deducción, queda demostrado que \\(P \implies Q\\). \\(\blacksquare\\)

### Ejemplo 1 (Paridad en los Enteros):
> **Teorema 4.1:**  
> Si \\(n\\) es un número entero par, entonces su cuadrado \\(n^2\\) es un número entero par.

*Demostración Directa:*
1. **Hipótesis:** Sea \\(n \in \mathbb{Z}\\) un número entero par.
2. Por definición formal de número par, existe un entero \\(k \in \mathbb{Z}\\) tal que:

\\[
n \;=\; 2k
\\]

3. Elevando ambos miembros al cuadrado:

\\[
n^2 \;=\; (2k)^2 \;=\; 4k^2 \;=\; 2(2k^2)
\\]

4. Como \\(k \in \mathbb{Z}\\), el número \\(m = 2k^2\\) es también un entero (\\(m \in \mathbb{Z}\\)).
5. Por lo tanto, \\(n^2 = 2m\\) con \\(m \in \mathbb{Z}\\), lo cual satisface la definición de número entero par. \\(\blacksquare\\)

---

## 2. El Método de Demostración por Contraposición (Prueba Indirecta)

La **prueba por contraposición** se fundamenta en la equivalencia lógica tautológica demostrada en la Unidad 1:

\\[
(P \implies Q) \;\equiv\; (\neg Q \implies \neg P)
\\]

> **Estructura de la Demostración por Contraposición:**  
> 1. **Paso 1 (Negación de la Conclusión):** Se asume como hipótesis de trabajo la negación de la tesis (es decir, que \\(Q\\) es **Falso**, \\(\neg Q\\) es Verdadero).
> 2. **Paso 2 (Deducción Directa de \\(\neg P\\)):** A partir de \\(\neg Q\\), se efectúa una deducción directa para llegar a la negación de la hipótesis original \\(\neg P\\).
> 3. **Paso 3 (Conclusión):** Habiendo probado que \\(\neg Q \implies \neg P\\), por equivalencia lógica queda automáticamente demostrado el teorema original \\(P \implies Q\\). \\(\blacksquare\\)

### ¿Cuándo es Preferible la Contraposición?
La contraposición es especialmente ventajosa cuando:
* La negación de la conclusión (\\(\neg Q\\)) proporciona una **estructura algebraica positiva y directa** mucho más fácil de manipular que la hipótesis original \\(P\\).

### Ejemplo 2 (El Recíproco de la Paridad Cuadrática):
> **Teorema 4.2:**  
> Sea \\(n \in \mathbb{Z}\\). Si \\(n^2\\) es un número par, entonces \\(n\\) es par.

*Análisis previo:* Si intentáramos una prueba directa, asumiríamos \\(n^2 = 2k\\), lo que nos llevaría a \\(n = \sqrt{2k}\\), una expresión radical irracional muy difícil de analizar en los enteros. Por contraposición, la prueba es limpia e inmediata:

*Demostración por Contraposición:*
1. Identifiquemos las proposiciones:
   * \\(P\\): "\\(n^2\\) es par"
   * \\(Q\\): "\\(n\\) es par"
2. Queremos demostrar la contrapositiva equivalente: \\(\neg Q \implies \neg P\\), es decir:  
   *"Si \\(n\\) es impar, entonces \\(n^2\\) es impar."*
3. **Hipótesis contrapositiva:** Sea \\(n \in \mathbb{Z}\\) un número impar. Por definición de entero impar, existe \\(k \in \mathbb{Z}\\) tal que:

\\[
n \;=\; 2k + 1
\\]

4. Calculamos su cuadrado:

\\[
n^2 \;=\; (2k + 1)^2 \;=\; 4k^2 + 4k + 1 \;=\; 2(2k^2 + 2k) + 1
\\]

5. Como \\(k \in \mathbb{Z}\\), definiendo \\(j = 2k^2 + 2k \in \mathbb{Z}\\), se tiene que:

\\[
n^2 \;=\; 2j + 1
\\]

6. Esto demuestra que \\(n^2\\) es impar (\\(\neg P\\)).
7. Al haberse demostrado que \\(\neg Q \implies \neg P\\), queda formalmente probado que \\(P \implies Q\\). \\(\blacksquare\\)

---

## 3. Demostración de Equivalencias (P ⟺ Q)

Para demostrar un teorema de doble implicación o equivalencia ("\\(P\\) si y sólo si \\(Q\\)"):

\\[
(P \iff Q) \;\equiv\; (P \implies Q) \;\land\; (Q \implies P)
\\]

Es obligatorio desglosar la prueba en dos etapas independientes:
1. **Necesidad (\\(P \implies Q\\)):** Se asume \\(P\\) y se deduce \\(Q\\) (de forma directa o contrapositiva).
2. **Suficiencia (\\(Q \implies P\\)):** Se asume \\(Q\\) y se deduce \\(P\\) (de forma directa o contrapositiva).