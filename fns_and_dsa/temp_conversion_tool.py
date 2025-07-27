FAHRENHEIT_TO_CELSIUS_FACTOR=5/9
CELSIUS_TO_FARENHEIT_FACTOR=9/5
def convert_to_celsius(temp):
    celsius_temp=temp*FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{temp}F is {round(celsius_temp,3)}C")
def convert_to_fahrenheit(temp):
    fahrenheit_temp=temp*CELSIUS_TO_FARENHEIT_FACTOR
    
    print(f"{temp}C is {round(fahrenheit_temp,3)}F")
temperature=float(input("Enter the temperature to convert: "))
sign=input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if sign=='C':
    convert_to_fahrenheit(temperature)
elif sign == 'F':
    convert_to_celsius(temperature)
else:
    print("Invalid sign")

        
