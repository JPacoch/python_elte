class BMI():

    def __str__(self):
        return "To jest kalkulator Body Mass Index."

    def bmi_ind(self, wzrost, waga):
        return waga / ((wzrost / 100) ** 2)

    def bmi(self, wzrost, waga):
        if waga / ((wzrost / 100) ** 2) < 18.5:
            print("You are underweight.")
        elif waga / ((wzrost / 100) ** 2) < 25:
            print("You are normal weight.")
        elif waga / ((wzrost / 100) ** 2) < 30:
            print("You are overweight.")
        else:
            print("You are obese.")


