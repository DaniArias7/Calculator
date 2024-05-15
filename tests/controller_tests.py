import unittest
from datetime import date
from src.controller.app_controller import ControladorHipotecas
from src.model.user import Usuario

class ControladorHipotecasTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.controlador = ControladorHipotecas()
        cls.controlador.CrearTablas()

    def setUp(self):
        self.controlador.CrearTablas()

    def tearDown(self):
        self.controlador.CrearTablas()

    def test_crear_tablas(self):
        usuarios = self.controlador.ObtenerUsuarios()
        hipotecas = self.controlador.ObtenerHipotecas(1)  # Asumiendo que no hay usuarios aún
        self.assertEqual(len(usuarios), 0)
        self.assertEqual(len(hipotecas), 0)

    def test_insertar_usuario(self):
        usuario = Usuario("Matias Herrera", 35)
        self.controlador.InsertarUsuario(usuario)
        usuarios = self.controlador.ObtenerUsuarios()
        self.assertEqual(len(usuarios), 1)
        self.assertEqual(usuarios[0].name, "Matias Herrera")
        self.assertEqual(usuarios[0].age, 35)

    def test_insertar_usuario_duplicado(self):
        usuario = Usuario("Matias Herrera", 35)
        self.controlador.InsertarUsuario(usuario)
        usuario_duplicado = Usuario("Matias Herrera", 35)
        self.controlador.InsertarUsuario(usuario_duplicado)
        usuarios = self.controlador.ObtenerUsuarios()
        self.assertEqual(len(usuarios), 1)

    def test_insertar_hipoteca(self):
        usuario = Usuario("Juan José", 40)
        self.controlador.InsertarUsuario(usuario)
        usuario_id = self.controlador.ObtenerUsuarios()[0].id
        monto_total = 200000.0
        fecha_inicio = date(2023, 1, 1)
        cuota_mensual = 1000
        self.controlador.InsertarHipoteca(usuario_id, monto_total, fecha_inicio, cuota_mensual)
        hipotecas = self.controlador.ObtenerHipotecas(usuario_id)
        self.assertEqual(len(hipotecas), 1)
        self.assertEqual(hipotecas[0]["monto_total"], monto_total)
        self.assertEqual(hipotecas[0]["fecha_inicio"], fecha_inicio)
        self.assertEqual(hipotecas[0]["cuota_mensual"], cuota_mensual)

    def test_modificar_usuario(self):
        usuario = Usuario("Matias Herrera", 35)
        self.controlador.InsertarUsuario(usuario)
        usuarios = self.controlador.ObtenerUsuarios()
        usuario_modificado = Usuario("Matias Herrera Vanegas", 40)
        usuario_modificado.id = usuarios[0].id
        self.controlador.ModificarUsuario(usuario_modificado)
        usuarios_actualizados = self.controlador.ObtenerUsuarios()
        self.assertEqual(len(usuarios_actualizados), 1)
        self.assertEqual(usuarios_actualizados[0].name, "Matias Herrera Vanegas")
        self.assertEqual(usuarios_actualizados[0].age, 40)

    def test_eliminar_usuario(self):
        usuario = Usuario("Matias Herrera", 35)
        self.controlador.InsertarUsuario(usuario)
        usuarios = self.controlador.ObtenerUsuarios()
        self.assertEqual(len(usuarios), 1)
        self.controlador.EliminarUsuario(usuarios[0].id)
        usuarios_despues_eliminar = self.controlador.ObtenerUsuarios()
        self.assertEqual(len(usuarios_despues_eliminar), 0)

    def test_obtener_usuarios(self):
        usuario1 = Usuario("Matias Herrera", 35)
        usuario2 = Usuario("Juan José", 40)
        self.controlador.InsertarUsuario(usuario1)
        self.controlador.InsertarUsuario(usuario2)
        usuarios = self.controlador.ObtenerUsuarios()
        self.assertEqual(len(usuarios), 2)
        self.assertEqual(usuarios[0].name, "Matias Herrera")
        self.assertEqual(usuarios[1].name, "Juan José")

    def test_obtener_hipotecas(self):
        usuario = Usuario("Matias Herrera", 35)
        self.controlador.InsertarUsuario(usuario)
        usuario_id = self.controlador.ObtenerUsuarios()[0].id
        monto_total = 200000.0
        fecha_inicio = date(2023, 1, 1)
        cuota_mensual = 1000
        self.controlador.InsertarHipoteca(usuario_id, monto_total, fecha_inicio, cuota_mensual)
        hipotecas = self.controlador.ObtenerHipotecas(usuario_id)
        self.assertEqual(len(hipotecas), 1)
        self.assertEqual(hipotecas[0]["monto_total"], monto_total)
        self.assertEqual(hipotecas[0]["fecha_inicio"], fecha_inicio)
        self.assertEqual(hipotecas[0]["cuota_mensual"], cuota_mensual)

    def test_modificar_hipoteca(self):
        usuario = Usuario("Jane Smith", 40)
        self.controlador.InsertarUsuario(usuario)
        usuario_id = self.controlador.ObtenerUsuarios()[0].id
        monto_total = 200000.0
        fecha_inicio = date(2023, 1, 1)
        cuota_mensual = 1000
        self.controlador.InsertarHipoteca(usuario_id, monto_total, fecha_inicio, cuota_mensual)
        
        # Modificamos la cuota mensual de la hipoteca
        nueva_cuota_mensual = 1200
        self.controlador.InsertarHipoteca(usuario_id, monto_total, fecha_inicio, nueva_cuota_mensual)
        
        # Obtenemos la hipoteca y verificamos que la cuota mensual se haya actualizado correctamente
        hipotecas = self.controlador.ObtenerHipotecas(usuario_id)
        self.assertEqual(len(hipotecas), 1)
        self.assertEqual(hipotecas[0]["cuota_mensual"], nueva_cuota_mensual)

if __name__ == '__main__':
    unittest.main(verbosity=2)
