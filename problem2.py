"""
Problem 2: Temperature Converter
Convert between Celsius and Fahrenheit temperatures.
"""
def temperature_converter():
    
    
    print("Temperature Converter")
    print("-" * 30)


def celsius_to_fahrenheit(celsius):
    
    return(celsius * 9/5) + 32

    # TODO: Implement this function
    


def fahrenheit_to_celsius(fahrenheit):
   return(fahrenheit-32) * 5/9
    # TODO: Implement this function





    # TODO: Implement the interactive converter
    # Remember to:
    # - Get temperature value from user
    # - Get unit (C or F) from user
    # - Validate input
    # - Perform conversion
    # - Display result rounded to 2 decimal places


#Get temp from user

while True:
    try:
        temp_value = float(input("Enter the temperature value: "))
        break
    except ValueError:
        print("Invalid input. Please enter a numerical temperature.")

# Get Unit from user

while True:
    unit = input("Enter the current unit (C for Celsius, F for Fahrenheit): ").upper().strip()
    if unit in ("C","F"):
        break
    else:
        print("Invalid unit. Please enter C or F.") 

#3 Convert and display results

original_symbol = " "
converted_symbol = " "
F= 0
C= 0

if unit == ("C"):
    original_symbol = "°C"
    converted_symbol = "°F"
elif unit == ("F"):
    original_symbol = "°F"
    converted_symbol = "°C"

if unit == ("C"):
    C = temp_value
    F = (C * 9/5) + 32
    F = int(F)
    print(f"Your original Value was: {C: .2f} , {original_symbol}")
    print(f"Your converted value is: {F: .2f} , {converted_symbol}")
elif unit == ("F"):
    F = temp_value
    C = (F - 32) * 5/9
    C = int(C)
    print(f"Your original Value was: {F: .2f} , {original_symbol}")
    print(f"Your converted value is: {C: .2f} , {converted_symbol}")





#print("The original symbol was ", original_symbol, " the converted symbol is ", converted_symbol)


# Test cases (DO NOT MODIFY)
if __name__ == "__main__":
    # Test conversions
    print("Running tests...")

    # Test Celsius to Fahrenheit
    assert celsius_to_fahrenheit(0) == 32, "0°C should be 32°F"
    assert celsius_to_fahrenheit(100) == 212, "100°C should be 212°F"

    # Test Fahrenheit to Celsius
    assert fahrenheit_to_celsius(32) == 0, "32°F should be 0°C"
    assert fahrenheit_to_celsius(212) == 100, "212°F should be 100°C"

    print("All tests passed!")
    print()

    # Run interactive converter
    temperature_converter()

