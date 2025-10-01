# ui\componentes\calculo_valor_total\guardar_valores_presupuesto.py

import sqlite3
import os

def guardar_valores_presupuesto(
    subtotal,
    campo_porcentaje,
    resultado_descuento,
    resultado_iva_105,
    resultado_iva_21,
    resultado_total,
    resultado_total_letras
):
    try:
        # Ruta absoluta a la base
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(base_dir, "../../../db/presupuesto.db")
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()

        # Procesar valores numéricos
        subtotal_valor = float(subtotal.value.replace("$", "").strip())
        descuento_porcentaje = float(campo_porcentaje.value)
        descuento_valor = float(resultado_descuento.value.replace("$", "").strip())
        iva_105 = float(resultado_iva_105.value.replace("$", "").strip())
        iva_21 = float(resultado_iva_21.value.replace("$", "").strip())
        total_final = float(resultado_total.value.replace("$", "").strip())
        total_letras = resultado_total_letras.value.strip()

        # Insertar en la tabla
        print("antes de insertar")
        print("SUBTOTAL:", subtotal.value)
        print("DESCUENTO %:", campo_porcentaje.value)
        print("DESCUENTO $:", resultado_descuento.value)
        print("IVA 10.5:", resultado_iva_105.value)
        print("IVA 21:", resultado_iva_21.value)
        print("TOTAL FINAL:", resultado_total.value)
        print("TOTAL EN LETRAS:", resultado_total_letras.value)

        cursor.execute("""
            INSERT INTO valores_presupuesto (
                subtotal,
                descuento_porcentaje,
                descuento_valor,
                iva_105,
                iva_21,
                total_final,
                total_letras
            ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            subtotal_valor,
            descuento_porcentaje,
            descuento_valor,
            iva_105,
            iva_21,
            total_final,
            total_letras
        ))

        conn.commit()
        conn.close()
        print("Valores guardados correctamente.")

    except Exception as e:
        print(f"❌ Error al guardar valores: {e}")
