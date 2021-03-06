
welcome = input("Welcome to my saving calculation!")

def power_saving(saving, num1, num2, num3):
    result = saving + num1
    for index in range(num3):
        result = num1 + result * (1 + num2/100)
    return result

try:

    saving = float(input("Enter what you have saved: "))
    num1 = float(input("Enter saving per year: "))
    num2 = float(input("Enter expected annual return: "))
    num3 = int(input("Enter years to retirement: "))

    if num3 <= 10:
        print("Your saving is expected to be:", int(power_saving(saving, num1, num2, num3)))
    else:
        for index in range(10, num3+1, 2):
            print("Your saving after", index, "years of compounding is", int(power_saving(saving, num1, num2, index)))

except ValueError:
    print("Oops, it is not a valid number, try again.")

def annuity(num4, num5):
    an_result = power_saving(saving, num1,num2, num3)
    for index in range(num5):
        an_result = (an_result - num4)*(1+num2/100)
    return an_result


try:
    print("Would you like to plan withdrawal after retirement?")
    num4 = float(input("Enter annual withdrawal: "))
    num5 = int(input("Your expectancy after retirement: "))

    print("Your annuity leftover is:", int(annuity(num4, num5)))


except ValueError:
    print("Oops, it is not a valid number, try again.")

finally:
    print("Processing Complete.")


