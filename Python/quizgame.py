
def new_game(questions, options):

    question_no = 1

    for key in questions.keys():

        print(f"Q.no.{question_no}: ", end="")
        print(key)

        for i in options[question_no-1]:
            print(i)
        print()

        question_no += 1
    check_result(questions)
    
    if play_again():
        new_game(questions, options)
    else:
        print("Bye bye!")
        
# ------------------------------

def check_result(questions):
    guesses = input("Enter your guesses respectively with space (A,B,C,D): ").upper()
    print()
    correct_guesses = ""
    for i in questions.values():
        correct_guesses += i + " "
    # print(correct_guesses)
    display_score(guesses, correct_guesses)

# -------------------------------

def display_score(guesses, correct_guesses):

    print("----------------------------------------------------")
    print("RESULTS: ")
    print()
    print("Your guesses: " + guesses)
    print("Correct guesses: " + correct_guesses)
    score = 0
    guesses_ = ""
    correct_guesses_ = ""
    for i in guesses:
        if i == " ":
            continue
        guesses_ += i
    for i in correct_guesses:
        if i == " ":
            continue
        correct_guesses_ += i
    # print(guesses_); print(correct_guesses_)

    for i in range(4):
        if guesses_[i] == correct_guesses_[i]:
            score += 1

    print(f"You score is: {(score/4)*100}%")

# --------------------------------------

def play_again():
    response = input('Do you want to play again? ').lower()
    if response == "yes":
        return True
    else:
        return False

# -------------------------------------------

new_game(questions, options)




questions = {
    "What's 2 + 2? " : "A",
    "What's 2 * 3? " : "C",
    "Who created Python? " : "D",
    "What's capital of Punjab? " : "B"
}

options = [
    ["A. 4", "B. 5", "C. Indefinite", "D. I don't know"],
    ["A. 5", "B. Zero", "C. 6", "D. Infinity"],
    ["A. Fizaan Ali", "B. Ans Ali", "C. Quaid-e-Azam", "D. Rossum"],
    ["A. Islamabad", "B. Lahore", "C. Karachi", "D. Quetta"]
]