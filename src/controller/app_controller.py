import sys
sys.path.append("src")

import psycopg2
from model.user import Usuario
import secret_config

class ControladorHipotecas:
    def CrearTablas(self):
        """Crea las tablas necesarias en la base de datos"""
        cursor = self.ObtenerCursor()

        # Crear tabla de usuarios
        cursor.execute("""CREATE TABLE IF NOT EXISTS usuarios (
                          id SERIAL PRIMARY KEY,
                          name TEXT NOT NULL,
                          age INTEGER NOT NULL,
                          mortgage_type INTEGER NOT NULL,
                          numbers_of_installments INTEGER NOT NULL,
                          monthly_fees FLOAT NOT NULL
                          )""")

        # Crear tabla de hipotecas
        cursor.execute("""CREATE TABLE IF NOT EXISTS hipotecas (
                          id SERIAL PRIMARY KEY,
                          usuario_id INTEGER NOT NULL,
                          monto_total FLOAT NOT NULL,
                          fecha_inicio DATE NOT NULL,
                          FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
                          )""")

        cursor.connection.commit()

    def InsertarUsuario(self, usuario):
        """Inserta un nuevo usuario en la base de datos"""
        cursor = self.ObtenerCursor()
        cursor.execute("""INSERT INTO usuarios (name, age, mortgage_type, numbers_of_installments, monthly_fees)
                          VALUES (%s, %s, %s, %s, %s)""",
                       (usuario.name, usuario.age, usuario.mortgage_type, usuario.numbers_of_installments, usuario.monthly_fees))
        cursor.connection.commit()

    def InsertarHipoteca(self, usuario_id, monto_total, fecha_inicio):
        """Inserta una nueva hipoteca en la base de datos"""
        cursor = self.ObtenerCursor()
        cursor.execute("""INSERT INTO hipotecas (usuario_id, monto_total, fecha_inicio)
                          VALUES (%s, %s, %s)""",
                       (usuario_id, monto_total, fecha_inicio))
        cursor.connection.commit()

    def ModificarUsuario(self, usuario):
        """Modifica los datos de un usuario existente"""
        cursor = self.ObtenerCursor()
        cursor.execute("""UPDATE usuarios
                          SET name = %s, age = %s, mortgage_type = %s, numbers_of_installments = %s, monthly_fees = %s
                          WHERE id = %s""",
                       (usuario.name, usuario.age, usuario.mortgage_type, usuario.numbers_of_installments, usuario.monthly_fees, usuario.id))
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
        cursor.execute("""SELECT id, name, age, mortgage_type, numbers_of_installments, monthly_fees
                          FROM usuarios""")
        usuarios = []
        for fila in cursor.fetchall():
            usuario = Usuario(fila[1], fila[2], fila[3], fila[4], fila[5])
            usuario.id = fila[0]
            usuarios.append(usuario)
        return usuarios

    def ObtenerHipotecas(self, usuario_id):
        """Obtiene todas las hipotecas de un usuario"""
        cursor = self.ObtenerCursor()
        cursor.execute("""SELECT id, monto_total, fecha_inicio
                          FROM hipotecas
                          WHERE usuario_id = %s""", (usuario_id,))
        hipotecas = []
        for fila in cursor.fetchall():
            hipoteca = {"id": fila[0], "monto_total": fila[1], "fecha_inicio": fila[2]}
            hipotecas.append(hipoteca)
        return hipotecas

    def ObtenerCursor(self):
        """Crea la conexión a la base de datos y retorna un cursor para hacer consultas"""
        connection = psycopg2.connect(database=secret_config.PGDATABASE, user=secret_config.PGUSER,
                                      password=secret_config.PGPASSWORD, host=secret_config.PGHOST)
        cursor = connection.cursor()
        return cursor