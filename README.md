## 貪食蛇
##### 資訊之芽2023Py大作業

### 追加功能
+ 蛇頭特殊圖案by Inkscape `head.svg` (draw_snake)
+ 碰撞確認(`Model.py check_Collision`)
+ `Debug.py`: Logging、printLog


### 必要功能

##### 移動
+ 玩家移動(Player.move)

##### 生成物件
+ 生成牆壁(`Controller.py generate_wall`)，新牆壁生在現有牆壁周圍，朝同方向
生成食物(`Controller.py generate_food`)
生成毒藥(`Controller.py generate_poison`)
生成蛇(`Player.new_block`)，藍黃相間

##### 碰撞
邊界碰撞(`Player.check_border`)
蛇碰撞(`Player.detect_player_collision`)
牆壁碰撞(`Player.detect_wall_collision`)
食物碰撞(`Player.detect_food_collision`)
毒藥碰撞(`Player.detect_poison_collision`)

##### 遊戲機制
+ 根據蛇長度調整移動間格(`Controller.py 的 calculate_time_interval`)`fps = 4+player.length//4`