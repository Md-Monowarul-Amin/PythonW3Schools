def calculateLeapYear(year: int)->bool: 
    if year % 400 == 0:
        return True
    else:
        if year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False

year = input("Enter year : ")
year = int(year)

if calculateLeapYear(year):
    print("Yes, it is leap year.")
else:
    print("No, it's not.")
    