# Reporte

## 1. Tabla Comparativa de Ejecuciones

| Algoritmo | Status | Path | Depth (roads) | Cost (km) | Nodos Expandidos |
| --- | --- | --- | --- | --- | --- |
| **BFS** | success | Oradea → Sibiu → Fagaras → Bucharest | 3 | 461 | 5 |
| **UCS** | success | Oradea → Sibiu → Rimnicu Vilcea → Pitesti → Bucharest | 4 | 429 | 10 |
| **DFS** | success | Oradea → Sibiu → Arad → Timisoara → Lugoj → Mehadia → Drobeta → Craiova → Pitesti → Bucharest | 9 | 1024 | 9 |
| **DLS** (`--limit 2`) | cutoff | Ninguno | N/A | N/A | 3 |
| **DLS** (`--limit 4`) | success | Oradea → Sibiu → Fagaras → Bucharest | 3 | 461 | 6 |
| **IDS** | success | Oradea → Sibiu → Fagaras → Bucharest | 3 | 461 | 8 |

## 2. Reporte Analítico

### Comparación entre BFS y UCS

BFS encuentra el camino con el menor número de carreteras, obteniendo una ruta de 3 saltos y 461 km a través de Fagaras.
UCS encuentra el camino con la menor distancia total, resultando en una ruta de 429 km y 4 saltos a través de Rimnicu Vilcea.
BFS optimiza la profundidad, mientras que UCS optimiza el costo acumulado.
UCS expande 10 nodos frente a los 5 de BFS, requiriendo más procesamiento para garantizar el costo mínimo en distancia.

### Comportamiento de DFS

DFS devuelve un trayecto ineficiente de 9 carreteras y 1024 km porque no ofrece garantías de optimalidad.
Al expandir los nodos vecinos en estricto orden alfabético, el algoritmo toma una decisión subóptima en Sibiu dirigiéndose hacia Arad,
lo que desvía la búsqueda por una ruta mucho más larga antes de alcanzar el destino.

### Límites en DLS y relación con BFS e IDS

La ejecución de DLS con `--limit 2` arroja un estado `cutoff` porque la solución más próxima requiere más de dos saltos.
Al incrementar a `--limit 4`, el algoritmo encuentra la meta exitosamente.
Este comportamiento coincide directamente con los hallazgos de BFS e IDS, donde este último confirma que la profundidad
de la solución óptima en carreteras es exactamente de 3 saltos, deteniéndose en su iteración `last_limit=3`.
