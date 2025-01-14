from simple_timer import simple_timer
from pomodoro_timer import pomodoro_timer
from workout_timer import workout_timer
from multi_timer import multi_timer
from utils import utils

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
                duration = utils("Enter the number of seconds for the timer: ")
                simple_timer(duration)
            case "2":
                work = utils("Enter work duration (in minutes): ")
                short_break = utils("Enter short break duration (in minutes): ")
                long_break = utils("Enter long break duration (in minutes): ")
                cycles = utils("Enter number of cycles: ")
                pomodoro_timer(work, short_break, long_break, cycles)
            case "3":
                exercise = utils("Enter exercise time (in seconds): ")
                rest = utils("Enter rest time (in seconds): ")
                rounds = utils("Enter number of rounds: ")
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