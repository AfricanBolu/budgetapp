import os
from time import sleep

# some text
print("a")
print("b")
print("c")
print("d")
print("e")
print("Screen will now be cleared in 5 Seconds")

# Waiting for 5 seconds to clear the screen
sleep(5)

# Clearing the Screen
os.system('cls')