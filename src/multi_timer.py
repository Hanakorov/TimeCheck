from simple_timer import simple_timer

def multi_timer(timers):
    try:
        for i, (name, duration) in enumerate(timers, 1):
            print(f"\nTimer {i}: {name} ({duration} seconds)")
            simple_timer(duration)
        print("All timers completed!\n")
    except KeyboardInterrupt:
        print("Multi-timer stopped.")