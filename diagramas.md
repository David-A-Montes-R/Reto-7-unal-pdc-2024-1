# diagrama punto 1:
```mermaid
flowchart 

A(iniciar programa) -->B[definir ''a'' como 1 ]
B --> C{¿Es ''a'' menor a 100?}
C-->|sí| D[elevar ''a'' al cuadrado]
D -->E[ imprimir ''a'' y su respectivo cuadrado]
E -->F[sumar 1 a ''a'']
F-->C
C-->|no| G(finalizar el programa)
```
# diagrama punto 2:

```mermaid
flowchart
A(iniciar programa) -->B[definir ''a'' como 1 y ''b'' como 2]
B-->C[imprimir: ''la lista de los números impares desde 1 hasta 999 son:'']
C-->H[imprimir ''a'']
H-->D{¿es ''a'' menor a 999? }
D -->|sí|E[sumar 2 a ''a'' e imprimir ''a'']
E-->D
D-->|no|I[imprimir ''la lista de los números pares desde 2 hasta mil son:'']
I-->J[imprimir ''b'']
J-->F
F{¿Es ''b'' menor a 1000?}
F-->|sí| G[sumar 2 a ''b'' e imprimir ''b'']
G-->F
F-->|no|K(finalizar programa)
```
# diagrama del punto 3:
```mermaid
flowchart
A(Iniciar programa)-->B[solicitar un número natural n]
B-->C{¿Es n mayor o igual a 2?}
C-->|sí|D{¿Es n un número par?}
C-->|no|E[solicitar que por favor el usuario solo ingrese números naturales mayores o iguales a 2]
E-->Z(finalizar el programa)

D-->|sí|F{¿Es n mayor a 2?}
F-->|sí|G[imprimir n y restarle 2]-->F
D-->|no|H[restarle 1 a n]-->F
F-->|no|I[imprimir n]-->Z