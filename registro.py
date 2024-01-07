# Función para registrar un paciente
def registrar_paciente(nombre_paciente, sexo_paciente, edad_paciente, tipo_especie, rasgos_paciente, enfermedad_paciente, nombre_dueno, numero_contacto, registro_gral_pacientes):
    if registro_gral_pacientes:
        # Si hay pacientes registrados, el ID del nuevo paciente será el siguiente al último ID utilizado
        ids = list(registro_gral_pacientes.keys())
        ultimo_id = max(ids)
        id_paciente = int(ultimo_id) + 1  # Convertir a entero
    else:
        # Si no hay pacientes registrados, el ID del nuevo paciente será 1
        id_paciente = 1

    registro_gral_pacientes[id_paciente] = {
        "nombre": nombre_paciente,
        "sexo": sexo_paciente,
        "edad": edad_paciente,
        "especie": tipo_especie,
        "rasgos": rasgos_paciente,
        "enfermedad": enfermedad_paciente,
        "dueño": nombre_dueno,
        "contacto": numero_contacto
    }
# Función para ver todos los pacientes
def ver_pacientes(registro_gral_pacientes):
    if len(registro_gral_pacientes) > 0:
        # Mostramos todos los pacientes
        for id, paciente in registro_gral_pacientes.items():
            print(f"""
                  ---- REGISTRO PACIENTE: {id} ----
                  Nombre: {paciente["nombre"]}
                  Sexo: {paciente["sexo"]}
                  Edad: {paciente["edad"]}
                  Especie: {paciente["especie"]}
                  Rasgos: {paciente["rasgos"]}
                  Enfermedad: {paciente["enfermedad"]}
                  Nombre del Dueño: {paciente["dueño"]}
                  Número de contacto: {paciente["contacto"]}
                  """)
    else:
        print("No hay pacientes registrados")

def modificar_paciente(registro_gral_pacientes, id, caract_a_modificar, nuevo_valor):
    # Verificar si el ID existe en el registro
    if id in registro_gral_pacientes:
        if caract_a_modificar in registro_gral_pacientes[id]:
            # Verificar si la característica a modificar existe en el paciente
            registro_gral_pacientes[id][caract_a_modificar] = nuevo_valor
            # Actualizar el valor de la característica
            print(f"Paciente ID {id} actualizado correctamente.")
        else:
            print(f"La característica {caract_a_modificar} no existe para el paciente ID {id}.")
    else:
        print(f"No se encontró ningún paciente con el ID {id}.")

def eliminar_paciente(registro_gral_pacientes, id, contar_eliminados):
    # Eliminar paciente
    if id in registro_gral_pacientes:
        del registro_gral_pacientes[id]
        contar_eliminados += 1
        print(f"Paciente ID {id} eliminado correctamente.")
    else:
        print(f"No se encontró ningún paciente con el ID {id}.")
    return contar_eliminados