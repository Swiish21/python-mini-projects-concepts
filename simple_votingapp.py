print("Hello, welcome to Junior High school Voting program")
print("There are 3 categories you will be required to vote in.")
print("They are School president, Head of academics and class lead.")

proceed_prompt = input("To proceed with this voting program, select yes or no.")
if proceed_prompt == "yes":
    print("For school president we have Mike, Diana, Jean and Kevin as candidates")
    mike = 0
    diana = 0
    jean = 0
    kevin = 0
    vote_sp = input("Please input the name of your preferred candidate:\n")
    if vote_sp == "mike":
        mike += 1
        diana = 0
        jean = 0
        kevin = 0
        print(f"Mike{mike},Diana{diana},Jean{jean},Kevin{kevin}")
    elif vote_sp == "diana":
        mike = 0
        diana += 1
        jean = 0
        kevin = 0
        print(f"Mike{mike},Diana{diana},Jean{jean},Kevin{kevin}")
    elif vote_sp == "jean":
        mike = 0
        diana = 0
        jean += 1
        kevin = 0
        print(f"Mike{mike},Diana{diana},Jean{jean},Kevin{kevin}")
    elif vote_sp == "kevin":
        mike = 0
        diana = 0
        jean = 0
        kevin += 1
        print(f"Mike{mike},Diana{diana},Jean{jean},Kevin{kevin}")

elif proceed_prompt == "no":
    print("You have chosen not to continue with the program, goodbye!")
else:
    print("Invalid input please try again!")