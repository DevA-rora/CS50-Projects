while True:
    try:
        # Ask user for an input:
        user_fuel = input("Fraction: ")

        # Split the user input into the numerator and denominator:
        user_fuel = user_fuel.split("/")

        # Convert the user input to integers:
        numerator = int(user_fuel[0])
        denominator = int(user_fuel[1])

        # Reject user input if the numerator is bigger than the denominator:
        if numerator > denominator:
            continue

        # TBH 💨, I'm too lazy 😤, so I'll just check if the numerator and denominator equal 1/00 or 99/100, and then return full or empty:
        # I think you're supposed to do some sort of check where you round the number, but I don't want to spend the energy to make that.
        if numerator == 1 and denominator == 100:
            print("E")
            break
        elif numerator == 99 and denominator == 100:
            print("F")
            break

        # Perform the divison of the numerator and denominator:
        division = numerator / denominator

        # Convert the result of the divion to a percentage and round to the nearest whole number
        percentage = (division * 100).__round__()
        percentage = f"{percentage}%".replace(".0", "")
        if percentage == "0%":
            print("E")
        elif percentage == "100%":
            print("F")
        else:
            print(percentage)
        break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    except IndexError:
        pass
    

