import random
'''
Lazy man's idear box
-maybe add random skills?
-damageTypes
-gitgood
-get board obstacles
-get turn base part rolling
-questline?
-play characters and balance them
-mult-level 2D game inbound
-watch Nakai own this thing when he inevitably joins in
-i put the above comment in at 3.11am I bet by 7pm he will be added to this repo
-if he doesnt im deleting this and the above
-Nakai appreciates the above
-are you still reading these
-get sprites working
-find someone who can make not ass sprites
-ignore lab work and do this
-get everyone to give me $20 to not do lab so I can make $$$
-https://www.youtube.com/watch?v=zQrdKtPJxI0
-what is this even?
-How dead were you when you wrote this?
'''
# Person Object for our Base Player
class Person(object):
    def __init__(self, name, health, cooldown, pos):
        self._name = name               # name of the player / baller
        self._health = health           # health of the player / baller
        self._cooldown = cooldown       # Cooldown time in terms of turns
        self._pos = pos                 # [x-cord, y-cord, z-cord, direction]0 = north, 1 = east, 2 = south, 3 = north

    def damage(self, damage):
        self._health -= damage
        if self._health < 0:
            self._health = 0

    def getPos(self):
        return (self._pos[0], self._pos[1], self._pos[2])

    def setPos(self, pos):
        self._pos = (pos[0], pos[1], pos[2], self._pos[3])


# Warrior Player
class Warrior(Person):
        def __init__(self, name, health, cooldown, pos):
            super(Warrior, self).__init__(name, health, cooldown, pos)

            #[2, 3, 2] 3 damage to guy directly in front of the player, 2 to guys on either side
            #[1, 0, 1] 1 damage to guy left / right of the player
            #[0, 0, 0]
            self._attack_area = [[0, 0, .5, 0, 0],[0, 2, 3, 2, 0],[.5, 1, 0, 1, .5],[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

        def getAttackArea():
            return self._attack_area



# Baller Player - aka Josh
class Baller(Person):
        def __init__(self, name, health, cooldown, pos):
            super(Warrior, self).__init__(name, health, cooldown, pos)
            self._attack_area = [[0, 1, 4, 1, 0],[0, 1, 4, 1, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

# Child Player - aka Jack lol jk <3 but a child that follows and annoys would be funny kinda like a zombie
class Child(Person):
        def __init__(self, name, health, cooldown, pos):
            super(Warrior, self).__init__(name, health, cooldown, pos)
            self._attack_area = [[1, 1, 1, 1, 1],[1, 1, 1, 1, 1], [1, 1, 1, 1, 1],[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]

# Teliporta Player
class Teliporta(Person):
        def __init__(self, name, health, cooldown, pos):
            super(Warrior, self).__init__(name, health, cooldown, pos)
            self._attack_area = [[0, 0, 0, 0, 0],[0, 1, 8, 1, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# Idea for Zeus, have two types of attacks one bolt or a random amount with the damage spread out randomly over the bolts
# Also as it stands, Zeus calculates the bolt O'death and that cord will always be hit relative to zeus
# Zeus (Chaos) Player
class Zeus(Person):
        def __init__(self, name, health, cooldown, pos):
            super(Warrior, self).__init__(name, health, cooldown, pos)
            self._attack_area = getAttackArea()

        def getBoltCords(self):
            return [random.randint(0, self._size),random.randint(0, self._size)]

        def getAttackArea(self):
            attack_area = [[0]*5 for i in range(5)]
            Cords = getBoltCords()
            attack_area[Cords[0],Cords[1]] = 50
            return attack_area

# Game
class Game():
    def __init__(self, size):
        self._size = (size, size, size)
        self._board = {}
        self.buildTraps()
        self.placePlayers()
        self.run()

    def buildTraps(self):
        pass
    def placePlayers(self):
        pass
    def run(self):
        pass
    # prolly gunna use this to place characters on board
    def getRandCords(self):
        return (random.randint(0, self._size),random.randint(0, self._size), 0, random.randint(0, 4))

    # Sets the player position
    def _setPerson(self, pos, player):

        self._board[player.getPos()] = player

    # Get the player at the position
    def _getPlayer(self, pos):
        return self._board[(pos[0], pos[1], pos[2])]

    # Moves person dpos from its current position
    def movePerson(self, person, dpos):
        pos = person.getPos()
        new_pos = (pos[0] + dpos[0], pos[1] + dpos[1], pos[2] + dpos[2])
        self._setPerson(self, new_pos)

    # Attacks the person at the position
    def attackPerson(self, damage, pos):
        person = self._getPlayer(pos)
        if (person is None):
            return None

        person.damage(attack)

    # Causes the player at pos to attack in his area
    def attackArea(self, pos):
        person = _getPerson(pos)
        if person is None:
            return
        area = person.getAttackArea()
        height = len(area)
        width = len(area[0])
        for col in range(height):
            for row in range(width):
                self.attackPerson(area[col][row], (pos[0] + (row - width/2), pos[1] + (col - height/2), 0)


G = Game(10)
print(G.getRandCords())
