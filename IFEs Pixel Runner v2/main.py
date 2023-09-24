'''
Welcome to the Ifechukwu or IFEs version of pixel runner

This game was made by a 14 year old (will be 14 on the 13th of May) and is the first
of hopefully many games to come from this young developer.

It is made using pygame and forgive me if the aaimation is terrible to you because I am
not very good at animation and I literally created all the characters on paint 3d in
a day so enough time for refinement because I will resume school in a few days so the
deadline was not too long according to my level of expertise in pygame and python in
general.

Any how the game is made in python using the pygame module and a few of my own _mods
created specifically for this game (some better than others) all aspects of the game
apart from the music and idea of the game are made by me and it took me about three
weeks to make and complete the credit for the music and the guy that I learnt it from
if you want to start of in pygame will be shown down below.

The game is the .exe file and updates will be made after my exams.

Plus: please if the is any way you could correct any thing especially in the code please
do.

SO ENJOY !!!!!!!!

Credits:
Game idea Youtube channel: Clear Code
Game idea: https://www.youtube.com/watch?v=AY9MnQ4x3zk
Music author: Juhani Junkala
Music link: https://opengameart.org/content/5-chiptunes-action
'''

import random
import sys
import mods
from variable_constants import *
import pygame
import json

pygame.init()
screen = pygame.display.set_mode((SCR_WIDTH,SCR_LENGTH))
pygame.display.set_caption('IFEs Pixel Runner')
logo = pygame.image.load('assets/Environment/Logos/Default.png')
pygame.display.set_icon(logo)
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self,logo: str='sk1') -> None:
        super().__init__()
        global GROUND
        self.skin_index = SKIN_INDEX
        self.player_index = PLAYER_INDEX
        self.player_hit_index = PLAYER_HIT_INDEX
        self.player_air_hit_index = PLAYER_AIR_HIT_INDEX
        self.gravity = GRAVITY
        
        self.skins = SKINS

        if logo == 'sk1':
            self.current_skin = [self.skins['default']]
            
            self.current_skin = ''.join(str(self.current_skin))
            self.rep = ['[',']',' ','\'']
            self.current_skin = mods.fullrep(self.current_skin,self.rep)
            self.current_skin = self.current_skin.split(',')

            self.player_walk1 = pygame.transform.rotozoom(pygame.image.load(self.current_skin[0]).convert_alpha(),0,.35)
            self.player_walk2 = pygame.transform.rotozoom(pygame.image.load(self.current_skin[1]).convert_alpha(),0,.35)
            self.player_walk3 = pygame.transform.rotozoom(pygame.image.load(self.current_skin[2]).convert_alpha(),0,.35)
            self.player_walk4 = pygame.transform.rotozoom(pygame.image.load(self.current_skin[3]).convert_alpha(),0,.35)
            
            self.player_jump = pygame.image.load(self.current_skin[4]).convert_alpha()
            
            self.player_hit1 = pygame.transform.rotozoom(pygame.image.load(self.current_skin[5]).convert_alpha(),0,.35)
            self.player_hit2 = pygame.transform.rotozoom(pygame.image.load(self.current_skin[6]).convert_alpha(),0,.35)
            self.player_hit3 = pygame.transform.rotozoom(pygame.image.load(self.current_skin[7]).convert_alpha(),0,.35)

            self.player_air_hit1 = pygame.transform.rotozoom(pygame.image.load(self.current_skin[8]).convert_alpha(),0,.35)
            self.player_air_hit2 = pygame.transform.rotozoom(pygame.image.load(self.current_skin[9]).convert_alpha(),0,.35)
        elif logo == 'sk2':
            self.current_skin = [self.skins['little sis']]
            
            self.current_skin = ''.join(str(self.current_skin))
            self.rep = ['[',']',' ','\'']
            self.current_skin = mods.fullrep(self.current_skin,self.rep)
            self.current_skin = self.current_skin.split(',')

            self.player_walk1 = pygame.transform.rotozoom(pygame.image.load(self.current_skin[0]).convert_alpha(),0,.35)
            self.player_walk2 = pygame.transform.rotozoom(pygame.image.load(self.current_skin[1]).convert_alpha(),0,.35)
            self.player_walk3 = pygame.transform.rotozoom(pygame.image.load(self.current_skin[2]).convert_alpha(),0,.35)
            self.player_walk4 = pygame.transform.rotozoom(pygame.image.load(self.current_skin[3]).convert_alpha(),0,.35)
            
            self.player_jump = pygame.image.load(self.current_skin[4]).convert_alpha()
            
            self.player_hit1 = pygame.transform.rotozoom(pygame.image.load(self.current_skin[5]).convert_alpha(),0,.35)
            self.player_hit2 = pygame.transform.rotozoom(pygame.image.load(self.current_skin[6]).convert_alpha(),0,.35)
            self.player_hit3 = pygame.transform.rotozoom(pygame.image.load(self.current_skin[7]).convert_alpha(),0,.35)

            self.player_air_hit1 = pygame.transform.rotozoom(pygame.image.load(self.current_skin[8]).convert_alpha(),0,.35)
            self.player_air_hit2 = pygame.transform.rotozoom(pygame.image.load(self.current_skin[9]).convert_alpha(),0,.35)

        self.player_hit_scr = pygame.transform.scale(pygame.image.load('assets/Environment/hit_screen.png').convert_alpha(),(850,500))
        
        self.player_walk = [self.player_walk1,self.player_walk2,self.player_walk3,self.player_walk4]
        self.player_air_hit = [self.player_air_hit1,self.player_air_hit2]
        self.player_hit = [self.player_hit1,self.player_hit2,self.player_hit3]
        
        self.sfx = pygame.mixer.Sound('assets/Audio/Game_music/hit_sound.mp3')
        self.sfx.set_volume(0.5)
        self.jump_sound = pygame.mixer.Sound('assets/Audio/Game_music/jump.mp3')
        self.jump_sound.set_volume(0.2)
        
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (150,GROUND))

    def player_input(self):
        global ac_down,anim_state,add
        keys = pygame.key.get_pressed()
        if ac_down:
            if (keys[pygame.K_UP] or keys[pygame.K_SPACE]) and self.rect.bottom == GROUND:
                self.jump_sound.play()
                self.gravity = -19
                ac_down = False

    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= GROUND:self.rect.bottom = GROUND

    def animation_state(self):
        global hit, col
        if self.rect.bottom >= GROUND:
           self.player_index += 0.15
           if self.player_index >= len(self.player_walk):self.player_index = 0
           self.image = self.player_walk[int(self.player_index)]
        else:self.image = self.player_jump
        if col == 1:
            if self.rect.bottom >= GROUND:
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
            fly_frame1 = pygame.image.load('assets/Characters/enemy/fly/fly(1).png').convert_alpha()
            fly_frame1 = pygame.transform.rotozoom(fly_frame1,0,.3)
            fly_frame2 = pygame.image.load('assets/Characters/enemy/fly/fly(2).png').convert_alpha()
            fly_frame2 = pygame.transform.rotozoom(fly_frame2,0,.1)
            self.frames = [fly_frame1,fly_frame2]
            y_pos = GROUND - 130
        else:
            snail_frame1 = pygame.image.load('assets/Characters/enemy/snail/snail(1).png').convert_alpha()
            snail_frame2 = pygame.image.load('assets/Characters/enemy/snail/snail(2).png').convert_alpha()
            self.frames = [snail_frame1,snail_frame2]
            y_pos = GROUND
        self.animation_index = 0
        self.image = self.frames[self.animation_index]
        self.rect = self.image.get_rect(bottomright = (random.randint(900,1100),y_pos))
    
    def animation_state(self):
        self.animation_index += 0.1
        if self.animation_index >= len(self.frames):self.animation_index = 0
        self.image = self.frames[int(self.animation_index)]
    
    def destroy(self):
        if self.rect.x <= -100:self.kill()
    
    def update(self):
        self.animation_state()
        self.rect.x -= 12

class Environment():
    def clouds():
        SPEED = 2
        global c1, c2, c3, c4, new_c1, new_c2 ,new_c3, new_c4, game_active     
        if game_active:
            c1.x -= SPEED
            c2.x -= SPEED
            c3.x -= SPEED
            c4.x -= SPEED
            if c1.x <= -200:c1.x = new_c1
            if c2.x <= -200:c2.x = new_c2
            if c3.x <= -200:c3.x = new_c3
            if c4.x <= -200:c4.x = new_c4
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
        global GROUNDx, GROUNDx2
        speed = 10
        GROUNDx-=speed
        GROUNDx2-=speed
        if GROUNDx <= -900:GROUNDx = 900
        if GROUNDx2 <= -900:GROUNDx2 = 900
        screen.blit(floor,(GROUNDx,GROUND))
        screen.blit(floor,(GROUNDx2,GROUND))
    
    def music():
        musics = [
        'assets/Audio/Game_music/music1.mp3',
        'assets/Audio/Game_music/music2.mp3',
        'assets/Audio/Game_music/music3.mp3',
                ]
        limit = len(musics)
        _index = random.randrange(0,limit)
        bg_music = pygame.mixer.Sound(musics[_index])
        bg_music.set_volume(0.5)
        bg_music.play(loops=-1)
    
    def sky():
        global pos1,pos2
        pos1 -= 1
        pos2 -= 1
        if pos1 <= -850:pos1 = 0
        if pos2 <= 0:pos2 = 850
        screen.blit(sky,(pos1,0))
        screen.blit(sky,(pos2,0))
    
    def update():
        Environment.sky()
        Environment.clouds()
        Environment.floor()

def thescore():
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
        full_health -= levelling()*3
        if full_health <= 0:
            new_obstacle.empty()
            pygame.time.delay(20)
            full_health = 100
            pygame.time.delay(20)
            return [False,full_health,1,hl_pos]
        return [True,full_health,1,hl_pos]
    return [True,full_health,0,hl_pos]

# You know what this does
Environment.music()

logo = ['sk1','Default']

cloud = pygame.image.load('assets/Environment/cloud.png').convert_alpha()
floor = pygame.image.load('assets/Environment/floor.png').convert_alpha()
sky = pygame.image.load('assets/Environment/sky.png').convert_alpha()

c1 = cloud.get_rect(midtop = (cloud_x_pos[0]-random.randint(0,5),random.randint(0,150)))
c2 = cloud.get_rect(midtop = (cloud_x_pos[1]+random.randint(0,5),random.randint(0,150)))
c3 = cloud.get_rect(midtop = (cloud_x_pos[2]-random.randint(0,5),random.randint(0,150)))
c4 = cloud.get_rect(midtop = (cloud_x_pos[3]+random.randint(0,5),random.randint(0,150)))
old_c1 = c1.x
old_c2 = c2.x
old_c3 = c3.x
old_c4 = c4.x
new_c1 = c1.x+random.randint(SCR_WIDTH+50,SCR_WIDTH+100)
new_c2 = c2.x+random.randint(SCR_WIDTH,SCR_WIDTH+100)
new_c3 = c3.x+random.randint(SCR_WIDTH,SCR_WIDTH+100)
new_c4 = c4.x+random.randint(SCR_WIDTH,SCR_WIDTH+100)

# Font declaration
font = pygame.font.Font("assets/Fonts/font(1).ttf",FT_SIZE)
health_font = pygame.font.Font("assets/Fonts/font(2).ttf",HT_FT_SIZE)

speed = 750

# Timer
event_inc = 1

level_up = True
obstacle_time = pygame.USEREVENT + event_inc
counter = levelling()

while True:
    for event in pygame.event.get():
        # Exit check
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Input check
        if event.type == pygame.KEYDOWN:
            ac_down = True
            keys = pygame.key.get_pressed()
            
            if not game_active:
                if (keys[pygame.K_SPACE] or keys[pygame.K_UP]):
                    game_active = True
                    started = True
                if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                    count+=1
                    if count%2 == 0:logo = ['sk1','Default']
                    else:logo = ['sk2','Little sis']
        
        if game_active:
            if level_up:
                pygame.time.set_timer(obstacle_time,speed)
                level_up = False
            if event.type == obstacle_time:
                new_obstacle.add(Enemy(random.choice(['snail', 'snail', 'fly', 'fly', 'snail', 'snail'])))

    if game_active:
        # Update
        Environment.update()
        # Scoring
        the_score = thescore()

        if levelling() != counter:
            counter += 1
            speed -= 90
            level_up = True

        game_active, hth, col, the_hth = get_info()
        nums = []
        nums.append(the_score)
        fin_score = nums[-1]
        # Player movement
        new_player.draw(screen)
        new_player.update()
        # Obstacle movement
        new_obstacle.draw(screen)
        new_obstacle.update()
        lent = int((200-((100-hth)*2))/2)

        scores = font.render(F'Score: {the_score}',False,'#123abc')
        score_rect = scores.get_rect(center = (430,50))

        health_msg = health_font.render(F'{lent}%',False,'#3f48cc')
        health_msg_rect = health_msg.get_rect(topleft = (90+HEALTH_RECT_X_ADJUST,the_hth+45+HEALTH_RECT_Y_ADJUST))

        health_rect = pygame.Rect(14+HEALTH_RECT_X_ADJUST*3,the_hth+50+HEALTH_RECT_Y_ADJUST,lent,20)
        health = pygame.draw.rect(screen,'red',health_rect)
        
        health_rect_out = pygame.Rect(12+HEALTH_RECT_X_ADJUST*3,the_hth+48+HEALTH_RECT_Y_ADJUST,int(205/2),FN_CHAR_SIZE)
        health_out = pygame.draw.rect(screen,'black',health_rect_out,3)
        
        # print(health_msg_rect)
        screen.blit(health_msg,health_msg_rect)
        screen.blit(scores,score_rect)
    else:
        # Name
        with open('assets\\Text_Based\\total_high_score.json') as file:
            saved_data = json.loads(file.read())
            high_score = saved_data['high score']
        
        high_score_txt = f'High score: {high_score}'
        fin_score_txt = f'Your score: {fin_score if fin_score is not None else high_score}'
        
        name = font.render('IFEs Pixel Runner',False,'#b83dba')
        name_rect = name.get_rect(center = (425,50))
        # Prompts
        message = font.render('Space or up to start',False,'#b83dba')
        message_rect = message.get_rect(center = (425,450))
        message_click = font.render('C to change',False,'#b83dba')
        message_click_rect = message_click.get_rect(center = (mods.position('',SCR_WIDTH,FN_CHAR_SIZE,False),200))
        # Score
        score_msg = font.render(fin_score_txt,False,'#b83dba')
        score_msg_rect = score_msg.get_rect(midleft = (mods.position(fin_score_txt,SCR_WIDTH,FN_CHAR_SIZE,True),(MID_SCR)-FN_CHAR_SIZE*2))
        # High score
        if fin_score is not None:
            if int(fin_score) > 0:
                with open('assets\\Text_Based\\total_high_score.json', 'w') as file:
                    if high_score < fin_score:
                        saved_data['high score'] = fin_score
                    else:
                        saved_data['high score'] = high_score
                    new_score = json.dumps(saved_data, indent=2)
                    file.write(new_score)

        high_score_msg = font.render(high_score_txt,False,'#b83dba')
        high_score_msg_rect = high_score_msg.get_rect(midleft = (mods.position(high_score_txt,SCR_WIDTH,FN_CHAR_SIZE,True),MID_SCR))
        # Skin
        skin_txt1 = font.render('Skin',False,'#b83dba')
        skin_txt1_rect = skin_txt1.get_rect(midleft = (mods.position('Skin',SCR_WIDTH,FN_CHAR_SIZE,False)-FN_CHAR_SIZE,MID_SCR))
        skin_txt2 = font.render(f'Skin:{logo[1]}',False,'#b83dba')
        skin_txt2_rect = skin_txt2.get_rect(midleft = (mods.position(f'Skin:{logo[1]}',SCR_WIDTH,FN_CHAR_SIZE,False)-2*FN_CHAR_SIZE,300))

        new_player = pygame.sprite.GroupSingle()
        new_player.add(Player(logo=logo[0]))
        new_obstacle = pygame.sprite.Group()
        # Fail/Start screen
        screen.fill('blue')
        screen.blit(pygame.transform.rotozoom(pygame.image.load(f'assets/Environment/Logos/{logo[1]}.png').\
                        convert_alpha(),0,0.7),\
                    pygame.transform.rotozoom(pygame.image.load(f'assets/Environment/Logos/{logo[1]}.png').\
                        convert_alpha(),0,0.7).get_rect(center = (400,MID_SCR)))
        screen.blit(name,name_rect)
        # Score initialiaztion and activation
        if started:
            screen.blit(score_msg,score_msg_rect)
            screen.blit(high_score_msg,high_score_msg_rect)
            screen.blit(skin_txt1,skin_txt1_rect)
            screen.blit(message_click,message_click_rect)
            screen.blit(skin_txt2,skin_txt2_rect)
        else:
            screen.blit(skin_txt1,skin_txt1_rect)
            screen.blit(skin_txt2,skin_txt2_rect)
            screen.blit(message,message_rect)
            screen.blit(message_click,message_click_rect)
        
        start_time = int(pygame.time.get_ticks() / 1000)
        
    pygame.display.update()
    clock.tick(60)