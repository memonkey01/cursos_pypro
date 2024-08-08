import sqlite3

def create_database():
    # Conectar a la base de datos (se creará si no existe)
    conn = sqlite3.connect('mi_base_de_datos.db')
    cursor = conn.cursor()

    # Crear la tabla 'clientes'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_cliente TEXT NOT NULL,
            fecha_creacion TEXT NOT NULL,
            tipo_cliente TEXT NOT NULL
        )
    ''')

    # Crear la tabla 'compras'
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS compras (
            id_compra INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cliente INTEGER NOT NULL,
            nombre_item TEXT NOT NULL,
            fecha_compra TEXT NOT NULL,
            precio_venta REAL NOT NULL,
            descuento REAL NOT NULL,
            FOREIGN KEY (id_cliente) REFERENCES clientes(id_cliente)
        )
    ''')

    # Confirmar los cambios y cerrar la conexión
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_database()
    print("Base de datos y tablas creadas exitosamente.")
