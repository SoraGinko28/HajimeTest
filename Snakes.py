import pygame
import random

# 游戏窗口大小
window_width = 800
window_height = 600

# 蛇身方块大小
block_size = 20

# 初始化pygame
pygame.init()

# 创建游戏窗口
game_window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('贪吃蛇游戏')

clock = pygame.time.Clock()

# 定义颜色
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# 绘制蛇
def draw_snake(snake_body):
    for block in snake_body:
        pygame.draw.rect(game_window, white, [block[0], block[1], block_size, block_size])

# 主游戏循环
def game_loop():
    game_over = False
    game_exit = False

    # 蛇的初始位置
    snake_x = window_width / 2
    snake_y = window_height / 2

    # 蛇的初始移动方向
    snake_x_change = 0
    snake_y_change = 0

    # 生成食物的随机位置
    food_x = round(random.randrange(0, window_width - block_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, window_height - block_size) / 20.0) * 20.0

    # 蛇身的列表，其中每个元素代表一个身体方块的位置
    snake_body = []
    snake_length = 1

    while not game_exit:
        while game_over:
            # 游戏结束界面
            game_window.fill(black)
            font_style = pygame.font.SysFont(None, 50)
            message = font_style.render("游戏结束！按Q退出，按R重新开始", True, white)
            game_window.blit(message, [window_width / 6, window_height / 3])
            pygame.display.update()

            # 处理游戏结束事件
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_exit = True
                        game_over = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            # 处理按键事件
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake_x_change = -block_size
                    snake_y_change = 0
                elif event.key == pygame.K_RIGHT:
                    snake_x_change = block_size
                    snake_y_change = 0
                elif event.key == pygame.K_UP:
                    snake_y_change = -block_size
                    snake_x_change = 0
                elif event.key == pygame.K_DOWN:
                    snake_y_change = block_size
                    snake_x_change = 0

        # 更新蛇头位置
        snake_x += snake_x_change
        snake_y += snake_y_change

        # 判断是否吃到食物
        if snake_x == food_x and snake_y == food_y:
            food_x = round(random.randrange(0, window_width - block_size) / 20.0) * 20.0
            food_y = round(random.randrange(0, window_height - block_size) / 20.0) * 20.0
            snake_length += 1

        # 更新蛇身长度
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_body.append(snake_head)
        if len(snake_body) > snake_length:
            del snake_body[0]

        # 判断是否撞到自己
        for block in snake_body[:-1]:
            if block == snake_head:
                game_over = True

        # 判断是否撞到墙壁
        if snake_x >= window_width or snake_x < 0 or snake_y >= window_height or snake_y < 0:
            game_over = True

        # 清空游戏窗口
        game_window.fill(black)

        # 绘制食物
        pygame.draw.rect(game_window, red, [food_x, food_y, block_size, block_size])

        # 绘制蛇身
        draw_snake(snake_body)

        # 刷新屏幕
        pygame.display.update()

        # 控制游戏的帧率
        clock.tick(10)  # 可以调整游戏速度

    # 退出游戏
    pygame.quit()
    quit()

# 运行游戏
game_loop()
