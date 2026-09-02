#Sistema de horario de estudiantes
import json

with open('RegistroHorario.json','r') as f:
    horario = json.load(f)

print('')
print('                              HORARIO DE CLASES'                                )
print('_______________________________________________________________________________')
#Horario de clases
# Encabezado
header = f"{'Día':<10} | {'Materia':<15} | {'Horario':<13} | {'Ubicación':<15}"
print(header)
print("-" * len(header))

# Filas
for clase in horario:
    horas = f"{clase['hora_inicio']} - {clase['hora_fin']}"
    print(f"{clase['dia']:<10} | {clase['materia']:<15} | {horas:<13} | {clase['ubicacion']:<15}")
    
while True:      
    print('_________________')
    opciones = input(
    'Que deseas hacer:\n'
    '1.Agregar evento o clase\n'
    '2.Modificar evento o clase\n'
    '3.Eliminar evento o clase\n'
    '4.Salir:').capitalize()
    
    if opciones == '1':
        # Lógica para agregar evento o clase
        print('')
        materia = input('Ingresa el nombre de la materia: ')
        horario.append({'materia': materia})
        dia=input('Ingresa el día de la semana: ')
        horario[-1]['dia'] = dia
        hora_inicio=input('Ingresa la hora de inicio (Segun las horas de clase en el horario original): ')
        horario[-1]['hora_inicio'] = hora_inicio
        hora_fin=input('Ingresa la hora de fin (Segun las horas de clase en el horario original): ')
        horario[-1]['hora_fin'] = hora_fin
        ubicacion=input('Ingresa la ubicación del evento o clase (Aula): ')
        horario[-1]['ubicacion'] = ubicacion

    elif opciones == '2':
        # Lógica para modificar evento o clase
        print('')
        materia = input('Ingresa el nombre de la materia que deseas modificar: ')
        for evento in horario:
            if evento['materia'] == materia:
                dia=input('Ingresa el nuevo día de la semana: ')
                evento['dia'] = dia
                hora_inicio=input('Ingresa la nueva hora de inicio (Segun las horas de clase en el horario original): ')
                evento['hora_inicio'] = hora_inicio
                hora_fin=input('Ingresa la nueva hora de fin (Segun las horas de clase en el horario original): ')
                evento['hora_fin'] = hora_fin
                ubicacion=input('Ingresa la nueva ubicación del evento o clase (Aula): ')
                evento['ubicacion'] = ubicacion
                print('Evento o clase modificada exitosamente.')
                break
            
    elif opciones == '3':
        # Lógica para eliminar evento o clase
        print('')
        materia = input('Ingresa el nombre de la materia que deseas eliminar: ')
        for evento in horario:
            if evento['materia'] == materia:
                horario.remove(evento)
                print('Evento o clase eliminada exitosamente.')
                break
        else:
            print('Materia no encontrada.')
            
    elif opciones == '4':
        print('')
        print('Saliendo del programa...')
        print('Horario final:')
        #print(horario)
        break
    else:
        print('Opción no válida. Por favor, selecciona una opción válida.')
with open('RegistroHorario.json', 'w') as f:
    json.dump(horario, f)