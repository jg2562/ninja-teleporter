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
    def __init__(self, name, health, cooldown, pos, direction):
        self._name = name               # name of the player / baller
        self._health = health           # health of the player / baller
        self._cooldown = cooldown       # Cooldown time in terms of turns
        self._pos = pos                 # [x-cord, y-cord]
        self._dir = direction;          # 0 = north, 1 = east, 2 = south, 3 = north
# Warrrior Player
class Warrior(Person):
        def __init__(self, name, health, cooldown, pos, direction):
            super(Warrior, self).__init__(name, health, cooldown, pos, direction)

            #[2, 3, 2] 3 damage to guy directly infront of the player, 2 to guys on either side
            #[1, 0, 1] 1 damage to guy left / right of the player
            #[0, 0, 0]           
            self._attack_area = [[0, 0, .5, 0, 0],[0, 2, 3, 2, 0],[.5, 1, 0, 1, .5],[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# Baller Player - aka Josh
class Baller(Person):
        def __init__(self, name, health, cooldown, pos, direction):
            super(Warrior, self).__init__(name, health, cooldown, pos, direction)        
            self._attack_area = [[0, 1, 4, 1, 0],[0, 1, 4, 1, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# Child Player - aka Jack lol jk <3 but an child that follows and annoys would be funny kinda like a zombie
class Child(Person):
        def __init__(self, name, health, cooldown, pos, direction):
            super(Warrior, self).__init__(name, health, cooldown, pos, direction)      
            self._attack_area = [[1, 1, 1, 1, 1],[1, 1, 1, 1, 1], [1, 1, 1, 1, 1],[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]

# Teliporta Player
class Teliporta(Person):
        def __init__(self, name, health, cooldown, pos, direction):
            super(Warrior, self).__init__(name, health, cooldown, pos, direction)         
            self._attack_area = [[0, 0, 0, 0, 0],[0, 1, 8, 1, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# Game
class Game():
    def __init__(self, size):
        self._board = []
        buildBoard(size)
        buildTraps()
        placePlayers()
        run()
    def buildBoard(size):
        for i in range(0, len(size)):
            board.append([])
            for j in range(0, len(size)):
                board[i][j] = ' '
    def buildTraps():
        pass
    def placePlayers():
        pass
    def run():
        pass

G = Game(10)
x = Warrior("jef", 100, 4, [0,0], 0)

print(x._attack_area)
