from typing import List
from Config import *
import pygame as pg


class PositionOBJ:
    """
    遊戲基底物件
    `self.pos_x``self.pos_y`等基礎函式
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def pos_x(self):
        return self.x

    @property
    def pos_y(self):
        return self.y


def check_GameOBJ_collision(obj: PositionOBJ, all: List[PositionOBJ]):
    """
    偵測物件是否碰到其他物件

    Keyword arguments:
        obj -- 待確認的物件PositionOBJ
        all -- 所有要偵測碰撞物件的List[PositionOBJ]

    Return:
        bool -- 是否碰到
    """
    x = obj.x
    y = obj.y
    for i in all:
        if (x == i.pos_x and y == i.pos_y):
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
        self.rect = self.surf.get_rect(topleft=[pos.pos_x, pos.pos_y])

    @property
    def pos_x(self):
        return self.rect.topleft[0]

    @property
    def pos_y(self):
        return self.rect.topleft[1]


class Poison:
    """
    毒藥物件，初始化方法為 `GameOBJ`
    `self.pos_x` 及 `self.pos_y` 為毒藥的座標
    """

    def __init__(self, pos):
        self.surf = pg.surface.Surface(size=(SNAKE_SIZE, SNAKE_SIZE))
        self.surf.fill(POISON_COLOR)
        self.rect = self.surf.get_rect(topleft=[pos.pos_x, pos.pos_y])

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
        # TODO
        self.snake_list.append(
            [new_pos[0], new_pos[1], SNAKE_SIZE, SNAKE_SIZE])

    def draw_snake(self, screen) -> None:
        """
        畫出蛇，顏色要黃藍相間，無回傳值
        顏色可以用 `SNAKE_COLOR_YELLOW` 及 `SNAKE_COLOR_BLUE`
        可以用 `pg.draw.rect(screen 物件, 顏色, (座標 x, 座標 y, 寬, 高))`

        Keyword arguments:
        screen -- pygame 螢幕物件
        """
        # TODO
        for i in self.snake_list:
            pg.draw.rect(screen, SNAKE_COLOR_BLUE, i)

    def check_border(self) -> bool:
        """
        判斷蛇的頭有沒有超出螢幕範圍
        有超出就回傳 `True`
        沒有超出回傳 `False`

        Return:
        bool -- 蛇的頭有沒有超出螢幕範圍
        """
        # TODO
        if self.head_x > 700 or self.head_y > 600 or self.head_x < 0 or self.head_y < 0:
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
        # TODO
        if (direction == UP):
            for i in self.snake_list:
                i[1] -= 1
        elif (direction == DOWN):
            for i in self.snake_list:
                i[1] += 1
        elif (direction == LEFT):
            for i in self.snake_list:
                i[0] -= 1
        elif (direction == RIGHT):
            for i in self.snake_list:
                i[0] += 1
        # print(self.snake_list)

    def detect_player_collision(self) -> bool:
        """
        判斷蛇的頭是否碰到蛇的其他段
        有碰到就回傳 `True`
        沒有碰到回傳 `False`

        Return:
        bool -- 是否碰到蛇 (自己) 的其他段
        """
        # TODO
        return (self.snake_list.count(self.snake_list[0]) == 0)

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
        # TODO
        # print(walls)
        return check_GameOBJ_collision(PositionOBJ(self.head_x, self.head_y), walls)

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
        # TODO
        return check_GameOBJ_collision(PositionOBJ(self.head_x, self.head_y), [PositionOBJ(i.pos_x, i.pos_y) for i in foods])

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

        # return 
