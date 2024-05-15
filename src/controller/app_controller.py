import sys
sys.path.append('.')

import psycopg2
from model.user import Usuario
import secret_config

class ControladorHipotecas:
    def CrearTablas(self):
        """Crea las tablas necesarias en la base de datos"""
        cursor = self.ObtenerCursor()

        # Crear tabla de usuarios
        cursor.execute("""DROP TABLE IF EXISTS usuarios CASCADE""")
        cursor.execute("""CREATE TABLE usuarios (
                        id SERIAL PRIMARY KEY,
                        name TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        UNIQUE (name, age)
                        )""")

        # Crear tabla de hipotecas
        cursor.execute("""DROP TABLE IF EXISTS hipotecas""")
        cursor.execute("""CREATE TABLE hipotecas (
                        id SERIAL PRIMARY KEY,
                        usuario_id INTEGER NOT NULL,
                        monto_total FLOAT NOT NULL,
                        fecha_inicio DATE NOT NULL,
                        cuota_mensual INTEGER NOT NULL,
                        UNIQUE (usuario_id, monto_total, fecha_inicio),
                        FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
                        )""")

        cursor.connection.commit()

    def InsertarUsuario(self, usuario):
        """Inserta un nuevo usuario en la base de datos"""
        cursor = self.ObtenerCursor()
        try:
            cursor.execute("""INSERT INTO usuarios (name, age)
                          VALUES (%s, %s) RETURNING id""",
                        (usuario.name, usuario.age))
            usuario_id = cursor.fetchone()[0]
            usuario.id = usuario_id
            cursor.connection.commit()
        except psycopg2.IntegrityError as e:
            cursor.connection.rollback()
            if "duplicate key value violates unique constraint" in str(e):
                print(f"Error: Ya existe un usuario con el nombre '{usuario.name}' y la edad {usuario.age}.")
            else:
                print(f"Error: {e}")

    def InsertarHipoteca(self, usuario_id, monto_total, fecha_inicio, cuota_mensual):
        """Inserta una nueva hipoteca en la base de datos"""
        cursor = self.ObtenerCursor()
        try:
            cursor.execute("""INSERT INTO hipotecas (usuario_id, monto_total, fecha_inicio, cuota_mensual)
                          VALUES (%s, %s, %s, %s)""",
                        (usuario_id, monto_total, fecha_inicio, cuota_mensual))
            cursor.connection.commit()
        except psycopg2.IntegrityError as e:
            cursor.connection.rollback()
            if "duplicate key value violates unique constraint" in str(e):
                cursor.execute("""UPDATE hipotecas
                              SET cuota_mensual = %s
                              WHERE usuario_id = %s AND monto_total = %s AND fecha_inicio = %s""",
                            (cuota_mensual, usuario_id, monto_total, fecha_inicio))
                cursor.connection.commit()
                print("Hipoteca actualizada correctamente.")
            else:
                print(f"Error: {e}")

    def ModificarUsuario(self, usuario):
        """Modifica los datos de un usuario existente"""
        cursor = self.ObtenerCursor()
        cursor.execute("""UPDATE usuarios
                          SET name = %s, age = %s
                          WHERE id = %s""",
                       (usuario.name, usuario.age, usuario.id))
        cursor.connection.commit()

    def EliminarUsuario(self, usuario_id):
        """Elimina un usuario y sus hipotecas asociadas"""
        cursor = self.ObtenerCursor()
        cursor.execute("""DELETE FROM hipotecas WHERE usuario_id = %s""", (usuario_id,))
        cursor.execute("""DELETE FROM usuarios WHERE id = %s""", (usuario_id,))
        cursor.connection.commit()

    def ObtenerUsuarios(self):
        """Obtiene todos los usuarios de la base de datos"""
        cursor = self.ObtenerCursor()
        cursor.execute("""SELECT id, name, age
                          FROM usuarios""")
        usuarios = []
        for fila in cursor.fetchall():
            usuario = Usuario(fila[1], fila[2])
            usuario.id = fila[0]
            usuarios.append(usuario)
        return usuarios

    def ObtenerHipotecas(self, usuario_id):
        """Obtiene todas las hipotecas de un usuario"""
        cursor = self.ObtenerCursor()
        cursor.execute("""SELECT id, monto_total, fecha_inicio, cuota_mensual
                          FROM hipotecas
                          WHERE usuario_id = %s""", (usuario_id,))
        hipotecas = []
        for fila in cursor.fetchall():
            hipoteca = {"id": fila[0], "monto_total": fila[1], "fecha_inicio": fila[2], "cuota_mensual": fila[3]}
            hipotecas.append(hipoteca)
        return hipotecas

    def ObtenerCursor(self):
        """Crea la conexión a la base de datos y retorna un cursor para hacer consultas"""
        connection = psycopg2.connect(database=secret_config.PGDATABASE, user=secret_config.PGUSER,
                                      password=secret_config.PGPASSWORD, host=secret_config.PGHOST)
        cursor = connection.cursor()
        return cursor