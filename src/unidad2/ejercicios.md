# Ejercicios de la Unidad 2

---

## 📝 Bloque A: Predicados y Conjuntos de Verdad

1. Sea el universo de discurso \\(U = \mathbb{Z}\\) (los números enteros). Determine el conjunto de verdad de cada uno de los siguientes predicados:
 - a) \\(P(x): "x^2 - 9 = 0"\\)
 - b) \\(Q(x): "x^2 + 1 = 0"\\)
 - c) \\(R(x): "|x| \le 3"\\)
 - d) \\(S(x): "x \text{ es múltiplo de 2 y múltiplo de 3}"\\)

2. Sean los predicados \\(P(x): "x \ge 0"\\) y \\(Q(x): "x^2 \le 4"\\) sobre el universo \\(U = \mathbb{R}\\). Determine explícitamente:
 - a) \\(T\_P \cap T\_Q\\)
 - b) \\(T\_P \cup T\_Q\\)
 - c) \\(T\_{\neg P}\\)
 - d) \\(T\_P \setminus T\_Q\\)

---

## 📝 Bloque B: Cuantificadores, Negación y Contraejemplos

3. Escriba la negación formal de cada una de las siguientes proposiciones de modo que ningún operador de negación quede precediendo a un cuantificador:
 - a) \\((\forall x \in \mathbb{R})(\exists y \in \mathbb{R})(x + y > 0)\\)
 - b) \\((\exists x \in \mathbb{Z})(\forall y \in \mathbb{Z})(x \cdot y = y)\\)
 - c) \\((\forall \varepsilon > 0)(\exists \delta > 0)(\forall x) [|x - c| < \delta \implies |f(x) - L| < \varepsilon]\\)
 - d) \\((\forall x) [P(x) \to Q(x) \lor R(x)]\\)

4. Para cada una de las siguientes afirmaciones universales sobre \\(U = \mathbb{R}\\), determine si es verdadera o falsa. Si es falsa, proporcione un **contraejemplo explícito**:
 - a) \\((\forall x \in \mathbb{R})(x^2 \ge x)\\)
 - b) \\((\forall x \in \mathbb{R})(x^2 > 0)\\)
 - c) \\((\forall x \in \mathbb{R})(\forall y \in \mathbb{R}) (|x + y| \le |x| + |y|)\\)
 - d) \\((\forall x \in \mathbb{R})(\exists y \in \mathbb{R})(x \cdot y = 1)\\)

---

## 📝 Bloque C: Deducción Natural y Demostraciones Formales

5. Proporcione una deducción formal paso a paso indicando la regla de inferencia empleada en cada línea para demostrar la validez de los siguientes argumentos:
 - a)
 - Premisa 1: \\(p \to (q \land r)\\)
 - Premisa 2: \\(p\\)
 - Conclusión: \\(q\\)
 - b)
 - Premisa 1: \\(\neg p \to q\\)
 - Premisa 2: \\(q \to \neg r\\)
 - Premisa 3: \\(r\\)
 - Conclusión: \\(p\\)
 - c)
 - Premisa 1: \\((\forall x)(P(x) \to Q(x))\\)
 - Premisa 2: \\((\forall x)(Q(x) \to R(x))\\)
 - Conclusión: \\((\forall x)(P(x) \to R(x))\\)

---

## 📝 Bloque D: Demostraciones Básicas con Cuantificadores (el Orden Importa)

6. Sobre el universo \\(U = \mathbb{Z}\\), demuestre que la proposición \\((\exists y \in \mathbb{Z})(\forall x \in \mathbb{Z})(x + y = 0)\\) es **falsa**. Para ello, escriba su negación de modo que ningún operador de negación preceda a un cuantificador y demuéstrela.

7. Sobre \\(U = \mathbb{Z}\\), demuestre que \\((\forall x \in \mathbb{Z})(\exists y \in \mathbb{Z})(x + y = 0)\\) es **verdadera**, indicando qué regla de la sección 2.3 sustenta cada paso. Compare con el Ejercicio 6: ¿qué muestra sobre el orden de los cuantificadores?

---

## 📝 Bloque E: Deducción Natural y Prueba Condicional

8. Demuestre la validez del argumento mediante una derivación en la que cada línea indique su regla:
 - Premisa 1: \\(p \to q\\)
 - Premisa 2: \\(q \to r\\)
 - Premisa 3: \\(\neg r\\)
 - Premisa 4: \\(p \lor s\\)
 - Conclusión: \\(s\\)

9. Usando la **prueba condicional** (sección 2.3, §I), derive \\((p \land q) \to r\\) a partir de la premisa \\(p \to (q \to r)\\). Compare con el Ejercicio 7 de la Unidad 1: allí se probó la misma relación por equivalencias; aquí se obtiene por derivación.

10. Demuestre mediante una derivación formal que de \\((\forall x)(P(x) \land Q(x))\\) se sigue \\((\forall x)P(x) \land (\forall x)Q(x)\\). Indique en cada paso la regla utilizada y explique por qué el elemento \\(c\\) es *arbitrario* al aplicar la generalización universal.

---

## 💡 Soluciones y Guías Seleccionadas

> **Solución al Ejercicio 3.c:** 
> Negación de la definición de límite: 
> \\(\neg [(\forall \varepsilon > 0)(\exists \delta > 0)(\forall x) (0 < |x - c| < \delta \to |f(x) - L| < \varepsilon)]\\) 
> \\(\equiv (\exists \varepsilon > 0) \neg [(\exists \delta > 0)(\forall x) (0 < |x - c| < \delta \to |f(x) - L| < \varepsilon)]\\) 
> \\(\equiv (\exists \varepsilon > 0)(\forall \delta > 0) \neg [(\forall x) (0 < |x - c| < \delta \to |f(x) - L| < \varepsilon)]\\) 
> \\(\equiv (\exists \varepsilon > 0)(\forall \delta > 0)(\exists x) \neg [0 < |x - c| < \delta \to |f(x) - L| < \varepsilon]\\) 
> Recordando que \\(\neg(A \to B) \equiv A \land \neg B\\): 
> \\(\equiv (\exists \varepsilon > 0)(\forall \delta > 0)(\exists x) [0 < |x - c| < \delta \land |f(x) - L| \ge \varepsilon]\\). \\(\blacksquare\\)

> **Solución al Ejercicio 4.a:** 
> La afirmación \\((\forall x \in \mathbb{R})(x^2 \ge x)\\) es **FALSA**. 
> *Contraejemplo:* Tomemos \\(x\_0 = \frac{1}{2} \in \mathbb{R}\\). 
> Se tiene \\(x\_0^2 = \left(\frac{1}{2}\right)^2 = \frac{1}{4}\\). 
> Como \\(\frac{1}{4} < \frac{1}{2}\\), se concluye que \\(x\_0^2 \not\ge x\_0\\). Por lo tanto, el enunciado universal queda refutado. \\(\blacksquare\\)

---

## 💡 Soluciones de los Bloques D y E (Ejercicios 6 a 10)

<details>
<summary><strong>Mostrar / ocultar las soluciones de los Ejercicios 6 a 10</strong></summary>

**Ejercicio 6.** La proposición original es \\((\exists y)(\forall x)(x + y = 0)\\). Su negación, pasando la negación a través de los cuantificadores (sección 2.2), es:

\\[
(\forall y \in \mathbb{Z})(\exists x \in \mathbb{Z})(x + y \neq 0)
\\]

*Demostración de la negación.* Sea \\(y \in \mathbb{Z}\\) arbitrario. Tomemos \\(x = 1 - y\\), que es un entero. Entonces \\(x + y = 1 \neq 0\\). Como \\(y\\) era arbitrario, la negación es verdadera y, por tanto, la proposición original es **falsa**. \\(\blacksquare\\)

**Ejercicio 7.**

| Paso | Expresión | Justificación |
| :---: | :--- | :--- |
| 1 | Sea \\(x \in \mathbb{Z}\\) | Elemento arbitrario (se prepara la G.U.) |
| 2 | \\(y = -x \in \mathbb{Z}\\) | Construcción del testigo; el opuesto de un entero es entero |
| 3 | \\(x + y = x + (-x) = 0\\) | Propiedad del opuesto |
| 4 | \\((\exists y \in \mathbb{Z})(x + y = 0)\\) | Generalización Existencial (G.E.) con el testigo del paso 2 |
| 5 | \\((\forall x \in \mathbb{Z})(\exists y \in \mathbb{Z})(x + y = 0)\\) | Generalización Universal (G.U.): \\(x\\) era arbitrario |

\\(\blacksquare\\) *Lección:* en \\(\forall x\,\exists y\\) el testigo \\(y\\) **puede depender de** \\(x\\) (aquí \\(y = -x\\)); en \\(\exists y\,\forall x\\) un único \\(y\\) debería servir para *todos* los \\(x\\), y eso falla (Ejercicio 6). Los cuantificadores heterogéneos no conmutan.

**Ejercicio 8.**

| Paso | Expresión Lógica | Justificación / Regla Utilizada |
| :---: | :--- | :--- |
| (1) | \\(p \to q\\) | Premisa 1 |
| (2) | \\(q \to r\\) | Premisa 2 |
| (3) | \\(\neg r\\) | Premisa 3 |
| (4) | \\(p \lor s\\) | Premisa 4 |
| (5) | \\(\neg q\\) | Modus Tollens (m.t.t.) entre (2) y (3) |
| (6) | \\(\neg p\\) | Modus Tollens (m.t.t.) entre (1) y (5) |
| (7) | \\(s\\) | Silogismo Disyuntivo (m.t.p.) entre (4) y (6) |

\\(\blacksquare\\)

**Ejercicio 9.**

| Paso | Expresión Lógica | Justificación / Regla Utilizada |
| :---: | :--- | :--- |
| (1) | \\(p \to (q \to r)\\) | Premisa |
| (2) | \\(p \land q\\) | Supuesto (se abre la prueba condicional) |
| (3) | \\(p\\) | Simplificación, de (2) |
| (4) | \\(q\\) | Simplificación, de (2) |
| (5) | \\(q \to r\\) | Modus Ponens entre (1) y (3) |
| (6) | \\(r\\) | Modus Ponens entre (4) y (5) |
| (7) | \\((p \land q) \to r\\) | Prueba Condicional, pasos (2) a (6); se descarga el supuesto (2) |

\\(\blacksquare\\)

**Ejercicio 10.**

| Paso | Expresión Lógica | Justificación / Regla Utilizada |
| :---: | :--- | :--- |
| (1) | \\((\forall x)(P(x) \land Q(x))\\) | Premisa |
| (2) | \\(P(c) \land Q(c)\\) | Ejemplificación Universal (E.U.) sobre (1), con \\(c\\) elemento arbitrario del universo |
| (3) | \\(P(c)\\) | Simplificación, de (2) |
| (4) | \\(Q(c)\\) | Simplificación, de (2) |
| (5) | \\((\forall x)P(x)\\) | Generalización Universal (G.U.) sobre (3) |
| (6) | \\((\forall x)Q(x)\\) | Generalización Universal (G.U.) sobre (4) |
| (7) | \\((\forall x)P(x) \land (\forall x)Q(x)\\) | Conjunción, de (5) y (6) |

\\(\blacksquare\\) *Por qué \\(c\\) es arbitrario:* \\(c\\) se introdujo en (2) mediante E.U. a partir de una premisa universal, sin ninguna suposición particular sobre él (no es un testigo existencial ni aparece en otra premisa). Por eso se puede generalizar en (5) y (6).

</details>
