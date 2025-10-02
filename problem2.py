def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9


def temperature_converter():
    print("Temperature Converter")
    print("-" * 30)

    # 1. Get temperature value from user
    while True:
        try:
            temp_value = float(input("Enter the temperature value: "))
            break
        except ValueError:
            print("Invalid input. Please enter a numerical temperature.")

    # 2. Get Unit from user
    while True:
        unit = input("Enter the current unit (C for Celsius, F for Fahrenheit): ").upper().strip()
        if unit in ("C", "F"):
            break
        else:
            print("Invalid unit. Please enter C or F.")

    # 3. Convert and display results
    
    original_symbol = ""
    converted_symbol = ""

    if unit == "C":
        original_symbol = "°C"
        converted_symbol = "°F"
    elif unit == "F":
        original_symbol = "°F"
        converted_symbol = "°C"

    if unit == "C":
        C = temp_value
        # Use the function and round to 2 decimal places
        F = round(celsius_to_fahrenheit(C), 2)
        
        # Display result rounded to 2 decimal places
        print(f"Your original Value was: {C:.2f}{original_symbol}")
        print(f"Your converted value is: {F:.2f}{converted_symbol}")
        
    elif unit == "F":
        F = temp_value
        # Use the function and round to 2 decimal places
        C = round(fahrenheit_to_celsius(F), 2)
        
        # Display result rounded to 2 decimal places
        print(f"Your original Value was: {F:.2f}{original_symbol}")
        print(f"Your converted value is: {C:.2f}{converted_symbol}")


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