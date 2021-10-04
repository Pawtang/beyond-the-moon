import time
import sys

def slowprint(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.02)
    time.sleep(1)
    print()

class Player:
    def __init__(self, name, health, oxygen):
        self.name = name
        self.health = health
        self.oxygen = oxygen

class Monster:
    def __init__(self, name, health, oxygen):
        self.name = name
        self.health = health
        self.oxygen = oxygen



