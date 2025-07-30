# PROYECTO: CALCULADORA DE NOTAS ESTUDIANTILES
# 
# DESCRIPCIÓN: Un programa que ayuda a calcular y gestionar las notas de un estudiante
# Proyecto más simple para practicar los conceptos básicos
#
# CONCEPTOS A PRACTICAR:
# - Variables y tipos de datos
# - Input del usuario
# - Listas y métodos básicos
# - Condicionales if/elif/else
# - Bucles while
# - Operaciones matemáticas
# - Casting de tipos

import os

def limpiar_pantalla():
    """Limpia la pantalla de la consola"""
    os.system("cls")

def mostrar_menu():
    """Muestra las opciones disponibles"""
    print("\n" + "="*40)
    print("   CALCULADORA DE NOTAS")
    print("="*40)
    print("1. Agregar nota")
    print("2. Ver todas las notas")
    print("3. Calcular promedio")
    print("4. Ver nota más alta y más baja")
    print("5. Contar notas por categoría")
    print("6. Salir")
    print("="*40)

# ========== VARIABLES PRINCIPALES ==========
notas = []
notas_estudiantes=True


# ========== MENSAJE DE BIENVENIDA ==========
limpiar_pantalla()
print("¡Bienvenido a la Calculadora de Notas!")
# COMPLETAR: Pedir el nombre del estudiante y saludarlo
bienvenida=input("Cual es tu nombre:  ")
print(f"Bienvenido {bienvenida}")

# ========== BUCLE PRINCIPAL ==========
while notas_estudiantes:
    mostrar_menu()
    opcion = input(f"\n{bienvenida}, elige una opción (1-6): ")
    
    # ========== OPCIÓN 1: AGREGAR NOTA ==========
    if opcion == "1":
        limpiar_pantalla()
        print("📝 AGREGAR NUEVA NOTA:")
        nota_input = input("Añade la nota (0 a 10): ").strip()

        try:
            numero = float(nota_input)
            if 0 <= numero <= 10:
                notas.append(numero)
                print(f"✅ Nota agregada: {numero}")
            else:
                print("⚠️ La nota debe estar entre 0 y 10.")
        except ValueError:
            print("❌ Entrada inválida. Por favor, escribe un número.")


    # ========== OPCIÓN 2: VER TODAS LAS NOTAS ==========
    # COMPLETAR: Mostrar todas las notas guardadas
    # 
    elif opcion == "2":
         print("📋 TODAS LAS NOTAS:")
         print("-" * 40)
         if len(notas) == 0:
            print("No hay notas")
         else:
            contador = 0
            while contador < len(notas):
                print(f"Nota {contador + 1}: {notas[contador]}")
                contador += 1
    
    # ========== OPCIÓN 3: CALCULAR PROMEDIO ==========
    elif opcion == "3":
        print("📊 PROMEDIO DE NOTAS:")
        print("-" * 40)
        if len(notas) == 0:
            print("No hay notas")
        else:
            suma = 0
            contador = 0
            while contador < len(notas):
                suma += notas[contador]
                contador += 1
            promedio = suma / len(notas)
            print(f"📊 Promedio: {promedio:.2f}")
            
            if promedio >= 6:
                print("¡Aprobado! 🎉")
            else:
                print("¡Necesitas mejorar! 😔")
    
    # ========== OPCIÓN 4: NOTA MÁS ALTA Y MÁS BAJA ==========
    # COMPLETAR: Encontrar la nota máxima y mínima
    elif opcion == "4":
        print("🏆 NOTA MÁS ALTA Y MÁS BAJA:")
        print("-" * 40)
        if len(notas) == 0:
            print("⚠️ No hay notas registradas.")
        else:
            # Encontrar la nota más alta y más baja usando bucle while
            nota_max = notas[0]
            nota_min = notas[0]
            contador = 1
            while contador < len(notas):
                if notas[contador] > nota_max:
                    nota_max = notas[contador]
                if notas[contador] < nota_min:
                    nota_min = notas[contador]
                contador += 1
            
            print(f"Nota más alta: {nota_max}")
            print(f"Nota más baja: {nota_min}")

        # Si hay notas, usar bucle while para encontrar max y min
        # Mostrar ambos resultados
    
    # ========== OPCIÓN 5: CONTAR POR CATEGORÍAS ==========
    # COMPLETAR: Clasificar las notas
    elif opcion == "5":
        print("📈 NOTAS POR CATEGORÍA:")
        if len(notas) == 0:
            print("⚠️ No hay notas registradas.")
        else:
            excelentes = 0
            buenas = 0
            regulares = 0
            insuficientes = 0
            contador = 0
            while contador < len(notas):
                if notas[contador] >= 9:
                    excelentes += 1
                elif notas[contador] >= 7:
                    buenas += 1
                elif notas[contador] >= 6:
                    regulares += 1
                else:
                    insuficientes += 1
                contador += 1
            print(f"Excelentes: {excelentes}")
            print(f"Buenas: {buenas}")
            print(f"Regulares: {regulares}")
            print(f"Insuficientes: {insuficientes}")

    
    # ========== OPCIÓN 6: SALIR ==========
    elif opcion == "6":
        limpiar_pantalla()
        print("👋 ¡HASTA LUEGO!")
        print("="*40)
        print("📈 RESUMEN FINAL:")
        print("-" * 40)
        
        if len(notas) == 0:
            print("No registraste ninguna nota.")
        else:
            # Calcular promedio
            suma = 0
            contador = 0
            while contador < len(notas):
                suma += notas[contador]
                contador += 1
            promedio = suma / len(notas)
            
            # Encontrar nota máxima y mínima
            nota_max = notas[0]
            nota_min = notas[0]
            contador = 1
            while contador < len(notas):
                if notas[contador] > nota_max:
                    nota_max = notas[contador]
                if notas[contador] < nota_min:
                    nota_min = notas[contador]
                contador += 1
            
            print(f"📊 Total de notas: {len(notas)}")
            print(f"📊 Promedio final: {promedio:.2f}")
            print(f"🏆 Nota más alta: {nota_max}")
            print(f"📉 Nota más baja: {nota_min}")
            
            if promedio >= 6:
                print("🎉 ¡Resultado final: APROBADO!")
            else:
                print("😔 Resultado final: Necesitas mejorar")
        
        print(f"\n¡Gracias por usar la calculadora, {bienvenida}!")
        notas_estudiantes = False  # Terminar el bucle
    
    # ========== OPCIÓN INVÁLIDA ==========
    else:
        print("❌ Opción inválida. Por favor, elige una opción del 1 al 6.")
    
    # Pausa para que el usuario lea el resultado (excepto al salir)
    if notas_estudiantes:
        input("\nPresiona Enter para continuar...")

# ========== INSTRUCCIONES DETALLADAS ==========
"""
GUÍA PASO A PASO PARA COMPLETAR EL PROYECTO:

🎯 PASO 1: VARIABLES INICIALES
- Crear lista vacía para las notas: notas = []
- Variable booleana para el bucle: programa_ejecutando = True
- Pedir nombre del estudiante con input()

🎯 PASO 2: BUCLE PRINCIPAL
- while programa_ejecutando:
- Dentro del bucle, pedir opción con input()

🎯 PASO 3: OPCIÓN 1 - AGREGAR NOTA
- Pedir nota con input() y convertir a float()
- Validar que esté entre 0 y 10 con if
- Si es válida: notas.append(nota)
- Mostrar mensaje de confirmación

🎯 PASO 4: OPCIÓN 2 - VER NOTAS
- if len(notas) == 0: mostrar "No hay notas"
- else: usar bucle while para mostrar cada nota
- contador = 0
- while contador < len(notas):
    print(f"Nota {contador + 1}: {notas[contador]}")
    contador += 1

🎯 PASO 5: OPCIÓN 3 - PROMEDIO
- if len(notas) == 0: mostrar mensaje
- else: 
  - suma = 0
  - contador = 0
  - while contador < len(notas):
      suma += notas[contador]
      contador += 1
  - promedio = suma / len(notas)
  - print(f"Promedio: {promedio:.2f}")
  - if promedio >= 6: print("¡Aprobado!")

🎯 PASO 6: OPCIÓN 4 - MAX Y MIN
- if len(notas) == 0: mostrar mensaje
- else:
  - nota_max = notas[0]
  - nota_min = notas[0]
  - contador = 1
  - while contador < len(notas):
      if notas[contador] > nota_max:
          nota_max = notas[contador]
      if notas[contador] < nota_min:
          nota_min = notas[contador]
      contador += 1

🎯 PASO 7: OPCIÓN 5 - CATEGORÍAS
- Crear contadores: excelentes = 0, buenas = 0, etc.
- Usar bucle while para recorrer notas
- Usar if/elif para clasificar cada nota
- Mostrar resultados

🎯 PASO 8: OPCIÓN 6 - SALIR
- Mostrar despedida
- Si hay notas, mostrar resumen
- programa_ejecutando = False

🎯 CONCEPTOS QUE PRACTICARÁS:
✅ Variables (listas, booleanos, números)
✅ Input del usuario con input()
✅ Casting con float() e int()
✅ Condicionales if/elif/else
✅ Bucles while con contadores
✅ Métodos de listas (append, len)
✅ Operaciones matemáticas
✅ Validación de datos
✅ Formateo con f-strings

¡Este proyecto es perfecto para practicar sin ser demasiado complejo!
¡Puedes hacerlo paso a paso siguiendo las instrucciones!
"""