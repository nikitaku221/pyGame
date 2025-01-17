import pygame


def game_menu(screen, WIDTH, HEIGHT):
    """Главное меню игры."""
    game_running = True
    
    # Загрузка изображений для игрового меню
    game_background = pygame.image.load("img/menu_background.png")
    button1_image = pygame.image.load("img/start_game_button.png")
    button2_image = pygame.image.load("img/invetor_button.png")
    button3_image = pygame.image.load("img/shop_button.png")
    
    # Масштабирование кнопок и их размещение
    button_width = WIDTH // 5
    button_height = HEIGHT // 10
    scaled_button1 = pygame.transform.scale(button1_image, (button_width, button_height))
    scaled_button2 = pygame.transform.scale(button2_image, (button_width, button_height))
    scaled_button3 = pygame.transform.scale(button3_image, (button_width, button_height))

    # Расчёт координат кнопок
    # Отцентрируем кнопки в левом верхнем углу (по вертикали и горизонтали)
    margin_top = 240  # Отступ сверху
    margin_left = 100  # Отступ слева
    button_spacing = button_height + 10  # Расстояние между кнопками

    button1_rect = pygame.Rect(
        margin_left,
        margin_top,
        button_width,
        button_height
    )
    button2_rect = pygame.Rect(
        margin_left,
        margin_top + button_spacing,
        button_width,
        button_height
    )
    button3_rect = pygame.Rect(
        margin_left,
        margin_top + button_spacing * 2,
        button_width,
        button_height
    )

    while game_running:
        # Отрисовка фона и кнопок
        scaled_game_background = pygame.transform.scale(game_background, (WIDTH, HEIGHT))
        screen.blit(scaled_game_background, (0, 0))
        screen.blit(scaled_button1, button1_rect)
        screen.blit(scaled_button2, button2_rect)
        screen.blit(scaled_button3, button3_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_running = False
            elif event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
                # Перерасчет размеров кнопок
                button_width = WIDTH // 5
                button_height = HEIGHT // 10
                scaled_button1 = pygame.transform.scale(button1_image, (button_width, button_height))
                scaled_button2 = pygame.transform.scale(button2_image, (button_width, button_height))
                scaled_button3 = pygame.transform.scale(button3_image, (button_width, button_height))

                # Перерасчет координат кнопок с учетом нового размера окна
                button_spacing = button_height + 10
                button1_rect = pygame.Rect(
                    margin_left,
                    margin_top,
                    button_width,
                    button_height
                )
                button2_rect = pygame.Rect(
                    margin_left,
                    margin_top + button_spacing,
                    button_width,
                    button_height
                )
                button3_rect = pygame.Rect(
                    margin_left,
                    margin_top + button_spacing * 2,
                    button_width,
                    button_height
                )

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button1_rect.collidepoint(event.pos):
                    start_game(screen, WIDTH, HEIGHT)
                elif button2_rect.collidepoint(event.pos):
                    print("Кнопка 2 нажата!")
                elif button3_rect.collidepoint(event.pos):
                    print("Кнопка 3 нажата!")

        pygame.display.flip()

def start_game(screen, WIDTH, HEIGHT):
    """Основной игровой цикл."""
    # Загрузка карты и персонажа
    map_image = pygame.image.load("img/mini_map.png")
    player_image = pygame.image.load("img/player.png")

    # Настройка масштаба карты и персонажа
    map_scale = 1  # Коэффициент увеличения карты (чем больше, тем больше карта)
    scaled_map = pygame.transform.scale(
        map_image,
        (map_image.get_width() * map_scale, map_image.get_height() * map_scale)
    )

    # Масштабирование персонажа
    player_width = WIDTH // 15  # Персонаж становится больше
    player_height = HEIGHT // 15
    scaled_player = pygame.transform.scale(player_image, (player_width, player_height))

    # Начальная позиция персонажа
    player_x = scaled_map.get_width() // 2
    player_y = scaled_map.get_height() // 2

    # Позиция камеры
    camera_x = player_x - WIDTH // 5
    camera_y = player_y - HEIGHT // 5

    # Скорость движения персонажа
    player_speed = 2

    running = True
    while running:
        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
                player_width = WIDTH // 10
                player_height = HEIGHT // 10
                scaled_player = pygame.transform.scale(player_image, (player_width, player_height))

        # Получение нажатий клавиш
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:  # Вверх
            player_y -= player_speed
        if keys[pygame.K_s]:  # Вниз
            player_y += player_speed
        if keys[pygame.K_a]:  # Влево
            player_x -= player_speed
        if keys[pygame.K_d]:  # Вправо
            player_x += player_speed

        # Ограничиваем перемещение персонажа внутри карты (оставляем зазор до краёв)
        player_x = max(0, min(player_x, scaled_map.get_width() - player_width))
        player_y = max(0, min(player_y, scaled_map.get_height() - player_height))

        # Перемещение камеры, чтобы персонаж был ближе к центру экрана
        camera_x = player_x - WIDTH // 2
        camera_y = player_y - HEIGHT // 2

        # Ограничиваем камеру по краям карты
        camera_x = max(0, min(camera_x, scaled_map.get_width() - WIDTH))
        camera_y = max(0, min(camera_y, scaled_map.get_height() - HEIGHT))

        # Отрисовка карты
        screen.blit(scaled_map, (-camera_x, -camera_y))

        # Отрисовка персонажа
        screen.blit(scaled_player, (WIDTH // 2, HEIGHT // 2))

        # Обновляем экран
        pygame.display.flip()