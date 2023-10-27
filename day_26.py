from replit import audio
import os

def play_song():
    source = audio.play_file('audio.wav')
    source.paused = False  # unpause the playback
    while True:
        # Start taking user input and doing something with it
        input()

while True:
    # clear the screen
    os.system("clear")
    # Show the menu
    print("Welcome to Replit's crappy song player")
    # take user's input
    play_choice = input("Play? (yes/y): ")
    if play_choice in ["yes", "y", "Yes"]:
        play_song()
    else:
        print("Ok, quitting now.")
        exit()
