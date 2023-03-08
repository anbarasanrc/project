def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Ask the user for input
temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit of the temperature (C/F): ")

# Convert the temperature
if unit.lower() == "c":
    converted_temp = celsius_to_fahrenheit(temperature)
    original_unit = "Celsius"
    new_unit = "Fahrenheit"
elif unit.lower() == "f":
    converted_temp = fahrenheit_to_celsius(temperature)
    original_unit = "Fahrenheit"
    new_unit = "Celsius"
else:
    print("Invalid unit. Please enter 'C' or 'F'.")
    exit()

# Print the result
print(f"{temperature} {original_unit} is {converted_temp} {new_unit}.")
