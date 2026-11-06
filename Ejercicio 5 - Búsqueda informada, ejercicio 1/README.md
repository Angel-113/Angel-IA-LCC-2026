# Ejercicio 1 — Greedy y A* en el mapa de Rumania

Elegí Timisoara → Bucharest, una de las parejas que sugería el ejercicio.

Mi razonamiento fue que desde Timisoara hay dos salidas muy distintas entre sí.

Una va hacia Arad y Sibiu, y la otra baja hacia Lugoj y Mehadia.

Como el destino es Bucharest, la heurística es la tabla AIMA de línea recta.

Con el script revisé que esa h es consistente en todas las aristas del mapa.

## Subgrafo

Dibujé solo las ciudades que aparecen en alguno de los dos caminos obtenidos.

Las aristas llevan sus km y cada ciudad lleva su h entre paréntesis.

```text
   Arad (366) ───140─── Sibiu (253) ──80─── Rimnicu Vilcea (193) ──97─── Pitesti (100) ───101─── Bucharest (0)
        │                                             │                        │
        │ 118                                         │ 146                    │ 138
        │                                             │                        │
 Timisoara (329)                                Craiova (160) ─────────────────┘
        │                                             │
        │ 111                                         │ 120
        │                                             │
   Lugoj (244) ───70─── Mehadia (241) ───75──── Drobeta (242)
```

## Aristas del subgrafo

| Ciudad A | Ciudad B | km |
|---|---|---:|
| Timisoara | Arad | 118 |
| Timisoara | Lugoj | 111 |
| Lugoj | Mehadia | 70 |
| Mehadia | Drobeta | 75 |
| Drobeta | Craiova | 120 |
| Craiova | Pitesti | 138 |
| Craiova | Rimnicu Vilcea | 146 |
| Pitesti | Bucharest | 101 |
| Pitesti | Rimnicu Vilcea | 97 |
| Arad | Sibiu | 140 |
| Sibiu | Rimnicu Vilcea | 80 |

## Los dos caminos

Debajo de cada ciudad anoté sus valores de g, h y f, en ese orden.

Primero el camino de Greedy, que termina costando 615 km en total.

```text
Timisoara     ──111──▶  Lugoj        ──70──▶  Mehadia      ──75──▶  Drobeta
(0/329/329)             (111/244/355)         (181/241/422)         (256/242/498)

   ──120──▶  Craiova      ──138──▶  Pitesti      ──101──▶  Bucharest
             (376/160/536)          (514/100/614)          (615/0/615)
```

Ahora el camino de A*, que termina costando 536 km en total.

```text
Timisoara     ──118──▶  Arad         ──140──▶  Sibiu
(0/329/329)             (118/366/484)           (258/253/511)

   ──80──▶  Rimnicu Vilcea  ──97──▶  Pitesti      ──101──▶  Bucharest
            (338/193/531)            (435/100/535)          (536/0/536)
```

## Tabla comparativa

| Algoritmo | Path | Depth | Cost | Expanded | Heurística |
|---|---|---:|---:|---:|---|
| Greedy | Timisoara → Lugoj → Mehadia → Drobeta → Craiova → Pitesti → Bucharest | 6 | 615 km | 6 | Tabla AIMA |
| A* | Timisoara → Arad → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest | 5 | 536 km | 10 | Tabla AIMA |

## Respuestas al reporte

### 1. ¿A* encontró el camino de menos km? ¿Greedy coincidió?

Sí, A* encontró el camino de menos km: 536 km pasando por Arad.

Para no fiarme solo del programa, calculé el óptimo aparte con Dijkstra.

También dio 536 km, así que ahí no hay duda de que A* acertó.

Greedy no coincidió: se fue por Lugoj, Mehadia, Drobeta y Craiova, con 615 km.

Son 79 km de más, casi un 15 por ciento sobre el óptimo.

Algo que no esperaba es que Greedy expandió menos nodos, seis contra diez.

O sea que trabajó menos, pero el camino que entregó es peor.

### 2. ¿Por qué Greedy puede salir más caro aunque h sea admisible?

Al principio pensé que si h es admisible, Greedy también debería salir bien.

Pero admisible solo significa que h nunca sobreestima lo que falta por recorrer.

Esa garantía protege a A*, porque A* suma g. Greedy ignora g por completo.

Greedy solo se pregunta qué ciudad se ve más cerca de Bucharest en línea recta.

Desde Timisoara, Lugoj (h = 244) se ve mucho mejor que Arad (h = 366).

Hasta ahí A* está de acuerdo, porque f(Lugoj) = 355 y f(Arad) = 484.

La diferencia real aparece después de expandir Mehadia, que es mi punto de decisión.

En ese momento la frontera tiene a Drobeta (h = 242) y a Arad (h = 366).

Greedy elige Drobeta, porque 242 es menor que 366, sin mirar cuánto lleva pagado.

A* calcula f(Drobeta) = 256 + 242 = 498 y f(Arad) = 118 + 366 = 484.

Como 484 es menor, A* regresa a Arad y deja de lado esa rama.

Creo que el fondo del problema es que la línea recta ignora los rodeos.

De Craiova a Pitesti la línea recta mejora 60 km, pero cuesta 138.

Además Greedy se detiene apenas llega al destino, sin comparar alternativas con otros caminos.

```text
              g     h     f
Drobeta     256   242   498   ← Greedy la elige (h = 242 < 366)
Arad        118   366   484   ← A* la elige    (f = 484 < 498)
```

### 3. ¿f tiende a no disminuir en el camino de A*?

En el camino de A*, f va 329, 484, 511, 531, 535 y 536.

Nunca baja, y el último valor coincide con el costo real, porque h(Bucharest) = 0.

Quise entender por qué pasa esto, y creo que viene de la consistencia.

Consistente significa que h(a) ≤ costo(a, b) + h(b) para cada arista.

Si escribo f(b) = g(a) + costo(a, b) + h(b), entonces f(b) ≥ g(a) + h(a).

Y eso es justamente f(a), así que f no puede bajar al avanzar.

El script confirma que la tabla AIMA cumple esto en todas las aristas del mapa.

Me llamó la atención el salto de 329 a 484 en Arad.

Ahí h sube porque Arad queda más lejos en línea recta que Timisoara.

Aun así no rompe nada, porque el tramo de 118 km compensa esa subida.

También vi que f en el camino de Greedy tampoco baja, de 329 hasta 615.

Entonces no es algo propio de A*, sino de tener una heurística consistente.

Lo que distingue a A* es que usa ese f para decidir qué expandir.

### Trabajo realizado por cada algoritmo

Greedy expandió 6 nodos y generó 15, mientras que A* expandió 10 y generó 27.

A* trabajó más, pero a cambio obtuvo el camino óptimo de 536 km.

Me quedo con que Greedy es rápido pero sin garantías, y A* es más caro.
