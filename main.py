from rsc.modules import registro

def main():
    reg_pacientes = {}
    contar_eliminados = 0

    while True:
            opcion_ingresada = int(input("""
                                
            ---- BIENVENIDO/A AL SISTEMA DE GESTIÓN DE PACIENTES DE VETERINARIA SALOMON ---------
           Elija una opción a continuación:
                                    
            ---MENÚ DE OPCIONES---
            1- Registrar nuevo paciente.
            2- Ver el registro de pacientes.
            3- Modificar el registro de un paciente.
            4- Eliminar el registro de un paciente.
            5- Salir del sistema.
            
            ¿Qué desea hacer?: """))

            match opcion_ingresada:
                case 1:
                # Registrar nuevo paciente
                    print("---- REGISTRAR NUEVO PACIENTE ----")

                    nombre = input("Ingrese el nombre del paciente: ")

                    while True:
                        sexo = input("Ingrese el sexo del paciente (H/M): ").lower()
                        if sexo in ["h", "m"]:
                            break
                        print("Opción inválida. Ingrese 'M' para macho o 'H' para hembra.")

                    edad = int(input("Ingrese la edad del paciente: "))

                    while True:
                        especie = input("Ingrese la especie del paciente (Felino/Canino): ").lower()
                        if especie in ["felino", "canino"]:
                            break
                        print("Opción inválida. Ingrese 'felino' para felino o 'canino' para canino.")

                    rasgos = input("Ingrese los rasgos del paciente: ")

                    enfermedad = input("Ingrese enfermedad del paciente: ")

                    dueno = input("Ingrese nombre del dueño: ")

                    contacto = int(input("Ingrese el número del/la dueño/a: "))

                    registro.registrar_paciente(nombre, sexo, edad, especie, rasgos, enfermedad, dueno, contacto, reg_pacientes)

                    print("---- PACIENTE REGISTRADO CORRECTAMENTE ----")

                case 2:
                # Ver todo el registro de pacientes
                    print("---- VER EL REGISTRO DE PACIENTES ----")
                    registro.ver_pacientes(reg_pacientes)

                case 3:
                # Modificar registro paciente
                    print("---- MODIFICAR REGISTRO DE PACIENTE ----")      
                    id_paciente = int(input("Ingrese el ID del paciente a modificar: "))
                    caract_a_modificar = input("Ingrese la característica a modificar: ")
                    nuevo_valor = input(f"Nuevo/a {caract_a_modificar}: ")
                    registro.modificar_paciente(reg_pacientes, id_paciente, caract_a_modificar, nuevo_valor)

                case 4:
                # Eliminar
                    print("---- ELIMINAR UN PACIENTE ----")
                    id_paciente_eliminar = int(input("Ingrese el ID del paciente a eliminar: "))
                    contar_eliminados = registro.eliminar_paciente(reg_pacientes, id_paciente_eliminar, contar_eliminados)

                case 5:
                # Reportes
                    print(f"""
                    ---- REPORTE FINAL: 
                    Cantidad de registros de pacientes: {len(reg_pacientes)}
                    Cantidad de pacientes eliminados: {contar_eliminados}
                    ¡Gracias por utilizar nuestra app! 
                    """)
                    break

                case _:
                    print("Opción inválida. Por favor, elija una opción del 1 al 5.")

if __name__ == "__main__":
    main()
