import time
import threading
import keyboard
import sys
import os
import json

CONFIG_FILE = "config.json"

def beep_alarm(stop_event):
    """Function to beep an alarm sound until the stop_event is set."""
    while not stop_event.is_set():
        print('\a')  # Beep sound for all platforms
        time.sleep(1)

def clear_console():
    """Function to clear the console."""
    os.system('cls' if os.name == 'nt' else 'clear')

def get_user_configuration():
    """Function to get buff configurations from the user."""
    buffs = []
    print("Welcome to the Maple Buff Timer setup!")

    while True:
        buff_name = input("Enter the name of the buff: ")
        duration = int(input(f"Enter the duration for {buff_name} in seconds: "))
        reset_key = input(f"Enter the key to reset the timer for {buff_name} (e.g., 'R', '5'): ")

        buffs.append({
            "name": buff_name,
            "duration": duration,
            "reset_key": reset_key.upper()
        })

        another = input("Would you like to add another buff? (y/n): ").strip().lower()
        if another != 'y':
            break

    return buffs

def save_configuration(buffs):
    """Save the buff configurations to a file."""
    with open(CONFIG_FILE, 'w') as config_file:
        json.dump(buffs, config_file, indent=4)
    print(f"Configuration saved to {CONFIG_FILE}.")

def load_configuration():
    """Load the buff configurations from a file."""
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, 'r') as config_file:
            return json.load(config_file)
    return None

def start_timer(buffs):
    """Function to start the buff timers based on user configuration."""
    timers = {buff['name']: buff['duration'] for buff in buffs}
    alarm_threads = {buff['name']: None for buff in buffs}
    stop_events = {buff['name']: threading.Event() for buff in buffs}

    def create_reset_function(buff):
        def reset_timer(_):
            nonlocal timers, alarm_threads, stop_events
            clear_console()
            timers[buff['name']] = buff['duration']
            print(f"{buff['name']} timer reset to {buff['duration']} seconds.")
            if alarm_threads[buff['name']] is not None:
                stop_events[buff['name']].set()
                alarm_threads[buff['name']] = None
        return reset_timer

    for buff in buffs:
        keyboard.on_press_key(buff['reset_key'], create_reset_function(buff))

    print("Buff timers started. Press the configured keys to reset the corresponding timers.")

    while True:
        time.sleep(1)
        for buff in buffs:
            timers[buff['name']] -= 1
            if timers[buff['name']] == 0:
                print(f"\nTime's up! Recast {buff['name']}!")
                if alarm_threads[buff['name']] is None:
                    stop_events[buff['name']].clear()
                    alarm_threads[buff['name']] = threading.Thread(
                        target=beep_alarm, args=(stop_events[buff['name']],), daemon=True)
                    alarm_threads[buff['name']].start()

        sys.stdout.write("\r" + " | ".join([f"{buff['name']} Time left: {timers[buff['name']]} seconds" for buff in buffs]))
        sys.stdout.flush()

if __name__ == "__main__":
    try:
        config = load_configuration()
        if config is None:
            config = get_user_configuration()
            save_configuration(config)

        start_timer(config)
    except KeyboardInterrupt:
        print("\nTimers stopped.")
