# Ejercicios de la Unidad 1

---

## 📝 Bloque A: Formalización y Clasificación de Enunciados

1. Determine cuáles de los siguientes enunciados son proposiciones lógicas y, en caso afirmativo, asigne su valor de verdad:
 - a) \\(p\\): "La suma de los ángulos interiores de todo triángulo euclidiano es \\(180^\circ\\)."
 - b) "¿Existe un número primo par mayor que 2?"
 - c) \\(q\\): "\\(3^2 + 4^2 = 5^2\\)."
 - d) "Resuelve la ecuación diferencial \\(y' = 2xy\\)."
 - e) \\(r\\): "Para todo número entero \\(n\\), el producto \\(n(n+1)\\) es divisible por 2."

2. Simbolice formalmente los siguientes enunciados definiendo explícitamente sus proposiciones atómicas:
 - a) "Si una función es derivable, entonces es continua; pero si no es continua, entonces no es derivable."
 - b) "Un número entero es par si y sólo si su cuadrado es par."
 - c) "El sistema de ecuaciones lineales tiene solución única o tiene infinitas soluciones, pero no ambas."

---

## 📝 Bloque B: Tablas de Verdad y Clasificación Semántica

3. Construya la tabla de verdad exhaustiva de cada una de las siguientes fórmulas proposicionales y clasifíquelas en **Tautología**, **Contradicción** o **Contingencia**:
 - a) \\(A = [p \land (p \to q)] \to q\\)
 - b) \\(B = (p \lor q) \land (\neg p \land \neg q)\\)
 - c) \\(C = (p \to q) \leftrightarrow (\neg q \to \neg p)\\)
 - d) \\(D = (p \to q) \land (q \to r) \to (p \to r)\\)
 - e) \\(E = [(p \lor q) \land \neg p] \to q\\)

---

## 📝 Bloque C: Simplificación Algebraica y Leyes de De Morgan

4. Utilizando únicamente las leyes del álgebra de proposiciones (sin construir tablas de verdad), demuestre las siguientes equivalencias lógicas indicando la ley empleada en cada paso:
 - a) \\(\neg(p \to q) \equiv p \land \neg q\\)
 - b) \\(p \lor (p \land q) \equiv p\\)
 - c) \\((p \land q) \lor (p \land \neg q) \equiv p\\)
 - d) \\(\neg(p \lor (\neg p \land q)) \equiv \neg p \land \neg q\\)

---

## 📝 Bloque D: Validez de Argumentos y Falacias

5. Analice la validez de los siguientes esquemas de argumento mediante el método de tablas de verdad o deducción por reglas de equivalencia:
 - a) Premisas: \\(p \to \neg q\\), \\(q\\). Conclusión: \\(\neg p\\).
 - b) Premisas: \\(p \lor q\\), \\(p \to r\\), \\(q \to r\\). Conclusión: \\(r\\).
 - c) Premisas: \\(p \to q\\), \\(\neg p\\). Conclusión: \\(\neg q\\). (¿Es válido o falaz?).
 - d) Premisas: \\(p \leftrightarrow q\\), \\(q \leftrightarrow r\\). Conclusión: \\(p \leftrightarrow r\\).

---

## 📝 Bloque E: Demostraciones Básicas — de la Tabla al Álgebra y a los Argumentos

Este bloque sigue el orden de la unidad: primero verificación **semántica** (tablas, sección 1.2 y 1.3), luego demostración **algebraica** (leyes de la sección 1.3) y, al final, **validez de argumentos** (sección 1.4).

6. Demuestre por tabla de verdad la ley distributiva \\(p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)\\). ¿Cuántas filas necesita y por qué?

7. Demuestre por cadena de equivalencias, indicando la ley de cada paso, la **ley de exportación** \\(p \to (q \to r) \equiv (p \land q) \to r\\).
 *Sugerencia:* escriba cada condicional como disyunción (sección 1.3, §5.A).

8. Demuestre por cadena de equivalencias que \\((p \to q) \land (p \to r) \equiv p \to (q \land r)\\).

9. Demuestre por cadena de equivalencias que \\((p \to r) \land (q \to r) \equiv (p \lor q) \to r\\), e interprételo con palabras: «si cada una de dos causas produce \\(r\\), entonces cualquiera de ellas lo produce».

10. Analice mediante tablas de verdad la validez de cada argumento. En los inválidos, señale la fila que lo refuta:
 - a) Premisas: \\(p \lor q\\), \\(\neg p\\). Conclusión: \\(q\\).
 - b) Premisas: \\(p \lor q\\), \\(p\\). Conclusión: \\(\neg q\\).
 - c) Premisas: \\(p \to q\\), \\(\neg q\\). Conclusión: \\(\neg p\\).

---

## 💡 Soluciones y Guías Seleccionadas

> **Solución al Ejercicio 3.a:** 
> \\(A = [p \land (p \to q)] \to q\\). 
> * Para \\(p=V, q=V\\): \\([V \land (V \to V)] \to V = [V \land V] \to V = V \to V = V\\). 
> * Para \\(p=V, q=F\\): \\([V \land (V \to F)] \to F = [V \land F] \to F = F \to F = V\\). 
> * Para \\(p=F, q=V\\): \\([F \land (F \to V)] \to V = [F \land V] \to V = F \to V = V\\). 
> * Para \\(p=F, q=F\\): \\([F \land (F \to F)] \to F = [F \land V] \to F = F \to F = V\\). 
> La fórmula es verdadera en las cuatro combinaciones: es una **Tautología** (el esquema formal de *Modus Ponens*).

> **Solución al Ejercicio 4.c:** 
> \\((p \land q) \lor (p \land \neg q)\\) 
> \\(\equiv p \land (q \lor \neg q)\\) por la Ley Distributiva de \\(\land\\) sobre \\(\lor\\). 
> \\(\equiv p \land \top\\) por la Ley del Complemento (Tercio Excluso \\(q \lor \neg q \equiv \top\\)). 
> \\(\equiv p\\) por la Ley de Identidad. \\(\blacksquare\\)

---

## 💡 Soluciones del Bloque E (Ejercicios 6 a 10)

<details>
<summary><strong>Mostrar / ocultar las soluciones de los Ejercicios 6 a 10</strong></summary>

**Ejercicio 6.** Con 3 variables hay \\(2^3 = 8\\) interpretaciones.

| \\(p\\) | \\(q\\) | \\(r\\) | \\(q \land r\\) | \\(p \lor (q \land r)\\) | \\(p \lor q\\) | \\(p \lor r\\) | \\((p \lor q) \land (p \lor r)\\) |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| V | V | V | V | **V** | V | V | **V** |
| V | V | F | F | **V** | V | V | **V** |
| V | F | V | F | **V** | V | V | **V** |
| V | F | F | F | **V** | V | V | **V** |
| F | V | V | V | **V** | V | V | **V** |
| F | V | F | F | **F** | V | F | **F** |
| F | F | V | F | **F** | F | V | **F** |
| F | F | F | F | **F** | F | F | **F** |

Las columnas quinta y octava coinciden en las ocho filas. \\(\blacksquare\\)

**Ejercicio 7.** Ley de exportación.

| Paso | Fórmula | Justificación |
| :---: | :--- | :--- |
| 1 | \\(p \to (q \to r)\\) | Punto de partida |
| 2 | \\(\neg p \lor (\neg q \lor r)\\) | Definición del condicional (dos veces) |
| 3 | \\((\neg p \lor \neg q) \lor r\\) | Asociatividad de \\(\lor\\) |
| 4 | \\(\neg(p \land q) \lor r\\) | De Morgan: \\(\neg p \lor \neg q \equiv \neg(p \land q)\\) |
| 5 | \\((p \land q) \to r\\) | Definición del condicional |

\\(\blacksquare\\)

**Ejercicio 8.**

| Paso | Fórmula | Justificación |
| :---: | :--- | :--- |
| 1 | \\((p \to q) \land (p \to r)\\) | Punto de partida |
| 2 | \\((\neg p \lor q) \land (\neg p \lor r)\\) | Definición del condicional |
| 3 | \\(\neg p \lor (q \land r)\\) | Distributividad de \\(\lor\\) sobre \\(\land\\) (leída de derecha a izquierda) |
| 4 | \\(p \to (q \land r)\\) | Definición del condicional |

\\(\blacksquare\\)

**Ejercicio 9.**

| Paso | Fórmula | Justificación |
| :---: | :--- | :--- |
| 1 | \\((p \to r) \land (q \to r)\\) | Punto de partida |
| 2 | \\((\neg p \lor r) \land (\neg q \lor r)\\) | Definición del condicional |
| 3 | \\((\neg p \land \neg q) \lor r\\) | Distributividad de \\(\lor\\) sobre \\(\land\\) (de derecha a izquierda), con \\(r\\) como factor común |
| 4 | \\(\neg(p \lor q) \lor r\\) | De Morgan: \\(\neg p \land \neg q \equiv \neg(p \lor q)\\) |
| 5 | \\((p \lor q) \to r\\) | Definición del condicional |

\\(\blacksquare\\) *Interpretación:* la equivalencia justifica el análisis «por casos»: para probar que \\(p \lor q\\) implica \\(r\\) basta probar cada caso por separado.

**Ejercicio 10.**

| \\(p\\) | \\(q\\) | \\(p \lor q\\) | \\(\neg p\\) | \\(\neg q\\) | \\(p \to q\\) |
| :---: | :---: | :---: | :---: | :---: | :---: |
| V | V | V | F | F | V |
| V | F | V | F | V | F |
| F | V | V | V | F | V |
| F | F | F | V | V | V |

* **a) Válido.** Las premisas \\(p \lor q\\) y \\(\neg p\\) son verdaderas a la vez solo en la fila 3 (\\(p = F,\ q = V\\)), y allí \\(q\\) es verdadera. (Es el silogismo disyuntivo, sección 2.3.)
* **b) Inválido.** En la fila 1 (\\(p = V,\ q = V\\)) las premisas \\(p \lor q\\) y \\(p\\) son verdaderas, pero la conclusión \\(\neg q\\) es falsa. Es la falacia de tratar la disyunción *inclusiva* como si fuera exclusiva.
* **c) Válido.** Las premisas \\(p \to q\\) y \\(\neg q\\) son verdaderas a la vez solo en la fila 4 (\\(p = F,\ q = F\\)), y allí \\(\neg p\\) es verdadera. (Es el modus tollens, sección 2.3.)

</details>
