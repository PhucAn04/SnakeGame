import pygame
import time
import random

pygame.init()

# Màu sắc
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Kích thước của cửa sổ
dis_width = 800
dis_height = 600

# Kích thước của con rắn
snake_block = 10
snake_speed = 15  # Tốc độ ban đầu của con rắn
speed_increase = 1  # Tốc độ tăng thêm sau mỗi lần ăn mồi

# Khởi tạo cửa sổ game
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

# Clock để quản lý tốc độ của game
clock = pygame.time.Clock()

font_style = pygame.font.SysFont(None, 50)

# Hàm để vẽ con rắn
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

# Hàm để hiển thị thông điệp trên màn hình
def message(msg, color, y_displace=0, x_displace=0):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 2 - mesg.get_width() / 2 + x_displace, dis_height / 2 + y_displace])

# Hàm chính của game
def gameLoop(snake_speed):
    game_over = False
    game_close = False

    # Vị trí ban đầu của con rắn
    x1 = dis_width / 2
    y1 = dis_height / 2

    # Thay đổi trong vị trí của con rắn
    x1_change = 0
    y1_change = 0

    # Độ dài ban đầu của con rắn
    snake_list = []
    length_of_snake = 1

    # Tạo vị trí ban đầu cho mồi
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red, -50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop(snake_speed)  # Truyền giá trị của snake_speed vào hàm gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        # Kiểm tra nếu con rắn đụng tường
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        
        # Vẽ mồi
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        # Vẽ và cập nhật con rắn
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        pygame.display.update()

        # Kiểm tra nếu con rắn ăn mồi
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            snake_speed += speed_increase  # Tăng tốc độ của con rắn

        clock.tick(round(snake_speed))  # Làm tròn giá trị của snake_speed trước khi truyền vào hàm tick()

        # Hiển thị giao diện outro nếu người chơi thua
        if game_close:
            game_outro()

    pygame.quit()
    quit()

def game_intro():
    intro = True
    play_button = pygame.Rect(dis_width / 3, dis_height / 2 - 50, 200, 50)
    quit_button = pygame.Rect(dis_width / 3, dis_height / 2 + 50, 200, 50)
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_button.collidepoint(mouse_pos):
                    gameLoop(snake_speed)
                elif quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    quit()
                    
        dis.fill(blue)
        message("Snake Game", black, -150, -35)

        # Vẽ nút "Play"
        pygame.draw.rect(dis, green, play_button)
        message("Play", black, -40, -35)
        
        # Vẽ nút "Quit"
        pygame.draw.rect(dis, red, quit_button)
        message("Quit", black, 60, -35)
        
        pygame.display.update()
        clock.tick(15)

def game_outro():
    outro = True
    play_again_button = pygame.Rect(dis_width / 3, dis_height / 2 - 50, 300, 50)
    quit_button = pygame.Rect(dis_width / 3, dis_height / 2 + 50, 300, 50)
    
    while outro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_again_button.collidepoint(mouse_pos):
                    gameLoop(snake_speed)
                elif quit_button.collidepoint(mouse_pos):
                    pygame.quit()
                    quit()
                    
        dis.fill(blue)
        message("You Lost!", red, -150, 20)
        
        # Vẽ nút "Play Again"
        pygame.draw.rect(dis, green, play_again_button)
        message("Play Again", black, -40, 20)
        
        # Vẽ nút "Quit"
        pygame.draw.rect(dis, red, quit_button)
        message("Quit", black, 60, 20)
        
        pygame.display.update()
        clock.tick(15)

game_intro()
