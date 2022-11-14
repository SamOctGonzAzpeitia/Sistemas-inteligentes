# Sistemas-inteligentes
## Juego de NIM
Este proyecto es un agente con el que puedes practicar el juego de NIM este es un juego matemático
de estrategia en el cual dos jugadores se turnan para quitar objetos de un conjunto. En cada turno, 
un jugador debe eliminar al menos un objeto y puede eliminar el número de objetos que se haya acordado


## Fórmula ganadora
EL jugador que hace el primer movimiento tiene una estrategia ganadora si y solo si la suma nim de los
tamaños de los montones no es cero, de lo contrario el segundo jugador tendría la estrategia ganadora.
Observe que la suma nim (⊕) obedece a las leyes asociativas y conmutativas habituales de la suma (+) 
y también satisface una propiedad adicional, x ⊕ x = 0.


Sean x1, ...,  xn los tamaños de los montones antes de un movimiento, e y1, ...,  yn los tamaños correspondientes 
después de un movimiento. Sea s = x1  ⊕ ... ⊕  xn y t = y1  ⊕ ... ⊕  yn. Si el movimiento fue en 
el montón k, tenemos xi = yi para todo i ≠ k , y xk > yk. Por las propiedades de ⊕ mencionadas anteriormente, tenemos.

El teorema se sigue por inducción sobre la duración del juego a partir de estos dos lemas.

Lema 1: Si s = 0, entonces t ≠ 0 sin importar qué movimiento se haga.

Prueba: si no hay movimiento posible, entonces el lema es vacuo cierto (y el primer jugador pierde el juego normal por definición). De lo contrario, cualquier movimiento en el montón k producirá t = xk ⊕ yk de (*). Este número es distinto de cero, ya que xk ≠ y k.

Lema 2: Si s ≠ 0, es posible hacer un movimiento de modo que t = 0.

Prueba: Sea d la posición del bit distinto de cero más a la izquierda (más significativo) en la representación binaria de s, y elija k tal que el bit d-ésimo de xk 
sea también distinto de cero. (Tal k debe existir, ya que de lo contrario el d-ésimo bit de s sería 0.) Entonces, dejando yk = s ⊕ xk, afirmamos que yk < xk: todos 
los bits a la izquierda de d son iguales en xk y yk, el bit d disminuye de 1 a 0 (disminuyendo el valor en 2d), y cualquier cambio en los bits restantes ascenderá a 
2d−1 como máximo. El primer jugador puede entonces hacer un movimiento tomando xk - yk objetos del montón k
