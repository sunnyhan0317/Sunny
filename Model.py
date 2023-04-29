from typing import List
from Config import *
import pygame as pg
from Debug import *
import copy

def check_Collision(pos: List, objs: List):
    '''
    偵測待測座標是否與其他座標重疊

    Keyword arguments:
        pos -- 待確認物件的座標[x, y]
        objs -- 其他座標[[x,y]]

    Return:
        bool -- 是否重疊
            True: 重疊
            False: 無重疊
    '''
    positions = [[i[0], i[1]] for i in objs]
    for i in positions:
        if abs(i[0]-pos[0]) < SNAKE_SIZE and abs(i[1]-pos[1]) < SNAKE_SIZE:
            return True
    return False


class Food:
    """
    食物物件，初始化方法為 `Food((左上角 x, 左上角 y))`
    `self.pos_x` 及 `self.pos_y` 為食物的座標
    """

    def __init__(self, pos):
        self.surf = pg.surface.Surface(size=(SNAKE_SIZE, SNAKE_SIZE))
        self.surf.fill(FOOD_COLOR)
        self.rect = self.surf.get_rect(topleft=pos)

    @property
    def pos_x(self):
        return self.rect.topleft[0]

    @property
    def pos_y(self):
        return self.rect.topleft[1]


class Poison:
    """
    毒藥物件，初始化方法為 `Poison((左上角 x, 左上角 y))`
    `self.pos_x` 及 `self.pos_y` 為毒藥的座標
    """

    def __init__(self, pos):
        self.surf = pg.surface.Surface(size=(SNAKE_SIZE, SNAKE_SIZE))
        self.surf.fill(POISON_COLOR)
        self.rect = self.surf.get_rect(topleft=pos)

    @property
    def pos_x(self):
        return self.rect.topleft[0]

    @property
    def pos_y(self):
        return self.rect.topleft[1]


class Wall:
    """
    牆壁物件，初始化方法為 `Wall((左上角 x, 左上角 y))`
    `self.pos_x` 及 `self.pos_y` 為牆壁的座標
    """

    def __init__(self, pos):
        self.surf = pg.surface.Surface(size=(SNAKE_SIZE, SNAKE_SIZE))
        self.surf.fill(WALL_COLOR)
        self.rect = self.surf.get_rect(topleft=pos)

    @property
    def pos_x(self):
        return self.rect.topleft[0]

    @property
    def pos_y(self):
        return self.rect.topleft[1]


class Player:
    """
    玩家物件
    `self.snake_list` 紀錄每一段蛇的資訊 `(左上 x, 左上 y, 寬, 高)`
    `self.head_x` 及 `self.head_y` 為蛇頭的座標
    `self.length` 為蛇的長度
    """

    def __init__(self):
        self.snake_list = [[200, 100, SNAKE_SIZE, SNAKE_SIZE]]

    @property
    def head_x(self):
        return self.snake_list[0][0]

    @property
    def head_y(self):
        return self.snake_list[0][1]

    @property
    def length(self):
        return len(self.snake_list)

    # 以下為大作業

    def new_block(self, new_pos) -> None:
        """
        將新一節蛇身的資訊加到 `snake_list` 最後面，無回傳值

        Keyword arguments:
        new_pos -- 新一節蛇身的座標 (左上 x, 左上 y)
        """
        # new
        self.snake_list.append(
            [new_pos[0], new_pos[1], SNAKE_SIZE, SNAKE_SIZE])
        logging("new_block", new_pos)
        logging("snake_list",self.snake_list)

    def draw_snake(self, screen) -> None:
        """
        畫出蛇，顏色要黃藍相間，無回傳值
        顏色可以用 `SNAKE_COLOR_YELLOW` 及 `SNAKE_COLOR_BLUE`
        可以用 `pg.draw.rect(screen 物件, 顏色, (座標 x, 座標 y, 寬, 高))`

        Keyword arguments:
        screen -- pygame 螢幕物件
        """
        # new
        rect = pg.image.load("head.svg").convert()
        screen.blit(rect, (self.head_x, self.head_y))
        for i in range(1, len(self.snake_list)):
            pg.draw.rect(screen, SNAKE_COLOR_BLUE, self.snake_list[i])

    def check_border(self) -> bool:
        """
        判斷蛇的頭有沒有超出螢幕範圍
        有超出就回傳 `True`
        沒有超出回傳 `False`

        Return:
        bool -- 蛇的頭有沒有超出螢幕範圍
        """
        # new
        if self.head_x > SCREEN_WIDTH-SNAKE_SIZE or self.head_y > SCREEN_HEIGHT-SNAKE_SIZE or self.head_x < 0 or self.head_y < 0:
            return True
        else:
            return False

    def move(self, direction) -> None:
        """
        根據 `direction` 移動蛇的座標，無回傳值，`direction` 為哪個按鍵被按到
        -1: 其他
        0: 上
        1: 右
        2: 下
        3: 左
        方向的代號也可以直接使用 `UP`, `RIGHT`, `DOWN`, `LEFT`，在 `Config.py` 裡面定義好了

        Keyword arguments:
        direction -- 蛇的移動方向
        """
        # new
        ori_snake_list = copy.deepcopy(self.snake_list)
        debugLog(ori_snake_list)
        if (direction == UP):
            self.snake_list[0][1] -= SNAKE_SIZE
        elif (direction == DOWN):
            self.snake_list[0][1] += SNAKE_SIZE
        elif (direction == LEFT):
            self.snake_list[0][0] -= SNAKE_SIZE
        elif (direction == RIGHT):
            self.snake_list[0][0] += SNAKE_SIZE
        logging("setHead",self.snake_list[0])
        for i in range(1,len(self.snake_list)):
            debugLog(ori_snake_list)
            logging("update_snake_list",f"{self.snake_list[i]} => {ori_snake_list[i-1]}")
            self.snake_list[i] = ori_snake_list[i-1]

    def detect_player_collision(self) -> bool:
        """
        判斷蛇的頭是否碰到蛇的其他段
        有碰到就回傳 `True`
        沒有碰到回傳 `False`

        Return:
        bool -- 是否碰到蛇 (自己) 的其他段
        """
        # new
        debugLog(self.snake_list.count(self.snake_list[0]))
        return not self.snake_list.count(self.snake_list[0])

    def detect_wall_collision(self, walls: List[Wall]) -> bool:
        """
        判斷蛇的頭是否碰到牆壁
        有碰到就回傳 `True`
        沒有碰到回傳 `False`

        Keyword arguments:
        walls -- 牆壁物件的 list

        Return:
        bool -- 是否碰到牆壁
        """
        # new
        return check_Collision([self.head_x, self.head_y], [[i.pos_x, i.pos_y] for i in walls])

    def detect_food_collision(self, foods: List[Food]) -> bool:
        """
        判斷蛇的頭是否碰到食物
        有碰到就回傳 `True`
        沒有碰到回傳 `False`

        Keyword arguments:
        foods -- 食物物件的 list

        Return:
        bool -- 是否碰到食物
        """
        # new
        return check_Collision([self.head_x, self.head_y], [[i.pos_x, i.pos_y] for i in foods])

    def detect_poison_collision(self, poison: Poison) -> bool:
        """
        判斷蛇的頭是否碰到毒藥
        有碰到就回傳 `True`
        沒有碰到回傳 `False`

        Keyword arguments:
        poison -- 毒藥物件

        Return:
        bool -- 是否碰到毒藥
        """
        # new
        return check_Collision([self.head_x, self.head_y], [[poison.pos_x, poison.pos_y]])
