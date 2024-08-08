import sqlite3
from faker import Faker
import random
from datetime import datetime, timedelta

def generate_dummy_data():
    # Conectar a la base de datos
    conn = sqlite3.connect('mi_base_de_datos.db')
    cursor = conn.cursor()
    fake = Faker()

    # Generar datos dummy para la tabla 'clientes'
    clientes = []
    for _ in range(100):
        nombre_cliente = fake.name()
        fecha_creacion = fake.date_between(start_date='-5y', end_date='today').strftime('%Y-%m-%d')
        tipo_cliente = random.choice(['Regular', 'Premium', 'VIP'])
        clientes.append((nombre_cliente, fecha_creacion, tipo_cliente))

    cursor.executemany('''
        INSERT INTO clientes (nombre_cliente, fecha_creacion, tipo_cliente)
        VALUES (?, ?, ?)
    ''', clientes)

    # Obtener los ids de los clientes insertados
    cursor.execute('SELECT id_cliente FROM clientes')
    cliente_ids = [row[0] for row in cursor.fetchall()]

    # Generar datos dummy para la tabla 'compras'
    compras = []
    for _ in range(1000):
        id_cliente = random.choice(cliente_ids)
        nombre_item = fake.word()
        fecha_compra = fake.date_between(start_date='-5y', end_date='today').strftime('%Y-%m-%d')
        precio_venta = round(random.uniform(5.0, 500.0), 2)
        descuento = round(random.uniform(0.0, 50.0), 2)
        compras.append((id_cliente, nombre_item, fecha_compra, precio_venta, descuento))

    cursor.executemany('''
        INSERT INTO compras (id_cliente, nombre_item, fecha_compra, precio_venta, descuento)
        VALUES (?, ?, ?, ?, ?)
    ''', compras)

    # Confirmar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

if __name__ == '__main__':
    generate_dummy_data()
    print("Datos dummy generados exitosamente.")
