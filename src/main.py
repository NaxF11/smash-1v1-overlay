import pymem
import time
import json
from datetime import datetime
import game_assets
import sys, os

def output_path(filename):
    """Devuelve un path de salida para archivos generados, fuera del ejecutable."""
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(os.path.dirname(sys.executable), filename)
    
    return os.path.join(os.path.abspath("."), filename)


def cargar_configuracion():
    with open(output_path('config.json'), 'r') as f:
        return json.load(f)


def guardar_datos(p1_wins, p2_wins, player_1, player_2, p1_char, p2_char, p1_damage, p2_damage, music, stage=None, state=None):
    total = p1_wins + p2_wins
    data = {
        "timestamp": datetime.now().strftime('%d/%m/%Y %H:%M'),
        "p1": {
            "name": player_1,
            "wins": p1_wins,
            "win_percent": round((p1_wins/total)*100, 2) if total > 0 else 0,
            "character": game_assets.CHARACTER_IMAGES.get(p1_char, 'random.png'),
            "damage": min(p1_damage, 130)  # Cap damage at 300%
        },
        "p2": {
            "name": player_2,
            "wins": p2_wins,
            "win_percent": round((p2_wins/total)*100, 2) if total > 0 else 0,
            "character": game_assets.CHARACTER_IMAGES.get(p2_char, 'random.png'),
            "damage": min(p2_damage, 130)
        },
        "stage": stage if stage else "Desconocido",
        "playing": music,
        "state": state if state else "Menu",
        "total": total
    }
    
    with open(output_path("overlay/game_data.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)



def main():
    config = cargar_configuracion()
    p1, p2 = config.get("jugador1", "P1"), config.get("jugador2", "P2")

    try:
        mem = pymem.Pymem("Project64KSE.exe")
    except pymem.exception.ProcessNotFound:
        print("Proceso no encontrado.")
        return
    except Exception as e:
        print(f"Error al conectar con el proceso: {e}")
        return

    # Direcciones de memoria
    p1_addr = int(config['muertes_p1_addr'], 16)
    p2_addr = int(config['muertes_p2_addr'], 16)
    stage_addr = int(config.get('Stage', '427F4ADC'), 16)
    p1_char_addr = int(config['character_p1_addr'], 16)
    p2_char_addr = int(config['character_p2_addr'], 16)
    p1_damage_addr = int(config['Damage_P1'], 16)
    p2_damage_addr = int(config['Damage_P2'], 16)
    game_state_addr = int(config['State_Game'], 16)
    ingame_music = int(config['ingame_music'], 16)
    
    stocks = config['stocks_iniciales']
    p1_wins = p2_wins = 0

    # Flags
    victoria_registrada = False
    juego_activo = False

    print("Monitor activo (Ctrl+C para salir)")

    while True:
        try:
            # Leer valores de memoria
            deaths_p1 = mem.read_bytes(p1_addr, 1)[0]
            deaths_p2 = mem.read_bytes(p2_addr, 1)[0]
            stage_id = mem.read_bytes(stage_addr, 1)[0]
            p1_char = mem.read_bytes(p1_char_addr, 1)[0]
            p2_char = mem.read_bytes(p2_char_addr, 1)[0]
            p1_damage = mem.read_int(p1_damage_addr) / 1.0
            p2_damage = mem.read_int(p2_damage_addr) / 1.0
            game_state_id = mem.read_bytes(game_state_addr, 1)[0]
            game_state = game_assets.GAME_STATES.get(game_state_id, "Desconocido")
            stage = game_assets.STAGE_NAMES.get(stage_id, "Desconocido")
            music_id = mem.read_bytes(ingame_music, 1)[0]
            actualMusic = ""
            
            # Lógica para mostrar correctamente el título de la música que está actualmente sonando
            if (stage_id >= 0 and stage_id <= 9) or stage_id == 25 or stage_id == 36 or stage_id == 37:      
                if (game_state_id == 22):
                    actualMusic = game_assets.VANILLA_MUSIC.get(music_id, game_assets.REMIX_MUSIC.get(music_id, "Desconocido"))

            # Activar juego cuando ambos están por debajo del máximo
            if not juego_activo and deaths_p1 < stocks and deaths_p2 < stocks:
                juego_activo = True
                victoria_registrada = False  # permitir una nueva victoria

            # Verificar ganadores
            if juego_activo and not victoria_registrada:
                if deaths_p1 >= stocks:
                    p2_wins += 1
                    victoria_registrada = True
                    juego_activo = False
                    time.sleep(5)
                elif deaths_p2 >= stocks:
                    p1_wins += 1
                    victoria_registrada = True
                    juego_activo = False
                    time.sleep(5)

            # Guardar datos continuamente
            guardar_datos(
                p1_wins, p2_wins, p1, p2,
                p1_char, p2_char,
                p1_damage, p2_damage,
                actualMusic,
                stage, game_state
            )

            time.sleep(0.1)

        except KeyboardInterrupt:
            print("Monitoreo detenido por el usuario.")
            break
        except Exception as e:
            nombreError = type(e).__name__
            if nombreError == "MemoryReadError":
                print("\nError: No se puede leer la memoria en el emulador. \nCausas posibles:\n1) El emulador está cerrado. Por favor, inicia el emulador y vuelve a intentarlo.\n2) Las direcciones de memoria están desactualizadas. Ejecuta el script pointer.py para actualizarlas.")
            else:
                print(f"\nTipo de error: {type(e).__name__}\n")
                print(f"Error inesperado: {str(e)}")
            break


if __name__ == "__main__":
    main()