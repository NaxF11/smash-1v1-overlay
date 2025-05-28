# Smash Remix 1.5.2 - OBS Stats Overlay

Este **(overlay)** para *Smash Remix 1.5.2*, está diseñado para mostrar en **OBS** información relevante de las partidas. Usa un sistema de lectura directa de memoria a través de un script en Python, que detecta eventos como muertes, victorias, reinicios, etc. Es ideal para transmisiones donde se quiere mostrar el rendimiento de los jugadores en tiempo real.

## Características

-  Overlay HTML personalizable compatible con OBS (resolución 1080p).
-  Contador de muertes en tiempo real por jugador.
-  Registro de partidas ganadas para cada jugador.
-  Configuración simple mediante archivo `config.json`.
-  Posibilidad de editar libremente el HTML y CSS para adaptar el diseño visual.
-  Probado solamente con Project64KSE

## ⚙️ Cómo usar

1. **Ejecuta `update_pointers.py`**
   - Esto generará las direcciones de memoria necesarias para el funcionamiento del overlay.

2. **Configura los nombres de los jugadores**
   - Abre el archivo `config.json` y edita los campos correspondientes para el nombre del **Player 1** y **Player 2**.

   **json**
   {
     "player1_name": "Jugador1",
     "player2_name": "Jugador2"
   }

3. Carga el ROM de Smash Remix 1.5.2 en el emulador **Project64KSE**

4. Ejecuta main.py
   - Asegúrate de que el juego esté corriendo. El script comenzará a actualizar los stats en tiempo real.

5. Coloca el archivo HTML como fuente en OBS
   - Puedes añadir el archivo HTML generado como una fuente de navegador en OBS para mostrar el overlay con las estadísticas.


**Lógica de conteo de victorias**
  - NO se suma una victoria si los jugadores reinician la partida con Start + A + B + Z + R.

  - SÍ se cuenta una victoria si un jugador gana la partida y hacen "salty runback" justo después de que el juego muestra "GAME SET".
