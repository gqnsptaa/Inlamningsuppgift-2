questions = [
  { "question": "Vilken är Skånes största stad?", "answer": "Malmö"},
  { "question": "Vilket språk Programmerar vi i?", "answer": "Python"},
  { "question": "Till vilken modul tillhör denna uppgift?", "answer": "3"}
]

current_question_nr = 0
answered = 0
answered_wrong = 0

def question(fråga, svar):
    global current_question_nr
    global answered
    global answered_wrong

    choice = input(fråga+"\n")

    # Asks question until getting the right answer
    while choice.lower() != svar.lower():
        answered_wrong += 1
        choice = input("Tyvärr fel svar, försök igen! ")

    # User answered correctly 
    print("Korrekt svarat, snyggt jobbat!")
    current_question_nr += 1
    answered += 1

    # If user answered all questions correctly
    if current_question_nr >= len(questions):
        current_question_nr = 0
        return 
    
    # If user has more questions to answer
    else:
        current = questions[current_question_nr]
        question(current["question"], current["answer"])
    

def question_game():
    welcome()
    while True:
        print_menu()

        user_choice = input("Val: ")

        if user_choice == "1":
            #Spela spel
            current = questions[current_question_nr]
            question(current["question"], current["answer"])
        elif user_choice == "2":
            #Stats
            view_stats()
        elif user_choice == "0":
            #Avsluta
            break
        else:
            print("Du valde inte ett giltigt alternativ, försök igen!")

    print("\nTack för att du spelade!")

def view_stats():
    print("\nStatistik")
    print("-------------")
    print(f"Du har svarat på {answered} frågor")
    print(f"Du har svarat fel {answered_wrong} gånger")

def welcome():
    print("--------------")
    print("Meny")
    print("--------------")

def print_menu():
    print("\nMeny")
    print("-------------")
    print("1.Spela")
    print("2.Statistik")
    print("0.Avsluta")

question_game()


