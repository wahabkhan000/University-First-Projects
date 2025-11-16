def binary_to_decimal(binary_str):
    """Convert binary to decimal"""
    decimal = 0
    power = 0
    for digit in reversed(binary_str):
        if digit not in '01':
            raise ValueError("Invalid binary number")
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal


def octal_to_decimal(octal_str):
    """Convert octal to decimal"""
    decimal = 0
    power = 0
    for digit in reversed(octal_str):
        if digit not in '01234567':
            raise ValueError("Invalid octal number")
        decimal += int(digit) * (8 ** power)
        power += 1
    return decimal


def hexadecimal_to_decimal(hex_str):
    """Convert hexadecimal to decimal"""
    hex_str = hex_str.upper()
    hex_chars = "0123456789ABCDEF"
    decimal = 0
    power = 0
    for digit in reversed(hex_str):
        if digit not in hex_chars:
            raise ValueError("Invalid hexadecimal number")
        decimal += hex_chars.index(digit) * (16 ** power)
        power += 1
    return decimal


def decimal_to_binary(num):
    """Convert decimal to binary"""
    if num == 0:
        return "0"
    binary = ""
    while num > 0:
        binary = str(num % 2) + binary
        num = num // 2
    return binary


def decimal_to_octal(num):
    """Convert decimal to octal"""
    if num == 0:
        return "0"
    octal = ""
    while num > 0:
        octal = str(num % 8) + octal
        num = num // 8
    return octal


def decimal_to_hexadecimal(num):
    """Convert decimal to hexadecimal"""
    if num == 0:
        return "0"
    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    while num > 0:
        hexadecimal = hex_chars[num % 16] + hexadecimal
        num = num // 16
    return hexadecimal


def binary_to_octal(binary_str):
    """Convert binary to octal"""
    decimal = binary_to_decimal(binary_str)
    return decimal_to_octal(decimal)


def binary_to_hexadecimal(binary_str):
    """Convert binary to hexadecimal"""
    decimal = binary_to_decimal(binary_str)
    return decimal_to_hexadecimal(decimal)


def octal_to_binary(octal_str):
    """Convert octal to binary"""
    decimal = octal_to_decimal(octal_str)
    return decimal_to_binary(decimal)


def octal_to_hexadecimal(octal_str):
    """Convert octal to hexadecimal"""
    decimal = octal_to_decimal(octal_str)
    return decimal_to_hexadecimal(decimal)


def hexadecimal_to_binary(hex_str):
    """Convert hexadecimal to binary"""
    decimal = hexadecimal_to_decimal(hex_str)
    return decimal_to_binary(decimal)


def hexadecimal_to_octal(hex_str):
    """Convert hexadecimal to octal"""
    decimal = hexadecimal_to_decimal(hex_str)
    return decimal_to_octal(decimal)


def display_menu():
    """Display all conversion options"""
    print("\n========================================")
    print("    NUMBER SYSTEM CONVERTER")
    print("========================================")
    print("1.  Binary to Decimal")
    print("2.  Octal to Decimal")
    print("3.  Hexadecimal to Decimal")
    print("4.  Decimal to Binary")
    print("5.  Decimal to Octal")
    print("6.  Decimal to Hexadecimal")
    print("7.  Binary to Octal")
    print("8.  Binary to Hexadecimal")
    print("9.  Octal to Binary")
    print("10. Octal to Hexadecimal")
    print("11. Hexadecimal to Binary")
    print("12. Hexadecimal to Octal")
    print("0.  Exit")
    print("========================================")


def main():
    """Main program"""
    while True:
        display_menu()
        choice = input("\nEnter your choice (0-12): ").strip()

        if choice == '0':
            print("\nThank you for using Number System Converter!")
            break

        if choice not in [str(i) for i in range(1, 13)]:
            print("\nError: Invalid choice! Please enter a number between 0-12.")
            continue

        value = input("Enter the number to convert: ").strip()

        if not value:
            print("\nError: No value entered!")
            continue

        try:
            if choice == '1':
                result = binary_to_decimal(value)
                print(f"\nResult: {value} (Binary) = {result} (Decimal)")

            elif choice == '2':
                result = octal_to_decimal(value)
                print(f"\nResult: {value} (Octal) = {result} (Decimal)")

            elif choice == '3':
                result = hexadecimal_to_decimal(value)
                print(f"\nResult: {value} (Hexadecimal) = {result} (Decimal)")

            elif choice == '4':
                num = int(value)
                if num < 0:
                    raise ValueError("Negative numbers not supported")
                result = decimal_to_binary(num)
                print(f"\nResult: {value} (Decimal) = {result} (Binary)")

            elif choice == '5':
                num = int(value)
                if num < 0:
                    raise ValueError("Negative numbers not supported")
                result = decimal_to_octal(num)
                print(f"\nResult: {value} (Decimal) = {result} (Octal)")

            elif choice == '6':
                num = int(value)
                if num < 0:
                    raise ValueError("Negative numbers not supported")
                result = decimal_to_hexadecimal(num)
                print(f"\nResult: {value} (Decimal) = {result} (Hexadecimal)")

            elif choice == '7':
                result = binary_to_octal(value)
                print(f"\nResult: {value} (Binary) = {result} (Octal)")

            elif choice == '8':
                result = binary_to_hexadecimal(value)
                print(f"\nResult: {value} (Binary) = {result} (Hexadecimal)")

            elif choice == '9':
                result = octal_to_binary(value)
                print(f"\nResult: {value} (Octal) = {result} (Binary)")

            elif choice == '10':
                result = octal_to_hexadecimal(value)
                print(f"\nResult: {value} (Octal) = {result} (Hexadecimal)")

            elif choice == '11':
                result = hexadecimal_to_binary(value)
                print(f"\nResult: {value} (Hexadecimal) = {result} (Binary)")

            elif choice == '12':
                result = hexadecimal_to_octal(value)
                print(f"\nResult: {value} (Hexadecimal) = {result} (Octal)")

        except ValueError as e:
            print(f"\nError: {str(e)}")
        except Exception as e:
            print(f"\nError: An unexpected error occurred - {str(e)}")


if __name__ == "__main__":
    main()
