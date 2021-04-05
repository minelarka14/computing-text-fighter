class DisplayGrid:
    def __init__(self, xl, yl, pos1=(0, 0), pos2=(1, 1), sHealth=100):
        self.xLength = xl
        self.yLength = yl
        self.pos1 = pos1
        self.pos2 = pos2
        self.health1 = sHealth
        self.health2 = sHealth

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

    def __displayHealthBar(self):  # (private method) shows the 2 healthbar
        print('\nPlayer 1 Health: ', end='')
        for i in range(10):
            if i < self.health1 // 10:
                print('*', end=' ')
            else:
                print('x', end=' ')
        print('\nPlayer 2 Health: ', end='')
        for i in range(10):
            if i < self.health2 // 10:
                print('*', end=' ')
            else:
                print('x', end=' ')

    def displaygrid(self):  # Display full grid
        self.__displayGrid()
        self.__displayHealthBar()

    def moveCharacter(self, x, y, c):  # moves a character
        if c == 0:
            self.pos1 = (x, y)
        else:
            self.pos2 = (x, y)

    def findDistance(self):  # calculates the distance between the two players
        if self.pos2[0] == self.pos1[0]:
            return max(self.pos2[1], self.pos1[1]) - min(self.pos2[1], self.pos1[1])
        elif self.pos2[1] == self.pos1[1]:
            return max(self.pos2[0], self.pos1[0]) - min(self.pos2[0], self.pos1[0])
        else:
            a = max(self.pos2[0], self.pos1[0]) - min(self.pos2[0], self.pos1[0])
            b = max(self.pos2[1], self.pos1[1]) - min(self.pos2[1], self.pos1[1])
            return (a**2 + b**2)**0.5


a = DisplayGrid(5, 6)
a.displaygrid()