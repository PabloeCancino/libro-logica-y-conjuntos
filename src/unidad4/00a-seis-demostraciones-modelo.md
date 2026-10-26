# 4.0.1 Seis demostraciones modelo: lógica y conjuntos

Esta sección reúne **seis demostraciones breves y completas** que sirven de patrón para el resto de la Unidad 4: tres en lógica proposicional y tres en teoría de conjuntos. Cada una ilustra **un método distinto** y se presenta con la misma anatomía:

* **Enunciado** (hipótesis y tesis).
* **Método** y la idea que lo motiva.
* **Demostración** con cada paso justificado.
* **Qué observar**: el rasgo del método que conviene retener.

> **Cómo usar esta sección.** Lea primero el enunciado e intente su propio borrador (sección 4.0, método hacia adelante y hacia atrás). Compare después con el modelo. Al final encontrará una tabla que conecta ambas partes y ejercicios graduados.

**Requisitos.** Esta sección supone las secciones 1.3 (equivalencias), 2.3 (reglas de inferencia, incluida la prueba condicional), 3.2 y 3.3 (inclusión, igualdad y operaciones) y 4.0 (esqueletos de demostración).

**Relación con secciones anteriores.** Los modelos L1 y L2 **repiten deliberadamente**, como patrones de método, dos resultados ya demostrados en la sección 1.3 (De Morgan por tabla de verdad y la contrapositiva por cadena de equivalencias); sirven de repaso y de pieza para los modelos conjuntistas. El modelo C2 ya aparece en la sección 3.3 por doble contención; aquí se demuestra por cadena de equivalencias para comparar ambos estilos.

| Modelo | Resultado | Método |
| :---: | :--- | :--- |
| L1 | \\(\neg(p \land q) \equiv \neg p \lor \neg q\\) | Tabla de verdad (semántico) |
| L2 | \\((p \to q) \equiv (\neg q \to \neg p)\\) | Cadena de equivalencias (algebraico) |
| L3 | \\(p \to q,\ q \to r \vdash p \to r\\) | Deducción natural y prueba condicional (sintáctico) |
| C1 | \\(A \cap B \subseteq A\\) | Elemento arbitrario |
| C2 | \\((A \cup B)^c = A^c \cap B^c\\) | Cadena de equivalencias sobre pertenencia |
| C3 | \\(A \subseteq B \iff A \cup B = B\\) | Doble implicación y prueba por casos |

---

## Parte I. Lógica proposicional

### Modelo L1: Ley de De Morgan por tabla de verdad

> **Enunciado.** Para cualesquiera proposiciones \\(p, q\\):
>
> \\[
> \neg(p \land q) \equiv \neg p \lor \neg q
> \\]

**Método.** Dos fórmulas son equivalentes si tienen la misma tabla de verdad (Definición 1.2). Con dos variables hay \\(2^2 = 4\\) interpretaciones: se evalúan todas.

**Demostración.**

| \\(p\\) | \\(q\\) | \\(p \land q\\) | \\(\neg(p \land q)\\) | \\(\neg p\\) | \\(\neg q\\) | \\(\neg p \lor \neg q\\) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| V | V | V | **F** | F | F | **F** |
| V | F | F | **V** | F | V | **V** |
| F | V | F | **V** | V | F | **V** |
| F | F | F | **V** | V | V | **V** |

Las columnas cuarta y séptima (en negritas) coinciden en las cuatro filas. Por lo tanto, las fórmulas son equivalentes. \\(\blacksquare\\)

**Qué observar.** El método es *exhaustivo y mecánico*: no exige ingenio, pero su costo crece como \\(2^n\\) con el número \\(n\\) de variables. Para fórmulas con muchas variables conviene el método algebraico del modelo siguiente.

---

### Modelo L2: La contrapositiva por cadena de equivalencias

> **Enunciado.** Para cualesquiera proposiciones \\(p, q\\):
>
> \\[
> (p \to q) \equiv (\neg q \to \neg p)
> \\]

**Método.** Se parte de un lado y se transforma, paso a paso, en el otro, usando únicamente equivalencias ya conocidas (sección 1.3). Cada paso se anota con su ley.

**Demostración.**

| Paso | Fórmula | Justificación |
| :---: | :--- | :--- |
| 1 | \\(p \to q\\) | Punto de partida |
| 2 | \\(\neg p \lor q\\) | Definición del condicional (\\(p \to q \equiv \neg p \lor q\\)) |
| 3 | \\(q \lor \neg p\\) | Conmutatividad de \\(\lor\\) |
| 4 | \\(\neg(\neg q) \lor \neg p\\) | Doble negación aplicada a \\(q\\) |
| 5 | \\(\neg q \to \neg p\\) | Definición del condicional, con \\(\neg q\\) como antecedente |

Como cada paso es una equivalencia, \\(p \to q \equiv \neg q \to \neg p\\). \\(\blacksquare\\)

**Qué observar.** Esta equivalencia es la base lógica de la demostración por contraposición, que se desarrolla en la sección 4.1. No debe confundirse con el *recíproco* \\(q \to p\\), que **no** es equivalente a \\(p \to q\\): la fila \\(p = F,\ q = V\\) lo refuta.

---

### Modelo L3: Silogismo hipotético por deducción natural

> **Enunciado.** De las premisas \\(p \to q\\) y \\(q \to r\\) se deduce \\(p \to r\\).

**Método.** Para probar un condicional se utiliza la **prueba condicional**: se *supone* temporalmente el antecedente, se deduce el consecuente y se **descarga** el supuesto (sección 2.3).

**Demostración.**

| N.º | Fórmula | Justificación |
| :---: | :--- | :--- |
| 1 | \\(p \to q\\) | Premisa |
| 2 | \\(q \to r\\) | Premisa |
| 3 | \\(p\\) | Supuesto (para la prueba condicional) |
| 4 | \\(q\\) | Modus ponens, de 1 y 3 |
| 5 | \\(r\\) | Modus ponens, de 2 y 4 |
| 6 | \\(p \to r\\) | Prueba condicional, líneas 3 a 5 (se descarga el supuesto 3) |

\\(\blacksquare\\)

**Qué observar.**

* La línea 3 **no** es una premisa: es un supuesto de trabajo que desaparece en la línea 6. Ninguna conclusión puede depender de un supuesto que sigue abierto.
* Este resultado es una *derivación* (\\(\vdash\\)). Su contraparte semántica es que \\(((p \to q) \land (q \to r)) \to (p \to r)\\) es una tautología (\\(\models\\)), que puede comprobarse con una tabla de \\(2^3 = 8\\) filas (es el Ejercicio 3.d de la Unidad 1).

---

## Parte II. Teoría de conjuntos

En esta parte el método central es el **elemento arbitrario**: para hablar de todos los elementos de un conjunto se toma uno genérico \\(x\\), se traduce su pertenencia a lógica y se razona con las reglas de la Parte I.

### Modelo C1: Una intersección está contenida en cada uno de sus factores

> **Enunciado.** Para cualesquiera conjuntos \\(A, B\\):
>
> \\[
> A \cap B \subseteq A
> \\]

**Método.** Esqueleto de la sección 4.0 para \\(X \subseteq Y\\): «Sea \\(x \in X\\) … luego \\(x \in Y\\)».

**Demostración.** Sea \\(x\\) un elemento arbitrario de \\(A \cap B\\). Por definición de intersección, \\(x \in A\\) **y** \\(x \in B\\). En particular, \\(x \in A\\). Como \\(x\\) era arbitrario, todo elemento de \\(A \cap B\\) pertenece a \\(A\\); es decir, \\(A \cap B \subseteq A\\). \\(\blacksquare\\)

**Qué observar.** El paso «de \\(x \in A\\) y \\(x \in B\\) se obtiene \\(x \in A\\)» es la regla lógica de **simplificación** (\\(p \land q \vdash p\\)). La demostración conjuntista es, por dentro, una inferencia lógica.

---

### Modelo C2: Ley de De Morgan para conjuntos

> **Enunciado.** Para cualesquiera subconjuntos \\(A, B\\) de un universo \\(\mathcal{U}\\):
>
> \\[
> (A \cup B)^c = A^c \cap B^c
> \\]

**Método.** Igualdad de conjuntos mediante una **cadena de equivalencias** sobre la pertenencia de un elemento arbitrario. Es válida porque *cada* paso es un «si y sólo si»: así se prueban de una vez las dos contenciones.

**Demostración.** Sea \\(x \in \mathcal{U}\\) arbitrario.

| Paso | Afirmación | Justificación |
| :---: | :--- | :--- |
| 1 | \\(x \in (A \cup B)^c\\) | Punto de partida |
| 2 | \\(\iff x \notin A \cup B\\) | Definición de complemento |
| 3 | \\(\iff \neg(x \in A \lor x \in B)\\) | Definición de unión |
| 4 | \\(\iff x \notin A \land x \notin B\\) | De Morgan lógico (Modelo L1) |
| 5 | \\(\iff x \in A^c \land x \in B^c\\) | Definición de complemento |
| 6 | \\(\iff x \in A^c \cap B^c\\) | Definición de intersección |

Como \\(x\\) era arbitrario, ambos conjuntos tienen los mismos elementos; por extensionalidad, son iguales. \\(\blacksquare\\)

**Qué observar.** El paso 4 es *exactamente* el Modelo L1. La ley de De Morgan de los conjuntos **hereda** su validez de la ley de De Morgan lógica. En la sección 3.3 se probó el mismo resultado por doble contención; compare ambos estilos.

---

### Modelo C3: Caracterización de la inclusión mediante la unión

> **Enunciado.** Para cualesquiera conjuntos \\(A, B\\):
>
> \\[
> A \subseteq B \iff A \cup B = B
> \\]

**Método.** Una equivalencia exige **dos implicaciones independientes** (esqueleto de \\(P \iff Q\\) en la sección 4.0). La primera incluye una igualdad de conjuntos (doble contención) y una **prueba por casos** (por la disyunción \\(x \in A \lor x \in B\\)).

**Demostración.**

\\((\Rightarrow)\\) Suponga \\(A \subseteq B\\). Se prueba \\(A \cup B = B\\) por doble contención.

* \\(B \subseteq A \cup B\\): si \\(x \in B\\), entonces \\(x \in A \lor x \in B\\), luego \\(x \in A \cup B\\).
* \\(A \cup B \subseteq B\\): sea \\(x \in A \cup B\\). Entonces \\(x \in A\\) o \\(x \in B\\).
 * *Caso 1:* \\(x \in A\\). Por hipótesis \\(A \subseteq B\\), luego \\(x \in B\\).
 * *Caso 2:* \\(x \in B\\). No hay nada que probar.

 En ambos casos \\(x \in B\\).

Por doble contención, \\(A \cup B = B\\).

\\((\Leftarrow)\\) Suponga \\(A \cup B = B\\). Sea \\(x \in A\\). Entonces \\(x \in A \cup B\\) y, como \\(A \cup B = B\\), se tiene \\(x \in B\\). Por tanto \\(A \subseteq B\\). \\(\blacksquare\\)

**Qué observar.** Los casos son **exhaustivos** porque provienen de una disyunción dada (\\(x \in A \lor x \in B\\)). Observe también que el dato \\(A \cup B = B\\) se usó como *sustitución*: si un elemento está en un conjunto, está en cualquier conjunto igual a él.

---

## Parte III. El diccionario entre lógica y conjuntos

Los modelos C1 a C3 funcionan porque cada operación conjuntista se define con una conectiva lógica sobre la pertenencia:

| Lógica | Conjuntos | Definición de la operación |
| :---: | :---: | :--- |
| \\(\neg\\) | \\(A^c\\) | \\(x \in A^c \iff \neg(x \in A)\\) |
| \\(\land\\) | \\(A \cap B\\) | \\(x \in A \cap B \iff x \in A \land x \in B\\) |
| \\(\lor\\) | \\(A \cup B\\) | \\(x \in A \cup B \iff x \in A \lor x \in B\\) |
| \\(\to\\) | \\(A \subseteq B\\) | \\(A \subseteq B \iff (\forall x)(x \in A \to x \in B)\\) |
| \\(\leftrightarrow\\) | \\(A = B\\) | \\(A = B \iff (\forall x)(x \in A \leftrightarrow x \in B)\\) |
| \\(\top\\) | \\(\mathcal{U}\\) | \\(x \in \mathcal{U}\\) es siempre verdadero |
| \\(\bot\\) | \\(\emptyset\\) | \\(x \in \emptyset\\) es siempre falso |

Cada ley lógica produce una ley conjuntista:

| Ley lógica | Ley conjuntista correspondiente |
| :--- | :--- |
| \\(\neg(p \land q) \equiv \neg p \lor \neg q\\) (Modelo L1) | \\((A \cap B)^c = A^c \cup B^c\\) |
| \\(\neg(p \lor q) \equiv \neg p \land \neg q\\) | \\((A \cup B)^c = A^c \cap B^c\\) (Modelo C2) |
| \\((p \to q) \equiv (\neg q \to \neg p)\\) (Modelo L2) | \\(A \subseteq B \iff B^c \subseteq A^c\\) |
| \\((p \land q) \to p\\) (simplificación) | \\(A \cap B \subseteq A\\) (Modelo C1) |
| Transitividad de \\(\to\\) (Modelo L3) | \\(A \subseteq B \land B \subseteq C \implies A \subseteq C\\) |
| \\((p \to q) \equiv ((p \lor q) \leftrightarrow q)\\) (Ejercicio 5) | \\(A \subseteq B \iff A \cup B = B\\) (Modelo C3) |

> **Advertencia.** La correspondencia \\(\to\\) y \\(\subseteq\\) no es literal: el condicional relaciona *proposiciones*, mientras que \\(\subseteq\\) relaciona *conjuntos* y encierra un cuantificador universal. Por eso aparece \\((\forall x)\\) en la definición de inclusión.

---

## Ejercicios

### Nivel básico

1. **(L)** Demuestre por tabla de verdad que \\(\neg(p \lor q) \equiv \neg p \land \neg q\\).
2. **(L)** Demuestre por una cadena de equivalencias, anotando la ley de cada paso, que \\(p \to q \equiv \neg(p \land \neg q)\\).
3. **(L)** Construya la tabla de verdad de \\(p \to (q \to p)\\) y verifique que es una tautología. Explique con palabras por qué «una proposición verdadera se sigue de cualquier cosa».
4. **(C)** Demuestre que \\(A \subseteq A \cup B\\).

### Nivel medio

5. **(L)** Demuestre por tabla de verdad que \\((p \to q) \equiv ((p \lor q) \leftrightarrow q)\\) y explique su relación con el Modelo C3.
6. **(C)** Demuestre por cadena de equivalencias que \\((A \cap B)^c = A^c \cup B^c\\).
7. **(C)** Demuestre que \\(A \subseteq B \iff A \cap B = A\\).
8. **(L)** Construya una derivación en deducción natural de \\(p \to (q \land r)\\) a partir de las premisas \\(p \to q\\) y \\(p \to r\\). *Pista:* suponga \\(p\\) y use la regla de introducción de la conjunción.

### Nivel de reto

9. **(C)** Demuestre que si \\(A \subseteq B\\), entonces \\(B^c \subseteq A^c\\), usando el Modelo L2 (contraposición) para escribir la prueba en pocas líneas.
10. **(C)** Decida si es verdadera o falsa la afirmación: «Si \\(A \cup B \subseteq A \cup C\\), entonces \\(B \subseteq C\\)». Si es verdadera, demuéstrela; si es falsa, dé un contraejemplo. *Pista:* pruebe con conjuntos de uno o dos elementos (sección 4.0, errores frecuentes).

> **Soluciones.** Al final de la Unidad 4, en la página [Ejercicios de la Unidad 4](ejercicios.md), hay un bloque plegable con las soluciones de estos diez ejercicios.
