class SafeDivider:
    def divide_from_string(self, str_number , divisor):
        try :
            number = float(str_number)
            result = number / divisor
            return result
        except ValueError :
            return "Input muust be a numric string"
        except ZeroDivisionError :
            return "Cannot divide by zero"
        except Exception as e :
            return f"Unexpected error: {e}"
