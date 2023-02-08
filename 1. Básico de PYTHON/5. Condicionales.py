#edad = input("Ingrese su edad: ")

#if (int(edad) >= 18):
#    print("Puede pasar")
#else:
#    print("No puede pasar")
    
#Condicionales anidados en py

nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")

if(edad >= 18):
    if(nombre.count >= 5):
        print("Puede pasar")
    else:
        print("Tu nombre es demasiado corto")
else:
    print("No puede pasar")