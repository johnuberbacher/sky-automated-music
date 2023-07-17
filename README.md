# Sky: CotL Automated Music

Automate music playback in the game Sky: Children of the Light by reading music sheets and sending commands through the remote-play application Chiaki (for PS4 and PS5 only).

## About

Sky: Automated Music is a Python script that enables you to play music automatically in the game Sky: Children of the Light. It leverages the Chiaki remote-play application to send commands to the game console (PS4 or PS5) and simulate key presses based on the provided music sheets.

The script reads JSON files containing music sheet data and translates the notes into corresponding key presses. It calculates the timing and duration of each note to maintain the desired tempo. By automating the music playback process, you can enjoy the game while listening to beautiful melodies without manually playing each note.

[Click here for information on playing music in Sky](https://sky-children-of-the-light.fandom.com/wiki/Sky_Music_Guide)


## Setup and Installation

1. Install Python on your system if you haven't already. You can download Python from the official website: python.org.

2. Clone this repository to your local machine or download the source code as a ZIP file.

3. Install the required dependencies by running the following command in your terminal or command prompt: `pip install pygetwindow pyautogui`

4. Make sure you have the Chiaki remote-play application installed on your computer. You can download it from the official Chiaki GitHub repository: [github.com/thestr4ng3r/chiaki](github.com/thestr4ng3r/chiaki)

5. In Chiaki, map the PlayStation controller buttons to match the key mappings used by the script. Ensure that the mappings are set up correctly according to the following key mapping dictionary:
```key_mapping = {
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
```


## Usage

1. Launch the Chiaki remote-play application and connect it to your PS4 or PS5 console.

2. Open the game Sky: Children of the Light on your console.

3. Equip your instrument of choice within the game.

4. Run the sky_automated_music.py script with the following command: `python sky_automated_music.py [song_name]`

Replace [song_name] with the name of the JSON file containing the music sheet data. The JSON file should be located in the songs/ directory of this repository.

For example, to play a song named "my_song.json", use the following command:

`python sky_automated_music.py my_song`

5. The script will automatically activate the Chiaki window and start playing the music in the game.