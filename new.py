def chatbot():
    print("Hey, I'm a simple chatbot. What is your name?")
    name = input("you:\n")
    print(f"Nice to meet you {name}, how can i assist you?")

    while True:
    user_input = input("You:").lower
    if user_input == "quit":
        break
    else:
        response = 