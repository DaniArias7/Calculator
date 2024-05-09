import sys

sys.path.append("C:/Users/dsana/Workspace/Calculator")
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from src.model.calculator import *


class CalculatorLayout(BoxLayout):
    def calculate(self):
        try:
            total_amount = int(self.ids.total_amount_input.text)
            age = int(self.ids.age_input.text)
            life_expectancy = int(self.ids.life_expectancy_input.text)
            payment_period = int(self.ids.payment_period_input.text)
            property_percentage = float(self.ids.property_percentage_input.text)
            mortgage_type = self.ids.mortgage_type_spinner.values.index(self.ids.mortgage_type_spinner.text) + 1

            calculator = Calculator(total_amount, age, life_expectancy, payment_period, property_percentage,
                                    mortgage_type)
            monthly_fee = calculator.calculate_monthly_fee()

            popup = Popup(title='Resultado', content=Label(text=f'Cuota Mensual: {monthly_fee}'),
                          size_hint=(None, None), size=(400, 200))
            popup.open()
        except Exception as e:
            popup = Popup(title='Error', content=Label(text=str(e)), size_hint=(None, None), size=(400, 200))
            popup.open()


class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()


if __name__ == '__main__':
    CalculatorApp().run()
