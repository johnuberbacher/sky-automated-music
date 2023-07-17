import pygetwindow as gw
import pyautogui
import time
import json

# Find the window with the specified title
window = gw.getWindowsWithTitle("Chiaki | Stream")[0]

# Activate the window
window.activate()

# Play Tunes
def play_music(json_data):
    bpm = json_data['bpm']
    song_notes = json_data['songNotes']
    beat_duration = 60 / bpm

    metronome_duration = beat_duration / 4  # Adjust metronome speed here
    metronome_ticks = int(beat_duration / metronome_duration)

    for i, note in enumerate(song_notes[:-1]):
        current_note_time = note['time']
        next_note_time = song_notes[i+1]['time']

        if current_note_time == next_note_time:
            current_note_key = note['key']
            next_note_key = song_notes[i+1]['key']

            if current_note_key in key_mapping and next_note_key in key_mapping:
                pyautogui.hotkey(key_mapping[current_note_key], key_mapping[next_note_key])
                pyautogui.PAUSE = 0
            else:
                print("skipped?")  # Add desired behavior if keys are not in the mapping

        elif note['key'] in key_mapping:
            pyautogui.press(key_mapping[note['key']])
            pyautogui.PAUSE = 0
        else:
            print("skipped?")

        # Wait for the next beat
        time.sleep(((next_note_time / 1000) - (current_note_time / 1000)) * 1.5)

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

# Read JSON data from local file
with open('songs/hp.json', 'r') as file:
    json_data = file.read()

# Parse JSON data
data = json.loads(json_data)

# Play the music
play_music(data)

