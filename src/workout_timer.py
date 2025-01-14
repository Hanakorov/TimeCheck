# src/workout_timer.py
from simple_timer import simple_timer

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