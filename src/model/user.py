class Usuario:
    """
    Pertenece la Capa de Reglas de Negocio (Model)

    Representa a un usuario de la Tarjeta de Credito en la aplicación
    """
    def __init__( self, name, age):
        self.name = name
        self.age = age
        


    def esIgual( self, compare_with) :
        """
        Compara el objeto actual, con otra instancia de la clase Usuario
        """
        assert(self.name == compare_with.name)
        assert(self.age == compare_with.age)
        

