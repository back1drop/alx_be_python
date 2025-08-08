FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}F is {round(celsius,3)}C")
def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}C is {round(fahrenheit,3)}F")
temperature=float(input("Enter the temperature to convert: "))
sign=input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if temperature != "":
    if sign=='C':
        convert_to_fahrenheit(temperature)
    elif sign == 'F':
        convert_to_celsius(temperature)
    else:
        print("Invalid sign")
else:
    print("Invalid temperature. Please enter a numeric value.")

        
