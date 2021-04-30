import os

class DisplayGrid:

    # def prRed(skk): print("\033[91m {}\033[00m" .format(skk))
    # def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
    # def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))
    # def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))
    # def prPurple(skk): print("\033[95m {}\033[00m" .format(skk))
    # def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))
    # def prLightGray(skk): print("\033[97m {}\033[00m" .format(skk))
    # def prBlack(skk): print("\033[98m {}\033[00m" .format(skk))

    def __init__(self, xl: int, yl: int, abilities, pos1=(0, 0), pos2=(1, 1), sHealth:int = 100):
        self.xLength = xl
        self.yLength = yl
        self.pos1 = pos1
        self.pos2 = pos2
        self.health1 = sHealth
        self.health2 = sHealth
        self.abilities = abilities

    def __displayGrid(self):  # (private method) Shows grid of characters
        print('''
        ┌────────────────────────────────────────────────────────────────────────┐
        │                                                                        │
        │      {}                                              {}         │
        │                                                                        │
        │       {}                                               {}        │
        │      {}                                         {}       │
        │      {}                                        /\.-`( '.' )       │
        │       \_-_/_                                       / /    \_-_/_       │
        │    .-"`'V'//-.                                     \ `-.-"`'V'//-.     │
        │   / ,   |// , \\                                     `.__,   |// , \\    │
        │  / /|Ll //Ll|\ \\      :::     :::       ::::::::        |Ll //Ll|\ \\   │
        │ / / |__//   | \_\     :+:     :+:      :+:    :+:       |__//   | \_\\  │
        │ \ \/---|[]==| / /     +:+     +:+      +:+             /---|[]==| / /  │
        │  \/\__/ |   \/\/      +#+     +:+      +#++:++#++      \__/ |   \/\/   │
        │   |/_   | Ll_\|       +#+   +#+              +#+       /_   | Ll_\|    │
        │     |`^"""^`|         #+#+#+#        #+#    #+#         |`^"""^`|      │
        │     |   |   |          ###           ########           |   |   |      │
        │     |   |   |                                           |   |   |      │
        │     |   |   |                                           |   |   |      │
        │     |   |   |                                           |   |   |      │
        │     L___l___J                                           L___l___J      │
        │      |_ | _|                                             |_ | _|       │
        │     (___|___)                                           (___|___)      │
        │                                                                        │
        └────────────────────────────────────────────────────────────────────────┘'''
        .format('\033[95mPlayer 1\033[00m','\033[93mBOT\033[00m','\033[95m.---.\033[00m','\033[93m.---.\033[00m','\033[95m/_____\\\033[00m','\033[93m___ /_____\\\033[00m','\033[95m( \'.\' )\033[00m'))
        print()

    def __resetDisplay(self, abl=None):
        os.system('clear')
        print()
        self.displaygrid()
        print()
        if abl: print('Player 1 has used the {} ability!'.format(abl.n))

    def __displayHealthBar(self):  # (private method) shows the 2 healthbars
        print('\nPlayer 1 Health: ', end='')
        for i in range(10):
            if i < (self.health1 // 10):
                print('\033[92m█\033[00m', end='')
            else:
                print('\033[91m░\033[00m', end='')
        print('\nPlayer 2 Health: ', end='')
        for j in range(10):
            if j < (self.health2 // 10):
                print('\033[92m█\033[00m', end='')
            else:
                print('\033[91m░\033[00m', end='')

    def displaygrid(self):  # Display full grid
        self.__displayGrid()
        self.__displayHealthBar()
        print()
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
        self.__resetDisplay(abl)

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
