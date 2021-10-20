from pico2d import *
import random
# 마리오 움직임
# 적절한 마리오 이미지가 없으므로 애니메이션시트로 대체
# 추후 마리오로 이미지교체예정

class Grass:
    def __init__(self): 
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Mario:
    def __init__(self):
        self.image = load_image('animation_sheet.png')
        # self.image = load_image('mario4.png')
        self.x, self.y = s_point, ground
        self.frame = 0 

    def update(self): 
        self.frame = (self.frame + 1) % 8 
        # self.frame = (self.frame + 1) % 7 
        self.x += x_dir*5
        if self.y >= ground:
            self.y += y_dir*5
        if self.y < ground:
            self.y = ground

    def draw(self): 
        self.image.clip_draw(self.frame*100, act * 100, 100, 100, self.x, self.y)
        # self.image.clip_draw(self.frame*96, 0, 96, 149, self.x, self.y)

def handle_events():
    global running
    global x_dir
    global y_dir
    global act
    events=pico2d.get_events()
    
    #이동 키 설정
    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                x_dir += 1
                act = 1
            elif event.key == SDLK_LEFT:
                x_dir -= 1
                act = 0
            # 점프모션 이상있음
            elif event.key == SDLK_UP:
                for i in range(10):
                    y_dir += 1

            # elif event.key == SDLK_DOWN:
            #     y_dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False

            
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                x_dir -= 1
                act += 2
            elif event.key == SDLK_LEFT:
                x_dir += 1
                act += 2
            # 점프모션 이상있음
            elif event.key == SDLK_UP:
                 for i in range(11):
                    y_dir -= 1
            # elif event.key == SDLK_DOWN:
            #     y_dir += 1
                
        pass

open_canvas()

grass = Grass()

running = True
#시작지점 설정
s_point = 400
ground = 90


x_dir = 0 # -1 left ,+1 right
y_dir = 0
act = 3 # 0 backrun  1 run  2 backstop 3 stop

mario = Mario() # 마리오 객체 생성

while running:

    update_canvas()
    mario.update()
    clear_canvas()

    grass.draw()
    handle_events()

    mario.draw()

   
    delay(0.03)

close_canvas()

