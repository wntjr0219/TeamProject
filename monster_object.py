from pico2d import *
import random
#3주차 적군 기본 오브젝트

#아직 샘플만 구현됨

class Grass:
    def __init__(self): 
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Monster:
    def __init__(self): 
        self.image = load_image('gomba_motion.png')
        self.x, self.y = random.randint(100, 700), random.randint(70, 80)
        self.frame = 0
        self.act = 0
    def update(self): 
        self.frame = (self.frame + 1) % 7

        next_x = self.x + random.randint(-20, 20)
        if self.x > next_x:
                self.act = 1
        else:
            self.act = 0

        if next_x <= 800 and next_x >= 0:
            self.x = next_x

        if next_x > 800:
            self.x = 800
        if next_x < 0:
            self.x = 0
        
        
        
    def draw(self): 
        self.image.clip_draw(self.frame*65, self.act * 75, 65, 75, self.x, self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


open_canvas()

grass = Grass()

running = True
# goombas = [Monster() for i in range(20)] #
goomba = Monster()
while running:
    

    handle_events()

    # for goomba in goombas:
    goomba.update()

    clear_canvas()
    grass.draw()

    # for goomba in goombas:
    goomba.draw()

    update_canvas()

    delay(0.1)
