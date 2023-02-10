# Samuel Esteban Valerín Villegas

# Muestra el mayor de dos números
primerNumero = int(input("Introduce el primer número: "))
segundoNumero = int(input("Introduce el segundo número: "))

if primerNumero > segundoNumero:
    print("El primer número:", primerNumero, " es mayor que el segundo número:", segundoNumero)
else:
    print("El segundo número:", segundoNumero, " es mayor que el primer número:", primerNumero)

# Muestra el mayor de cuatro números
primerNumero = int(input("Introduce el primer número: "))
segundoNumero = int(input("Introduce el segundo número: "))
tercerNumero = int(input("Introduce el tercer número: "))
cuartoNumero = int(input("Introduce el cuarto número: "))

if primerNumero > segundoNumero and primerNumero > tercerNumero and primerNumero > cuartoNumero:
    print("El primer número:", primerNumero, " es el mayor")
elif segundoNumero > primerNumero and segundoNumero > tercerNumero and segundoNumero > cuartoNumero:
    print("El segundo número:", segundoNumero, " es el mayor")
elif tercerNumero > primerNumero and tercerNumero > segundoNumero and tercerNumero > cuartoNumero:
    print("El tercer número:", tercerNumero, " es el mayor")
else:
    print("El cuarto número:", cuartoNumero, " es el mayor")
