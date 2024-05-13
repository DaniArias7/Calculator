class Usuario:
    """
    Pertenece la Capa de Reglas de Negocio (Model)

    Representa a un usuario de la Tarjeta de Credito en la aplicación
    """
    def __init__( self, name, age, mortgage_type, numbers_of_installments, monthly_fees):
        self.name = name
        self.age = age
        self.mortgage_type = mortgage_type
        self.numbers_of_installments = numbers_of_installments
        self.monthly_fees = monthly_fees
    


    def esIgual( self, compare_with) :
        """
        Compara el objeto actual, con otra instancia de la clase Usuario
        """
        assert(self.name == compare_with.name)
        assert(self.age == compare_with.age)
        assert(self.mortgage_type == compare_with.mortgage_type)
        assert(self.numbers_of_installments == compare_with.numbers_of_installments)
        assert(self.monthly_fees == compare_with.monthly_fees)

