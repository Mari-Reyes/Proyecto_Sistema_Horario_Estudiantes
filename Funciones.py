#=============================================================================
#SISTEMA HORARIO DE ESTUDIANTES
#=============================================================================
import json
from datetime import datetime

# Cargar el horario al inicio----------------------------------------------------------------------------------------
with open('RegistroHorario.json', 'r', encoding='utf-8') as f:
    horario = json.load(f)
    
    with open('Reportes.json', 'w', encoding='utf-8') as f:
        json.dump(horario, f, ensure_ascii=False, indent=2)

# Lista de días válidos para validación------------------------------------------------------------------------------
DIAS_VALIDOS = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes"]

# ============================================================================
# FUNCIÓN: MOSTRAR HORARIO 
# ============================================================================
def mostrar_horario():
    
    #Muestra el horario de clases en pantalla-----------------------------------------------------------------------
    print('')
    print('                            HORARIO DE CLASES')
    print('________________________________________________________________________')
    header = f"{'Día':<10} | {'Materia':<15} | {'Horario':<13} | {'Ubicación':<15}"
    print(header)
    print("-" * len(header))
    
    for clase in horario:
        horas = f"{clase['hora_inicio']} - {clase['hora_fin']}"
        print(f"{clase['dia']:<10} | {clase['materia']:<15} | {horas:<13} | {clase['ubicacion']:<15}")
        print()

# ============================================================================
# FUNCIÓN: VALIDAR DÍA
# ============================================================================
def validar_dia(dia):
    
#Valida que el día sea uno de los días de la semana--------------------------------------------------------------------
    return dia in DIAS_VALIDOS

# ============================================================================
# FUNCIÓN: VALIDAR HORA
# ============================================================================
def validar_hora(hora):
    
    
#Valida que la hora tenga formato HH:MM-------------------------------------------------------------------------------
    if len(hora) != 5:
        return False
    if hora[2] != ":":
        return False
    try:
        horas = int(hora[0:2])
        minutos = int(hora[3:5])
        return 0 <= horas <= 23 and 0 <= minutos <= 59
    except ValueError:
        return False

# ============================================================================
# FUNCIÓN: VALIDAR DÍA
# ============================================================================
from datetime import datetime

def hay_conflicto(dia, hora_inicio, hora_fin):
    nueva_inicio = datetime.strptime(hora_inicio, "%H:%M")
    nueva_fin = datetime.strptime(hora_fin, "%H:%M")

    for evento in horario:

        if evento["dia"] != dia:
            continue

        existente_inicio = datetime.strptime(
            evento["hora_inicio"], "%H:%M"
        )

        existente_fin = datetime.strptime(
            evento["hora_fin"], "%H:%M"
        )

        if nueva_inicio < existente_fin and nueva_fin > existente_inicio:
            return True

    return False
    
# ============================================================================
# FUNCIÓN 4: AGREGAR EVENTO
# ============================================================================
def agregar_evento():
    
#Agrega una nueva clase o evento al horario----------------------------------------------------------------------------
    print('')
    while True:
        materia = input("Ingresa la nueva materia o evento: ").strip().capitalize()
        
        if materia.replace(" ", "").isalpha():
                break
        print(" Solo se permiten letras.")

    # Validar día-------------------------------------------------------------------------------------------------------
    while True:
        dia = input('Ingresa el día (Lunes a Viernes): ').strip().capitalize()
        if validar_dia(dia):
            break
        print(' Día inválido. Usa un día de Lunes a Viernes.')
    
        # Validar hora inicio--------------------------------------------------------------------------------------------
    while True:
            hora_inicio = input('Ingresa la hora de inicio (HH:MM): ').strip()
            
            if validar_hora(hora_inicio):
                break
            
            print(' Hora inválida. Usa formato HH:MM (ejemplo: 08:00)')
    
        # Validar hora fin------------------------------------------------------------------------------------------------
    while True:
            hora_fin = input('Ingresa la hora de fin (HH:MM): ').strip()
            
            if not validar_hora(hora_fin):
                print(' Hora inválida. Usa formato HH:MM (ejemplo: 10:00)')
                continue
            
            if hora_fin <= hora_inicio:
                print(' La hora de fin debe ser mayor que la hora de inicio.')
                continue
            break
    
    ubicacion = input('Ingresa la ubicación del evento o clase (Ingresa el numero de aula):  ')

    # Verificar conflictos--------------------------------------------------------------------------------------------
    if hay_conflicto(dia, hora_inicio, hora_fin):
        print(" Ya existe una clase o evento en ese horario.")
        return

        # Agregar al horario-------------------------------------------------------------------------------------------
    horario.append({
        'materia': materia,
        'dia': dia,
        'hora_inicio': hora_inicio,
        'hora_fin': hora_fin,
        'ubicacion': 'Aula  ' + ubicacion
    })
    
    # Guardar en el archivo---------------------------------------------------------------------------------------------------
    with open('RegistroHorario.json', 'w', encoding='utf-8') as f:
        json.dump(horario, f, ensure_ascii=False, indent=2)
        
    with open('Reportes.json', 'w', encoding='utf-8') as f:
        json.dump(horario, f, ensure_ascii=False, indent=2)
    
print(' Evento o clase agregada exitosamente.')
    

# ============================================================================
# FUNCIÓN 5: MODIFICAR EVENTO 
# ============================================================================
def modificar_evento():
    
    #Modifica una clase o evento existente------------------------------------------------------------------------------
    print('')
    materia_buscar = input('Ingresa la materia que deseas modificar: ').strip().capitalize()
    
    # Buscar la materia---------------------------------------------------------------------------------------------------
    coincidencias = [i for i in horario if i['materia'].capitalize() == materia_buscar]
    if not coincidencias:
        print(f"No se encontró la materia '{materia_buscar}'.")
        return

    # 2. Mostrar las opciones especificando el DÍA de cada clase------------------------------------------------------------
    print(f'\n--- Días disponibles para la materia "{materia_buscar.title()}" ---')
    for i, evento in enumerate(coincidencias, 1):
        print(f'{i}. Día: {evento["dia"]} ({evento["hora_inicio"]} - {evento["hora_fin"]}) | Ubicación: {evento["ubicacion"]}')
        
        # El usuario elige el día según el número de opción-----------------------------------------------------------------------------
    while True:
        try:
            opcion = int(input('\nSelecciona el número del día que deseas modificar: '))
        except ValueError:
            print('Ingresa un número válido.')
            continue

        if 1 <= opcion <= len(coincidencias):
            break
        print(f'Opción inválida. Elige un número entre 1 y {len(coincidencias)}.')

    # Evento seleccionado------------------------------------------------------------------------------------------------------
    evento = coincidencias[opcion - 1]
    print(f'\nModificando la clase del día {evento["dia"]}:')
            
    # Validar nuevo día---------------------------------------------------------------------------------------------------------
    while True:
        nuevo_dia = input(f'Ingresa el nuevo día (actual: {evento["dia"]}): ').strip().capitalize()
        if validar_dia(nuevo_dia):
            evento['dia'] = nuevo_dia
            break
        print(f' Día inválido. Usa: {", ".join(DIAS_VALIDOS)}')
            
    # Validar nueva hora inicio---------------------------------------------------------------------------------------
    while True:
        nueva_hora_inicio = input(f'Ingresa la nueva hora de inicio (actual: {evento["hora_inicio"]}): ')
        if validar_hora(nueva_hora_inicio):
            evento['hora_inicio'] = nueva_hora_inicio
            break
        print(' Hora inválida. Usa formato HH:MM (ejemplo: 08:00)')
                        
    # Validar nueva hora fin----------------------------------------------------------------------------------------------
    while True:
        nueva_hora_fin = input(f'Ingresa la nueva hora de fin (actual: {evento["hora_fin"]}): ')
        if not validar_hora(nueva_hora_fin):
            print(' Hora inválida. Usa formato HH:MM (ejemplo: 10:00)')
        elif nueva_hora_fin <= evento['hora_inicio']:
            print(' La hora de fin debe ser mayor que la hora de inicio.')
        else:
            evento['hora_inicio'] = nueva_hora_inicio
            evento['hora_fin'] = nueva_hora_fin
            break
            
    # Ubicación (sin validación)----------------------------------------------------------------------------------------------
    nueva_ubicacion = input(f'Ingresa la nueva ubicación (actual: {evento["ubicacion"]}):').strip().capitalize()
    evento['ubicacion'] = 'Aula ' + nueva_ubicacion
            
    # Guardar cambios-------------------------------------------------------------------------------------------------------------
    with open('RegistroHorario.json', 'w', encoding='utf-8') as f:
        json.dump(horario, f, ensure_ascii=False, indent=2)
                
    with open('Reportes.json', 'w', encoding='utf-8') as f:
        json.dump(horario, f, ensure_ascii=False, indent=2)
            
    print(' Evento o clase modificada exitosamente.')
    
    if len(coincidencias) == 0:
        print('Materia no encontrada.')
    return


# ============================================================================
# FUNCIÓN: ELIMINAR EVENTO
# ============================================================================
def eliminar_evento():
    #Elimina una clase o evento del horario------------------------------------------------------------------------------------
            
    print('')
    materia_buscar = input('Ingresa la materia o evento que deseas eliminar: ').strip().capitalize()

    coincidencias = [
        i for i in horario
        if i['materia'].capitalize() == materia_buscar
]

    # Validar si existe la materia------------------------------------------------------------------------------------------
    if not coincidencias:
        print('Materia no encontrada.')
        return 

    # Mostrar las opciones encontradas---------------------------------------------------------------------------------------
    print(f'\n--- Días disponibles para la materia "{materia_buscar.title()}" ---')
    for i, evento in enumerate(coincidencias, 1):
        print(f'{i}. Día: {evento["dia"]} ({evento["hora_inicio"]} - {evento["hora_fin"]}) | Ubicación: {evento["ubicacion"]}')
        
    # El usuario elige el día según el número de opción----------------------------------------------------------------------------------
    while True:
                try:
                    opcion = int(input('\nSelecciona el número del día que deseas eliminar: '))
                    if 1 <= opcion <= len(coincidencias):  
                        break
                    print(f'Opción inválida. Elige un número entre 1 y {len(coincidencias)}.')
                except ValueError:
                    print('Ingresa un número válido.')

                    evento_eliminar = coincidencias[opcion - 1]
                    horario.remove(evento_eliminar)
            
            # Guardar cambios
    with open('RegistroHorario.json', 'w', encoding='utf-8') as f:
                json.dump(horario, f, ensure_ascii=False, indent=2)
                
    with open('Reportes.json', 'w', encoding='utf-8') as f:
                json.dump(horario, f, ensure_ascii=False, indent=2)
                
                print('')
                print('Evento o clase eliminada exitosamente.')
        