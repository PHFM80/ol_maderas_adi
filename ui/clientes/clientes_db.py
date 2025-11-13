# ui/clientes/clientes_db.py
import sqlite3

def buscar_cliente(conn, razon, cuit):
    cursor = conn.cursor()
    cuit_value = int(cuit) if cuit.isdigit() else -1
    cursor.execute(
        "SELECT * FROM clientes WHERE razon_social LIKE ? OR cuit_dni=? LIMIT 1",
        (f"%{razon}%", cuit_value)
    )
    cliente = cursor.fetchone()
    return cliente

def guardar_cliente_db(conn, cliente_data):
    cursor = conn.cursor()

    if not cliente_data["cuit_dni"].isdigit():
        return False, "El CUIT/DNI debe ser numérico"
    if not cliente_data["telefono"].isdigit():
        return False, "El Teléfono debe ser numérico"

    cuit_value = int(cliente_data["cuit_dni"])
    telefono_value = int(cliente_data["telefono"])

    cursor.execute("SELECT id_cliente FROM clientes WHERE cuit_dni=?", (cuit_value,))
    existente = cursor.fetchone()

    if existente:
        cursor.execute(
            """UPDATE clientes 
               SET razon_social=?, domicilio=?, provincia=?, localidad=?, condicion_iva=?, telefono=?, email=?
               WHERE cuit_dni=?""",
            (cliente_data["razon_social"], cliente_data["domicilio"], cliente_data["provincia"],
             cliente_data["localidad"], cliente_data["condicion_iva"], telefono_value,
             cliente_data["email"], cuit_value)
        )
        mensaje = "Cliente modificado correctamente"
    else:
        cursor.execute(
            """INSERT INTO clientes 
               (razon_social, domicilio, provincia, localidad, cuit_dni, condicion_iva, telefono, email)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (cliente_data["razon_social"], cliente_data["domicilio"], cliente_data["provincia"],
             cliente_data["localidad"], cuit_value, cliente_data["condicion_iva"], telefono_value,
             cliente_data["email"])
        )
        mensaje = "Cliente guardado correctamente"

    conn.commit()
    return True, mensaje
