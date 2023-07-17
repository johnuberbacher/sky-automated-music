import pygetwindow as gw
import pyautogui
import time
import json
import sys

# Find the window with the specified title
window = gw.getWindowsWithTitle("Chiaki | Stream")[0]

# Access the command-line arguments
arguments = sys.argv

# Activate the window
window.activate()

# Chiaki Key Mappings
key_mapping = {
    '1Key0': '3',
    '1Key1': '4',
    '1Key2': 'k',
    '1Key3': 'x',
    '1Key4': 'j',
    '1Key5': 'v',
    '1Key6': 'i',
    '1Key7': 'z',
    '1Key8': 'l',
    '1Key9': 'c',
    '1Key10': '1',
    '1Key11': '2',
    '1Key12': 'a',
    '1Key13': 'j',
    '1Key14': 'd'
}

# Play Tunes
def play_music(json_data):
    song_notes = json_data[0]['songNotes']
    bpm = json_data[0]['bpm']

    # Calculate the duration of a beat in seconds
    beat_duration = 60.0 / bpm

    # Start playing the music
    start_time = time.perf_counter()

    for i, note in enumerate(song_notes):
        note_time = note['time']
        note_key = note['key']

        if note_key in key_mapping:
            pyautogui.press(key_mapping[note_key])
        else:
            print("Skipped: Key not found in mapping")

        # Calculate the elapsed time since the start of the song
        elapsed_time = time.perf_counter() - start_time

        if i < len(song_notes) - 1:
            next_note_time = song_notes[i + 1]['time']
            # Calculate the time to wait before playing the next note
            wait_time = (next_note_time - note_time) / 1000  # Convert milliseconds to seconds

            # Adjust wait time to maintain the desired tempo
            remaining_time = max(0, note_time / 1000 + wait_time - elapsed_time)

            print("note_time:", note_time)
            print("wait_time:", wait_time)
            print("elapsed_time:", elapsed_time)
            print("remaining_time:", remaining_time)

            time.sleep(remaining_time)

    # Stop playing after the song
    time.sleep(2)  # Add a small delay to ensure the last note is played completely
    pyautogui.press('t')

# Check if an argument was passed
if len(arguments) > 1:
    custom_value = arguments[1]

    try:
        # Read JSON data from local file
        with open(f'songs/{custom_value}.json', 'r') as file:
            json_data = json.load(file)

        # Play the music
        play_music(json_data)
    except FileNotFoundError:
        print("Song not found.")
else:
    print("No song specified.")
