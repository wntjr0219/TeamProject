import game_framework
import pico2d

import main_state
# 게임 시작하는 곳


# 11.18 / 이미지 로드 불가 
pico2d.open_canvas(800, 600)
game_framework.run(main_state)
pico2d.close_canvas()
