from src.model.calculator import *


def format_number_with_dots(number):
    """
    Formats the number by adding dots for readability.

    Args:
        number (int): The number to be formatted.

    Returns:
        str: The formatted number.
    """
    return "{:,}".format(number)


def format_input_number(input_string):
    """
    Formats the input string by removing dots and commas for conversion to integer.

    Args:
        input_string (str): The input string to be formatted.

    Returns:
        str: The formatted input string.
    """
    return input_string.replace('.', '').replace(',', '')


def main():
    print("Bienvenido a la calculadora de hipotecas inversas")

    try:
        total_amount_input = input("Ingrese el monto total de la hipoteca: ").replace(',', '')
        total_amount = int(total_amount_input)
        formatted_total_amount = format_number_with_dots(total_amount)
        print(f"Monto total de la hipoteca: {formatted_total_amount}")

        age = int(input("Ingrese la edad del titular de la hipoteca: "))
        expected_life = int(input("Ingrese la esperanza de vida esperada del titular de la hipoteca: "))
        fee_time = int(input("Ingrese el período de tiempo para las tarifas (en años): "))
        property_percentage = float(input("Ingrese el porcentaje de valor de la propiedad (porcentaje): "))
        mortgage_type = int(input(
            "Ingrese el tipo de hipoteca (1 para hipoteca vitalicia, 2 para hipoteca parcial, 3 para hipoteca total): "))

        calculator = Calculator(total_amount, age, expected_life, fee_time, property_percentage, mortgage_type)
        monthly_fee = calculator.calculate_monthly_fee()

        formatted_monthly_fee = format_number_with_dots(monthly_fee)
        print(f"La cuota mensual de la hipoteca inversa es: {formatted_monthly_fee}")

    except ValueError:
        print("Error: Por favor, ingrese un valor numérico válido.")

    except (
            InvalidAmount, InvalidAge, InvalidExpectedLife, InvalidFeeTime, InvalidPropertyPercentage,
            InvalidOption) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
