import string
# from mingus.midi import fluidsynth
from mingus.containers import Note
import time
import random
import fluidsynth


def main():
    print("Hi there, I'm your music generator!")
    text = input("please enter your text: ")
    while not isEnglish(text):
        text = input("Sorry, your string contains non-English characters, please try again:")
    fs = fluidsynth.Synth()
    fs.open("soundfont.SF2")
    fs.program_set(0, 6)
    # fluidsynth.settings_add("synth.gain", 2.0)
    # fluidsynth.init("soundfont.SF2")
    # fluidsynth.set_instrument(1, 6)
    for letter in text:
        if letter in dict.keys():
            n = Note(dict[letter.lower()])
        else:
            n = Note(dict[random.choice(string.ascii_letters).lower()])
        n.channel = 0
        n.velocity = 50
        fs.program_change(0, 100, 127)
        # fluidsynth.play_Note(n)
        # time.sleep(0.2)
        # fluidsynth.stop_Note(n)
        
        # Play the note and wait for 0.2 seconds
        fs.note_on(n)
        time.sleep(0.2)

        # Stop the note
        fs.note_off(n)

    
dict = {
  "a": "A-3",
  "b": "B-3",
  "c": "C-4",
  "d": "D-4",
  "e": "E-4",
  "f": "F-4",
  "g": "G-4",
  "h": "A-4",
  "i": "B-4",
  "j": "C-5",
  "k": "D-5",
  "l": "E-5",
  "m": "F-5",
  "n": "G-5",
  "o": "A-5",
  "p": "B-5",
  "q": "C-6",
  "r": "D-6",
  "s": "E-6",
  "t": "F-6",
  "u": "G-6",
  "v": "A-6",
  "w": "B-6",
  "x": "C-7",
  "y": "D-7",
  "z": "E-7",
  " ": "C-2"
}
    

def isEnglish(text):
    try:
        text.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

if __name__ == "__main__":
    main()
    
