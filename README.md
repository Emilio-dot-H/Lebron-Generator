### Lebron-Generator

This is a small project in large part dedicated to the r/nba community. This is meant to be taken as light, fun, and in good spirit. Lebron James is a high-level athlete and a bonafide superstar in the NBA. The play on words originated as a meme where you take the first part of Jame's ("Le") name and attach it to a word of your choosing.   While this is a project to refine my coding skills, I look to clean it up and add more feature to the applications.  Upcoming features that I would like to incorporate is a 'Random' feature as well as 'Celebrity/Famous People' feature.

## How it works

The program takes in a word as input. Using PyDictionairy's library and APIs, it generates a list of synonyms for the input word. The program proceeds to execute the logic programmed to transform each synonym in that list into a 'LeWord'. 

## Logic

The 1st and 3rd letter of every word must always be capitalized.

* If the 2nd letter in the word is an 'e': Replace the first letter of the word with the letter 'L'. (i.e. Refrigerated --> LeFrigerated)
* If the 1st letter in the word is a 'b': Add 'Le' to the beginning of the word. (i.e. Banana --> LeBanana)
* If the 1st letter in the word is an 'e': Add 'L' to the beginning og the word. (i.e. Elephant --> LeLephant)
* Else: Add 'Le' to the front of the word.

## Views

![SNAG-0713](https://i.imgur.com/pBBLK3U.png)

![SNAG-0713](https://i.imgur.com/ZZnmlK2.png)

## Creating a Windows EXE file of the application

Upload the 'Lebron Generator' file to your machine. Inside of the file on your command line:
'''
pip install PySimpleGUI
pip install PyInstaller
pyinstaller -wF display.py
'''
You will be left with a single file, display.exe, located in a folder named dist under the folder where you executed the pyinstaller command.
