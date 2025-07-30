# PROYECTO: SISTEMA DE GESTIÓN DE TAREAS - VERSIÓN COMPLETA
# 
# DESCRIPCIÓN: Un programa que permite al usuario gestionar una lista de tareas
# Este proyecto integra todos los conceptos aprendidos hasta ahora
#
# CONCEPTOS APLICADOS:
# - Variables y tipos de datos
# - Input del usuario con validación
# - Condicionales (if/elif/else)
# - Booleanos y operadores lógicos
# - Listas y métodos de listas
# - Bucles while
# - Casting de tipos

import os

def limpiar_pantalla():
    """Función para limpiar la pantalla"""
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_menu():
    """Muestra el menú principal del programa"""
    print("\n" + "="*50)
    print("    SISTEMA DE GESTIÓN DE TAREAS")
    print("="*50)
    print("1. Ver todas las tareas")
    print("2. Agregar nueva tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Buscar tarea")
    print("6. Estadísticas")
    print("7. Salir")
    print("="*50)

# ========== VARIABLES PRINCIPALES ==========
# Lista para almacenar las tareas (cada tarea será una lista con [descripción, completada])
tareas = []
programa_activo = True

# ========== MENSAJE DE BIENVENIDA ==========
limpiar_pantalla()
print("¡Bienvenido al Sistema de Gestión de Tareas!")
nombre_usuario = input("¿Cuál es tu nombre? ")
print(f"¡Hola {nombre_usuario}! Vamos a organizar tus tareas.")

# ========== BUCLE PRINCIPAL DEL PROGRAMA ==========
while programa_activo:
    mostrar_menu()
    
    # Obtener opción del usuario con validación
    opcion = input(f"\n{nombre_usuario}, elige una opción (1-7): ")
    
    # ========== OPCIÓN 1: VER TODAS LAS TAREAS ==========
    if opcion == "1":
        limpiar_pantalla()
        print("📋 LISTA DE TAREAS:")
        print("-" * 40)
        
        if len(tareas) == 0:
            print("No tienes tareas registradas.")
        else:
            # Usar bucle while para mostrar todas las tareas
            contador = 0
            while contador < len(tareas):
                descripcion = tareas[contador][0]
                completada = tareas[contador][1]
                
                if completada:
                    estado = "✅ Completada"
                else:
                    estado = "❌ Pendiente"
                
                print(f"{contador + 1}. {descripcion} - {estado}")
                contador += 1
    
    # ========== OPCIÓN 2: AGREGAR NUEVA TAREA ==========
    elif opcion == "2":
        limpiar_pantalla()
        print("➕ AGREGAR NUEVA TAREA:")
        
        # Pedir descripción de la tarea con validación
        descripcion = input("Describe la tarea: ").strip()
        
        if len(descripcion) == 0:
            print("❌ Error: La descripción no puede estar vacía.")
        else:
            # Agregar tarea como [descripción, False] (False = no completada)
            tareas.append([descripcion, False])
            print(f"✅ Tarea '{descripcion}' agregada exitosamente.")
    
    # ========== OPCIÓN 3: MARCAR TAREA COMO COMPLETADA ==========
    elif opcion == "3":
        limpiar_pantalla()
        print("✅ MARCAR TAREA COMO COMPLETADA:")
        
        if len(tareas) == 0:
            print("No tienes tareas para completar.")
        else:
            # Mostrar solo las tareas pendientes
            print("Tareas pendientes:")
            tareas_pendientes = []
            contador = 0
            
            while contador < len(tareas):
                if not tareas[contador][1]:  # Si no está completada
                    tareas_pendientes.append(contador)
                    print(f"{len(tareas_pendientes)}. {tareas[contador][0]}")
                contador += 1
            
            if len(tareas_pendientes) == 0:
                print("¡Todas las tareas están completadas!")
            else:
                try:
                    seleccion = int(input("¿Qué tarea quieres marcar como completada? "))
                    
                    if 1 <= seleccion <= len(tareas_pendientes):
                        indice_real = tareas_pendientes[seleccion - 1]
                        tareas[indice_real][1] = True
                        print(f"✅ Tarea '{tareas[indice_real][0]}' marcada como completada.")
                    else:
                        print("❌ Número de tarea inválido.")
                except ValueError:
                    print("❌ Por favor ingresa un número válido.")
    
    # ========== OPCIÓN 4: ELIMINAR TAREA ==========
    elif opcion == "4":
        limpiar_pantalla()
        print("🗑️ ELIMINAR TAREA:")
        
        if len(tareas) == 0:
            print("No tienes tareas para eliminar.")
        else:
            # Mostrar todas las tareas con números
            print("Todas las tareas:")
            contador = 0
            while contador < len(tareas):
                descripcion = tareas[contador][0]
                completada = tareas[contador][1]
                estado = "✅" if completada else "❌"
                print(f"{contador + 1}. {descripcion} {estado}")
                contador += 1
            
            try:
                seleccion = int(input("¿Qué tarea quieres eliminar? "))
                
                if 1 <= seleccion <= len(tareas):
                    tarea_a_eliminar = tareas[seleccion - 1][0]
                    confirmacion = input(f"¿Estás seguro de eliminar '{tarea_a_eliminar}'? (s/n): ").lower()
                    
                    if confirmacion == "s" or confirmacion == "si":
                        tareas.pop(seleccion - 1)
                        print(f"🗑️ Tarea '{tarea_a_eliminar}' eliminada.")
                    else:
                        print("Eliminación cancelada.")
                else:
                    print("❌ Número de tarea inválido.")
            except ValueError:
                print("❌ Por favor ingresa un número válido.")
    
    # ========== OPCIÓN 5: BUSCAR TAREA ==========
    elif opcion == "5":
        limpiar_pantalla()
        print("🔍 BUSCAR TAREA:")
        
        if len(tareas) == 0:
            print("No tienes tareas para buscar.")
        else:
            termino = input("Ingresa el término de búsqueda: ").lower().strip()
            
            if len(termino) == 0:
                print("❌ El término de búsqueda no puede estar vacío.")
            else:
                print(f"Resultados para '{termino}':")
                print("-" * 30)
                
                encontradas = 0
                contador = 0
                
                while contador < len(tareas):
                    descripcion = tareas[contador][0]
                    completada = tareas[contador][1]
                    
                    # Buscar el término en la descripción (sin distinguir mayúsculas)
                    if termino in descripcion.lower():
                        estado = "✅ Completada" if completada else "❌ Pendiente"
                        print(f"{contador + 1}. {descripcion} - {estado}")
                        encontradas += 1
                    
                    contador += 1
                
                if encontradas == 0:
                    print("No se encontraron tareas con ese término.")
                else:
                    print(f"\nSe encontraron {encontradas} tarea(s).")
    
    # ========== OPCIÓN 6: ESTADÍSTICAS ==========
    elif opcion == "6":
        limpiar_pantalla()
        print("📊 ESTADÍSTICAS:")
        print("-" * 30)
        
        if len(tareas) == 0:
            print("No tienes tareas registradas.")
        else:
            # Calcular estadísticas usando bucle while
            total_tareas = len(tareas)
            tareas_completadas = 0
            contador = 0
            
            while contador < len(tareas):
                if tareas[contador][1]:  # Si está completada
                    tareas_completadas += 1
                contador += 1
            
            tareas_pendientes = total_tareas - tareas_completadas
            porcentaje_completado = (tareas_completadas / total_tareas) * 100
            
            print(f"📝 Total de tareas: {total_tareas}")
            print(f"✅ Tareas completadas: {tareas_completadas}")
            print(f"❌ Tareas pendientes: {tareas_pendientes}")
            print(f"📈 Porcentaje completado: {porcentaje_completado:.1f}%")
            
            # Mostrar barra de progreso simple
            barras_completadas = int(porcentaje_completado / 10)
            barras_pendientes = 10 - barras_completadas
            barra_progreso = "█" * barras_completadas + "░" * barras_pendientes
            print(f"📊 Progreso: [{barra_progreso}] {porcentaje_completado:.1f}%")
    
    # ========== OPCIÓN 7: SALIR ==========
    elif opcion == "7":
        limpiar_pantalla()
        print(f"¡Hasta luego {nombre_usuario}!")
        print("Gracias por usar el Sistema de Gestión de Tareas.")
        
        # Mostrar resumen final si hay tareas
        if len(tareas) > 0:
            completadas = 0
            contador = 0
            while contador < len(tareas):
                if tareas[contador][1]:
                    completadas += 1
                contador += 1
            
            print(f"\nResumen final:")
            print(f"📝 Tienes {len(tareas)} tarea(s) registrada(s)")
            print(f"✅ {completadas} completada(s)")
            print(f"❌ {len(tareas) - completadas} pendiente(s)")
        
        programa_activo = False
    
    # ========== OPCIÓN INVÁLIDA ==========
    else:
        print("❌ Opción inválida. Por favor elige un número del 1 al 7.")
    
    # Pausa para que el usuario pueda leer el resultado
    if programa_activo:
        input("\nPresiona Enter para continuar...")

print("\n¡Programa terminado! 👋")