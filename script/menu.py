import pygame
import random


def game_menu(screen, WIDTH, HEIGHT):
    """Главное меню игры."""
    game_running = True
    
    # Загрузка изображений для игрового меню
    game_background = pygame.image.load("img/background/menu_background.png")
    button1_image = pygame.image.load("img/button/start_game_button.png")
    button2_image = pygame.image.load("img/button/invetor_button.png")
    button3_image = pygame.image.load("img/button/shop_button.png")
    
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
                    shop_window(screen, WIDTH, HEIGHT)
                elif button3_rect.collidepoint(event.pos):
                    inventory_window(screen, WIDTH, HEIGHT)

        pygame.display.flip()

def shop_window(screen, WIDTH, HEIGHT):
    new_window_running = True
    new_background = pygame.image.load("img/background/shop_background.png")  # Замените на ваш фон
    back_button_image = pygame.image.load("img/button/back_button.png")  # Укажите ваш PNG для кнопки

    # Масштабирование кнопки "Назад"
    button_width, button_height = WIDTH // 5, HEIGHT // 10
    scaled_back_button = pygame.transform.scale(back_button_image, (button_width, button_height))
    back_button_rect = pygame.Rect(
        20,  # Отступ 20px от левого края
        20,  # Отступ 20px от верхнего края
        button_width,
        button_height
    )

    while new_window_running:
        # Отрисовка фона и кнопки
        screen.blit(pygame.transform.scale(new_background, (WIDTH, HEIGHT)), (0, 0))
        screen.blit(scaled_back_button, back_button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                new_window_running = False  # Закрыть окно
            elif event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

                # Перерасчёт размеров кнопки и её позиции
                button_width, button_height = WIDTH // 5, HEIGHT // 10
                scaled_back_button = pygame.transform.scale(back_button_image, (button_width, button_height))
                back_button_rect = pygame.Rect(
                    20,  # Отступ остаётся фиксированным
                    20,
                    button_width,
                    button_height
                )
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    new_window_running = False  # Вернуться в главное меню

        pygame.display.flip()


def inventory_window(screen, WIDTH, HEIGHT):
    new_window_running = True
    new_background = pygame.image.load("img/background/inventory_background.png")  # Замените на ваш фон
    back_button_image = pygame.image.load("img/button/back_button.png")  # Укажите ваш PNG для кнопки

    # Масштабирование кнопки "Назад"
    button_width, button_height = WIDTH // 5, HEIGHT // 10
    scaled_back_button = pygame.transform.scale(back_button_image, (button_width, button_height))
    back_button_rect = pygame.Rect(
        20,  # Отступ 20px от левого края
        20,  # Отступ 20px от верхнего края
        button_width,
        button_height
    )

    while new_window_running:
        # Отрисовка фона и кнопки
        screen.blit(pygame.transform.scale(new_background, (WIDTH, HEIGHT)), (0, 0))
        screen.blit(scaled_back_button, back_button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                new_window_running = False  # Закрыть окно
            elif event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

                # Перерасчёт размеров кнопки и её позиции
                button_width, button_height = WIDTH // 5, HEIGHT // 10
                scaled_back_button = pygame.transform.scale(back_button_image, (button_width, button_height))
                back_button_rect = pygame.Rect(
                    20,  # Отступ остаётся фиксированным
                    20,
                    button_width,
                    button_height
                )
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button_rect.collidepoint(event.pos):
                    new_window_running = False  # Вернуться в главное меню

        pygame.display.flip()


def show_game_over_screen(screen, WIDTH, HEIGHT):
    """Функция для отображения окна с сообщением после окончания игры."""
    font = pygame.font.Font(None, 60)  # Настраиваем шрифт
    text = font.render("Вы проиграли! Нажмите 'ОК'.", True, (255, 255, 255))  # Сообщение
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))  # Позиция текста

    # Кнопка "ОК"
    button_font = pygame.font.Font(None, 50)
    button_text = button_font.render("OK", True, (0, 0, 0))
    button_width = 100
    button_height = 50
    button_x = WIDTH // 2 - button_width // 2
    button_y = HEIGHT // 2 + 50
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)

    # Отрисовка окна
    while True:
        screen.fill((0, 0, 0))  # Чёрный фон
        screen.blit(text, text_rect)  # Отображение текста

        # Отображение кнопки
        pygame.draw.rect(screen, (255, 255, 255), button_rect)  # Белая рамка кнопки
        screen.blit(button_text, (button_x + 20, button_y + 10))  # Текст на кнопке

        pygame.display.flip()  # Обновление экрана

        # Обработка событий
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):  # Проверка клика на кнопке
                    return  # Выход из функции после нажатия "ОК"

def start_game(screen, WIDTH, HEIGHT):
    """Основной игровой цикл с врагами, аптечками и взаимодействием с картой."""
    import pygame
    import random

    # Загрузка карты
    map_image = pygame.image.load("img/map_1/map.png")
    map_scale = 4
    scaled_map = pygame.transform.scale(
        map_image,
        (map_image.get_width() * map_scale, map_image.get_height() * map_scale)
    )

    # Загрузка изображений персонажа
    player_images = {
        "down": pygame.image.load("img/kat/kat_up.png"),
        "up": pygame.image.load("img/kat/kat_down.png"),
        "left": pygame.image.load("img/kat/kat_left.png"),
        "right": pygame.image.load("img/kat/kat_right.png"),
    }

    # Загрузка изображений врагов и аптечек
    enemy_image = pygame.image.load("img/kris.png")
    health_image = pygame.image.load("img/heal.png")

    # Загрузка изображений элементов
    elements = {
        "flower": {"image": pygame.image.load("img/map_1/flower.png"), "damage": 5},
        "grass": {"image": pygame.image.load("img/map_1/grass.png"), "damage": 3},
        "stump": {"image": pygame.image.load("img/map_1/stump.png"), "damage": 10},
        "bush": {"image": pygame.image.load("img/map_1/bush.png"), "damage": 7},
        "tree": {"image": pygame.image.load("img/map_1/tree.png"), "damage": 12},
        "mud": {"image": pygame.image.load("img/map_1/mud.png"), "damage": 4},
    }

    # Масштабирование объектов
    for element in elements.values():
        element["image"] = pygame.transform.scale(element["image"], (WIDTH // 15, HEIGHT // 15))
        element["size"] = element["image"].get_size()

    enemy_image = pygame.transform.scale(enemy_image, (WIDTH // 12, HEIGHT // 12))
    health_image = pygame.transform.scale(health_image, (WIDTH // 15, HEIGHT // 15))

    # Распределение объектов на карте
    num_elements = 15
    map_elements = []
    for name, props in elements.items():
        for _ in range(num_elements):
            map_elements.append({
                "name": name,
                "x": random.randint(0, scaled_map.get_width() - props["size"][0]),
                "y": random.randint(0, scaled_map.get_height() - props["size"][1]),
                "damage": props["damage"],
                "image": props["image"]
            })

    # Создание врагов
    num_enemies = 5
    enemies = []
    for _ in range(num_enemies):
        enemies.append({
            "x": random.randint(0, scaled_map.get_width() - enemy_image.get_width()),
            "y": random.randint(0, scaled_map.get_height() - enemy_image.get_height()),
            "hp": 50,
            "damage": 10
        })

    # Создание аптечек
    num_health_packs = 5
    health_packs = []
    for _ in range(num_health_packs):
        health_packs.append({
            "x": random.randint(0, scaled_map.get_width() - health_image.get_width()),
            "y": random.randint(0, scaled_map.get_height() - health_image.get_height()),
            "heal": 20
        })

    # Масштабирование персонажа
    player_width = WIDTH // 10
    player_height = HEIGHT // 10
    scaled_player_images = {direction: pygame.transform.scale(image, (player_width, player_height))
                            for direction, image in player_images.items()}

    current_player_image = scaled_player_images["down"]
    player_map_x = scaled_map.get_width() // 2
    player_map_y = scaled_map.get_height() // 2
    camera_x = player_map_x - WIDTH // 2
    camera_y = player_map_y - HEIGHT // 2
    player_speed = 10
    player_hp = 100
    player_max_hp = 100

    # Таймеры для предотвращения повторного урона от элементов карты
    element_damage_cooldown = 500  # миллисекунды
    last_element_damage_time = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player_map_y -= player_speed
            current_player_image = scaled_player_images["up"]
        if keys[pygame.K_s]:
            player_map_y += player_speed
            current_player_image = scaled_player_images["down"]
        if keys[pygame.K_a]:
            player_map_x -= player_speed
            current_player_image = scaled_player_images["left"]
        if keys[pygame.K_d]:
            player_map_x += player_speed
            current_player_image = scaled_player_images["right"]

        # Атака врагов
        if keys[pygame.K_SPACE]:  # Клавиша атаки
            player_rect = pygame.Rect(player_map_x, player_map_y, player_width, player_height)
            for enemy in enemies[:]:
                enemy_rect = pygame.Rect(enemy["x"], enemy["y"], enemy_image.get_width(), enemy_image.get_height())
                if player_rect.colliderect(enemy_rect):
                    enemy["hp"] -= 20  # Урон врагу
                    if enemy["hp"] <= 0:
                        enemies.remove(enemy)

        player_map_x = max(0, min(player_map_x, scaled_map.get_width() - 1))
        player_map_y = max(0, min(player_map_y, scaled_map.get_height() - 1))
        camera_x = max(0, min(player_map_x - WIDTH // 2, scaled_map.get_width() - WIDTH))
        camera_y = max(0, min(player_map_y - HEIGHT // 2, scaled_map.get_height() - HEIGHT))
        player_screen_x = max(0, min(player_map_x - camera_x, WIDTH - player_width))
        player_screen_y = max(0, min(player_map_y - camera_y, HEIGHT - player_height))

        current_time = pygame.time.get_ticks()

        # Проверка урона от элементов карты
        for element in map_elements[:]:
            element_rect = pygame.Rect(element["x"], element["y"], element["image"].get_width(),
                                        element["image"].get_height())
            player_rect = pygame.Rect(player_map_x, player_map_y, player_width, player_height)
            if player_rect.colliderect(element_rect):
                if current_time - last_element_damage_time > element_damage_cooldown:
                    player_hp -= element["damage"]
                    last_element_damage_time = current_time
                    dx = player_map_x - element["x"]
                    dy = player_map_y - element["y"]
                    dist = max(1, (dx ** 2 + dy ** 2) ** 0.5)
                    player_map_x += int(dx / dist * 20)
                    player_map_y += int(dy / dist * 20)

        # Урон от врагов
        for enemy in enemies[:]:
            enemy_rect = pygame.Rect(enemy["x"], enemy["y"], enemy_image.get_width(), enemy_image.get_height())
            player_rect = pygame.Rect(player_map_x, player_map_y, player_width, player_height)
            if player_rect.colliderect(enemy_rect):
                player_hp -= enemy["damage"]
                enemies.remove(enemy)

        # Сбор аптечек
        for health in health_packs[:]:
            health_rect = pygame.Rect(health["x"], health["y"], health_image.get_width(), health_image.get_height())
            player_rect = pygame.Rect(player_map_x, player_map_y, player_width, player_height)
            if player_rect.colliderect(health_rect):
                player_hp = min(player_max_hp, player_hp + health["heal"])
                health_packs.remove(health)

        # Проверка здоровья игрока
        if player_hp <= 0:
            show_game_over_screen(screen, WIDTH, HEIGHT)
            return

        # Отрисовка объектов
        screen.blit(scaled_map, (-camera_x, -camera_y))
        for element in map_elements:
            element_screen_x = element["x"] - camera_x
            element_screen_y = element["y"] - camera_y
            if 0 <= element_screen_x <= WIDTH and 0 <= element_screen_y <= HEIGHT:
                screen.blit(element["image"], (element_screen_x, element_screen_y))

        for enemy in enemies:
            enemy_screen_x = enemy["x"] - camera_x
            enemy_screen_y = enemy["y"] - camera_y
            screen.blit(enemy_image, (enemy_screen_x, enemy_screen_y))
            enemy_hp_ratio = enemy["hp"] / 50
            pygame.draw.rect(screen, (255, 0, 0), (enemy_screen_x, enemy_screen_y - 10, enemy_image.get_width(), 5))
            pygame.draw.rect(screen, (0, 255, 0), (enemy_screen_x, enemy_screen_y - 10, enemy_image.get_width() * enemy_hp_ratio, 5))

        for health in health_packs:
            health_screen_x = health["x"] - camera_x
            health_screen_y = health["y"] - camera_y
            screen.blit(health_image, (health_screen_x, health_screen_y))

        screen.blit(current_player_image, (player_screen_x, player_screen_y))
        player_hp_bar_width = player_width
        player_hp_bar_height = 5
        player_health_ratio = player_hp / player_max_hp
        pygame.draw.rect(screen, (255, 0, 0),
                         (player_screen_x, player_screen_y - player_hp_bar_height - 5, player_hp_bar_width, player_hp_bar_height))
        pygame.draw.rect(screen, (0, 255, 0),
                         (player_screen_x, player_screen_y - player_hp_bar_height - 5, player_hp_bar_width * player_health_ratio, player_hp_bar_height))

        pygame.display.flip()
