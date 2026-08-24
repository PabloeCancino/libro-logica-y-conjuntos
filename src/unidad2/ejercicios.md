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