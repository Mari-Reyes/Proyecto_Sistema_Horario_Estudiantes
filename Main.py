from Funciones import mostrar_horario, agregar_evento, modificar_evento, eliminar_evento   

# ============================================================================
# MENÚ PRINCIPAL
# ============================================================================
# Mostrar horario inicial
mostrar_horario()

while True:      
    print('___________________________________________________________________')
    opciones = input(
        'Que deseas hacer:\n'
        '1. Agregar evento o clase\n'
        '2. Modificar evento o clase\n'
        '3. Eliminar evento o clase\n'
        '4. Generar reporte de horario final\n'
        '5. Salir\n'
        'Selecciona una opción: '
    ).strip().capitalize()
    
    if opciones == '1':
        agregar_evento()  # Llama a la función de agregar
        
    elif opciones == '2':
        modificar_evento()  # Llama a la función de modificar
        
    elif opciones == '3':
        eliminar_evento()  # Llama a la función de eliminar
        
    elif opciones == '4':
        mostrar_horario()  # Llama a la función de mostrar
    
    elif opciones == '5':
        print('')
        print('Saliendo del programa...')
        break
    
    else:
        print(' Opción no válida. Por favor, selecciona una opción válida.')