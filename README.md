# Smash Remix 1.5.2 - OBS Stats Overlay

Este **(overlay)** para *Smash Remix 1.5.2*, está diseñado para mostrar en **OBS** información relevante de las partidas. Usa un sistema de lectura directa de memoria a través de un script en Python, que detecta eventos como muertes, victorias, reinicios, etc. Es ideal para transmisiones donde se quiere mostrar el rendimiento de los jugadores en tiempo real.

## Características

-  Overlay HTML personalizable compatible con OBS (resolución 1080p).
-  Contador de muertes en tiempo real por jugador.
-  Registro de partidas ganadas para cada jugador.
-  Configuración simple mediante archivo `config.json`.
-  Posibilidad de editar libremente el HTML y CSS para adaptar el diseño visual.
-  Probado solamente con Project64KSE

## ⚙️ Cómo compilar
## Para main.exe (Programa principal)

**1. Estructura requerida:**
- ├── main.py            (en directorio raíz)
- ├── game_assets.py     (en directorio raíz)
- ├── config.json        (crear manualmente si no existe)
- ├── overlay/           (carpeta vacía)
- └── main.spec

**2. Compilar:**
- Ejecuta desde la terminal:
   pyinstaller main.spec
- El ejecutable se generará en dist/main.exe.

## Para update_pointers.exe

**1. Estructura requerida:**
- ├── update_pointers.py  (en directorio raíz)
- └── update_pointers.spec

**2. Compilar:**
- Ejecuta desde la terminal:
   pyinstaller update_pointers.spec
- El ejecutable se generará en dist/update_pointers.exe.

## Notas importantes:
Los archivos .spec ya contienen la configuración necesaria para la compilación (incluyendo parámetros como --onefile o --icon).

No es necesario modificar los archivos .spec a menos que requieras cambios en la configuración de PyInstaller.

Los ejecutables generados funcionarán independientemente de su ubicación después de la compilación.


## Lógica de conteo de victorias
  - NO se suma una victoria si los jugadores reinician la partida con Start + A + B + Z + R.

  - SÍ se cuenta una victoria si un jugador gana la partida y hacen "salty runback" justo después de que el juego muestra "GAME SET".
