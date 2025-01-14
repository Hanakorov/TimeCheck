from simple_timer import simple_timer

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