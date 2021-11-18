import random
import json
import os

from pico2d import *
import game_framework
import game_world

# 오브젝트
from grass import Grass
from mario import Mario
from monster_object import Monster
from fire_ball import Fire_Ball



name = "MainState"


mario = None
monster = None

def enter():
    global mario, monster

    mario = Mario()
    grass = Grass()
    monster = Monster() 
    game_world.add_object(grass, 0)
    game_world.add_object(mario, 1)
    game_world.add_object(monster, 1)


def exit():
    game_world.clear()

def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                game_framework.quit()
        else:
            mario.handle_event(event)



def update():
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()

