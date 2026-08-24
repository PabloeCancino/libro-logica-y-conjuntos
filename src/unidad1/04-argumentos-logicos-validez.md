# 1.4 Argumentos Lógicos, Validez Formal y Falacias

El objetivo central de la lógica deductiva es formalizar y analizar los **argumentos**, proporcionando criterios rigurosos e independientes del contenido empírico para discernir entre razonamientos válidos y razonamientos falaces.

---

## 1. Definición Formal de Argumento Deductivo

> **Definición 1.3 (Argumento Lógico):**  
> Un **argumento deductivo** es una estructura lógica compuesta por un conjunto finito de proposiciones \\(p\_1, p\_2, \dots, p\_k\\) llamadas **premisas** (o hipótesis), y una proposición \\(c\\) llamada **conclusión** (o tesis), denotado formalmente por:
> \\[
> p_1, \; p_2, \; \dots, \; p_k \; \vdash \; c \qquad \text{o bien} \qquad \frac{p_1, \; p_2, \; \dots, \; p_k}{\therefore c}
> \\]

---

## 2. Criterio Semántico de Validez

> **Definición 1.4 (Validez de un Argumento):**  
> Un argumento \\(p\_1, p\_2, \dots, p\_k \vdash c\\) es **válido** si y sólo si es **lógicamente imposible** que todas sus premisas sean simultáneamente verdaderas y su conclusión sea falsa.  
> Formalmente, el argumento es válido si la implicación conjuntiva:
> \\[
> (p_1 \land p_2 \land \dots \land p_k) \;\to\; c
> \\]
> es una **Tautología**.

### Verdad Material vs. Validez Formal
Es imprescindible distinguir con absoluta claridad entre:
* **Verdad de una proposición:** propiedad empírica o factual sobre si lo expresado coincide o no con la realidad.
* **Validez de un argumento:** propiedad puramente **estructural y formal** de la relación de implicación entre premisas y conclusión.

Un argumento puede ser **formalmente válido** aun cuando sus premisas sean empíricamente falsas:
> *Premisa 1:* Todos los peces son mamíferos. (Falso)  
> *Premisa 2:* El tiburón es un pez. (Verdadero)  
> *Conclusión:* Por lo tanto, el tiburón es un mamífero. (Falso)  
> $\implies$ **El argumento es formalmente VÁLIDO**, ya que la estructura sigue el esquema riguroso: "Todo \\(A\\) es \\(B\\), \\(x\\) es \\(A\\), luego \\(x\\) es \\(B\\)".

Un argumento es **sólido** (en inglés, *sound*) cuando es **válido** y además todas sus premisas son **materialmente verdaderas**.

---

## 3. Método de Verificación de Validez mediante Tablas de Verdad

Para verificar si un argumento es válido mediante tablas de verdad:
1. Se construye la tabla con todas las variables involucradas.
2. Se evalúan las columnas de cada una de las premisas \\(p\_1, p\_2, \dots, p\_k\\) y de la conclusión \\(c\\).
3. Se identifican las **filas críticas** (aquellas filas donde **TODAS las premisas son simultáneamente Verdaderas**).
4. **Criterio:**
   * Si en **todas** las filas críticas la conclusión \\(c\\) es **Verdadera (\\(V\\))**, el argumento es **VÁLIDO**.
   * Si existe **al menos una fila crítica** donde la conclusión \\(c\\) sea **Falsa (\\(F\\))**, el argumento es **INVÁLIDO** (esa fila proporciona un contraejemplo formal).

---

## 4. Ejemplos de Análisis de Validez

### Ejemplo A: Argumento Válido (Modus Ponens)
Premisas: \\(p \to q\\), \\(p\\). Conclusión: \\(q\\).

| Fila | \\(p\\) | \\(q\\) | Premisa 1: \\(p \to q\\) | Premisa 2: \\(p\\) | Conclusión: \\(q\\) | Estado |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1** | **\\(V\\)** | **\\(V\\)** | **\\(V\\)** | **\\(V\\)** | **\\(V\\)** | **Fila crítica: Conclusión V (Válido)** |
| 2 | \\(V\\) | \\(F\\) | \\(F\\) | \\(V\\) | \\(F\\) | No crítica (Premisa 1 es F) |
| 3 | \\(F\\) | \\(V\\) | \\(V\\) | \\(F\\) | \\(V\\) | No crítica (Premisa 2 es F) |
| 4 | \\(F\\) | \\(F\\) | \\(V\\) | \\(F\\) | \\(F\\) | No crítica (Premisa 2 es F) |

La única fila crítica es la Fila 1 (ambas premisas son \\(V\\)), y allí la conclusión \\(q\\) es \\(V\\). Por lo tanto, el argumento es **válido**.

---

## 5. Falacias Formales Clásicas

Una **falacia formal** es un patrón de inferencia defectuoso que aparenta ser válido pero cuya implicación asociada no es una tautología.

### A. Falacia de Afirmación del Consecuente
Consiste en intentar deducir la hipótesis a partir de la conclusión:

\\[
\frac{p \to q, \quad q}{\therefore p} \quad \text{(INVÁLIDO)}
\\]

*Tabla de verdad:*

| \\(p\\) | \\(q\\) | Premisa 1: \\(p \to q\\) | Premisa 2: \\(q\\) | Conclusión: \\(p\\) | Estado |
| :---: | :---: | :---: | :---: | :---: | :---: |
| \\(V\\) | \\(V\\) | \\(V\\) | \\(V\\) | \\(V\\) | Fila crítica (Conclusión V) |
| **\\(F\\)** | **\\(V\\)** | **\\(V\\)** | **\\(V\\)** | **\\(F\\)** | **¡Fila crítica con Conclusión F! (Inválido)** |
| \\(V\\) | \\(F\\) | \\(F\\) | \\(F\\) | \\(V\\) | No crítica |
| \\(F\\) | \\(F\\) | \\(V\\) | \\(F\\) | \\(F\\) | No crítica |

La fila con \\(p=F, q=V\\) invalida el argumento.  
*Ejemplo en lenguaje natural:* "Si llueve, la calle se moja. La calle está mojada. Por lo tanto, llovió." (Pudo haberse mojado con una manguera).

### B. Falacia de Negación del Antecedente
Consiste en intentar negar la conclusión negando la hipótesis:

\\[
\frac{p \to q, \quad \neg p}{\therefore \neg q} \quad \text{(INVÁLIDO)}
\\]

*Ejemplo en lenguaje natural:* "Si un número termina en 0, es divisible por 5. El número 15 no termina en 0. Por lo tanto, 15 no es divisible por 5." (Falso, 15 sí es divisible por 5).