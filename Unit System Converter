def display_main_menu():
    """Display the main conversion type menu"""
    print("\n" + "=" * 50)
    print("         UNIT CONVERTER SYSTEM")
    print("=" * 50)
    print("1. Length Conversion")
    print("2. Weight Conversion")
    print("3. Temperature Conversion")
    print("4. Exit")
    print("=" * 50)


def display_unit_menu(conversion_type, units):
    """Display available units for the selected conversion type"""
    print(f"\n--- {conversion_type} Units ---")
    for idx, unit in enumerate(units, 1):
        print(f"{idx}. {unit}")


def get_conversion_factors():
    """Return nested dictionary with conversion factors for all unit types"""
    return {
        "Length": {
            "Meter": {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Mile": 0.000621371,
                      "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701},
            "Kilometer": {"Meter": 1000, "Kilometer": 1, "Centimeter": 100000, "Millimeter": 1000000, "Mile": 0.621371,
                          "Yard": 1093.61, "Foot": 3280.84, "Inch": 39370.1},
            "Centimeter": {"Meter": 0.01, "Kilometer": 0.00001, "Centimeter": 1, "Millimeter": 10,
                           "Mile": 0.00000621371, "Yard": 0.0109361, "Foot": 0.0328084, "Inch": 0.393701},
            "Millimeter": {"Meter": 0.001, "Kilometer": 0.000001, "Centimeter": 0.1, "Millimeter": 1,
                           "Mile": 0.000000621371, "Yard": 0.00109361, "Foot": 0.00328084, "Inch": 0.0393701},
            "Mile": {"Meter": 1609.34, "Kilometer": 1.60934, "Centimeter": 160934, "Millimeter": 1609340, "Mile": 1,
                     "Yard": 1760, "Foot": 5280, "Inch": 63360},
            "Yard": {"Meter": 0.9144, "Kilometer": 0.0009144, "Centimeter": 91.44, "Millimeter": 914.4,
                     "Mile": 0.000568182, "Yard": 1, "Foot": 3, "Inch": 36},
            "Foot": {"Meter": 0.3048, "Kilometer": 0.0003048, "Centimeter": 30.48, "Millimeter": 304.8,
                     "Mile": 0.000189394, "Yard": 0.333333, "Foot": 1, "Inch": 12},
            "Inch": {"Meter": 0.0254, "Kilometer": 0.0000254, "Centimeter": 2.54, "Millimeter": 25.4,
                     "Mile": 0.000015783, "Yard": 0.0277778, "Foot": 0.0833333, "Inch": 1}
        },
        "Weight": {
            "Kilogram": {"Kilogram": 1, "Gram": 1000, "Milligram": 1000000, "Pound": 2.20462, "Ounce": 35.274,
                         "Ton": 0.001},
            "Gram": {"Kilogram": 0.001, "Gram": 1, "Milligram": 1000, "Pound": 0.00220462, "Ounce": 0.035274,
                     "Ton": 0.000001},
            "Milligram": {"Kilogram": 0.000001, "Gram": 0.001, "Milligram": 1, "Pound": 0.00000220462,
                          "Ounce": 0.000035274, "Ton": 0.000000001},
            "Pound": {"Kilogram": 0.453592, "Gram": 453.592, "Milligram": 453592, "Pound": 1, "Ounce": 16,
                      "Ton": 0.000453592},
            "Ounce": {"Kilogram": 0.0283495, "Gram": 28.3495, "Milligram": 28349.5, "Pound": 0.0625, "Ounce": 1,
                      "Ton": 0.0000283495},
            "Ton": {"Kilogram": 1000, "Gram": 1000000, "Milligram": 1000000000, "Pound": 2204.62, "Ounce": 35274,
                    "Ton": 1}
        }
    }


def celsius_to_others(celsius):
    """Convert Celsius to other temperature units"""
    return {
        "Celsius": celsius,
        "Fahrenheit": (celsius * 9 / 5) + 32,
        "Kelvin": celsius + 273.15
    }


def fahrenheit_to_others(fahrenheit):
    """Convert Fahrenheit to other temperature units"""
    celsius = (fahrenheit - 32) * 5 / 9
    return {
        "Celsius": celsius,
        "Fahrenheit": fahrenheit,
        "Kelvin": celsius + 273.15
    }


def kelvin_to_others(kelvin):
    """Convert Kelvin to other temperature units"""
    celsius = kelvin - 273.15
    return {
        "Celsius": celsius,
        "Fahrenheit": (celsius * 9 / 5) + 32,
        "Kelvin": kelvin
    }


def convert_temperature(value, from_unit):
    """Handle temperature conversions"""
    if from_unit == "Celsius":
        return celsius_to_others(value)
    elif from_unit == "Fahrenheit":
        return fahrenheit_to_others(value)
    elif from_unit == "Kelvin":
        return kelvin_to_others(value)


def convert_unit(value, from_unit, to_unit, conversion_factors):
    """Perform the unit conversion using conversion factors"""
    return value * conversion_factors[from_unit][to_unit]


def get_user_choice(prompt, max_choice):
    """Get and validate user's menu choice"""
    while True:
        try:
            choice = int(input(prompt))
            if 1 <= choice <= max_choice:
                return choice
            else:
                print(f"❌ Please enter a number between 1 and {max_choice}")
        except ValueError:
            print("❌ Invalid input! Please enter a number.")


def get_value_input():
    """Get and validate numeric value from user"""
    while True:
        try:
            value = float(input("\nEnter the value to convert: "))
            return value
        except ValueError:
            print("❌ Invalid input! Please enter a numeric value.")


def length_conversion():
    """Handle length conversion"""
    conversion_factors = get_conversion_factors()["Length"]
    units = list(conversion_factors.keys())

    display_unit_menu("Length", units)
    from_choice = get_user_choice("\nSelect FROM unit (1-8): ", len(units))
    from_unit = units[from_choice - 1]

    value = get_value_input()

    display_unit_menu("Length", units)
    to_choice = get_user_choice("\nSelect TO unit (1-8): ", len(units))
    to_unit = units[to_choice - 1]

    result = convert_unit(value, from_unit, to_unit, conversion_factors)
    print(f"\n✅ Result: {value} {from_unit} = {result:.6f} {to_unit}")


def weight_conversion():
    """Handle weight conversion"""
    conversion_factors = get_conversion_factors()["Weight"]
    units = list(conversion_factors.keys())

    display_unit_menu("Weight", units)
    from_choice = get_user_choice("\nSelect FROM unit (1-6): ", len(units))
    from_unit = units[from_choice - 1]

    value = get_value_input()

    display_unit_menu("Weight", units)
    to_choice = get_user_choice("\nSelect TO unit (1-6): ", len(units))
    to_unit = units[to_choice - 1]

    result = convert_unit(value, from_unit, to_unit, conversion_factors)
    print(f"\n✅ Result: {value} {from_unit} = {result:.6f} {to_unit}")


def temperature_conversion():
    """Handle temperature conversion"""
    units = ["Celsius", "Fahrenheit", "Kelvin"]

    display_unit_menu("Temperature", units)
    from_choice = get_user_choice("\nSelect FROM unit (1-3): ", len(units))
    from_unit = units[from_choice - 1]

    value = get_value_input()

    # Convert to all temperature units
    results = convert_temperature(value, from_unit)

    print(f"\n✅ Conversion Results:")
    for unit, converted_value in results.items():
        if unit != from_unit:
            print(f"   {value} {from_unit} = {converted_value:.2f} {unit}")


def main():
    """Main function to run the unit converter"""
    print("🌟 Welcome to the Unit Converter System! 🌟")

    while True:
        display_main_menu()
        choice = get_user_choice("\nEnter your choice (1-4): ", 4)

        if choice == 1:
            length_conversion()
        elif choice == 2:
            weight_conversion()
        elif choice == 3:
            temperature_conversion()
        elif choice == 4:
            print("\n👋 Thank you for using the Unit Converter! Goodbye!")
            break

        input("\n⏎ Press Enter to continue...")


if __name__ == "__main__":
    main()
