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
   - a) \\(\neg(p \to q) \;\equiv\; p \land \neg q\\)
   - b) \\(p \lor (p \land q) \;\equiv\; p\\)
   - c) \\((p \land q) \lor (p \land \neg q) \;\equiv\; p\\)
   - d) \\(\neg(p \lor (\neg p \land q)) \;\equiv\; \neg p \land \neg q\\)

---

## 📝 Bloque D: Validez de Argumentos y Falacias

5. Analice la validez de los siguientes esquemas de argumento mediante el método de tablas de verdad o deducción por reglas de equivalencia:
   - a) Premisas: \\(p \to \neg q\\), \\(q\\). Conclusión: \\(\neg p\\).
   - b) Premisas: \\(p \lor q\\), \\(p \to r\\), \\(q \to r\\). Conclusión: \\(r\\).
   - c) Premisas: \\(p \to q\\), \\(\neg p\\). Conclusión: \\(\neg q\\). (¿Es válido o falaz?).
   - d) Premisas: \\(p \leftrightarrow q\\), \\(q \leftrightarrow r\\). Conclusión: \\(p \leftrightarrow r\\).

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