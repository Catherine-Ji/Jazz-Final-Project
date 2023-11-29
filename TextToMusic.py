import string
from mingus.midi import fluidsynth
from mingus.containers import Note
import time
import random
import numpy as np
import pygame
# import fluidsynth

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
  " ": "C-2",
}
punctation = set(string.punctuation)
punctation_dict = {
    "!": 5,
    "?": 2,
    ".": 1,
    "-": 2,
    ",": 3,
    ";": 4
}

def main():
    print("""
    Welcome to the Jazz Symphony Generator!

        ♫    ♪                ♫     ♫
        ♫        ♪         ♪           ♫
          ♫           ♪             ♫
             ♫                 ♫
                 ♪     ♫
    """)
    while True:
        text = input("Please enter your text to convert to jazz (type 'exit' to stop): ")
        
        if text.lower() == 'exit':
            print("Thank you for playing :)")
            break

        while not isEnglish(text):
            text = input("Sorry, your string contains non-English characters, please try again: ")

        fluidsynth.init("FluidR3_GM2-2.SF2")
        fluidsynth.set_instrument(1, 6)

        for letter in text:
            if letter in dict.keys():
                n = Note(dict[letter.lower()])
            elif letter in punctation_dict:
                snare_sound_file = "./snare.wav"  # Replace with the path to your snare drum sound file
                for _ in range(punctation_dict[letter]):
                    play_drum_sound(snare_sound_file)
                    n = Note(dict[random.choice(string.ascii_letters).lower()])
                    n.channel = 0
                    n.velocity = 50
                    fluidsynth.play_Note(n)
                    time.sleep(0.2)
                    fluidsynth.stop_Note(n)
                continue
            else:
                n = Note(dict[random.choice(string.ascii_letters).lower()])
                
            n.channel = 0
            n.velocity = 50
            fluidsynth.play_Note(n)
            time.sleep(0.2)
            fluidsynth.stop_Note(n)
    
def isEnglish(text):
    try:
        text.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True
def play_drum_sound(sound_file):
    pygame.mixer.init()
    sound = pygame.mixer.Sound(sound_file)
    sound.play()
    time.sleep(1)

if __name__ == "__main__":
    main()
    
