def ConvertFromCelsiusToFarenheit(temperatue:float) -> float:
    f = (temperatue / 5) * 9 + 32
    return f

def ConvertFromFarenheitToCelcius(temperatue: float) -> float:
    c = ((temperatue - 32) / 9) * 5
    return c


type_ = input("Enter F for Farenheit, and C for Cesius: ")
temperatue = int(input("Enter Temperature: "))

if type_ == "F":
    print(ConvertFromFarenheitToCelcius(temperatue))

elif type_ == "C":
    print(ConvertFromCelsiusToFarenheit(temperatue))
else:
    print("Invalid Type")
