# CALCULADORA CON MANEJO DE ERRORES
# Conceptos: try/except, casting, operaciones básicas

import os

def limpiar_pantalla():
    """Limpia la pantalla"""
    os.system("cls")

def mostrar_menu():
    """Muestra el menú de operaciones"""
    print("\n" + "="*30)
    print("   CALCULADORA BÁSICA")
    print("="*30)
    print("1. Sumar")
    print("2. Restar") 
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    print("="*30)

# ========== PROGRAMA PRINCIPAL ==========
limpiar_pantalla()
print("¡Bienvenido a la Calculadora con Manejo de Errores!")

programa_activo = True

while programa_activo:
    mostrar_menu()
    
    # Pedir opción con manejo de errores
    try:
        opcion = input("\nElige una opción (1-5): ")
        
        if opcion == "5":
            print("¡Hasta luego! 👋")
            programa_activo = False
            continue
        
        if opcion not in ["1", "2", "3", "4"]:
            print("❌ Opción inválida. Elige del 1 al 5.")
            continue
        
        # Pedir números con manejo de errores
        print("\n📝 Ingresa los números:")
        
        try:
            num1 = float(input("Primer número: "))
            num2 = float(input("Segundo número: "))
            
            # Realizar operación según la opción
            if opcion == "1":
                resultado = num1 + num2
                print(f"✅ {num1} + {num2} = {resultado}")
                
            elif opcion == "2":
                resultado = num1 - num2
                print(f"✅ {num1} - {num2} = {resultado}")
                
            elif opcion == "3":
                resultado = num1 * num2
                print(f"✅ {num1} × {num2} = {resultado}")
                
            elif opcion == "4":
                try:
                    if num2 == 0:
                        print("❌ Error: No se puede dividir entre cero")
                    else:
                        resultado = num1 / num2
                        print(f"✅ {num1} ÷ {num2} = {resultado:.2f}")
                except ZeroDivisionError:
                    print("❌ Error: División entre cero no permitida")
                    
        except ValueError:
            print("❌ Error: Por favor ingresa números válidos")
            
    except KeyboardInterrupt:
        print("\n\n👋 Programa interrumpido por el usuario")
        programa_activo = False
    
    if programa_activo:
        input("\nPresiona Enter para continuar...")
        limpiar_pantalla()

print("¡Gracias por usar la calculadora!")