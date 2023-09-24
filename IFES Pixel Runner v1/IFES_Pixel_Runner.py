

import random as rand
import pygame
import sys
import IFES_Pixel_Runner_mods 

# Initiation
pygame.init()

screen = pygame.display.set_mode((850,500))
pygame.display.set_caption('Ifechukwu\'s Pixel Runner')
logo = pygame.image.load('IFES_Pixel_Runner_assets/Characters/player/logo.png')
pygame.display.set_icon(logo)
clock = pygame.time.Clock()
ground = 388

class Player(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        global ground
        self.skin_index = 0

        self.skin1 = ['IFES_Pixel_Runner_assets/Characters/player/player1.png',
                      'IFES_Pixel_Runner_assets/Characters/player/player2.png',
                      'IFES_Pixel_Runner_assets/Characters/player/player3.png',
                      'IFES_Pixel_Runner_assets/Characters/player/player4.png',
                      'IFES_Pixel_Runner_assets/Characters/player/jump.png',
                      'IFES_Pixel_Runner_assets/Characters/player/hit1.png',
                      'IFES_Pixel_Runner_assets/Characters/player/hit2.png',
                      'IFES_Pixel_Runner_assets/Characters/player/hit3.png',
                      'IFES_Pixel_Runner_assets/Characters/player/air_hit1.png',
                      'IFES_Pixel_Runner_assets/Characters/player/air_hit2.png',
                      'IFES_Pixel_Runner_assets/Characters/player/hit_screen.png']
        

        self.current_skin = [self.skin1]
        
        self.current_skin = ''.join(str(self.current_skin))
        self.rep = ['[',']',' ','\'']
        self.current_skin = IFES_Pixel_Runner_mods.fullrep(self.current_skin,self.rep)
        self.current_skin = self.current_skin.split(',')

        player_walk1 = pygame.image.load(self.current_skin[0]).convert_alpha()
        player_walk1 = pygame.transform.rotozoom(player_walk1,0,.35)
        player_walk2 = pygame.image.load(self.current_skin[1]).convert_alpha()
        player_walk2 = pygame.transform.rotozoom(player_walk2,0,.35)
        player_walk3 = pygame.image.load(self.current_skin[2]).convert_alpha()
        player_walk3 = pygame.transform.rotozoom(player_walk3,0,.35)
        player_walk4 = pygame.image.load(self.current_skin[3]).convert_alpha()
        player_walk4 = pygame.transform.rotozoom(player_walk4,0,.35)
        
        self.player_walk = [player_walk1,player_walk2,player_walk3,player_walk4]
        
        self.player_jump = pygame.image.load(self.current_skin[4]).convert_alpha()
        
        self.player_hit1 = pygame.image.load(self.current_skin[5]).convert_alpha()
        self.player_hit1 = pygame.transform.rotozoom(self.player_hit1,0,.35)
        
        self.player_hit2 = pygame.image.load(self.current_skin[6]).convert_alpha()
        self.player_hit2 = pygame.transform.rotozoom(self.player_hit2,0,.35)
        
        self.player_hit3 = pygame.image.load(self.current_skin[7]).convert_alpha()
        self.player_hit3 = pygame.transform.rotozoom(self.player_hit3,0,.35)

        self.player_air_hit1 = pygame.image.load(self.current_skin[8]).convert_alpha()
        self.player_air_hit1 = pygame.transform.rotozoom(self.player_air_hit1,0,.35)
        
        self.player_air_hit2 = pygame.image.load(self.current_skin[9]).convert_alpha()
        self.player_air_hit2 = pygame.transform.rotozoom(self.player_air_hit2,0,.35)
        self.player_hit_scr = pygame.image.load(self.current_skin[10]).convert_alpha()
        self.player_hit_scr = pygame.transform.scale(self.player_hit_scr,(850,500))
        self.player_air_hit = [self.player_air_hit1,self.player_air_hit2]
        self.player_hit = [self.player_hit1,self.player_hit2,self.player_hit3]
        
        self.player_index = 0
        self.player_hit_index = 0
        self.player_air_hit_index = 0

        self.sfx = pygame.mixer.Sound('IFES_Pixel_Runner_assets\Audio\Game_music\hit_sound.mp3')
        self.sfx.set_volume(0.5)
        self.jump_sound = pygame.mixer.Sound('IFES_Pixel_Runner_assets\Audio\Game_music\jump.mp3')
        self.jump_sound.set_volume(0.2)
        
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (150,ground))
        self.gravity = 0
    def player_input(self):
        global jumped
        keys = pygame.key.get_pressed()
        if jumped:
            if (keys[pygame.K_UP] or keys[pygame.K_SPACE]) and self.rect.bottom == ground:
                self.jump_sound.play()
                self.gravity = -19
            jumped = False
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= ground:
            self.rect.bottom = ground
    def animation_state(self):
        global hit
        
        if self.rect.bottom >= ground:
           self.player_index += 0.15
           if self.player_index >= len(self.player_walk):self.player_index = 0
           self.image = self.player_walk[int(self.player_index)]
        else:self.image = self.player_jump
        if info[2] == 1:
            if self.rect.bottom >= ground:
                self.player_hit_index += 0.15
                if self.player_hit_index >= len(self.player_hit):self.player_hit_index = 0
                self.image = self.player_hit[int(self.player_hit_index)]
                screen.blit(self.player_hit_scr,(0,0))
                if hit:
                    self.sfx.play()
                    hit = False
            else:
                self.player_air_hit_index += 0.15
                if self.player_air_hit_index >= len(self.player_air_hit):self.player_air_hit_index = 0
                self.image = self.player_air_hit[int(self.player_air_hit_index)]
                screen.blit(self.player_hit_scr,(0,0))
                if hit:
                    self.sfx.play()
                    hit = False
        else:hit = True
    def update(self):
        global hl_pos
        self.player_input()
        self.apply_gravity()
        self.animation_state()
        hl_pos = self.rect.top
class Enemy(pygame.sprite.Sprite):
    def __init__(self,type):
        super().__init__()
        if type == 'fly':
            fly_frame1 = pygame.image.load('IFES_Pixel_Runner_assets/Characters/enemy/fly/fly(1).png').convert_alpha()
            fly_frame1 = pygame.transform.rotozoom(fly_frame1,0,.3)
            fly_frame2 = pygame.image.load('IFES_Pixel_Runner_assets/Characters/enemy/fly/fly(2).png').convert_alpha()
            fly_frame2 = pygame.transform.rotozoom(fly_frame2,0,.1)
            self.frames = [fly_frame1,fly_frame2]
            y_pos = ground - 130
        else:
            snail_frame1 = pygame.image.load('IFES_Pixel_Runner_assets/Characters/enemy/snail/snail(1).png').convert_alpha()
            snail_frame2 = pygame.image.load('IFES_Pixel_Runner_assets/Characters/enemy/snail/snail(2).png').convert_alpha()
            self.frames = [snail_frame1,snail_frame2]
            y_pos = ground
        
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(bottomright = (rand.randint(900,1100),y_pos))
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
    def destroy(self):
        if self.rect.x <= -100:
            self.kill()
    def update(self):
        self.animation_state()
        self.rect.x -= 8
class Environment():
    def clouds():
        global c1, c2, c3, c4, new_c1, new_c2 ,new_c3, new_c4, game_active     
        if game_active:
            c1.x -= 1
            c2.x -= 1
            c3.x -= 1
            c4.x -= 1
            if c1.x <= -200:
                c1.x = new_c1
            if c2.x <= -200:
                c2.x = new_c2
            if c3.x <= -200:
                c3.x = new_c3
            if c4.x <= -200:
                c4.x = new_c4
        else:
            c1.x = old_c1
            c2.x = old_c2
            c3.x = old_c3
            c4.x = old_c4

        screen.blit(cloud,(c1.x,c1.y))
        screen.blit(cloud,(c2.x,c2.y))
        screen.blit(cloud,(c3.x,c3.y))
        screen.blit(cloud,(c4.x,c4.y))
    def floor():
        global groundx, groundx2
        groundx-=5
        groundx2-=5
        if groundx <= -900:
            groundx = 900
        if groundx2 <= -900:
            groundx2 = 900
        screen.blit(floor,(groundx,ground))
        screen.blit(floor,(groundx2,ground))
    def music():
        musics = [
        'IFES_Pixel_Runner_assets\Audio\Game_music\music1.mp3',
        'IFES_Pixel_Runner_assets\Audio\Game_music\music2.mp3',
        'IFES_Pixel_Runner_assets\Audio\Game_music\music3.mp3',
                ]
        limit = len(musics)-1
        __index = rand.randint(0,limit)
        bg_music = pygame.mixer.Sound(musics[__index])
        bg_music.set_volume(0.5)
        bg_music.play(loops = -1)

def the__score():
    time = int(pygame.time.get_ticks() / 1000)-start_time
    return time
def levelling():
    global level,inc_rate,increment

    time = int(pygame.time.get_ticks() / 1000)-start_time

    if time == inc_rate+inc_rate:
        inc_rate+=inc_rate
        increment = True
    if time == inc_rate:
        if increment:
            level += 1
        increment = False

    return level
def get_info():
    global full_health,inc_rate,level,new_player,hl_pos
    
    while pygame.sprite.spritecollide(new_player.sprite,new_obstacle,False) and full_health != 0:
        full_health -= levelling()
        if full_health <= 0:
            new_obstacle.empty()
            pygame.time.delay(20)
            full_health = 100
            return [False,full_health,1,hl_pos]
        else:return [True,full_health,1,hl_pos]
    return [True,full_health,0,hl_pos]


# Other variables
new_player = pygame.sprite.GroupSingle()
new_player.add(Player())
new_obstacle = pygame.sprite.Group()

# Interger variables
hl_pos = 317
inc_rate = 10
level = 1
start_time = 0
fin_score = 0
high_score = 0
base = 0
full_health = 100
groundx = 0
groundx2 = groundx+900

# Boolean variables
game_active = False
started = False
increment = True
hit = True

# Background
cloud = pygame.image.load('IFES_Pixel_Runner_assets/Environment/cloud.png').convert_alpha()
floor = pygame.image.load('IFES_Pixel_Runner_assets/Environment/floor.png').convert_alpha()
sky = pygame.image.load('IFES_Pixel_Runner_assets/Environment/sky.png').convert_alpha()

# Cloud variables
var = [10,212,212*2,212*3]
c1 = cloud.get_rect(midtop = (var[0]-rand.randint(0,5),rand.randint(0,150)))
c2 = cloud.get_rect(midtop = (var[1]+rand.randint(0,5),rand.randint(0,150)))
c3 = cloud.get_rect(midtop = (var[2]-rand.randint(0,5),rand.randint(0,150)))
c4 = cloud.get_rect(midtop = (var[3]+rand.randint(0,5),rand.randint(0,150)))

old_c1 = c1.x
old_c2 = c2.x
old_c3 = c3.x
old_c4 = c4.x

new_c1 = c1.x+rand.randint(screen.get_width()+50,screen.get_width()+100)
new_c2 = c2.x+rand.randint(screen.get_width(),screen.get_width()+100)
new_c3 = c3.x+rand.randint(screen.get_width(),screen.get_width()+100)
new_c4 = c4.x+rand.randint(screen.get_width(),screen.get_width()+100)

# Music
Environment.music()

# Font
font = pygame.font.Font("IFES_Pixel_Runner_assets/Fonts/font(1).ttf",40)
health_font = pygame.font.Font("IFES_Pixel_Runner_assets/Fonts/font(2).ttf",22)

# Intro/Ending
player_stand = pygame.image.load('IFES_Pixel_Runner_assets/Characters/player/logo.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,0.7)
player_stand_rect = player_stand.get_rect(center = (425,250))

name = font.render('Nervous Bob Runner',False,'#b83dba')
name_rect = name.get_rect(center = (425,50))

message = font.render('Click space or up to start',False,'#b83dba')
message_rect = message.get_rect(center = (425,450))

# Timer
obstacle_time = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_time,800)

while True:
        # Event loop
    for event in pygame.event.get():
        # Exit check
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
        # Input check
        if event.type == pygame.KEYDOWN:
            jumped = True
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_SPACE] or keys[pygame.K_UP]) and not game_active:
                game_active = True
                started = True
                
        if game_active:
        # Enemy spawner
            if event.type == obstacle_time:
                new_obstacle.add(Enemy(rand.choice(['fly','fly','snail','snail','snail'])))


    if game_active:
        # Local variable
        info = get_info()
        # Sky
        screen.blit(sky,(0,0))
        # Clouds
        Environment.clouds()
        # Floor movement
        Environment.floor()
        # Scoring
        the_score = the__score()
        nums = []
        nums.append(the_score)
        fin_score = nums[-1]
        # Collision
        game_active = info[0]
        # print(collision_sprite(False))
        # Player movement
        new_player.draw(screen)
        new_player.update()
        # Obstacle movement
        new_obstacle.draw(screen)
        new_obstacle.update()
        lent = int((200-((100-info[1])*2))/2)
        x_add = 26
        y_add = -90

        scores = font.render(F'Score: {the_score}',False,'#123abc')
        score_rect = scores.get_rect(center = (430,50))

        health_msg = health_font.render(F'{lent}%',False,'#3f48cc')
        health_msg_rect = health_msg.get_rect(topleft = (90+x_add,info[3]+45+y_add))

        health_rect = pygame.Rect(14+x_add*3,info[3]+50+y_add,lent,20)
        health = pygame.draw.rect(screen,'red',health_rect)
        
        health_rect_out = pygame.Rect(12+x_add*3,info[3]+48+y_add,int(205/2),25)
        health_out = pygame.draw.rect(screen,'black',health_rect_out,3)
        
        # print(health_msg_rect)
        screen.blit(health_msg,health_msg_rect)
        screen.blit(scores,score_rect)
    else:
        # Fail/Start screen
        screen.fill('blue')
        screen.blit(player_stand,player_stand_rect)
        screen.blit(name,name_rect)
        # High score retrieval
        perm_high_score = int(IFES_Pixel_Runner_mods.file_read('IFES_Pixel_Runner_assets/Docs/total_high_score.txt'))    
        if fin_score > base:
            base = fin_score
            high_score = base
            
            if perm_high_score < high_score:high_score = IFES_Pixel_Runner_mods.file_write('IFES_Pixel_Runner_assets/Docs/total_high_score.txt',str(high_score))
            else:IFES_Pixel_Runner_mods.file_write('IFES_Pixel_Runner_assets/Docs/total_high_score.txt',str(perm_high_score))
        # Score
        score_msg = font.render(f'Your score is {fin_score}',False,'#b83dba')
        score_msg_rect = score_msg.get_rect(center = (425,450))
        # High score
        high_score_msg = font.render(f'High score: {perm_high_score}',False,'#b83dba')
        high_score_msg_rect = high_score_msg.get_rect(midleft = (50,250))
        # Score initialiaztion and activation
        if started:
            screen.blit(score_msg,score_msg_rect)
            screen.blit(high_score_msg,high_score_msg_rect)
        else:screen.blit(message,message_rect)
        start_time = int(pygame.time.get_ticks() / 1000)
        
    pygame.display.update()
    clock.tick(60)
