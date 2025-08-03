def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        return num / denom
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")
