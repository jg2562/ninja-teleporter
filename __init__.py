import random
'''
Lazy mans Idear box
-maybe add random skills?
-dagageTypes
-gitgood
-get board obsticals
-get turn base part rolling
-questline?
-play characters and balance them
-mult-level 2D game inbound
-watch Nakai own this thing when he inevitably joins in
-i put the above comment in at 3.11am I bet by 7pm he will be added to this repo
-if he doesnt im deleting this and the above
-are you still reading these
-get sprites working
-find someone who can make not ass sprites
-ignore lab work and do this
-get everyone to give me $20 to not do lab so I can make $$$
-https://www.youtube.com/watch?v=zQrdKtPJxI0
'''
# Person Ojbect for our Base Player
class Person(object):
    def __init__(self, name, health, cooldown, pos):
        self._name = name               # name of the player / baller
        self._health = health           # health of the player / baller
        self._cooldown = cooldown       # Cooldown time in terms of turns
        self._pos = pos                 # [x-cord, y-cord, direction]0 = north, 1 = east, 2 = south, 3 = north
# Warrrior Player
class Warrior(Person):
        def __init__(self, name, health, cooldown, pos):
            super(Warrior, self).__init__(name, health, cooldown, pos)

            #[2, 3, 2] 3 damage to guy directly infront of the player, 2 to guys on either side
            #[1, 0, 1] 1 damage to guy left / right of the player
            #[0, 0, 0]           
            self._attack_area = [[0, 0, .5, 0, 0],[0, 2, 3, 2, 0],[.5, 1, 0, 1, .5],[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# Baller Player - aka Josh
class Baller(Person):
        def __init__(self, name, health, cooldown, pos):
            super(Warrior, self).__init__(name, health, cooldown, pos)        
            self._attack_area = [[0, 1, 4, 1, 0],[0, 1, 4, 1, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# Child Player - aka Jack lol jk <3 but an child that follows and annoys would be funny kinda like a zombie
class Child(Person):
        def __init__(self, name, health, cooldown, pos):
            super(Warrior, self).__init__(name, health, cooldown, pos)      
            self._attack_area = [[1, 1, 1, 1, 1],[1, 1, 1, 1, 1], [1, 1, 1, 1, 1],[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]

# Teliporta Player
class Teliporta(Person):
        def __init__(self, name, health, cooldown, pos):
            super(Warrior, self).__init__(name, health, cooldown, pos)         
            self._attack_area = [[0, 0, 0, 0, 0],[0, 1, 8, 1, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# Game
class Game():
    def __init__(self, size):
        self._size = size
        self._board = []
        self.buildBoard(size)
        self.buildTraps()
        self.placePlayers()
        self.run()
    def buildBoard(self, size):
        self._board = [[0]*self._size for i in range(self._size)]
        
    def buildTraps(self):
        pass
    def placePlayers(self):
        pass
    def run(self):
        pass
    def getRandCords(self):
        return [random.randint(0, self._size),random.randint(0, self._size),random.randint(0, 4)]

G = Game(10)
print(G.getRandCords())
