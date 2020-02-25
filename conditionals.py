## prosty kalkulator BMI
height = float(input("Height in cm: "))
weight = float(input("Weight in kg: "))

height_m = height / 100
BMI = weight / height_m ** 2
print("BMI: %.2f" % BMI)
if BMI < 18.5:
    print("You are underweight.")
elif BMI < 25:
    print("You are normal weight.")
elif BMI < 30:
    print("You are overweight.")
else:
    print("You are obese.")
