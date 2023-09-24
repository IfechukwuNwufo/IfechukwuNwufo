SCR_LENGTH = 500
SCR_WIDTH = 850
SKIN_INDEX = 0
PLAYER_INDEX = 0
PLAYER_HIT_INDEX = 0
PLAYER_AIR_HIT_INDEX = 0
GRAVITY = 0
GROUND = 388
HEALTH_RECT_X_ADJUST = 26
HEALTH_RECT_Y_ADJUST = -90
FT_SIZE = 40
HT_FT_SIZE = 22
SPEED = 750
FN_CHAR_SIZE = 25
MID_SCR = SCR_LENGTH//2

pos1 = 0
pos2 = 850
hl_pos = 317
inc_rate = 10
level = 1
start_time = 0
fin_score = 0
high_score = 0
base = 0
full_health = 100
anim_state = 0
count = 0
GROUNDx = 0
GROUNDx2 = GROUNDx+900
game_active = False
started = False
increment = True
hit = True
cloud_x_pos = [10,212,212*2,212*3]

SKINS = {
            'default':[
            'assets/Characters/player/Player1/player1.png',
            'assets/Characters/player/Player1/player2.png',
            'assets/Characters/player/Player1/player3.png',
            'assets/Characters/player/Player1/player4.png',
            'assets/Characters/player/Player1/jump.png',
            'assets/Characters/player/Player1/hit1.png',
            'assets/Characters/player/Player1/hit2.png',
            'assets/Characters/player/Player1/hit3.png',
            'assets/Characters/player/Player1/air_hit1.png',
            'assets/Characters/player/Player1/air_hit2.png'
            ],
            'little sis':[
            'assets/Characters/player/Player2/player1.png',
            'assets/Characters/player/Player2/player2.png',
            'assets/Characters/player/Player2/player3.png',
            'assets/Characters/player/Player2/player4.png',
            'assets/Characters/player/Player2/jump.png',
            'assets/Characters/player/Player2/hit1.png',
            'assets/Characters/player/Player2/hit2.png',
            'assets/Characters/player/Player2/hit3.png',
            'assets/Characters/player/Player2/air_hit1.png',
            'assets/Characters/player/Player2/air_hit2.png'
            ]
}



