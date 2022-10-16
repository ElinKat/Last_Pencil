import string

possibles = ['1', '2', '3']


def input_pencils():
    global pencils, error_exist
    error_exist = True

    print("How many pencils would you like to use:")
    while error_exist:
        pencils = input()
        error_found = False

        if pencils.isdigit() == False:
            print("The number of pencils should be numeric")
        elif int(pencils) == 0:
            print("The number of pencils should be positive")
        elif int(pencils) < 0:
            print("The number of pencils should be numeric")
        else:
            error_exist = False


def set_players():
    player_not_set = True
    print("Who will be the first (John, Jack):")

    while player_not_set:
        global person

        person = input()
        if person == "Jack":
            player_not_set = False
        elif person == "John":
            player_not_set = False
        else:
            print("Choose between 'John' and 'Jack'")


def print_initial_pencil_and_turn():
    print(int(pencils) * "|")
    if person == "Jack":
        print("{}'s turn:".format(person))
        bot_turn()

    elif person == "John":
        print("{}'s turn!".format(person))
        print_pencils()


def print_pencils():
    global pencils, error_exist, remove_pencils
    error_exist = True

    while error_exist:
        remove_pencils = input()
        check_turn_errors()

    pencils = int(pencils) - int(remove_pencils)
    if pencils > 0:
        print(pencils * "|")
    else:
        declare_winner()


def check_turn_errors():
    global error_exist

    if remove_pencils not in possibles:
        print("Possible values: '1', '2' or '3'")
    elif int(remove_pencils) > int(pencils):
        print("Too many pencils were taken")
    else:
        error_exist = False


def print_player_turn():
    global person
    global pencils

    if person == "Jack":
        person = "John"
    else:
        person = "Jack"

    if int(pencils) > 0:
        if person == "Jack":
            print("{}'s turn:".format(person))
            bot_turn()
        elif person == "John":
            print("{}'s turn!".format(person))
            print_pencils()


def declare_winner():
    if person == "Jack":
        print("John won!")
    else:
        print("Jack won!")


def bot_turn():
    global remove_pencils
    global pencils

    if int(pencils) % 4 == 0:
        remove_pencils = 3
    elif int(pencils) % 4 == 3:
        remove_pencils = 2
    elif int(pencils) % 4 == 2:
        remove_pencils = 1
    else:
        remove_pencils = 1
    print(remove_pencils)
    pencils = int(pencils) - int(remove_pencils)
    if int(pencils) > 0:
        print(int(pencils) * "|")
    else:
        declare_winner()


input_pencils()
set_players()
print_initial_pencil_and_turn()
# print_pencils()

while int(pencils) > 0:
    print_player_turn()
