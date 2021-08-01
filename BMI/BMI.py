# Evaluate and print out the condition of weight based on the BMI value
def evaluteBMI(bmi):
    if bmi > 40:
        print("You are in the condition of Morbid Obesity.")
    elif 35 < bmi:
        print("You are in the condition of Obesity (Class 2).")
    elif 30 < bmi:
        print("You are in the condition of Obesity (Class 1).")
    elif 25 < bmi:
        print("You are overweight.")
    elif 18.5 < bmi:
        print("You are normal weight.")
    else:
        print("You are underweight.")

# Calculate the BMI value from weight and height (version1)
# Using non imperial values for the height and weight 
def Calculator() -> float:
    height_in_m = float(input("What is your height in meter? "))
    weight_in_kg = float(input("What is your weight in kilogram? "))
    bmi = round(weight_in_kg / (height_in_m ** 2), 2)
    print(f"Your BMI is {bmi}")
    return bmi

# Calculate the BMI value from weight and height (version2)
# Using imperial values for the height and weight 
def ImperialCalculator() -> float:
    height_in_m = float(input("What is your height in feet? "))
    weight_in_kg = float(input("What is your weight in pound? "))
    bmi = round((weight_in_kg) * 0.453592 / ((height_in_m * 0.3048) ** 2 ), 2)
    print(f"Your BMI is {bmi}")
    return bmi


# User comamnd line interface for the BMI calculating program 
def main():
    print("Hi This is BMI calculator machine!")
    name = input("What is your name? ")
    print(f"Hi! {name}")

    try:
        measurement = int(input("Which measurement are you familiar with? (1. meter and kilogram 2. feet and pound) "))
        if measurement == 1:
            value = Calculator()
            evaluteBMI(value)

        elif measurement == 2:
            value = ImperialCalculator()
            evaluteBMI(value)
        else:
            print("Invalid Input Error")
    except ValueError:
        print("Invalid input Error")
main()