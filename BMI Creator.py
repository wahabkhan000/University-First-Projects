def display_welcome():
    """Display welcome message"""
    print("\n" + "="*60)
    print("        WELCOME TO YOUR PERSONAL BMI CALCULATOR")
    print("          Let's check your Body Mass Index!")
    print("="*60)


def get_measurement_system():
    """Let user choose between metric and imperial systems"""
    print("\nFirst, which measurement system do you prefer?\n")
    print("  [1] Metric (Kilograms & Centimeters)")
    print("  [2] Imperial (Pounds & Inches)")
    print("-" * 60)
    
    while True:
        try:
            choice = int(input("\nEnter your choice (1 or 2): "))
            if choice in [1, 2]:
                return choice
            else:
                print("Please choose either 1 or 2!")
        except ValueError:
            print("Oops! That's not a valid number. Try again!")


def get_positive_float(prompt, unit):
    """Get and validate positive numeric input"""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print(f"Hmm, {unit} should be a positive number. Let's try again!")
            else:
                return value
        except ValueError:
            print("That doesn't look like a number. Please enter a valid value!")


def get_metric_inputs():
    """Get height and weight in metric system"""
    print("\nGreat! Let's get your measurements (Metric System)")
    print("-" * 60)
    
    weight = get_positive_float("Enter your weight in kilograms (e.g., 70): ", "weight")
    height_cm = get_positive_float("Enter your height in centimeters (e.g., 175): ", "height")
    
    # Convert height to meters for BMI calculation
    height_m = height_cm / 100
    
    return weight, height_m, f"{height_cm} cm", f"{weight} kg"


def get_imperial_inputs():
    """Get height and weight in imperial system"""
    print("\nAwesome! Let's get your measurements (Imperial System)")
    print("-" * 60)
    
    weight_lbs = get_positive_float("Enter your weight in pounds (e.g., 154): ", "weight")
    height_inches = get_positive_float("Enter your height in inches (e.g., 69): ", "height")
    
    # Convert to metric for calculation
    weight_kg = weight_lbs * 0.453592
    height_m = height_inches * 0.0254
    
    return weight_kg, height_m, f"{height_inches} inches", f"{weight_lbs} lbs"


def calculate_bmi(weight_kg, height_m):
    """Calculate BMI using the standard formula: weight(kg) / height(m)²"""
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 2)


def classify_bmi(bmi):
    """Classify BMI and return category with details"""
    if bmi < 16.0:
        return {
            "category": "Severe Underweight",
            "status": "[CRITICAL]",
            "advice": "This is seriously low. Please consult a healthcare professional immediately.",
            "health_tip": "Consider nutrient-dense foods and professional guidance."
        }
    elif 16.0 <= bmi < 17.0:
        return {
            "category": "Moderate Underweight",
            "status": "[WARNING]",
            "advice": "You're underweight. Consider consulting a doctor or nutritionist.",
            "health_tip": "Focus on balanced meals with healthy proteins and fats."
        }
    elif 17.0 <= bmi < 18.5:
        return {
            "category": "Mild Underweight",
            "status": "[CAUTION]",
            "advice": "You're slightly underweight. A balanced diet can help!",
            "health_tip": "Add more calories through nutritious foods like nuts and avocados."
        }
    elif 18.5 <= bmi < 25.0:
        return {
            "category": "Normal (Healthy Weight)",
            "status": "[HEALTHY]",
            "advice": "Perfect! You're in the healthy weight range!",
            "health_tip": "Keep up the good work with balanced diet and regular exercise!"
        }
    elif 25.0 <= bmi < 30.0:
        return {
            "category": "Overweight",
            "status": "[CAUTION]",
            "advice": "You're slightly overweight. Small lifestyle changes can help!",
            "health_tip": "Try incorporating more veggies and 30 minutes of daily exercise."
        }
    elif 30.0 <= bmi < 35.0:
        return {
            "category": "Obese Class I",
            "status": "[WARNING]",
            "advice": "You're in the obese range. Consider consulting a healthcare provider.",
            "health_tip": "Focus on gradual weight loss through diet and exercise."
        }
    elif 35.0 <= bmi < 40.0:
        return {
            "category": "Obese Class II",
            "status": "[CRITICAL]",
            "advice": "This is a serious concern. Please seek medical advice.",
            "health_tip": "Professional guidance can help create a safe weight loss plan."
        }
    else:  # bmi >= 40.0
        return {
            "category": "Obese Class III (Severe)",
            "status": "[CRITICAL]",
            "advice": "This requires immediate medical attention for your health.",
            "health_tip": "A healthcare team can provide comprehensive support."
        }


def display_bmi_scale():
    """Display the BMI scale reference"""
    print("\nBMI Scale Reference:")
    print("=" * 60)
    print("  Below 16.0       -> Severe Underweight")
    print("  16.0 - 17.0      -> Moderate Underweight")
    print("  17.0 - 18.5      -> Mild Underweight")
    print("  18.5 - 25.0      -> Normal (Healthy)")
    print("  25.0 - 30.0      -> Overweight")
    print("  30.0 - 35.0      -> Obese Class I")
    print("  35.0 - 40.0      -> Obese Class II")
    print("  Above 40.0       -> Obese Class III")
    print("=" * 60)


def display_results(bmi, classification, height_display, weight_display):
    """Display BMI results with classification"""
    print("\n" + "="*60)
    print("                    YOUR BMI RESULTS")
    print("="*60)
    
    print(f"\nHeight: {height_display}")
    print(f"Weight: {weight_display}")
    print(f"\nYour BMI: {bmi}")
    
    print("\n" + "-" * 60)
    print(f"{classification['status']} Category: {classification['category']}")
    print("-" * 60)
    
    print(f"\nAnalysis: {classification['advice']}")
    print(f"\nHealth Tip: {classification['health_tip']}")
    
    display_bmi_scale()


def display_health_reminders():
    """Display general health reminders"""
    print("\n" + "="*60)
    print("                  IMPORTANT REMINDERS")
    print("="*60)
    print("\n  * BMI is just one indicator of health")
    print("  * Muscle weighs more than fat")
    print("  * Age, gender, and body composition matter")
    print("  * Always consult healthcare professionals for advice")
    print("  * Focus on overall wellness, not just numbers!")
    print("\n" + "="*60)


def calculate_ideal_weight_range(height_m):
    """Calculate healthy weight range for given height"""
    min_weight = 18.5 * (height_m ** 2)
    max_weight = 24.9 * (height_m ** 2)
    return round(min_weight, 1), round(max_weight, 1)


def display_ideal_range(height_m, system_choice):
    """Display ideal weight range for user's height"""
    min_kg, max_kg = calculate_ideal_weight_range(height_m)
    
    print("\nHealthy Weight Range for Your Height:")
    print("-" * 60)
    
    if system_choice == 1:  # Metric
        print(f"  Recommended: {min_kg} kg to {max_kg} kg")
    else:  # Imperial
        min_lbs = round(min_kg * 2.20462, 1)
        max_lbs = round(max_kg * 2.20462, 1)
        print(f"  Recommended: {min_lbs} lbs to {max_lbs} lbs")
        print(f"               ({min_kg} kg to {max_kg} kg)")
    
    print("-" * 60)


def main():
    """Main function to run the BMI calculator"""
    display_welcome()
    
    while True:
        # Get measurement system preference
        system_choice = get_measurement_system()
        
        # Get measurements based on system choice
        if system_choice == 1:
            weight_kg, height_m, height_display, weight_display = get_metric_inputs()
        else:
            weight_kg, height_m, height_display, weight_display = get_imperial_inputs()
        
        # Calculate BMI
        bmi = calculate_bmi(weight_kg, height_m)
        
        # Classify BMI
        classification = classify_bmi(bmi)
        
        # Display results
        display_results(bmi, classification, height_display, weight_display)
        
        # Display ideal weight range
        display_ideal_range(height_m, system_choice)
        
        # Display health reminders
        display_health_reminders()
        
        # Ask if user wants to calculate again
        print("\n" + "="*60)
        retry = input("\nWould you like to calculate again? (yes/no): ").lower().strip()
        
        if retry not in ['yes', 'y', 'yeah', 'yep', 'sure']:
            print("\n" + "="*60)
            print("      Thank you for using BMI Calculator!")
            print("           Stay healthy and take care!")
            print("="*60 + "\n")
            break


if __name__ == "__main__":
    main()
