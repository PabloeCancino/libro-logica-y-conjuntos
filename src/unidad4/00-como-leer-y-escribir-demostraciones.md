# 4.0 Cómo Leer, Descubrir y Escribir Demostraciones

Las secciones siguientes presentan los métodos de demostración (directo, contraposición, contradicción, casos, inducción). Antes de aplicarlos conviene dominar tres habilidades que los preceden y que ningún método sustituye:

1. **Leer** un enunciado: identificar qué se supone, qué se pide y qué significan sus términos.
2. **Descubrir** la prueba: encontrar la idea en un borrador, sin preocuparse aún por la redacción.
3. **Escribir** la prueba: presentar el argumento de modo que cualquier lector pueda verificarlo paso a paso.

> **Principio rector.** Una demostración no es una prueba de que *usted* está convencido: es un texto que permite a *otra persona* comprobar, sin adivinar nada, que la conclusión se sigue de las hipótesis.

---

## 1. Leer el Enunciado: Hipótesis, Tesis y Definiciones

Todo teorema de este curso puede reescribirse con la forma

\\[
(\forall x \in U)\,[P(x) \implies Q(x)]
\\]

Antes de escribir una sola línea, responda por escrito tres preguntas:

| Pregunta | Ejemplo: «Si \\(A \subseteq B\\), entonces \\(A \cap C \subseteq B \cap C\\)» |
| :--- | :--- |
| **¿Qué se supone?** (hipótesis) | \\(A \subseteq B\\), con \\(A, B, C\\) conjuntos arbitrarios |
| **¿Qué se quiere probar?** (tesis) | \\(A \cap C \subseteq B \cap C\\) |
| **¿Qué significan los símbolos?** (definiciones) | \\(X \subseteq Y\\) significa \\((\forall x)(x \in X \implies x \in Y)\\); \\(x \in X \cap Y\\) significa \\(x \in X \land x \in Y\\) |

Casi toda dificultad de un principiante se resuelve en la tercera fila: **desempacar las definiciones**. Una prueba en este curso es, en gran medida, traducir la tesis a su definición, traducir la hipótesis a su definición y encontrar el puente lógico entre ambas.

---

## 2. Descubrir la Prueba: el Método Hacia Adelante y Hacia Atrás

El **método hacia adelante y hacia atrás** (*forward-backward*) organiza el borrador en dos movimientos que se encuentran a la mitad del camino.

> **Proceso hacia adelante.** Parta de la hipótesis \\(P\\) y pregunte: *«¿Qué se sigue de esto?»* Reescríbala con su definición y extraiga consecuencias.
>
> **Proceso hacia atrás.** Parta de la tesis \\(Q\\) y pregunte: *«¿Qué me bastaría saber para concluir \\(Q\\)?»* Cada respuesta es una nueva meta más sencilla, \\(Q \Longleftarrow Q\_1 \Longleftarrow Q\_2 \Longleftarrow \cdots\\).
>
> La prueba está terminada cuando la cadena hacia adelante alcanza la cadena hacia atrás.

### Ejemplo trabajado

> **Proposición.** Si \\(A \subseteq B\\), entonces \\(A \cap C \subseteq B \cap C\\).

**Borrador (no es la demostración final):**

| | Hacia atrás (desde la tesis) | Hacia adelante (desde la hipótesis) |
| :--- | :--- | :--- |
| Inicio | Meta: \\(A \cap C \subseteq B \cap C\\) | Dato: \\(A \subseteq B\\) |
| Paso 1 | Por definición de \\(\subseteq\\): *basta* tomar \\(x \in A \cap C\\) y probar \\(x \in B \cap C\\) | Por definición: \\(x \in A \implies x \in B\\) para todo \\(x\\) |
| Paso 2 | Por definición de \\(\cap\\): *basta* probar \\(x \in B\\) **y** \\(x \in C\\) | Como \\(x \in A \cap C\\), se tiene \\(x \in A\\) y \\(x \in C\\) |
| Encuentro | \\(x \in C\\) ya se tiene; falta \\(x \in B\\) | De \\(x \in A\\) y \\(A \subseteq B\\) se obtiene \\(x \in B\\) |

Las dos columnas se encuentran: la prueba está descubierta. Obsérvese que el borrador se leyó «de afuera hacia adentro» y la redacción final se leerá en orden lógico, de la hipótesis a la tesis.

**Demostración (versión final):**

Sea \\(x\\) un elemento arbitrario de \\(A \cap C\\). Por definición de intersección, \\(x \in A\\) y \\(x \in C\\). Como \\(x \in A\\) y, por hipótesis, \\(A \subseteq B\\), se concluye que \\(x \in B\\). Así, \\(x \in B\\) y \\(x \in C\\), es decir, \\(x \in B \cap C\\). Como \\(x\\) era arbitrario, \\(A \cap C \subseteq B \cap C\\). \\(\blacksquare\\)

---

## 3. Esqueletos de Demostración según la Forma de la Tesis

La **forma lógica de la tesis** dicta la estructura de la prueba, incluso antes de saber *por qué* es verdadera. La tabla siguiente es un catálogo de arranques.

| Si la tesis tiene la forma… | Empiece así | Termine así |
| :--- | :--- | :--- |
| \\(\forall x\,P(x)\\) | «Sea \\(x\\) un elemento arbitrario del universo.» | «Como \\(x\\) era arbitrario, \\(\forall x\,P(x)\\).» |
| \\(\exists x\,P(x)\\) | Proponga o construya un candidato \\(x\_0\\). | Verifique que \\(P(x\_0)\\) se cumple. |
| \\(P \implies Q\\) | «Suponga \\(P\\).» | «Por lo tanto \\(Q\\).» |
| \\(P \iff Q\\) | Dos partes: \\((\Rightarrow)\\) y \\((\Leftarrow)\\). | Cada parte es una implicación independiente. |
| \\(P \land Q\\) | Pruebe \\(P\\); pruebe \\(Q\\). | «Luego \\(P \land Q\\).» |
| \\(P \lor Q\\) | «Suponga \\(\neg P\\)» y pruebe \\(Q\\) (o por casos). | «Luego \\(P \lor Q\\).» |
| \\(\neg P\\) | «Suponga \\(P\\)» y llegue a una contradicción. | «Contradicción; luego \\(\neg P\\).» |
| \\(A \subseteq B\\) | «Sea \\(x \in A\\).» | «Luego \\(x \in B\\); por tanto \\(A \subseteq B\\).» |
| \\(A = B\\) | Pruebe \\(A \subseteq B\\) y \\(B \subseteq A\\) (doble contención). | «Por doble contención, \\(A = B\\).» |
| \\(A \cap B = \emptyset\\) | «Suponga que existe \\(x \in A \cap B\\).» | Llegue a una contradicción. |

Del mismo modo, la **forma de la hipótesis** dicta cómo *usarla*:

| Si se tiene como dato… | Cómo se usa |
| :--- | :--- |
| \\(\forall x\,P(x)\\) | Se puede **instanciar** en cualquier elemento concreto \\(a\\): se obtiene \\(P(a)\\). |
| \\(\exists x\,P(x)\\) | Se **nombra** un testigo: «Sea \\(x\_0\\) tal que \\(P(x\_0)\\).» |
| \\(P \lor Q\\) | Se procede **por casos**: caso \\(P\\) y caso \\(Q\\). |
| \\(A \subseteq B\\) y \\(a \in A\\) | Se concluye \\(a \in B\\). |
| \\(x \in A \cup B\\) | Se divide en casos: \\(x \in A\\) o \\(x \in B\\). |

> **Advertencia sobre \\(\forall\\) y \\(\exists\\).** El elemento «arbitrario» de una prueba universal es *cualquiera*, no uno elegido por conveniencia. En cambio, el «testigo» de una hipótesis existencial *existe pero no se conoce*: solo puede usarse lo que dice \\(P(x\_0)\\), nada más.

---

## 4. Escribir la Prueba: Normas de Redacción

Una demostración es un texto en prosa matemática. Se recomienda observar estas normas.

1. **Declare las variables antes de usarlas.** Escriba «Sea \\(n \in \mathbb{Z}\\)», no solo «\\(n\\)». Cada símbolo nuevo debe presentarse con su tipo y su cuantificación («sea», «existe», «para todo»).
2. **Distinga el borrador de la prueba.** El borrador explora; la prueba justifica. Nunca entregue el borrador.
3. **Justifique cada paso.** Cada afirmación debe provenir de la hipótesis, de una definición, de un teorema ya demostrado o de los pasos previos. Use «por hipótesis», «por definición de…», «por el Teorema…».
4. **Use conectores lógicos con sentido.** «Por lo tanto», «luego», «ya que», «puesto que», «en consecuencia». El símbolo \\(\implies\\) no es una coma ni una abreviatura de «entonces» en cualquier frase.
5. **Anuncie la estructura.** Diga desde el principio el método: «Procedemos por contraposición», «Por doble contención», «Por inducción sobre \\(n\\)».
6. **Marque el final.** Cierre con \\(\blacksquare\\) (o «c.q.d.») solo cuando la tesis exacta ha sido alcanzada, y repítala si ayuda.
7. **Escriba oraciones completas.** Las fórmulas son parte de la gramática: «Entonces \\(n^2 = 2m\\), con \\(m \in \mathbb{Z}\\).»

---

## 5. Errores Frecuentes

Los siguientes errores aparecen una y otra vez en las primeras demostraciones. Aprender a reconocerlos es parte del oficio.

| Error | Descripción | Ejemplo |
| :--- | :--- | :--- |
| **Probar con ejemplos** | Un ejemplo concreto no prueba un enunciado universal \\(\forall\\). Solo sirve para *refutar* (contraejemplo) o para *probar* un \\(\exists\\). | «\\(n=2\\): \\(n^2 = 4\\) es par; luego el cuadrado de todo par es par.» |
| **Razonamiento circular** | Usar en algún paso lo que se quiere demostrar. | Para probar \\(A \subseteq B\\), escribir «como \\(A \subseteq B\\)…» |
| **Afirmar el consecuente** | Concluir \\(P\\) a partir de \\(P \implies Q\\) y \\(Q\\) (falacia vista en la Unidad 1). | «Si \\(x \in A\\) entonces \\(x \in A\cup B\\); como \\(x \in A \cup B\\), entonces \\(x \in A\\).» |
| **Confundir recíproco y contrarrecíproco** | \\(P \implies Q\\) equivale a \\(\neg Q \implies \neg P\\), **no** a \\(Q \implies P\\). | Probar «si \\(n\\) es par, \\(n^2\\) es par» y declarar probado «si \\(n^2\\) es par, \\(n\\) es par». |
| **Reutilizar un símbolo** | Usar la misma letra para dos objetos distintos. | Dos testigos \\(\exists a\\) y \\(\exists b\\) nombrados ambos «\\(k\\)». |
| **Casos no exhaustivos** | Dividir en casos que no cubren todas las posibilidades. | Analizar solo «\\(x>0\\)» y «\\(x<0\\)», olvidando \\(x=0\\). |
| **Probar solo una contención** | Concluir \\(A = B\\) habiendo probado solo \\(A \subseteq B\\). | Omitir \\(B \subseteq A\\). |
| **Invertir implicaciones** | Escribir cadenas de equivalencias donde solo una dirección es válida. | Elevar al cuadrado ambos lados de una desigualdad sin verificar signos. |

### Ejemplo comentado de una prueba incorrecta

> **Afirmación.** Para todos los conjuntos \\(A, B, C\\): si \\(A \cap B = A \cap C\\), entonces \\(B = C\\).

*Intento de prueba:* «Cancelando \\(A \cap\\) de ambos lados se obtiene \\(B = C\\).»

**Diagnóstico.** No existe una «ley de cancelación» para la intersección; este paso no está justificado por ninguna definición ni teorema. De hecho, el enunciado es **falso**. Un **contraejemplo** lo refuta:

\\[
A = \\{1\\}, \quad B = \\{1, 2\\}, \quad C = \\{1, 3\\}
\\]

Aquí \\(A \cap B = \\{1\\} = A \cap C\\), pero \\(B \neq C\\). Un único contraejemplo basta para refutar un enunciado universal.

> **Moraleja.** Antes de intentar demostrar un enunciado, pruébelo con casos pequeños. Si falla, no hay prueba que buscar; hay un contraejemplo que escribir.

---

## 6. Ejemplo Integral: de la Idea a la Prueba

> **Teorema 4.0.** Para cualesquiera conjuntos \\(A, B, C\\):
>
> \\[
> A \setminus (B \cup C) = (A \setminus B) \cap (A \setminus C)
> \\]

**Lectura.** La tesis es una igualdad de conjuntos; el esqueleto de la sección 3 indica **doble contención**. Las definiciones relevantes son

\\[
x \in X \setminus Y \iff x \in X \land x \notin Y, \qquad x \in X \cup Y \iff x \in X \lor x \in Y
\\]

**Borrador (hacia adelante, con equivalencias).** Para \\(x\\) arbitrario:

\\[
x \in A \setminus (B \cup C) \iff x \in A \land \neg(x \in B \lor x \in C) \iff x \in A \land x \notin B \land x \notin C
\\]

Esto sugiere agrupar de otro modo: \\((x \in A \land x \notin B) \land (x \in A \land x \notin C)\\). Como cada paso es una equivalencia, no será necesario probar dos contenciones por separado, pero **hay que justificar cada \\(\iff\\)**.

**Demostración (versión final).** Sea \\(x\\) un elemento arbitrario del universo. Se tiene la siguiente cadena de equivalencias:

1. \\(x \in A \setminus (B \cup C)\\) \\(\iff\\) \\(x \in A\\) y \\(x \notin B \cup C\\), por definición de diferencia.
2. \\(\iff\\) \\(x \in A\\) y \\(\neg(x \in B \lor x \in C)\\), por definición de unión.
3. \\(\iff\\) \\(x \in A\\) y \\(x \notin B\\) y \\(x \notin C\\), por la ley de De Morgan (Unidad 1).
4. \\(\iff\\) \\((x \in A \land x \notin B) \land (x \in A \land x \notin C)\\), por idempotencia de \\(\land\\) (\\(x \in A\\) se repite).
5. \\(\iff\\) \\(x \in A \setminus B\\) y \\(x \in A \setminus C\\), por definición de diferencia.
6. \\(\iff\\) \\(x \in (A \setminus B) \cap (A \setminus C)\\), por definición de intersección.

Como \\(x\\) era arbitrario, ambos conjuntos tienen los mismos elementos; por extensionalidad, son iguales. \\(\blacksquare\\)

> **Observación.** Esta prueba ilustra el «diccionario» entre lógica y conjuntos (Unidades 1 y 3): una identidad de conjuntos se obtiene traduciendo cada operación a su conectiva y aplicando una equivalencia lógica ya conocida.

---

## 7. Lista de Verificación Final

Antes de entregar una demostración, compruebe:

- [ ] ¿Está claro qué se supone y qué se prueba?
- [ ] ¿Cada variable fue introducida («sea», «existe», «para todo») antes de usarse?
- [ ] ¿Cada paso se justifica con la hipótesis, una definición o un resultado previo?
- [ ] ¿La estructura corresponde a la forma lógica de la tesis (esqueleto de la sección 3)?
- [ ] ¿Se evita probar con ejemplos y se evita suponer la tesis?
- [ ] ¿Si hay casos, son exhaustivos? ¿Si hay una igualdad de conjuntos, se probaron ambas contenciones?
- [ ] ¿La última línea es exactamente la tesis?
- [ ] ¿Un compañero que no conoce el problema podría verificar la prueba sin adivinar nada?

---

## 8. Ejercicios

1. **Esqueleto.** Para cada una de las siguientes tesis, escriba únicamente las **primeras y últimas líneas** de la demostración (el esqueleto de la sección 3), sin completar el cuerpo:
   1. \\(A \cap B \subseteq A \cup B\\)
   2. \\((\forall x \in \mathbb{R})(\exists y \in \mathbb{R})(y > x)\\)
   3. \\(A \subseteq B \iff A \cup B = B\\)
   4. \\(A \cap B = \emptyset \implies A \subseteq B^c\\)

2. **Hacia adelante y hacia atrás.** Demuestre, presentando primero el borrador de dos columnas y después la redacción final: si \\(A \subseteq B\\) y \\(C \subseteq D\\), entonces \\(A \times C \subseteq B \times D\\).

3. **Detecte el error.** Cada «demostración» siguiente es incorrecta. Identifique el error de la tabla de la sección 5 y diga si el enunciado es verdadero o falso:
   1. *Enunciado:* «\\(A \cup B = A \cup C \implies B = C\\).» *Prueba:* «Quitando \\(A\\) de ambos lados queda \\(B = C\\).»
   2. *Enunciado:* «Si \\(A \cap B \subseteq C\\) entonces \\(A \subseteq C\\).» *Prueba:* «Sea \\(x \in A\\). Tomemos \\(x \in B\\) también. Entonces \\(x \in A\cap B \subseteq C\\), luego \\(x \in C\\).»
   3. *Enunciado:* «Si \\(n^2\\) es divisible por 4, entonces \\(n\\) es divisible por 4.» *Prueba:* «\\(n=4\\): \\(n^2 = 16\\) es divisible por 4 y \\(n\\) también.»

4. **Contraejemplo o prueba.** Para cada afirmación decida, probando con casos pequeños, si es verdadera o falsa; si es verdadera, demuéstrela; si es falsa, dé un contraejemplo:
   1. \\(\mathcal{P}(A \cup B) = \mathcal{P}(A) \cup \mathcal{P}(B)\\)
   2. \\(\mathcal{P}(A \cap B) = \mathcal{P}(A) \cap \mathcal{P}(B)\\)
   3. \\(A \times (B \cap C) = (A \times B) \cap (A \times C)\\)

5. **Reescritura.** Tome una demostración de este libro (por ejemplo, la del Teorema 4.2) y escriba su *borrador* de dos columnas: qué se supone, qué se quiere y qué definiciones se desempacaron.
