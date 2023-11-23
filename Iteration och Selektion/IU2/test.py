answered = 0
answered_wrong = 0

def main():
    welcome()
    while True:
        print_menu()

        user_choice = input("Val: ")

        if user_choice == "1":
            #Spela spel
            user_pick = get_user_pick()
            right_pick = get_right_pick()

            get_result(user_pick, right_pick)

        elif user_choice == "2":
            #Stats
            view_stats()


def view_stats():
    print("\nStatistik")
    print("-------------")
    print(f"Du har svarat på {answered}")
    print(f"Du har svarat fel {answered_wrong} gånger")

def get_result(user_choice, right_choice):
    global answered
    global answered_wrong

    print(f"Du valde: {user_choice}")
    print(f"Rätt svar: {right_choice}")

    if user_choice == right_choice:
        print("Korrekt svarat, snyggt jobbat!")
        answered += 1 
    else:
        print("Tyvärr fel svarat, försök igen!")
        answered_wrong += 1
        answered += 1

def get_right_pick():
    choice = 1

    if choice == 1:
        print("Korrekt svarat, snyggt jobbat!")

def get_user_pick():
    choice = input("Vad gissar du på? ").lower()

    while choice != 1:
        print("Du valde inte ett giltigt alternativ")
        choice = input("Vad gissar du på? ").lower()

    return choice

def print_menu():
    print("\nMeny")
    print("-------------")
    print("1.Spela")
    print("2.Statistik")
    print("0.Avsluta")

def welcome():
    print("--------------")
    print("Meny")
    print("--------------")

main()
