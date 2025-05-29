import pymem
import pymem.process
import json

def calcularDirecciones():
    try:
        mem = pymem.Pymem("Project64KSE.exe")
        
        # Obtener la dirección base del módulo
        module = pymem.process.module_from_name(mem.process_handle, "Project64KSE.exe")
        module_base = module.lpBaseOfDll
        
        # Calcular la dirección Project64KSE.exe+9264C
        offset = 0x9264C
        target_address = module_base + offset
        
        # Leer el valor en esa dirección (que es 46680000)
        base_value = pymem.memory.read_int(mem.process_handle, target_address)
        
        # Convertir offsets a enteros
        offset_p1 = 0x000A4D38
        offset_p2 = 0x000A4DAC
        offset_stage = 0x000A4D0A
        offset_dmg_p1 = 0x00131598
        offset_dmg_p2 = 0x00131604
        offset_char_p1 = 0x000A4D28
        offset_char_p2 = 0x000A4D9C
        offset_ingame_music = 0x0013139C

        # Calcular direcciones sumando
        direcciones = {
            "jugador1": "",
            "jugador2": "",
            "stocks_iniciales": 4,
            "muertes_p1_addr": hex(base_value + offset_p1),
            "muertes_p2_addr": hex(base_value + offset_p2),
            "State_Game": hex(base_value + offset_p2)[:6] + "4AD3",
            "Stage": hex(base_value + offset_stage),
            "Damage_P1": hex(base_value + offset_dmg_p1),
            "Damage_P2": hex(base_value + offset_dmg_p2),
            "character_p1_addr": hex(base_value + offset_char_p1),
            "character_p2_addr": hex(base_value + offset_char_p2),
            "ingame_music": hex(base_value + offset_ingame_music)
        }

        with open("config.json", "w", encoding="utf-8") as f:
            json.dump(direcciones, f, ensure_ascii=False, indent=4)
            
        print("Direcciones calculadas correctamente:")
        print(json.dumps(direcciones, indent=4))
        salida = input("Datos cargados exitosamente! Ahora escribe los nombres de los jugadores en config.json para tener la configuración completa.")
        
    except Exception as e:
        print(f"Error: {e}")

calcularDirecciones()



    
