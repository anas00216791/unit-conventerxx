def convert_length():
    print("\nLength Converter:")
    print("1. Meters to Kilometers")
    print("2. Meters to Centimeters")
    print("3. Kilometers to Meters")
    print("4. Centimeters to Meters")
    
    choice = input("Choose a conversion option (1/2/3/4): ")

    length_value = float(input("Enter the value to convert: "))

    if choice == '1':
        result = length_value / 1000
        print(f"{length_value} meters = {result} kilometers")
    elif choice == '2':
        result = length_value * 100
        print(f"{length_value} meters = {result} centimeters")
    elif choice == '3':
        result = length_value * 1000
        print(f"{length_value} kilometers = {result} meters")
    elif choice == '4':
        result = length_value / 100
        print(f"{length_value} centimeters = {result} meters")
    else:
        print("Invalid choice!")

def convert_weight():
    print("\nWeight Converter:")
    print("1. Grams to Kilograms")
    print("2. Kilograms to Grams")
    print("3. Grams to Pounds")
    print("4. Pounds to Grams")
    
    choice = input("Choose a conversion option (1/2/3/4): ")

    weight_value = float(input("Enter the value to convert: "))

    if choice == '1':
        result = weight_value / 1000
        print(f"{weight_value} grams = {result} kilograms")
    elif choice == '2':
        result = weight_value * 1000
        print(f"{weight_value} kilograms = {result} grams")
    elif choice == '3':
        result = weight_value * 0.00220462
        print(f"{weight_value} grams = {result} pounds")
    elif choice == '4':
        result = weight_value * 453.592
        print(f"{weight_value} pounds = {result} grams")
    else:
        print("Invalid choice!")

def convert_temperature():
    print("\nTemperature Converter:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    
    choice = input("Choose a conversion option (1/2): ")

    temp_value = float(input("Enter the value to convert: "))

    if choice == '1':
        result = (temp_value * 9/5) + 32
        print(f"{temp_value} Celsius = {result} Fahrenheit")
    elif choice == '2':
        result = (temp_value - 32) * 5/9
        print(f"{temp_value} Fahrenheit = {result} Celsius")
    else:
        print("Invalid choice!")

def unit_converter():
    print("Welcome to the Unit Converter!")
    print("1. Length Conversion")
    print("2. Weight Conversion")
    print("3. Temperature Conversion")
    
    choice = input("Choose the type of conversion (1/2/3): ")

    if choice == '1':
        convert_length()
    elif choice == '2':
        convert_weight()
    elif choice == '3':
        convert_temperature()
    else:
        print("Invalid choice!")

# Run the unit converter
unit_converter()
