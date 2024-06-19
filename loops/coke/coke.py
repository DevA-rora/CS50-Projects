# I think this problem needs to use a while True loop:

AMOUNT_DUE = 50

while True:
    print(f"Amount Due: {AMOUNT_DUE}")
    user_coin = input("Insert Coin: ")
    if "25" in user_coin:
        AMOUNT_DUE = AMOUNT_DUE - 25
    elif "10" in user_coin:
        AMOUNT_DUE = AMOUNT_DUE - 10
    elif "5" in user_coin:
        AMOUNT_DUE = AMOUNT_DUE - 5

    if AMOUNT_DUE <= 0:
        if AMOUNT_DUE == 0:
            print(f"Change Owed: {AMOUNT_DUE}")
        else:
            AMOUNT_DUE = (
                AMOUNT_DUE * -1
            )  # remove the negative symbol from the AMMOUNT_DUE:
            print(f"Change Owed: {AMOUNT_DUE}")
        break
