def dollars_to_float(d):
    # Take in a string (d) and convert it from dollars ($10.00) to a float (10.00)
    d = d.strip("$")
    d = float(d)
    return d


def percent_to_float(p):
    # Turn a string (p) and convert it from a percentage (15%) to a float (0.15)
    p = p.strip("%")
    p = float(p) / 100
    return p


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


main()
