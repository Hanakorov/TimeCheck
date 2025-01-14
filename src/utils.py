def utils(prompt, error_message="Invalid input. Please enter a number."):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(error_message)