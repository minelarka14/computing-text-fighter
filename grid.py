import os

class DisplayGrid:
    def __init__(self, xl: int, yl: int, abilities, pos1=(0, 0), pos2=(1, 1), sHealth:int = 100):
        self.xLength = xl
        self.yLength = yl
        self.pos1 = pos1
        self.pos2 = pos2
        self.health1 = sHealth
        self.health2 = sHealth
        self.abilities = abilities

    def __displayGrid(self):  # (private method) Shows grid of characters
        for i in range(self.yLength):
            for j in range(self.xLength):
                if (j, i) == self.pos1:
                    print('O', end='  ')
                elif (j, i) == self.pos2:
                    print('x', end='  ')
                else:
                    print('.', end='  ')
            print()

    def __resetDisplay(self):
        os.system('clear')
        print()
        self.displaygrid()

    def __displayHealthBar(self):  # (private method) shows the 2 healthbars
        print('\nPlayer 1 Health: ', end='')
        for i in range(10):
            if i < (self.health1 // 10):
                print('*', end=' ')
            else:
                print('x', end=' ')
        print('\nPlayer 2 Health: ', end='')
        for j in range(10):
            if j < (self.health2 // 10):
                print('*', end=' ')
            else:
                print('x', end=' ')

    def displaygrid(self):  # Display full grid
        self.__displayGrid()
        self.__displayHealthBar()
        print('\nAbilities: ', end='')
        for i in self.abilities:
            print('{} [{}],'.format(i.n, i.sk), end=' ')
        print()

    def moveCharacter(self, x, y, c):  # moves a character
        if c == 0:
            self.pos1 = (x, y)
            self.__resetDisplay()
        else:
            self.pos2 = (x, y)
            self.__resetDisplay()

    def findDistance(self):  # calculates the distance between the two players
        if self.pos2[0] == self.pos1[0]:
            return max(self.pos2[1], self.pos1[1]) - min(self.pos2[1], self.pos1[1])
        elif self.pos2[1] == self.pos1[1]:
            return max(self.pos2[0], self.pos1[0]) - min(self.pos2[0], self.pos1[0])
        else:
            a = max(self.pos2[0], self.pos1[0]) - min(self.pos2[0], self.pos1[0])
            b = max(self.pos2[1], self.pos1[1]) - min(self.pos2[1], self.pos1[1])
            return (a**2 + b**2)**0.5

    def useAbility(self, ind): # uses an ability
        abl = self.abilities[ind]
        if abl.r[1] < self.findDistance() < abl.r[0]: # checking range
            self.health1 -= abl.sd
            self.health2 -= abl.d
        self.__resetDisplay()

    def enterKeyboardStroke(self, inp):
        if inp == 'd':
            x = a.pos1[0] + 1
            y = a.pos1[1]
        if inp == 'a':
            x = a.pos1[0] - 1
            y = a.pos1[1]
        if inp == 'w':
            x = a.pos1[0]
            y = a.pos1[1] - 1
        if inp == 's':
            x = a.pos1[0]
            y = a.pos1[1] + 1
        if inp in [i.sk for i in self.abilities]:
            self.useAbility([i.sk for i in self.abilities].index(inp))
            return
        self.moveCharacter(x, y, 0)


class Ability:
    def __init__(self, typ):
        with open('ability.txt', 'r') as f:
            abil = ([ab.split() for ab in f.read().split('\n')][1:])[typ]
        self.n = abil[0]  # name
        self.r = (int(abil[2]), int(abil[1]))  # (max, min) / range
        self.d = int(abil[3])  # damage
        self.sd = int(abil[4])  # self damage
        self.sk = abil[5]  # shortcut key


a = DisplayGrid(5, 6, [Ability(0), Ability(1)])
a.displaygrid()
while 1:
    inp = input('\n')
    a.enterKeyboardStroke(inp)
