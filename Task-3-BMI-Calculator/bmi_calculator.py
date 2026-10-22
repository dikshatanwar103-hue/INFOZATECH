user_height = float(input("enter your height in cm: "))
user_weight = float(input("enter your weight in kg: "))

user_height_m = user_height/100

BMI = user_weight/(user_height_m**2)

print(f"Your BMI is: {BMI:.2f}")

if (BMI <= 18.5):
    print("Category: Underweight")

elif (BMI > 18.5 and BMI <= 24.9):
    print("Category: Normal")

elif (BMI > 24.9 and BMI <= 29.9):
    print("Category: Overweight")

else:
    print("Category: Obese")
