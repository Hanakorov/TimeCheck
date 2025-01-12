import time

def simple_timer(seconds):
    try:
        print(f"Timer started for {seconds} seconds...")
        while seconds:
            mins, secs = divmod(seconds, 60)
            print(f"{mins:02}:{secs:02}", end="\r")
            time.sleep(1)
            seconds -= 1
        print("Time is up!\n")
    except KeyboardInterrupt:
        print("Timer stopped.")

def pomodoro_timer(work_duration, short_break, long_break, cycles):
    try:
        for cycle in range(1, cycles + 1):
            print(f"\nCycle {cycle} of {cycles}: Work for {work_duration} minutes")
            simple_timer(work_duration * 60)
            if cycle < cycles:
                print("Short break")
                simple_timer(short_break * 60)
            else:
                print("Long break")
                simple_timer(long_break * 60)
        print("All cycles completed! Great job!\n")
    except KeyboardInterrupt:
        print("Pomodoro timer stopped.")

def workout_timer(exercise_time, rest_time, rounds):
    try:
        for round_num in range(1, rounds + 1):
            print(f"\nRound {round_num} of {rounds}: Exercise for {exercise_time} seconds")
            simple_timer(exercise_time)
            if round_num < rounds:
                print("Rest")
                simple_timer(rest_time)
        print("Workout complete!\n")
    except KeyboardInterrupt:
        print("Workout timer stopped.")

def multi_timer(timers):
    try:
        for i, (name, duration) in enumerate(timers, 1):
            print(f"\nTimer {i}: {name} ({duration} seconds)")
            simple_timer(duration)
        print("All timers completed!\n")
    except KeyboardInterrupt:
        print("Multi-timer stopped.")

def get_int_input(prompt, error_message="Invalid input. Please enter a number."):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print(error_message)

def main_menu():
    print("\nSelect timer mode:")
    print("1. Simple Timer")
    print("2. Pomodoro Timer")
    print("3. Workout Timer")
    print("4. Multi-Timer")
    print("5. Exit Program")

if __name__ == "__main__":
    while True:
        main_menu()
        choice = input("Enter the mode number: ")

        match choice:
            case "1":
                duration = get_int_input("Enter the number of seconds for the timer: ")
                simple_timer(duration)
            case "2":
                work = get_int_input("Enter work duration (in minutes): ")
                short_break = get_int_input("Enter short break duration (in minutes): ")
                long_break = get_int_input("Enter long break duration (in minutes): ")
                cycles = get_int_input("Enter number of cycles: ")
                pomodoro_timer(work, short_break, long_break, cycles)
            case "3":
                exercise = get_int_input("Enter exercise time (in seconds): ")
                rest = get_int_input("Enter rest time (in seconds): ")
                rounds = get_int_input("Enter number of rounds: ")
                workout_timer(exercise, rest, rounds)
            case "4":
                timers = []
                print("Enter timers in the format 'name,duration' (without quotes). Type 'stop' to finish.")
                while True:
                    timer_input = input("Add a timer: ")
                    if timer_input.lower() == "stop":
                        break
                    try:
                        name, duration = timer_input.split(",")
                        timers.append((name.strip(), int(duration.strip())))
                    except ValueError:
                        print("Input error. Ensure the format is 'name,duration'.")
                multi_timer(timers)
            case "5":
                print("Exiting the program. Goodbye!")
                break
            case _:
                print("Invalid choice. Please try again.")
