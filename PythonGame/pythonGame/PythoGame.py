from random import *
import ctypes

user32 = ctypes.WinDLL('user32')

SW_MAXIMISE = 3

hWnd = user32.GetForegroundWindow()

user32.ShowWindow(hWnd, SW_MAXIMISE)


player = "ccS"
rat = " r "
score = 0
attack = 1

#Game Variables

ratHealth = 5
health = 10


gameOver = 0

x = 5
y = 5

enemyX = 2
enemyY = 2

previousXPosition = 0
previousEnemyXPosition = 0

previousYPosition = 0
previousEnemyYPosition = 0

#Components for console art

consoleComponent = ["***","   "," n - North ", " e - East ", " s - South ", " w - West ", " i - Inv ", "  s - Stats "]



#w39 x l39
levelComponent = [ ["TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT","TTT"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III"],
                   ["III","   ","   ","   ","III","III","   ","   ","   ","III","III","III","III","III","III","III","   ","   ","   ","   ","   ","   ","III","III","III","III","III","III","III","   ","   ","   ","   ","III","III","III","   ","   ","   ","III"],
                   ["III","   ","   ","   ","III","III","   ","   ","   ","III","III","III","III","III","III","III","   ","   ","   ","   ","   ","   ","III","III","III","III","III","III","III","   ","   ","   ","   ","III","III","III","   ","   ","   ","III"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","III","III","III","III","   ","   ","   ","   ","   ","   ","III","III","III","III","III","III","III","   ","   ","   ","   ","III","III","III","   ","   ","   ","III"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","III","III","III","III","   ","   ","   ","   ","   ","   ","III","III","III","III","III","III","III","   ","   ","   ","   ","III","III","III","   ","   ","   ","III"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","III","III","III","III","   ","   ","   ","   ","   ","   ","III","III","III","III","III","III","III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III"],
                   ["III","   ","   ","   ","III","III","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III"],
                   ["III","   ","   ","   ","III","III","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","   ","III","III","   ","   ","   ","   ","III","III","III","   ","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","III"],
                   ["III","   ","   ","   ","III","III","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","III","III","III","III","   ","   ","   ","III","III","III","   ","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","III"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","   ","   ","III","III","III","III","III","III","   ","   ","III","III","III","   ","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","III"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","III","III","III","III","III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","III"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","III","III","III","III","III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","III","III","III","III","III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","III","III","III","III","III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III"],                   
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","III","III","III","III","III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III"],
                   ["III","   ","   ","   ","III","III","   ","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","III","III","III","III","III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III"],
                   ["III","   ","   ","   ","III","III","   ","   ","   ","   ","   ","III","III","III","   ","III","III","III","III","III","III","III","III","   ","III","III","III","   ","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","III"],
                   ["III","   ","   ","   ","III","III","   ","   ","   ","   ","   ","III","III","III","   ","   ","III","III","III","III","III","III","   ","   ","III","III","III","   ","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","III"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","III","III","III","III","   ","   ","   ","III","III","III","   ","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","III"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","   ","III","III","   ","   ","   ","   ","III","III","III","   ","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","III"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","III","III","III","III","   ","   ","   ","   ","   ","   ","III","III","III","III","III","III","III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III"],
                   ["III","   ","   ","   ","III","III","   ","   ","   ","III","III","III","III","III","III","III","   ","   ","   ","   ","   ","   ","III","III","III","III","III","III","III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III"],
                   ["III","   ","   ","   ","III","III","   ","   ","   ","III","III","III","III","III","III","III","   ","   ","   ","   ","   ","   ","III","III","III","III","III","III","III","   ","   ","   ","   ","III","III","III","   ","   ","   ","III"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","III","III","III","III","   ","   ","   ","   ","   ","   ","III","III","III","III","III","III","III","   ","   ","   ","   ","III","III","III","   ","   ","   ","III"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","III","III","III","III","   ","   ","   ","   ","   ","   ","III","III","III","III","III","III","III","   ","   ","   ","   ","III","III","III","   ","   ","   ","III"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III","III","III","   ","   ","   ","III"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III"],
                   ["III","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","   ","III"],
                   ["LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL","LLL"],]

def creatLevel():
    print(levelComponent[0][0] + levelComponent[0][1] + levelComponent[0][2] + levelComponent[0][3] + levelComponent[0][4] + levelComponent[0][5] + levelComponent[0][6] + levelComponent[0][7] + levelComponent[0][8] + levelComponent[0][9] + levelComponent[0][10] + levelComponent[0][11] + levelComponent[0][12] + levelComponent[0][13] + levelComponent[0][14] + levelComponent[0][15] + levelComponent[0][16] + levelComponent[0][17] + levelComponent[0][18] + levelComponent[0][19] + levelComponent[0][20] + levelComponent[0][21] + levelComponent[0][22] + levelComponent[0][23] + levelComponent[0][24] + levelComponent[0][25] + levelComponent[0][26] + levelComponent[0][27] + levelComponent[0][28] + levelComponent[0][29] + levelComponent[0][30] + levelComponent[0][31] + levelComponent[0][32] + levelComponent[0][33] + levelComponent[0][34] + levelComponent[0][35] + levelComponent[0][36] + levelComponent[0][37] + levelComponent[0][38] + levelComponent[0][39])
    print(levelComponent[1][0] + levelComponent[1][1] + levelComponent[1][2] + levelComponent[1][3] + levelComponent[1][4] + levelComponent[1][5] + levelComponent[1][7] + levelComponent[1][7] + levelComponent[1][8] + levelComponent[1][9] + levelComponent[1][10] + levelComponent[1][11] + levelComponent[1][12] + levelComponent[1][13] + levelComponent[1][14] + levelComponent[1][15] + levelComponent[1][17] + levelComponent[1][17] + levelComponent[1][18] + levelComponent[1][19] + levelComponent[1][20] + levelComponent[1][21] + levelComponent[1][22] + levelComponent[1][23] + levelComponent[1][24] + levelComponent[1][25] + levelComponent[1][27] + levelComponent[1][27] + levelComponent[1][28] + levelComponent[1][29] + levelComponent[1][30] + levelComponent[1][31] + levelComponent[1][32] + levelComponent[1][33] + levelComponent[1][34] + levelComponent[1][35] + levelComponent[1][37] + levelComponent[1][37] + levelComponent[1][38] + levelComponent[1][39])
    print(levelComponent[2][0] + levelComponent[2][1] + levelComponent[2][2] + levelComponent[2][3] + levelComponent[2][4] + levelComponent[2][5] + levelComponent[2][6] + levelComponent[2][7] + levelComponent[2][8] + levelComponent[2][9] + levelComponent[2][10] + levelComponent[2][11] + levelComponent[2][12] + levelComponent[2][13] + levelComponent[2][14] + levelComponent[2][15] + levelComponent[2][16] + levelComponent[2][17] + levelComponent[2][18] + levelComponent[2][19] + levelComponent[2][20] + levelComponent[2][21] + levelComponent[2][22] + levelComponent[2][23] + levelComponent[2][24] + levelComponent[2][25] + levelComponent[2][26] + levelComponent[2][27] + levelComponent[2][28] + levelComponent[2][29] + levelComponent[2][30] + levelComponent[2][31] + levelComponent[2][32] + levelComponent[2][33] + levelComponent[2][34] + levelComponent[2][35] + levelComponent[2][36] + levelComponent[2][37] + levelComponent[2][38] + levelComponent[2][39])
    print(levelComponent[3][0] + levelComponent[3][1] + levelComponent[3][2] + levelComponent[3][3] + levelComponent[3][4] + levelComponent[3][5] + levelComponent[3][6] + levelComponent[3][7] + levelComponent[3][8] + levelComponent[3][9] + levelComponent[3][10] + levelComponent[3][11] + levelComponent[3][12] + levelComponent[3][13] + levelComponent[3][14] + levelComponent[3][15] + levelComponent[3][16] + levelComponent[3][17] + levelComponent[3][18] + levelComponent[3][19] + levelComponent[3][20] + levelComponent[3][21] + levelComponent[3][22] + levelComponent[3][23] + levelComponent[3][24] + levelComponent[3][25] + levelComponent[3][26] + levelComponent[3][27] + levelComponent[3][28] + levelComponent[3][29] + levelComponent[3][30] + levelComponent[3][31] + levelComponent[3][32] + levelComponent[3][33] + levelComponent[3][34] + levelComponent[3][35] + levelComponent[3][36] + levelComponent[3][37] + levelComponent[3][38] + levelComponent[3][39])
    print(levelComponent[4][0] + levelComponent[4][1] + levelComponent[4][2] + levelComponent[4][3] + levelComponent[4][4] + levelComponent[4][5] + levelComponent[4][6] + levelComponent[4][7] + levelComponent[4][8] + levelComponent[4][9] + levelComponent[4][10] + levelComponent[4][11] + levelComponent[4][12] + levelComponent[4][13] + levelComponent[4][14] + levelComponent[4][15] + levelComponent[4][16] + levelComponent[4][17] + levelComponent[4][18] + levelComponent[4][19] + levelComponent[4][20] + levelComponent[4][21] + levelComponent[4][22] + levelComponent[4][23] + levelComponent[4][24] + levelComponent[4][25] + levelComponent[4][26] + levelComponent[4][27] + levelComponent[4][28] + levelComponent[4][29] + levelComponent[4][30] + levelComponent[4][31] + levelComponent[4][32] + levelComponent[4][33] + levelComponent[4][34] + levelComponent[4][35] + levelComponent[4][36] + levelComponent[4][37] + levelComponent[4][38] + levelComponent[4][39])
    print(levelComponent[5][0] + levelComponent[5][1] + levelComponent[5][2] + levelComponent[5][3] + levelComponent[5][4] + levelComponent[5][5] + levelComponent[5][6] + levelComponent[5][7] + levelComponent[5][8] + levelComponent[5][9] + levelComponent[5][10] + levelComponent[5][11] + levelComponent[5][12] + levelComponent[5][13] + levelComponent[5][14] + levelComponent[5][15] + levelComponent[5][16] + levelComponent[5][17] + levelComponent[5][18] + levelComponent[5][19] + levelComponent[5][20] + levelComponent[5][21] + levelComponent[5][22] + levelComponent[5][23] + levelComponent[5][24] + levelComponent[5][25] + levelComponent[5][26] + levelComponent[5][27] + levelComponent[5][28] + levelComponent[5][29] + levelComponent[5][30] + levelComponent[5][31] + levelComponent[5][32] + levelComponent[5][33] + levelComponent[5][34] + levelComponent[5][35] + levelComponent[5][36] + levelComponent[5][37] + levelComponent[5][38] + levelComponent[5][39])
    print(levelComponent[6][0] + levelComponent[6][1] + levelComponent[6][2] + levelComponent[6][3] + levelComponent[6][4] + levelComponent[6][5] + levelComponent[6][6] + levelComponent[6][7] + levelComponent[6][8] + levelComponent[6][9] + levelComponent[6][10] + levelComponent[6][11] + levelComponent[6][12] + levelComponent[6][13] + levelComponent[6][14] + levelComponent[6][15] + levelComponent[6][16] + levelComponent[6][17] + levelComponent[6][18] + levelComponent[6][19] + levelComponent[6][20] + levelComponent[6][21] + levelComponent[6][22] + levelComponent[6][23] + levelComponent[6][24] + levelComponent[6][25] + levelComponent[6][26] + levelComponent[6][27] + levelComponent[6][28] + levelComponent[6][29] + levelComponent[6][30] + levelComponent[6][31] + levelComponent[6][32] + levelComponent[6][33] + levelComponent[6][34] + levelComponent[6][35] + levelComponent[6][36] + levelComponent[6][37] + levelComponent[6][38] + levelComponent[6][39])
    print(levelComponent[7][0] + levelComponent[7][1] + levelComponent[7][2] + levelComponent[7][3] + levelComponent[7][4] + levelComponent[7][5] + levelComponent[7][7] + levelComponent[7][7] + levelComponent[7][8] + levelComponent[7][9] + levelComponent[7][10] + levelComponent[7][11] + levelComponent[7][12] + levelComponent[7][13] + levelComponent[7][14] + levelComponent[7][15] + levelComponent[7][17] + levelComponent[7][17] + levelComponent[7][18] + levelComponent[7][19] + levelComponent[7][20] + levelComponent[7][21] + levelComponent[7][22] + levelComponent[7][23] + levelComponent[7][24] + levelComponent[7][25] + levelComponent[7][27] + levelComponent[7][27] + levelComponent[7][28] + levelComponent[7][29] + levelComponent[7][30] + levelComponent[7][31] + levelComponent[7][32] + levelComponent[7][33] + levelComponent[7][34] + levelComponent[7][35] + levelComponent[7][37] + levelComponent[7][37] + levelComponent[7][38] + levelComponent[7][39])
    print(levelComponent[8][0] + levelComponent[8][1] + levelComponent[8][2] + levelComponent[8][3] + levelComponent[8][4] + levelComponent[8][5] + levelComponent[8][6] + levelComponent[8][7] + levelComponent[8][8] + levelComponent[8][9] + levelComponent[8][10] + levelComponent[8][11] + levelComponent[8][12] + levelComponent[8][13] + levelComponent[8][14] + levelComponent[8][15] + levelComponent[8][16] + levelComponent[8][17] + levelComponent[8][18] + levelComponent[8][19] + levelComponent[8][20] + levelComponent[8][21] + levelComponent[8][22] + levelComponent[8][23] + levelComponent[8][24] + levelComponent[8][25] + levelComponent[8][26] + levelComponent[8][27] + levelComponent[8][28] + levelComponent[8][29] + levelComponent[8][30] + levelComponent[8][31] + levelComponent[8][32] + levelComponent[8][33] + levelComponent[8][34] + levelComponent[8][35] + levelComponent[8][36] + levelComponent[8][37] + levelComponent[8][38] + levelComponent[8][39])
    print(levelComponent[9][0] + levelComponent[9][1] + levelComponent[9][2] + levelComponent[9][3] + levelComponent[9][4] + levelComponent[9][5] + levelComponent[9][6] + levelComponent[9][7] + levelComponent[9][8] + levelComponent[9][9] + levelComponent[9][10] + levelComponent[9][11] + levelComponent[9][12] + levelComponent[9][13] + levelComponent[9][14] + levelComponent[9][15] + levelComponent[9][16] + levelComponent[9][17] + levelComponent[9][18] + levelComponent[9][19] + levelComponent[9][20] + levelComponent[9][21] + levelComponent[9][22] + levelComponent[9][23] + levelComponent[9][24] + levelComponent[9][25] + levelComponent[9][26] + levelComponent[9][27] + levelComponent[9][28] + levelComponent[9][29] + levelComponent[9][30] + levelComponent[9][31] + levelComponent[9][32] + levelComponent[9][33] + levelComponent[9][34] + levelComponent[9][35] + levelComponent[9][36] + levelComponent[9][37] + levelComponent[9][38] + levelComponent[9][39])
    print(levelComponent[10][0] + levelComponent[10][1] + levelComponent[10][2] + levelComponent[10][3] + levelComponent[10][4] + levelComponent[10][5] + levelComponent[10][6] + levelComponent[10][7] + levelComponent[10][8] + levelComponent[10][9] + levelComponent[10][10] + levelComponent[10][11] + levelComponent[10][12] + levelComponent[10][13] + levelComponent[10][14] + levelComponent[10][15] + levelComponent[10][16] + levelComponent[10][17] + levelComponent[10][18] + levelComponent[10][19] + levelComponent[10][20] + levelComponent[10][21] + levelComponent[10][22] + levelComponent[10][23] + levelComponent[10][24] + levelComponent[10][25] + levelComponent[10][26] + levelComponent[10][27] + levelComponent[10][28] + levelComponent[10][29] + levelComponent[10][30] + levelComponent[10][31] + levelComponent[10][32] + levelComponent[10][33] + levelComponent[10][34] + levelComponent[10][35] + levelComponent[10][36] + levelComponent[10][37] + levelComponent[10][38] + levelComponent[10][39])
    print(levelComponent[11][0] + levelComponent[11][1] + levelComponent[11][2] + levelComponent[11][3] + levelComponent[11][4] + levelComponent[11][5] + levelComponent[11][6] + levelComponent[11][7] + levelComponent[11][8] + levelComponent[11][9] + levelComponent[11][10] + levelComponent[11][11] + levelComponent[11][12] + levelComponent[11][13] + levelComponent[11][14] + levelComponent[11][15] + levelComponent[11][16] + levelComponent[11][17] + levelComponent[11][18] + levelComponent[11][19] + levelComponent[11][20] + levelComponent[11][21] + levelComponent[11][22] + levelComponent[11][23] + levelComponent[11][24] + levelComponent[11][25] + levelComponent[11][26] + levelComponent[11][27] + levelComponent[11][28] + levelComponent[11][29] + levelComponent[11][30] + levelComponent[11][31] + levelComponent[11][32] + levelComponent[11][33] + levelComponent[11][34] + levelComponent[11][35] + levelComponent[11][36] + levelComponent[11][37] + levelComponent[11][38] + levelComponent[11][39])
    print(levelComponent[12][0] + levelComponent[12][1] + levelComponent[12][2] + levelComponent[12][3] + levelComponent[12][4] + levelComponent[12][5] + levelComponent[12][6] + levelComponent[12][7] + levelComponent[12][8] + levelComponent[12][9] + levelComponent[12][10] + levelComponent[12][11] + levelComponent[12][12] + levelComponent[12][13] + levelComponent[12][14] + levelComponent[12][15] + levelComponent[12][16] + levelComponent[12][17] + levelComponent[12][18] + levelComponent[12][19] + levelComponent[12][20] + levelComponent[12][21] + levelComponent[12][22] + levelComponent[12][23] + levelComponent[12][24] + levelComponent[12][25] + levelComponent[12][26] + levelComponent[12][27] + levelComponent[12][28] + levelComponent[12][29] + levelComponent[12][30] + levelComponent[12][31] + levelComponent[12][32] + levelComponent[12][33] + levelComponent[12][34] + levelComponent[12][35] + levelComponent[12][36] + levelComponent[12][37] + levelComponent[12][38] + levelComponent[12][39])
    print(levelComponent[13][0] + levelComponent[13][1] + levelComponent[13][2] + levelComponent[13][3] + levelComponent[13][4] + levelComponent[13][5] + levelComponent[13][6] + levelComponent[13][7] + levelComponent[13][8] + levelComponent[13][9] + levelComponent[13][10] + levelComponent[13][11] + levelComponent[13][12] + levelComponent[13][13] + levelComponent[13][14] + levelComponent[13][15] + levelComponent[13][16] + levelComponent[13][17] + levelComponent[13][18] + levelComponent[13][19] + levelComponent[13][20] + levelComponent[13][21] + levelComponent[13][22] + levelComponent[13][23] + levelComponent[13][24] + levelComponent[13][25] + levelComponent[13][26] + levelComponent[13][27] + levelComponent[13][28] + levelComponent[13][29] + levelComponent[13][30] + levelComponent[13][31] + levelComponent[13][32] + levelComponent[13][33] + levelComponent[13][34] + levelComponent[13][35] + levelComponent[13][36] + levelComponent[13][37] + levelComponent[13][38] + levelComponent[13][39])
    print(levelComponent[14][0] + levelComponent[14][1] + levelComponent[14][2] + levelComponent[14][3] + levelComponent[14][4] + levelComponent[14][5] + levelComponent[14][6] + levelComponent[14][7] + levelComponent[14][8] + levelComponent[14][9] + levelComponent[14][10] + levelComponent[14][11] + levelComponent[14][12] + levelComponent[14][13] + levelComponent[14][14] + levelComponent[14][15] + levelComponent[14][16] + levelComponent[14][17] + levelComponent[14][18] + levelComponent[14][19] + levelComponent[14][20] + levelComponent[14][21] + levelComponent[14][22] + levelComponent[14][23] + levelComponent[14][24] + levelComponent[14][25] + levelComponent[14][26] + levelComponent[14][27] + levelComponent[14][28] + levelComponent[14][29] + levelComponent[14][30] + levelComponent[14][31] + levelComponent[14][32] + levelComponent[14][33] + levelComponent[14][34] + levelComponent[14][35] + levelComponent[14][36] + levelComponent[14][37] + levelComponent[14][38] + levelComponent[14][39])
    print(levelComponent[15][0] + levelComponent[15][1] + levelComponent[15][2] + levelComponent[15][3] + levelComponent[15][4] + levelComponent[15][5] + levelComponent[15][6] + levelComponent[15][7] + levelComponent[15][8] + levelComponent[15][9] + levelComponent[15][10] + levelComponent[15][11] + levelComponent[15][12] + levelComponent[15][13] + levelComponent[15][14] + levelComponent[15][15] + levelComponent[15][16] + levelComponent[15][17] + levelComponent[15][18] + levelComponent[15][19] + levelComponent[15][20] + levelComponent[15][21] + levelComponent[15][22] + levelComponent[15][23] + levelComponent[15][24] + levelComponent[15][25] + levelComponent[15][26] + levelComponent[15][27] + levelComponent[15][28] + levelComponent[15][29] + levelComponent[15][30] + levelComponent[15][31] + levelComponent[15][32] + levelComponent[15][33] + levelComponent[15][34] + levelComponent[15][35] + levelComponent[15][36] + levelComponent[15][37] + levelComponent[15][38] + levelComponent[15][39])
    print(levelComponent[16][0] + levelComponent[16][1] + levelComponent[16][2] + levelComponent[16][3] + levelComponent[16][4] + levelComponent[16][5] + levelComponent[16][6] + levelComponent[16][7] + levelComponent[16][8] + levelComponent[16][9] + levelComponent[16][10] + levelComponent[16][11] + levelComponent[16][12] + levelComponent[16][13] + levelComponent[16][14] + levelComponent[16][15] + levelComponent[16][16] + levelComponent[16][17] + levelComponent[16][18] + levelComponent[16][19] + levelComponent[16][20] + levelComponent[16][21] + levelComponent[16][22] + levelComponent[16][23] + levelComponent[16][24] + levelComponent[16][25] + levelComponent[16][26] + levelComponent[16][27] + levelComponent[16][28] + levelComponent[16][29] + levelComponent[16][30] + levelComponent[16][31] + levelComponent[16][32] + levelComponent[16][33] + levelComponent[16][34] + levelComponent[16][35] + levelComponent[16][36] + levelComponent[16][37] + levelComponent[16][38] + levelComponent[16][39])
    print(levelComponent[17][0] + levelComponent[17][1] + levelComponent[17][2] + levelComponent[17][3] + levelComponent[17][4] + levelComponent[17][5] + levelComponent[17][6] + levelComponent[17][7] + levelComponent[17][8] + levelComponent[17][9] + levelComponent[17][10] + levelComponent[17][11] + levelComponent[17][12] + levelComponent[17][13] + levelComponent[17][14] + levelComponent[17][15] + levelComponent[17][16] + levelComponent[17][17] + levelComponent[17][18] + levelComponent[17][19] + levelComponent[17][20] + levelComponent[17][21] + levelComponent[17][22] + levelComponent[17][23] + levelComponent[17][24] + levelComponent[17][25] + levelComponent[17][26] + levelComponent[17][27] + levelComponent[17][28] + levelComponent[17][29] + levelComponent[17][30] + levelComponent[17][31] + levelComponent[17][32] + levelComponent[17][33] + levelComponent[17][34] + levelComponent[17][35] + levelComponent[17][36] + levelComponent[17][37] + levelComponent[17][38] + levelComponent[17][39])
    print(levelComponent[18][0] + levelComponent[18][1] + levelComponent[18][2] + levelComponent[18][3] + levelComponent[18][4] + levelComponent[18][5] + levelComponent[18][6] + levelComponent[18][7] + levelComponent[18][8] + levelComponent[18][9] + levelComponent[18][10] + levelComponent[18][11] + levelComponent[18][12] + levelComponent[18][13] + levelComponent[18][14] + levelComponent[18][15] + levelComponent[18][16] + levelComponent[18][17] + levelComponent[18][18] + levelComponent[18][19] + levelComponent[18][20] + levelComponent[18][21] + levelComponent[18][22] + levelComponent[18][23] + levelComponent[18][24] + levelComponent[18][25] + levelComponent[18][26] + levelComponent[18][27] + levelComponent[18][28] + levelComponent[18][29] + levelComponent[18][30] + levelComponent[18][31] + levelComponent[18][32] + levelComponent[18][33] + levelComponent[18][34] + levelComponent[18][35] + levelComponent[18][36] + levelComponent[18][37] + levelComponent[18][38] + levelComponent[18][39])
    print(levelComponent[19][0] + levelComponent[19][1] + levelComponent[19][2] + levelComponent[19][3] + levelComponent[19][4] + levelComponent[19][5] + levelComponent[19][6] + levelComponent[19][7] + levelComponent[19][8] + levelComponent[19][9] + levelComponent[19][10] + levelComponent[19][11] + levelComponent[19][12] + levelComponent[19][13] + levelComponent[19][14] + levelComponent[19][15] + levelComponent[19][16] + levelComponent[19][17] + levelComponent[19][18] + levelComponent[19][19] + levelComponent[19][20] + levelComponent[19][21] + levelComponent[19][22] + levelComponent[19][23] + levelComponent[19][24] + levelComponent[19][25] + levelComponent[19][26] + levelComponent[19][27] + levelComponent[19][28] + levelComponent[19][29] + levelComponent[19][30] + levelComponent[19][31] + levelComponent[19][32] + levelComponent[19][33] + levelComponent[19][34] + levelComponent[19][35] + levelComponent[19][36] + levelComponent[19][37] + levelComponent[19][38] + levelComponent[19][39])
    print(levelComponent[20][0] + levelComponent[20][1] + levelComponent[20][2] + levelComponent[20][3] + levelComponent[20][4] + levelComponent[20][5] + levelComponent[20][6] + levelComponent[20][7] + levelComponent[20][8] + levelComponent[20][9] + levelComponent[20][10] + levelComponent[20][11] + levelComponent[20][12] + levelComponent[20][13] + levelComponent[20][14] + levelComponent[20][15] + levelComponent[20][16] + levelComponent[20][17] + levelComponent[20][18] + levelComponent[20][19] + levelComponent[20][20] + levelComponent[20][21] + levelComponent[20][22] + levelComponent[20][23] + levelComponent[20][24] + levelComponent[20][25] + levelComponent[20][26] + levelComponent[20][27] + levelComponent[20][28] + levelComponent[20][29] + levelComponent[20][30] + levelComponent[20][31] + levelComponent[20][32] + levelComponent[20][33] + levelComponent[20][34] + levelComponent[20][35] + levelComponent[20][36] + levelComponent[20][37] + levelComponent[20][38] + levelComponent[20][39])
    print(levelComponent[21][0] + levelComponent[21][1] + levelComponent[21][2] + levelComponent[21][3] + levelComponent[21][4] + levelComponent[21][5] + levelComponent[21][6] + levelComponent[21][7] + levelComponent[21][8] + levelComponent[21][9] + levelComponent[21][10] + levelComponent[21][11] + levelComponent[21][12] + levelComponent[21][13] + levelComponent[21][14] + levelComponent[21][15] + levelComponent[21][16] + levelComponent[21][17] + levelComponent[21][18] + levelComponent[21][19] + levelComponent[21][20] + levelComponent[21][21] + levelComponent[21][22] + levelComponent[21][23] + levelComponent[21][24] + levelComponent[21][25] + levelComponent[21][26] + levelComponent[21][27] + levelComponent[21][28] + levelComponent[21][29] + levelComponent[21][30] + levelComponent[21][31] + levelComponent[21][32] + levelComponent[21][33] + levelComponent[21][34] + levelComponent[21][35] + levelComponent[21][36] + levelComponent[21][37] + levelComponent[21][38] + levelComponent[21][39])
    print(levelComponent[22][0] + levelComponent[22][1] + levelComponent[22][2] + levelComponent[22][3] + levelComponent[22][4] + levelComponent[22][5] + levelComponent[22][6] + levelComponent[22][7] + levelComponent[22][8] + levelComponent[22][9] + levelComponent[22][10] + levelComponent[22][11] + levelComponent[22][12] + levelComponent[22][13] + levelComponent[22][14] + levelComponent[22][15] + levelComponent[22][16] + levelComponent[22][17] + levelComponent[22][18] + levelComponent[22][19] + levelComponent[22][20] + levelComponent[22][21] + levelComponent[22][22] + levelComponent[22][23] + levelComponent[22][24] + levelComponent[22][25] + levelComponent[22][26] + levelComponent[22][27] + levelComponent[22][28] + levelComponent[22][29] + levelComponent[22][30] + levelComponent[22][31] + levelComponent[22][32] + levelComponent[22][33] + levelComponent[22][34] + levelComponent[22][35] + levelComponent[22][36] + levelComponent[22][37] + levelComponent[22][38] + levelComponent[22][39])
    print(levelComponent[23][0] + levelComponent[23][1] + levelComponent[23][2] + levelComponent[23][3] + levelComponent[23][4] + levelComponent[23][5] + levelComponent[23][6] + levelComponent[23][7] + levelComponent[23][8] + levelComponent[23][9] + levelComponent[23][10] + levelComponent[23][11] + levelComponent[23][12] + levelComponent[23][13] + levelComponent[23][14] + levelComponent[23][15] + levelComponent[23][16] + levelComponent[23][17] + levelComponent[23][18] + levelComponent[23][19] + levelComponent[23][20] + levelComponent[23][21] + levelComponent[23][22] + levelComponent[23][23] + levelComponent[23][24] + levelComponent[23][25] + levelComponent[23][26] + levelComponent[23][27] + levelComponent[23][28] + levelComponent[23][29] + levelComponent[23][30] + levelComponent[23][31] + levelComponent[23][32] + levelComponent[23][33] + levelComponent[23][34] + levelComponent[23][35] + levelComponent[23][36] + levelComponent[23][37] + levelComponent[23][38] + levelComponent[23][39])
    print(levelComponent[24][0] + levelComponent[24][1] + levelComponent[24][2] + levelComponent[24][3] + levelComponent[24][4] + levelComponent[24][5] + levelComponent[24][6] + levelComponent[24][7] + levelComponent[24][8] + levelComponent[24][9] + levelComponent[24][10] + levelComponent[24][11] + levelComponent[24][12] + levelComponent[24][13] + levelComponent[24][14] + levelComponent[24][15] + levelComponent[24][16] + levelComponent[24][17] + levelComponent[24][18] + levelComponent[24][19] + levelComponent[24][20] + levelComponent[24][21] + levelComponent[24][22] + levelComponent[24][23] + levelComponent[24][24] + levelComponent[24][25] + levelComponent[24][26] + levelComponent[24][27] + levelComponent[24][28] + levelComponent[24][29] + levelComponent[24][30] + levelComponent[24][31] + levelComponent[24][32] + levelComponent[24][33] + levelComponent[24][34] + levelComponent[24][35] + levelComponent[24][36] + levelComponent[24][37] + levelComponent[24][38] + levelComponent[24][39])
    print(levelComponent[25][0] + levelComponent[25][1] + levelComponent[25][2] + levelComponent[25][3] + levelComponent[25][4] + levelComponent[25][5] + levelComponent[25][6] + levelComponent[25][7] + levelComponent[25][8] + levelComponent[25][9] + levelComponent[25][10] + levelComponent[25][11] + levelComponent[25][12] + levelComponent[25][13] + levelComponent[25][14] + levelComponent[25][15] + levelComponent[25][16] + levelComponent[25][17] + levelComponent[25][18] + levelComponent[25][19] + levelComponent[25][20] + levelComponent[25][21] + levelComponent[25][22] + levelComponent[25][23] + levelComponent[25][24] + levelComponent[25][25] + levelComponent[25][26] + levelComponent[25][27] + levelComponent[25][28] + levelComponent[25][29] + levelComponent[25][30] + levelComponent[25][31] + levelComponent[25][32] + levelComponent[25][33] + levelComponent[25][34] + levelComponent[25][35] + levelComponent[25][36] + levelComponent[25][37] + levelComponent[25][38] + levelComponent[25][39])
    print(levelComponent[26][0] + levelComponent[26][1] + levelComponent[26][2] + levelComponent[26][3] + levelComponent[26][4] + levelComponent[26][5] + levelComponent[26][6] + levelComponent[26][7] + levelComponent[26][8] + levelComponent[26][9] + levelComponent[26][10] + levelComponent[26][11] + levelComponent[26][12] + levelComponent[26][13] + levelComponent[26][14] + levelComponent[26][15] + levelComponent[26][16] + levelComponent[26][17] + levelComponent[26][18] + levelComponent[26][19] + levelComponent[26][20] + levelComponent[26][21] + levelComponent[26][22] + levelComponent[26][23] + levelComponent[26][24] + levelComponent[26][25] + levelComponent[26][26] + levelComponent[26][27] + levelComponent[26][28] + levelComponent[26][29] + levelComponent[26][30] + levelComponent[26][31] + levelComponent[26][32] + levelComponent[26][33] + levelComponent[26][34] + levelComponent[26][35] + levelComponent[26][36] + levelComponent[26][37] + levelComponent[26][38] + levelComponent[26][39])
    print(levelComponent[27][0] + levelComponent[27][1] + levelComponent[27][2] + levelComponent[27][3] + levelComponent[27][4] + levelComponent[27][5] + levelComponent[27][6] + levelComponent[27][7] + levelComponent[27][8] + levelComponent[27][9] + levelComponent[27][10] + levelComponent[27][11] + levelComponent[27][12] + levelComponent[27][13] + levelComponent[27][14] + levelComponent[27][15] + levelComponent[27][16] + levelComponent[27][17] + levelComponent[27][18] + levelComponent[27][19] + levelComponent[27][20] + levelComponent[27][21] + levelComponent[27][22] + levelComponent[27][23] + levelComponent[27][24] + levelComponent[27][25] + levelComponent[27][26] + levelComponent[27][27] + levelComponent[27][28] + levelComponent[27][29] + levelComponent[27][30] + levelComponent[27][31] + levelComponent[27][32] + levelComponent[27][33] + levelComponent[27][34] + levelComponent[27][35] + levelComponent[27][36] + levelComponent[27][37] + levelComponent[27][38] + levelComponent[27][39])
    print(levelComponent[28][0] + levelComponent[28][1] + levelComponent[28][2] + levelComponent[28][3] + levelComponent[28][4] + levelComponent[28][5] + levelComponent[28][6] + levelComponent[28][7] + levelComponent[28][8] + levelComponent[28][9] + levelComponent[28][10] + levelComponent[28][11] + levelComponent[28][12] + levelComponent[28][13] + levelComponent[28][14] + levelComponent[28][15] + levelComponent[28][16] + levelComponent[28][17] + levelComponent[28][18] + levelComponent[28][19] + levelComponent[28][20] + levelComponent[28][21] + levelComponent[28][22] + levelComponent[28][23] + levelComponent[28][24] + levelComponent[28][25] + levelComponent[28][26] + levelComponent[28][27] + levelComponent[28][28] + levelComponent[28][29] + levelComponent[28][30] + levelComponent[28][31] + levelComponent[28][32] + levelComponent[28][33] + levelComponent[28][34] + levelComponent[28][35] + levelComponent[28][36] + levelComponent[28][37] + levelComponent[28][38] + levelComponent[28][39])
    print(levelComponent[29][0] + levelComponent[29][1] + levelComponent[29][2] + levelComponent[29][3] + levelComponent[29][4] + levelComponent[29][5] + levelComponent[29][6] + levelComponent[29][7] + levelComponent[29][8] + levelComponent[29][9] + levelComponent[29][10] + levelComponent[29][11] + levelComponent[29][12] + levelComponent[29][13] + levelComponent[29][14] + levelComponent[29][15] + levelComponent[29][16] + levelComponent[29][17] + levelComponent[29][18] + levelComponent[29][19] + levelComponent[29][20] + levelComponent[29][21] + levelComponent[29][22] + levelComponent[29][23] + levelComponent[29][24] + levelComponent[29][25] + levelComponent[29][26] + levelComponent[29][27] + levelComponent[29][28] + levelComponent[29][29] + levelComponent[29][30] + levelComponent[29][31] + levelComponent[29][32] + levelComponent[29][33] + levelComponent[29][34] + levelComponent[29][35] + levelComponent[29][36] + levelComponent[29][37] + levelComponent[29][38] + levelComponent[29][39])
    print(levelComponent[30][0] + levelComponent[30][1] + levelComponent[30][2] + levelComponent[30][3] + levelComponent[30][4] + levelComponent[30][5] + levelComponent[30][6] + levelComponent[30][7] + levelComponent[30][8] + levelComponent[30][9] + levelComponent[30][10] + levelComponent[30][11] + levelComponent[30][12] + levelComponent[30][13] + levelComponent[30][14] + levelComponent[30][15] + levelComponent[30][16] + levelComponent[30][17] + levelComponent[30][18] + levelComponent[30][19] + levelComponent[30][20] + levelComponent[30][21] + levelComponent[30][22] + levelComponent[30][23] + levelComponent[30][24] + levelComponent[30][25] + levelComponent[30][26] + levelComponent[30][27] + levelComponent[30][28] + levelComponent[30][29] + levelComponent[30][30] + levelComponent[30][31] + levelComponent[30][32] + levelComponent[30][33] + levelComponent[30][34] + levelComponent[30][35] + levelComponent[30][36] + levelComponent[30][37] + levelComponent[30][38] + levelComponent[30][39])
    print(levelComponent[31][0] + levelComponent[31][1] + levelComponent[31][2] + levelComponent[31][3] + levelComponent[31][4] + levelComponent[31][5] + levelComponent[31][6] + levelComponent[31][7] + levelComponent[31][8] + levelComponent[31][9] + levelComponent[31][10] + levelComponent[31][11] + levelComponent[31][12] + levelComponent[31][13] + levelComponent[31][14] + levelComponent[31][15] + levelComponent[31][16] + levelComponent[31][17] + levelComponent[31][18] + levelComponent[31][19] + levelComponent[31][20] + levelComponent[31][21] + levelComponent[31][22] + levelComponent[31][23] + levelComponent[31][24] + levelComponent[31][25] + levelComponent[31][26] + levelComponent[31][27] + levelComponent[31][28] + levelComponent[31][29] + levelComponent[31][30] + levelComponent[31][31] + levelComponent[31][32] + levelComponent[31][33] + levelComponent[31][34] + levelComponent[31][35] + levelComponent[31][36] + levelComponent[31][37] + levelComponent[31][38] + levelComponent[31][39])
    print(levelComponent[32][0] + levelComponent[32][1] + levelComponent[32][2] + levelComponent[32][3] + levelComponent[32][4] + levelComponent[32][5] + levelComponent[32][6] + levelComponent[32][7] + levelComponent[32][8] + levelComponent[32][9] + levelComponent[32][10] + levelComponent[32][11] + levelComponent[32][12] + levelComponent[32][13] + levelComponent[32][14] + levelComponent[32][15] + levelComponent[32][16] + levelComponent[32][17] + levelComponent[32][18] + levelComponent[32][19] + levelComponent[32][20] + levelComponent[32][21] + levelComponent[32][22] + levelComponent[32][23] + levelComponent[32][24] + levelComponent[32][25] + levelComponent[32][26] + levelComponent[32][27] + levelComponent[32][28] + levelComponent[32][29] + levelComponent[32][30] + levelComponent[32][31] + levelComponent[32][32] + levelComponent[32][33] + levelComponent[32][34] + levelComponent[32][35] + levelComponent[32][36] + levelComponent[32][37] + levelComponent[32][38] + levelComponent[32][39])
    print(levelComponent[33][0] + levelComponent[33][1] + levelComponent[33][2] + levelComponent[33][3] + levelComponent[33][4] + levelComponent[33][5] + levelComponent[33][6] + levelComponent[33][7] + levelComponent[33][8] + levelComponent[33][9] + levelComponent[33][10] + levelComponent[33][11] + levelComponent[33][12] + levelComponent[33][13] + levelComponent[33][14] + levelComponent[33][15] + levelComponent[33][16] + levelComponent[33][17] + levelComponent[33][18] + levelComponent[33][19] + levelComponent[33][20] + levelComponent[33][21] + levelComponent[33][22] + levelComponent[33][23] + levelComponent[33][24] + levelComponent[33][25] + levelComponent[33][26] + levelComponent[33][27] + levelComponent[33][28] + levelComponent[33][29] + levelComponent[33][30] + levelComponent[33][31] + levelComponent[33][32] + levelComponent[33][33] + levelComponent[33][34] + levelComponent[33][35] + levelComponent[33][36] + levelComponent[33][37] + levelComponent[33][38] + levelComponent[33][39])
    print(levelComponent[34][0] + levelComponent[34][1] + levelComponent[34][2] + levelComponent[34][3] + levelComponent[34][4] + levelComponent[34][5] + levelComponent[34][6] + levelComponent[34][7] + levelComponent[34][8] + levelComponent[34][9] + levelComponent[34][10] + levelComponent[34][11] + levelComponent[34][12] + levelComponent[34][13] + levelComponent[34][14] + levelComponent[34][15] + levelComponent[34][16] + levelComponent[34][17] + levelComponent[34][18] + levelComponent[34][19] + levelComponent[34][20] + levelComponent[34][21] + levelComponent[34][22] + levelComponent[34][23] + levelComponent[34][24] + levelComponent[34][25] + levelComponent[34][26] + levelComponent[34][27] + levelComponent[34][28] + levelComponent[34][29] + levelComponent[34][30] + levelComponent[34][31] + levelComponent[34][32] + levelComponent[34][33] + levelComponent[34][34] + levelComponent[34][35] + levelComponent[34][36] + levelComponent[34][37] + levelComponent[34][38] + levelComponent[34][39])
    print(levelComponent[35][0] + levelComponent[35][1] + levelComponent[35][2] + levelComponent[35][3] + levelComponent[35][4] + levelComponent[35][5] + levelComponent[35][6] + levelComponent[35][7] + levelComponent[35][8] + levelComponent[35][9] + levelComponent[35][10] + levelComponent[35][11] + levelComponent[35][12] + levelComponent[35][13] + levelComponent[35][14] + levelComponent[35][15] + levelComponent[35][16] + levelComponent[35][17] + levelComponent[35][18] + levelComponent[35][19] + levelComponent[35][20] + levelComponent[35][21] + levelComponent[35][22] + levelComponent[35][23] + levelComponent[35][24] + levelComponent[35][25] + levelComponent[35][26] + levelComponent[35][27] + levelComponent[35][28] + levelComponent[35][29] + levelComponent[35][30] + levelComponent[35][31] + levelComponent[35][32] + levelComponent[35][33] + levelComponent[35][34] + levelComponent[35][35] + levelComponent[35][36] + levelComponent[35][37] + levelComponent[35][38] + levelComponent[35][39])
    print(levelComponent[36][0] + levelComponent[36][1] + levelComponent[36][2] + levelComponent[36][3] + levelComponent[36][4] + levelComponent[36][5] + levelComponent[36][6] + levelComponent[36][7] + levelComponent[36][8] + levelComponent[36][9] + levelComponent[36][10] + levelComponent[36][11] + levelComponent[36][12] + levelComponent[36][13] + levelComponent[36][14] + levelComponent[36][15] + levelComponent[36][16] + levelComponent[36][17] + levelComponent[36][18] + levelComponent[36][19] + levelComponent[36][20] + levelComponent[36][21] + levelComponent[36][22] + levelComponent[36][23] + levelComponent[36][24] + levelComponent[36][25] + levelComponent[36][26] + levelComponent[36][27] + levelComponent[36][28] + levelComponent[36][29] + levelComponent[36][30] + levelComponent[36][31] + levelComponent[36][32] + levelComponent[36][33] + levelComponent[36][34] + levelComponent[36][35] + levelComponent[36][36] + levelComponent[36][37] + levelComponent[36][38] + levelComponent[36][39])
    print(levelComponent[37][0] + levelComponent[37][1] + levelComponent[37][2] + levelComponent[37][3] + levelComponent[37][4] + levelComponent[37][5] + levelComponent[37][6] + levelComponent[37][7] + levelComponent[37][8] + levelComponent[37][9] + levelComponent[37][10] + levelComponent[37][11] + levelComponent[37][12] + levelComponent[37][13] + levelComponent[37][14] + levelComponent[37][15] + levelComponent[37][16] + levelComponent[37][17] + levelComponent[37][18] + levelComponent[37][19] + levelComponent[37][20] + levelComponent[37][21] + levelComponent[37][22] + levelComponent[37][23] + levelComponent[37][24] + levelComponent[37][25] + levelComponent[37][26] + levelComponent[37][27] + levelComponent[37][28] + levelComponent[37][29] + levelComponent[37][30] + levelComponent[37][31] + levelComponent[37][32] + levelComponent[37][33] + levelComponent[37][34] + levelComponent[37][35] + levelComponent[37][36] + levelComponent[37][37] + levelComponent[37][38] + levelComponent[37][39])
    print(levelComponent[38][0] + levelComponent[38][1] + levelComponent[38][2] + levelComponent[38][3] + levelComponent[38][4] + levelComponent[38][5] + levelComponent[38][6] + levelComponent[38][7] + levelComponent[38][8] + levelComponent[38][9] + levelComponent[38][10] + levelComponent[38][11] + levelComponent[38][12] + levelComponent[38][13] + levelComponent[38][14] + levelComponent[38][15] + levelComponent[38][16] + levelComponent[38][17] + levelComponent[38][18] + levelComponent[38][19] + levelComponent[38][20] + levelComponent[38][21] + levelComponent[38][22] + levelComponent[38][23] + levelComponent[38][24] + levelComponent[38][25] + levelComponent[38][26] + levelComponent[38][27] + levelComponent[38][28] + levelComponent[38][29] + levelComponent[38][30] + levelComponent[38][31] + levelComponent[38][32] + levelComponent[38][33] + levelComponent[38][34] + levelComponent[38][35] + levelComponent[38][36] + levelComponent[38][37] + levelComponent[38][38] + levelComponent[38][39])
    print(levelComponent[39][0] + levelComponent[39][1] + levelComponent[39][2] + levelComponent[39][3] + levelComponent[39][4] + levelComponent[39][5] + levelComponent[39][6] + levelComponent[39][7] + levelComponent[39][8] + levelComponent[39][9] + levelComponent[39][10] + levelComponent[39][11] + levelComponent[39][12] + levelComponent[39][13] + levelComponent[39][14] + levelComponent[39][15] + levelComponent[39][16] + levelComponent[39][17] + levelComponent[39][18] + levelComponent[39][19] + levelComponent[39][20] + levelComponent[39][21] + levelComponent[39][22] + levelComponent[39][23] + levelComponent[39][24] + levelComponent[39][25] + levelComponent[39][26] + levelComponent[39][27] + levelComponent[39][28] + levelComponent[39][29] + levelComponent[39][30] + levelComponent[39][31] + levelComponent[39][32] + levelComponent[39][33] + levelComponent[39][34] + levelComponent[39][35] + levelComponent[39][36] + levelComponent[39][37] + levelComponent[39][38] + levelComponent[39][39])

clearComponent = "   "

arenaComponent = [  ["***","***","***","***","***","***","***","***","***","***"],
                    ["***","   ","A -","Ata","ck ","   ","E -","Eat","   ","***"],
                    ["***","   ","   ","   ","   ","   ","   ","   ","   ","***"],
                    ["***","   ","   ","   ","   ","   ","   ","   ","   ","***"],
                    ["***","***","***","***","***","***","***","***","***","***"],]

#Game Funtions

def clear():
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
    print(clearComponent[0] * 10)
 
def createConsole():
    print(consoleComponent[0] + consoleComponent[0] + consoleComponent[0] + consoleComponent[0] + consoleComponent[0] + consoleComponent[0] + consoleComponent[0] + consoleComponent[0] + consoleComponent[0] + consoleComponent[0])
    print(consoleComponent[0] + consoleComponent[2] + consoleComponent[3] + consoleComponent[1] + consoleComponent[0])
    print(consoleComponent[0] + consoleComponent[4] + consoleComponent[5] + consoleComponent[1] + consoleComponent[0])
    print(consoleComponent[0] + consoleComponent[1] + consoleComponent[1] + consoleComponent[1] + consoleComponent[1] + consoleComponent[1] + consoleComponent[1] + consoleComponent[1] + consoleComponent[1] + consoleComponent[0])
    print(consoleComponent[0] + consoleComponent[6] + consoleComponent[7] + consoleComponent[1] + consoleComponent[0])
    print(consoleComponent[0] + consoleComponent[0] + consoleComponent[0] + consoleComponent[0] + consoleComponent[0] + consoleComponent[0] + consoleComponent[0] + consoleComponent[0] + consoleComponent[0] + consoleComponent[0])


def creatArena():
    print(arenaComponent[0][0] + arenaComponent[0][1] + arenaComponent[0][2] + arenaComponent[0][3] + arenaComponent[0][4] + arenaComponent[0][5] + arenaComponent[0][6] + arenaComponent[0][7] + arenaComponent[0][8] + arenaComponent[0][9])
    print(arenaComponent[1][0] + arenaComponent[1][1] + arenaComponent[1][2] + arenaComponent[1][3] + arenaComponent[1][4] + arenaComponent[1][5] + arenaComponent[1][6] + arenaComponent[1][7] + arenaComponent[1][8] + arenaComponent[1][9])
    print(arenaComponent[2][0] + arenaComponent[2][1] + arenaComponent[2][2] + arenaComponent[2][3] + arenaComponent[2][4] + arenaComponent[2][5] + arenaComponent[2][6] + arenaComponent[2][7] + arenaComponent[2][8] + arenaComponent[2][9])
    print(arenaComponent[3][0] + arenaComponent[3][1] + arenaComponent[3][2] + arenaComponent[3][3] + arenaComponent[3][4] + arenaComponent[3][5] + arenaComponent[3][6] + arenaComponent[3][7] + arenaComponent[3][8] + arenaComponent[3][9])
    print(arenaComponent[4][0] + arenaComponent[4][1] + arenaComponent[4][2] + arenaComponent[4][3] + arenaComponent[4][4] + arenaComponent[4][5] + arenaComponent[4][6] + arenaComponent[4][7] + arenaComponent[4][8] + arenaComponent[4][9])  


def ratImage():
    print("""
          (q\_/p)
           /. .\
         \n\t   \_t_/=   __
           /   \   (
          ((   ))   )
          /\) (/\  /
          \  Y  /-'
           nn^nn
    """)

def deadRat():
    print("""
          (q\_/p)
           /X X\
         \n\t   \_t_/=   __
           /   \   (
          ((   ))   )
          /\) (/\  /
          \  Y  /-'
           nn^nn
    """)

def eatRat():
    print(""" 
             (|\ /      / /| \
             \n\t     /  /     .'  -=-'   `.
            /  /    .'             )
          _/  /   .'        _.)   /
         / o   o        _.-' /  .'
         \          _.-'    / .'*|
(q\_/p)   \______.-'//    .'.' \*|
/X X\      \|  \ | //   .'.' _ |*|
\_t_/=      `   \|//  .'.'_ _ _|*|
 /   \   (   .  .// .'.'   _ _ \*|
((   ))          \`-|\_/ /    \ _ _ \*\\n
/\) (/\  /        `/'\__/      \ _ _ \*\\n
\  Y  /-'                       \ _ _ \* \n
nn^nn     '  `                   \ _ _ \  \n
     """)


def combat(ratHealth, health, score):
    while(health != 0 and ratHealth != 0):
            print("""\tRat\n\tHealth: """ + str(ratHealth))
            print("""\tPython\n\tHealth: """ + str(health))
            ratImage()
            creatArena()
            playerAttack = input()
            if playerAttack in ["a","A","Attack"]:
                attackRoll = random()
                clear()
                if attackRoll < .68:
                    print("Miss")
                else:
                    print("Hit")
                    ratHealth-=1
                    
                attackRoll = random()
                if attackRoll < .68:
                    print("Enemy Miss")
                else:
                    print("Enemy Hit")
                    health-=1
            elif playerAttack in ["e","E","Eat"]:
                attackRoll = random()
                clear()
                if ratHealth <= 1:
                    health = health + 4
                    ratHealth-= 1
                else:
                    print("You try to eat the rat but he nimblly avoids your clutches. Perhaps you should wait till he is mortally wounded...")
                   
                attackRoll = random()
                if attackRoll < .68:
                    print("Enemy Miss")
                else:
                    print("Enemy Hit")
                    health-=1        
            else:
                print("You should probably just [A]ttack!")

    clear()
    
    if health > 0:
        if playerAttack in ["e"]:
            print("Victory!!!")
            eatRat()
            input("Press Any Key to Continue...")
            clear()
            combat = 0
            score = score + 10
            levelComponent[y][x] = player
            creatLevel()
            createConsole()
            return(health, score)
            #print("X = " + str(x) + "Y = " + str(y))
            #print("X = " + str(enemyX) + "Y = " + str(enemyY))
        else:
            print("Victory!!!")
            deadRat()
            input("Press Any Key to Continue...")
            clear()
            combat = 0
            score = score + 10
            levelComponent[y][x] = player
            creatLevel()
            createConsole()
            return(health, score)
    else:
        clear()
        print("You have died!")
        return(health, score)


def respawnRat(enemyX,enemyY):
    if enemyX == x and enemyY == y:
            enemyX = randint(1,38)
            enemyY = randint(1,38)
            if levelComponent[enemyY][enemyX] in ["TTT","III","LLL"]:
                respawnRat(enemyX,enemyY)
    return(enemyX,enemyY)


#Game Initiate  

levelComponent[y][x] = player
levelComponent[enemyY][enemyX] = rat

clear()

print("Health: " + str(health) + "\tScore: " + str(score))
creatLevel()

print("""
            TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
            III              Controls                                 Stats                               III
             III        n - North  e - East                           Health: """ + str(health) + """\t\t\tIII
             III        s - South  w - West                           Score: """ + str(score) + """  \t\t\tIII
            III                                                                                          III
            IIITTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
            """)



while (gameOver != 1):
    if health <= 0:
        gameOver = 1
    else:
        
        enemyX, enemyY = respawnRat(enemyX,enemyY)
        
        #print("X = " + str(x) + "Y = " + str(y)")
        #print("X = " + str(enemyX) + "Y = " + str(enemyY)")
        playerAction = input("What woud you like to do?")

        previousXPosition = x
        previousYPosition = y

        previousEnemyXPosition = enemyX
        previousEnemyYPosition = enemyY

        if playerAction == "n":
            if levelComponent[y-1][x] not in ["III","TTT","LLL"]:
                y-=1
            else:
                print("You cant slither that way!")
        elif playerAction == "s":
            if levelComponent[y+1][x] not in ["III","TTT","LLL"]:
                y+=1
            else:
                print("You cant slither that way!")
        elif playerAction == "w":
            if levelComponent[y][x-1] not in ["III","TTT","LLL"]:
                x-=1
            else:
                print("You cant slither that way!")
        elif playerAction == "e":
            if levelComponent[y][x+1] not in ["III","TTT","LLL"]:
                x+=1
            else:
                print("You cant slither that way!")
        else:
            print("Please use 'n' 's' 'e' 'w' to move your hero")
        
        if (enemyX + enemyY) == (y+x):
            enemyX = enemyX
        elif abs((enemyX - x)) >= abs((enemyY - y)):
            if levelComponent[enemyY][enemyX+1] not in ["III","TTT","LLL"]:
                enemyX += 1
            else:
                enemyX -= 1
        else:
            if levelComponent[enemyY+1][enemyX] not in ["III","TTT","LLL"]:
                enemyY += 1
            else:
                enemyY -= 1



        levelComponent[previousYPosition][previousXPosition] = "   "
        levelComponent[previousEnemyYPosition][previousEnemyXPosition] = "   "

        if enemyY == y and enemyX == x:
            health, score = combat(ratHealth, health, score)
        
        else:
            levelComponent[enemyY][enemyX] = rat
            levelComponent[y][x] = player 
           
            print("Health: " + str(health) + "\tScore: " + str(score))
            creatLevel()
            print("""
            TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
            III                                                                                             III
            III         n - North  e - East                           Health: """ + str(health) + """\t\t\t\tIII
            III         s - South  w - West                           Score: """ + str(score) + """  \t\t\t\tIII
            III                                                                                             III
            IIITTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
            """)


       