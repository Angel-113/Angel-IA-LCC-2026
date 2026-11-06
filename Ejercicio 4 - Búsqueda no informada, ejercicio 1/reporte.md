# A* y Greedy Best-First Search

## Diagrama del Subgrafo (Oradea → Bucharest)

Las aristas muestran el costo en kilómetros y cada nodo incluye su heurística $h(n)$ basada en la distancia en línea recta hacia la meta.

```text
                          Oradea (h=380)
                                |
                              (151)
                                |
                          Sibiu (h=253)
                         /             \
                      (99)             (80)
                      /                   \
            Fagaras (h=176)       Rimnicu Vilcea (h=193)
                   |                        |
                 (211)                     (97)
                   |                        |
                   |                  Pitesti (h=100)
                   |                        |
                   +------- (101) ----------+
                           |
                     Bucharest (h=0)
```

**¿A* encontró el camino de menos km? ¿Greedy coincidió o se desvió?**

A* encontró el camino de menor costo con 429 km. Greedy se desvió, resultando en una ruta más costosa de 461 km.

**¿Por qué Greedy puede devolver un camino más caro aunque `h` sea admisible?**

Greedy selecciona el siguiente nodo basándose exclusivamente en el menor valor de $h(n)$ yomite el costo real acumulado $g(n)$. Al llegar a Sibiu,
Greedy eligió Fagaras porque su valor heurístico ($h=176$) es menor que el de Rimnicu Vilcea ($h=193$), ignorando que el trayecto restante
por Fagaras encarece el costo total del viaje.

**En el camino de A*, ¿`f` tiende a no disminuir a lo largo de la ruta?**

El valor de $f(n)$ en A* aumenta de forma constante a lo largo de la ruta ($380 -> 404 -> 424 -> 428 -> 429$).
Este crecimiento monótono ocurre porque la heurística aplicada (distancia en línea recta de la tabla AIMA) es
consistente y admisible, asegurando que el costo estimado no sufra variaciones ilógicas entre nodos sucesivos.
