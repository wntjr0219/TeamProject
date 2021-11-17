from pico2d import *
import random
import game_framework
#8(?)주차 적군 기본 오브젝트

#아직 샘플만 구현됨

PIXEL_PER_METER = (10.0 / 0.3) # 0.3미터당 10픽셀
RUN_SPEED_KMPH = 5.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS* PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Monster:
    image = None

    def __init__(self): 
        self.x, self.y = random.randint(100, 700), random.randint(70, 80)
        self.frame = 0
        self.act = 0
        if Monster.image == None:
            self.image = load_image('gomba_motion.png')

    def update(self): 
        global RUN_SPEED_PPS
        self.frame = (self.frame +  FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 7
        
        timer = random.randint(200, 400)
        dir = random.randint(-1, 1)
        self.act = dir
        # 움직임 대충 구현
        while timer > 0:
            velocity = RUN_SPEED_PPS * dir
            self.x += velocity * game_framework.frame_time
            timer -= 1
            delay(0.05)

        self.x = clamp(25, self.x, 800 - 25)
        
        
        
    def draw(self): 
        self.image.clip_draw(int(self.frame) * 65, self.act * 75, 65, 75, self.x, self.y)


