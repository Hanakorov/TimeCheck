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