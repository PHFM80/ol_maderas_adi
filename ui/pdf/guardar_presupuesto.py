# ui/pdf/guardar_presupuesto.py

from db.db_config import get_connection
from db.init_db import crear_tablas

def guardar_presupuesto(datos_presupuesto, items, resumen, condiciones):
    """
    Guarda el presupuesto y sus ítems en la base de datos.
    Retorna el id_presupuesto generado.
    """
    crear_tablas()  # Asegura que las tablas existan

    conn = get_connection()
    cursor = conn.cursor()

    try:
        # --- Insertar presupuesto ---
        cursor.execute("""
            INSERT INTO presupuestos (
                id_cliente, fecha, moneda, validez_oferta, forma_pago,
                condicion_pago, plazo_entrega, lugar_entrega, transporte,
                subtotal, descuento_porcentaje, descuento_valor,
                iva_105, iva_21, total_final, total_letras
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            datos_presupuesto["id_cliente"],
            datos_presupuesto["fecha"],
            datos_presupuesto["moneda"],
            condiciones["validez_oferta"],
            condiciones["forma_pago"],
            condiciones["condicion_pago"],
            condiciones["plazo_entrega"],
            condiciones["lugar_entrega"],
            condiciones["transporte"],
            resumen["subtotal"],
            resumen["descuento_porcentaje"],
            resumen["descuento_valor"],
            resumen["iva_105"],       
            resumen["iva_21"],        
            resumen["total"],         
            resumen.get("total_letras", "")
        ))


        id_presupuesto = cursor.lastrowid

        # --- Insertar ítems ---
        for item in items:
            cursor.execute("""
                INSERT INTO items (id_presupuesto, cantidad, descripcion, precio_unitario, total)
                VALUES (?, ?, ?, ?, ?)
            """, (
                id_presupuesto,
                item["cantidad"],
                item["descripcion"],
                item["precio_unitario"],
                item["total"]
            ))

        conn.commit()
        return id_presupuesto

    except Exception as e:
        conn.rollback()
        print(f"Error al guardar el presupuesto: {e}")
        return None

    finally:
        conn.close()
