class Person(object):
    def __init__(self, name, health, cooldown, pos, direction):
        self._name = name               # name of the player / baller
        self._health = health           # health of the player / baller
        self._cooldown = cooldown       # Cooldown time in terms of turns
        self._pos = pos                 # [x-cord, y-cord]
        self._dir = direction;          # 0 = north, 1 = east, 2 = south, 3 = north
class Warrior(Person):
        def __init__(self, name, health, cooldown, pos, direction):
            super(Warrior, self).__init__(name, health, cooldown, pos, direction)

            #[2, 3, 2] 3 damage to guy directly infront of the player, 2 to guys on either side
            #[1, 0, 1] 1 damage to guy left / right of the player
            #[0, 0, 0]           
            self._attack_area = [[2,3,2],[1, 0, 1], [0, 0, 0]]
            
x = Warrior("jef", 100, 4, [0,0], 0)

print(x._attack_area)
