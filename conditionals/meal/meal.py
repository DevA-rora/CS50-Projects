"""
Time:
- Breakfast if the 24 hour time is between 7:00 to 8:00 (7.0, 8.0 in float) 
- Lunch if the 24 hour time is between 12:00 to 13:00 (12.0, 13.0 in float) 
- Dinner if the 24 hour time is between 18:00 to 19:00 (18.0, 19.0 in float)
"""


def main():
    # Get the current time from the user:
    current_time = input("What time is it? ")

    # Calculate the time, decide weather to eat breakfast, lunch or dinner.
    time = convert(current_time)

    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time <= 19:
        print("dinner time")
    else:
        return


def convert(time):
    # IDEA 💡: We could take in the time, then we could replace the colon with a space, then you could split the string into the two parts and convert it into a float:?
    final_time = time.replace(":", " ")
    final_time = final_time.split()
    hours = float(final_time[0])
    minutes = float(final_time[1])
    minutes = minutes / 60

    # Finalise the time which is the hours plus minutes.
    final_time = float(hours + minutes)

    # Return the final time after calculation:
    return final_time


if __name__ == "__main__":
    main()
