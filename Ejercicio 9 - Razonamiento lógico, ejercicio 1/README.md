# Reporte

## 1. ¿Por qué `Becario(Ana)` sale en el encadenamiento hacia adelante de `AccesoNoche(Ana)` y
no en el de hacia atrás?

En el encadenamiento hacia adelante, el programa simplemente saca todas las conclusiones posibles
a partir de los datos que ya tiene (es dirigido por los datos).
Como Ana es estudiante y tiene credencial, dispara la regla `R_beca` y por
eso genera el átomo de que es becaria. En cambio, cuando uso el
encadenamiento hacia atrás, el algoritmo va directo a la meta; solo busca lo
estrictamente necesario para probar si tiene acceso en la noche. Como saber si
es becaria no sirve de nada para entrar a la biblioteca de noche,
el programa ni siquiera se molesta en revisar esa regla.

## 2. ¿Por qué hacia atrás prueba `R_miembro_est` al buscar `Miembro(Marta)`, si Marta es profesora?

Principalmente por el orden en que escribí las reglas. El algoritmo hacia atrás
lee la base de conocimiento de arriba hacia abajo, tal cual la puse
en el archivo YAML. Como puse la regla de los estudiantes (`R_miembro_est`) antes
que la de los profesores, es la primera que intenta evaluar para ver
si Marta es miembro. Al darse cuenta de que no hay ningún hecho
que diga que Marta es estudiante, falla, y hasta entonces se pasa a
la siguiente regla (`R_miembro_prof`), donde ya confirma que es profesora y acierta.

## 3. Si se añade el hecho `TieneCredencial(Luis)` y se vuelve a preguntar `AccesoNoche(Luis)`, ¿qué
átomos nuevos aparecen y la consulta queda probada?

Por curiosidad hice la prueba agregando el hecho a la base y volví a
correr el script. Como ahora Luis ya cumple con ser estudiante y tener credencial,
el encadenamiento hacia adelante logra sacar átomos nuevos para él. Los que aparecen son
`Miembro(Luis)`, `Becario(Luis)` y `AccesoNoche(Luis)`. Al final, con este cambio, la consulta sí queda probada.
