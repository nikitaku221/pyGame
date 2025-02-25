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
    on_shield = False
    on_maich = False
    # Инициализация переменной map_item
    map_item = {
        "x": -1000,  # Начальные координаты за пределами экрана
        "y": -1000,
    }

    # Загрузка карты
    map_image = pygame.image.load("img/map_1/map.png")
    map_scale = 4
    scaled_map = pygame.transform.scale(
        map_image,
        (map_image.get_width() * map_scale, map_image.get_height() * map_scale)
    )

    # Загрузка изображений персонажа
    player_images = {
        "down": pygame.image.load("img/kat/default/kat_up.png"),
        "up": pygame.image.load("img/kat/default/kat_down.png"),
        "left": pygame.image.load("img/kat/default/kat_left.png"),
        "right": pygame.image.load("img/kat/default/kat_right.png"),
    }
    player_images_on_shiald = {
        "up": pygame.image.load("img/kat/on_shiald/kat_up.png"),
        "down": pygame.image.load("img/kat/on_shiald/kat_down.png"),
        "left": pygame.image.load("img/kat/default/kat_left.png"),
        "right": pygame.image.load("img/kat/on_shiald/kat_right.png"),
    }
    player_images_on_maich = {
        "up": pygame.image.load("img/kat/on_maich/kat_up.png"),
        "down": pygame.image.load("img/kat/on_maich/kat_down.png"),
        "left": pygame.image.load("img/kat/on_maich/kat_left.png"),
        "right": pygame.image.load("img/kat/default/kat_right.png"),
    }
    player_images_on_two_flags = {
        "up": pygame.image.load("img/kat/on_two_flags/kat_up.png"),
        "down": pygame.image.load("img/kat/on_two_flags/kat_down.png"),
        "left": pygame.image.load("img/kat/on_maich/kat_left.png"),
        "right": pygame.image.load("img/kat/on_shiald/kat_right.png"),
    }

    # Загрузка изображений врагов и аптечек
    enemy_image = pygame.image.load("img/kris/kris_1lvl.png")
    health_image = pygame.image.load("img/heal.png")
    shiald_image = pygame.image.load("img/shiald.png")
    maich_image = pygame.image.load("img/maich.png")

    # Загрузка изображений элементов
    elements = {
        "flower": {"image": pygame.image.load("img/map_1/flower.png"), "damage": 0},
        "grass": {"image": pygame.image.load("img/map_1/grass.png"), "damage": 0},
        "stump": {"image": pygame.image.load("img/map_1/stump.png"), "damage": 5},
        "bush": {"image": pygame.image.load("img/map_1/bush.png"), "damage": 3},
        "tree": {"image": pygame.image.load("img/map_1/tree.png"), "damage": 10},
        "mud": {"image": pygame.image.load("img/map_1/mud.png"), "damage": 7},
    }

    # Масштабирование объектов
    for element in elements.values():
        element["image"] = pygame.transform.scale(element["image"], (WIDTH // 15, HEIGHT // 15))
        element["size"] = element["image"].get_size()

    enemy_image = pygame.transform.scale(enemy_image, (WIDTH // 12, HEIGHT // 12))
    health_image = pygame.transform.scale(health_image, (WIDTH // 15, HEIGHT // 15))
    shiald_image = pygame.transform.scale(shiald_image, (WIDTH // 15, HEIGHT // 15))
    maich_image = pygame.transform.scale(maich_image, (WIDTH // 15, HEIGHT // 15))

    # Загрузка изображения безобидного персонажа
    helpless_image = pygame.image.load("img/npc_cat.png")
    helpless_image = pygame.transform.scale(helpless_image, (WIDTH // 12, HEIGHT // 12))

    # Загрузка изображения карты
    map_item_image = pygame.image.load("img/map_item.png")
    map_item_image = pygame.transform.scale(map_item_image, (WIDTH // 15, HEIGHT // 15))

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

    # Создание безобидного персонажа
    helpless = {
        "x": random.randint(0, scaled_map.get_width() - helpless_image.get_width()),
        "y": random.randint(0, scaled_map.get_height() - helpless_image.get_height()),
    }

    # Создание врагов вокруг безобидного персонажа
    num_enemies = 5
    enemies = []
    for _ in range(num_enemies):
        enemy_x = helpless["x"] + random.randint(-100, 100)
        enemy_y = helpless["y"] + random.randint(-100, 100)
        enemies.append({
            "x": enemy_x,
            "y": enemy_y,
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

    num_shiald_packs = 1
    shiald_packs = []
    for _ in range(num_shiald_packs):
        shiald_packs.append({
            "x": random.randint(0, scaled_map.get_width() - shiald_image.get_width()),
            "y": random.randint(0, scaled_map.get_height() - shiald_image.get_height()),
        })

    num_maich_packs = 1
    maich_packs = []
    for _ in range(num_maich_packs):
        maich_packs.append({
            "x": random.randint(0, scaled_map.get_width() - maich_image.get_width()),
            "y": random.randint(0, scaled_map.get_height() - maich_image.get_height()),
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
    player_speed = 1
    player_hp = 100
    player_max_hp = 100

    # Таймеры для предотвращения повторного урона от элементов карты
    element_damage_cooldown = 500  # миллисекунды
    last_element_damage_time = 0

    # Флаг для проверки, все ли враги уничтожены
    all_enemies_defeated = False

    # Флаг для проверки, подобрана ли карта
    map_picked_up = False

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
                    player_map_x += int(dx / dist * 50)
                    player_map_y += int(dy / dist * 50)

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

        # Сбор щитов
        for shiald in shiald_packs[:]:
            shiald_rect = pygame.Rect(shiald["x"], shiald["y"], shiald_image.get_width(), shiald_image.get_height())
            player_rect = pygame.Rect(player_map_x, player_map_y, player_width, player_height)
            if player_rect.colliderect(shiald_rect):
                on_shield = True
                shiald_packs.remove(shiald)
                # Обновляем изображения персонажа
                if on_maich:
                    scaled_player_images = {direction: pygame.transform.scale(image, (player_width, player_height))
                                        for direction, image in player_images_on_two_flags.items()}
                else:
                    scaled_player_images = {direction: pygame.transform.scale(image, (player_width, player_height))
                                        for direction, image in player_images_on_shiald.items()}
                current_player_image = scaled_player_images["down"]

        # Сбор мейчей
        for maich in maich_packs[:]:
            maich_rect = pygame.Rect(maich["x"], maich["y"], maich_image.get_width(), maich_image.get_height())
            player_rect = pygame.Rect(player_map_x, player_map_y, player_width, player_height)
            if player_rect.colliderect(maich_rect):
                on_maich = True
                maich_packs.remove(maich)
                # Обновляем изображения персонажа
                if on_shield:
                    scaled_player_images = {direction: pygame.transform.scale(image, (player_width, player_height))
                                        for direction, image in player_images_on_two_flags.items()}
                else:
                    scaled_player_images = {direction: pygame.transform.scale(image, (player_width, player_height))
                                        for direction, image in player_images_on_maich.items()}
                current_player_image = scaled_player_images["down"]

        # Проверка здоровья игрока
        if player_hp <= 0:
            show_game_over_screen(screen, WIDTH, HEIGHT)
            return

        # Проверка, все ли враги уничтожены
        if not enemies and not all_enemies_defeated:
            all_enemies_defeated = True

        # Взаимодействие с безобидным персонажем
        if all_enemies_defeated:
            helpless_rect = pygame.Rect(helpless["x"], helpless["y"], helpless_image.get_width(), helpless_image.get_height())
            player_rect = pygame.Rect(player_map_x, player_map_y, player_width, player_height)
            if player_rect.colliderect(helpless_rect):
                # Разговор с персонажем и спавн карты
                map_item = {
                    "x": helpless["x"],
                    "y": helpless["y"],
                }
                map_picked_up = False

        # Подбор карты
        if all_enemies_defeated and not map_picked_up:
            map_item_rect = pygame.Rect(map_item["x"], map_item["y"], map_item_image.get_width(), map_item_image.get_height())
            player_rect = pygame.Rect(player_map_x, player_map_y, player_width, player_height)
            if player_rect.colliderect(map_item_rect):
                map_picked_up = True
                running = False  # Останавливаем текущий игровой цикл
                start_game2(screen, WIDTH, HEIGHT, on_shield, on_maich)
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

        if all_enemies_defeated and not map_picked_up:
            helpless_screen_x = helpless["x"] - camera_x
            helpless_screen_y = helpless["y"] - camera_y
            screen.blit(helpless_image, (helpless_screen_x, helpless_screen_y))

            map_item_screen_x = map_item["x"] - camera_x
            map_item_screen_y = map_item["y"] - camera_y
            screen.blit(map_item_image, (map_item_screen_x, map_item_screen_y))

        
        for shiald in shiald_packs:
            shiald_screen_x = shiald["x"] - camera_x
            shiald_screen_y = shiald["y"] - camera_y
            screen.blit(shiald_image, (shiald_screen_x, shiald_screen_y))
        
        
        for maich in maich_packs:
            maich_screen_x = maich["x"] - camera_x
            maich_screen_y = maich["y"] - camera_y
            screen.blit(maich_image, (maich_screen_x, maich_screen_y))

        screen.blit(current_player_image, (player_screen_x, player_screen_y))
        player_hp_bar_width = player_width
        player_hp_bar_height = 5
        player_health_ratio = player_hp / player_max_hp
        pygame.draw.rect(screen, (255, 0, 0),
                         (player_screen_x, player_screen_y - player_hp_bar_height - 5, player_hp_bar_width, player_hp_bar_height))
        pygame.draw.rect(screen, (0, 255, 0),
                         (player_screen_x, player_screen_y - player_hp_bar_height - 5, player_hp_bar_width * player_health_ratio, player_hp_bar_height))

        pygame.display.flip()

def start_game2(screen, WIDTH, HEIGHT, on_shield, on_maich):
    map_image = pygame.image.load("img/map_2/map.png")
    map_scale = 4
    scaled_map = pygame.transform.scale(
        map_image,
        (map_image.get_width() * map_scale, map_image.get_height() * map_scale)
    )

    aganim = False

    # Загрузка изображений для ентити
    elements = {
        "волшебный пруд": {"image": pygame.image.load("img/map_2/pond.png"), "damage": 0},
        "грибы": {"image": pygame.image.load("img/map_2/mushrooms.png"), "damage": 0},
        "елка": {"image": pygame.image.load("img/map_2/tree.png"), "damage": 10},
        "камни желтые": {"image": pygame.image.load("img/map_2/yellow_stones.png"), "damage": 1},
        "камни красные": {"image": pygame.image.load("img/map_2/red_stones.png"), "damage": 4},
        "камни оранжевые": {"image": pygame.image.load("img/map_2/orange_stones.png"), "damage": 3},
        "пещера": {"image": pygame.image.load("img/map_2/cave.png"), "damage": 0},
        "твара высокая": {"image": pygame.image.load("img/map_2/tall_creature.png"), "damage": 1},
        "трава жёлтая": {"image": pygame.image.load("img/map_2/yellow_grass.png"), "damage": 2},
        "трава равнины": {"image": pygame.image.load("img/map_2/plain_grass.png"), "damage": 3},
    }

    aganim_elementss = {
        "афи": {"image": pygame.image.load("img/map2_item/afi.png")},
        "агрошка": {"image": pygame.image.load("img/map2_item/agrochka.png")},
        "алз": {"image": pygame.image.load("img/map2_item/alz.png")},
        "арг": {"image": pygame.image.load("img/map2_item/arg.png")},
        "арк": {"image": pygame.image.load("img/map2_item/ark.png")},
        "арушка": {"image": pygame.image.load("img/map2_item/Aruchka.png")},
    }

    enemy_image = pygame.image.load("img/kris/kris_2lvl.png")
    health_image = pygame.image.load("img/heal.png")

    enemy_image = pygame.transform.scale(enemy_image, (WIDTH // 12, HEIGHT // 12))
    health_image = pygame.transform.scale(health_image, (WIDTH // 15, HEIGHT // 15))

    # Масштабирование изображений ентити
    for element in elements.values():
        element["image"] = pygame.transform.scale(element["image"], (WIDTH // 15, HEIGHT // 15))
        element["size"] = element["image"].get_size()

    for element in aganim_elementss.values():
        element["image"] = pygame.transform.scale(element["image"], (WIDTH // 15, HEIGHT // 15))
        element["size"] = element["image"].get_size()

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

    num_aganim_elements = 1  # Количество каждого элемента Аганима
    aganim_elements = []
    for name, props in aganim_elementss.items():
        for _ in range(num_aganim_elements):
            aganim_elements.append({
                "name": name,
                "x": random.randint(0, scaled_map.get_width() - props["size"][0]),
                "y": random.randint(0, scaled_map.get_height() - props["size"][1]),
                "image": props["image"]
            })

    # Инициализация переменных для Аганима и зелья
    aganim = None
    potion = None
    collected_aganim_elements = []  # Список для хранения собранных элементов

    # Загрузка изображений персонажа
    player_images = {
        "down": pygame.image.load("img/kat/default/kat_up.png"),
        "up": pygame.image.load("img/kat/default/kat_down.png"),
        "left": pygame.image.load("img/kat/default/kat_left.png"),
        "right": pygame.image.load("img/kat/default/kat_right.png"),
    }
    player_images_on_shiald = {
        "down": pygame.image.load("img/kat/on_shiald/kat_up.png"),
        "up": pygame.image.load("img/kat/on_shiald/kat_down.png"),
        "left": pygame.image.load("img/kat/default/kat_left.png"),
        "right": pygame.image.load("img/kat/on_shiald/kat_right.png"),
    }
    player_images_on_maich = {
        "down": pygame.image.load("img/kat/on_maich/kat_up.png"),
        "up": pygame.image.load("img/kat/on_maich/kat_down.png"),
        "left": pygame.image.load("img/kat/on_maich/kat_left.png"),
        "right": pygame.image.load("img/kat/default/kat_right.png"),
    }
    player_images_on_two_flags = {
        "down": pygame.image.load("img/kat/on_two_flags/kat_up.png"),
        "up": pygame.image.load("img/kat/on_two_flags/kat_down.png"),
        "left": pygame.image.load("img/kat/on_maich/kat_left.png"),
        "right": pygame.image.load("img/kat/on_shiald/kat_right.png"),
    }

    num_enemies = 5
    enemies = []
    for _ in range(num_enemies):
        enemies.append({
            "x": random.randint(0, scaled_map.get_width() - health_image.get_width()),
            "y": random.randint(0, scaled_map.get_width() - health_image.get_width()),
            "hp": 50,
            "damage": 10
        })

    # Создание аптечек
    num_health_packs = 10
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
    if on_maich and on_shield:
        scaled_player_images = {direction: pygame.transform.scale(image, (player_width, player_height))
                               for direction, image in player_images_on_two_flags.items()}
    elif on_maich:
        scaled_player_images = {direction: pygame.transform.scale(image, (player_width, player_height))
                               for direction, image in player_images_on_maich.items()}
    elif on_shield:
        scaled_player_images = {direction: pygame.transform.scale(image, (player_width, player_height))
                               for direction, image in player_images_on_shiald.items()}
    else:
        scaled_player_images = {direction: pygame.transform.scale(image, (player_width, player_height))
                               for direction, image in player_images.items()}

    current_player_image = scaled_player_images["down"]
    player_map_x = scaled_map.get_width() // 2
    player_map_y = scaled_map.get_height() // 2
    camera_x = player_map_x - WIDTH // 2
    camera_y = player_map_y - HEIGHT // 2
    player_speed = 10
    # Таймеры для предотвращения повторного урона от элементов карты
    element_damage_cooldown = 500  # миллисекунды
    last_element_damage_time = 0
    player_hp = 100
    player_max_hp = 150

    # Основной игровой цикл
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

        player_map_x = max(0, min(player_map_x, scaled_map.get_width() - 1))
        player_map_y = max(0, min(player_map_y, scaled_map.get_height() - 1))
        camera_x = max(0, min(player_map_x - WIDTH // 2, scaled_map.get_width() - WIDTH))
        camera_y = max(0, min(player_map_y - HEIGHT // 2, scaled_map.get_height() - HEIGHT))
        player_screen_x = max(0, min(player_map_x - camera_x, WIDTH - player_width))
        player_screen_y = max(0, min(player_map_y - camera_y, HEIGHT - player_height))

        current_time = pygame.time.get_ticks()

        # В основном игровом цикле добавляем проверку на сбор элементов Аганима
        for element in aganim_elements[:]:  # Используем срез [:] для безопасного удаления элементов
            element_rect = pygame.Rect(element["x"], element["y"], element["image"].get_width(), element["image"].get_height())
            player_rect = pygame.Rect(player_map_x, player_map_y, player_width, player_height)
            if player_rect.colliderect(element_rect):
                collected_aganim_elements.append(element["name"])
                aganim_elements.remove(element)

        # Спавн Аганима, если все элементы собраны
        if not aganim and len(collected_aganim_elements) == len(aganim_elementss) * num_aganim_elements:
            aganim = {
                "x": player_map_x + 50,  # Спавн рядом с персонажем
                "y": player_map_y + 50,
                "image": pygame.image.load("img/map2_item/aganim.png")
            }
            aganim["image"] = pygame.transform.scale(aganim["image"], (WIDTH // 15, HEIGHT // 15))

        if aganim:
            aganim_rect = pygame.Rect(aganim["x"], aganim["y"], aganim["image"].get_width(), aganim["image"].get_height())
            player_rect = pygame.Rect(player_map_x, player_map_y, player_width, player_height)
            if player_rect.colliderect(aganim_rect):
                potion = {
                    "x": player_map_x + 50,  # Спавн рядом с персонажем
                    "y": player_map_y + 50,
                    "image": pygame.image.load("img/map2_item/potion.png")
                }
                potion["image"] = pygame.transform.scale(potion["image"], (WIDTH // 15, HEIGHT // 15))
                aganim = None

        if potion:
            potion_rect = pygame.Rect(potion["x"], potion["y"], potion["image"].get_width(), potion["image"].get_height())
            player_rect = pygame.Rect(player_map_x, player_map_y, player_width, player_height)
            if player_rect.colliderect(potion_rect):
                start_game3(screen, WIDTH, HEIGHT, on_shield, on_maich)  # Вызов функции start_game3
                return


        # Проверка столкновений с ентити
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
                    player_map_x += int(dx / dist * 70)
                    player_map_y += int(dy / dist * 70)

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
            
        for element in aganim_elements:
            element_screen_x = element["x"] - camera_x
            element_screen_y = element["y"] - camera_y
            if 0 <= element_screen_x <= WIDTH and 0 <= element_screen_y <= HEIGHT:  # Проверка видимости
                screen.blit(element["image"], (element_screen_x, element_screen_y))

        # Отрисовка Аганима
        if aganim:
            aganim_screen_x = aganim["x"] - camera_x
            aganim_screen_y = aganim["y"] - camera_y
            if 0 <= aganim_screen_x <= WIDTH and 0 <= aganim_screen_y <= HEIGHT:  # Проверка видимости
                screen.blit(aganim["image"], (aganim_screen_x, aganim_screen_y))

        # Отрисовка зелья
        if potion:
            potion_screen_x = potion["x"] - camera_x
            potion_screen_y = potion["y"] - camera_y
            if 0 <= potion_screen_x <= WIDTH and 0 <= potion_screen_y <= HEIGHT:  # Проверка видимости
                screen.blit(potion["image"], (potion_screen_x, potion_screen_y))

        screen.blit(current_player_image, (player_screen_x, player_screen_y))
        player_hp_bar_width = player_width
        player_hp_bar_height = 5
        player_health_ratio = player_hp / player_max_hp
        pygame.draw.rect(screen, (255, 0, 0),
                         (player_screen_x, player_screen_y - player_hp_bar_height - 5, player_hp_bar_width, player_hp_bar_height))
        pygame.draw.rect(screen, (0, 255, 0),
                         (player_screen_x, player_screen_y - player_hp_bar_height - 5, player_hp_bar_width * player_health_ratio, player_hp_bar_height))

        pygame.display.flip()


def start_game3(screen, WIDTH, HEIGHT, on_shield, on_maich):
    map_image = pygame.image.load("img/map_3/map.png")
    map_scale = 4
    scaled_map = pygame.transform.scale(
        map_image,
        (map_image.get_width() * map_scale, map_image.get_height() * map_scale)
    )

    # Загрузка изображений для ентити
    elements = {
        "куст": {"image": pygame.image.load("img/map_3/bush.png"), "damage":0},
        "пик1": {"image": pygame.image.load("img/map_3/spike_1.png"), "damage":5},
        "пик2": {"image": pygame.image.load("img/map_3/spike_2.png"), "damage":5},
        "камень1": {"image": pygame.image.load("img/map_3/stone_1.png"), "damage":5},
        "камень2": {"image": pygame.image.load("img/map_3/stone_2.png"), "damage":5},
        "дерево": {"image": pygame.image.load("img/map_3/tree.png"), "damage":5},
    }

    enemy_image = pygame.image.load("img/kris/kris_2lvl.png")
    enemy_king_image =pygame.image.load("img/kris/king_kris.png")
    health_image = pygame.image.load("img/heal.png")

    enemy_image = pygame.transform.scale(enemy_image, (WIDTH // 12, HEIGHT // 12))
    enemy_king_image = pygame.transform.scale(enemy_king_image, (WIDTH // 12, HEIGHT // 12))
    health_image = pygame.transform.scale(health_image, (WIDTH // 15, HEIGHT // 15))

    # Масштабирование изображений ентити
    for element in elements.values():
        element["image"] = pygame.transform.scale(element["image"], (WIDTH // 15, HEIGHT // 15))
        element["size"] = element["image"].get_size()

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


    # Загрузка изображений персонажа
    player_images = {
        "down": pygame.image.load("img/kat/default/kat_up.png"),
        "up": pygame.image.load("img/kat/default/kat_down.png"),
        "left": pygame.image.load("img/kat/default/kat_left.png"),
        "right": pygame.image.load("img/kat/default/kat_right.png"),
    }
    player_images_on_shiald = {
        "down": pygame.image.load("img/kat/on_shiald/kat_up.png"),
        "up": pygame.image.load("img/kat/on_shiald/kat_down.png"),
        "left": pygame.image.load("img/kat/default/kat_left.png"),
        "right": pygame.image.load("img/kat/on_shiald/kat_right.png"),
    }
    player_images_on_maich = {
        "down": pygame.image.load("img/kat/on_maich/kat_up.png"),
        "up": pygame.image.load("img/kat/on_maich/kat_down.png"),
        "left": pygame.image.load("img/kat/on_maich/kat_left.png"),
        "right": pygame.image.load("img/kat/default/kat_right.png"),
    }
    player_images_on_two_flags = {
        "down": pygame.image.load("img/kat/on_two_flags/kat_up.png"),
        "up": pygame.image.load("img/kat/on_two_flags/kat_down.png"),
        "left": pygame.image.load("img/kat/on_maich/kat_left.png"),
        "right": pygame.image.load("img/kat/on_shiald/kat_right.png"),
    }

    num_enemies = 5
    enemies = []
    for _ in range(num_enemies):
        enemies.append({
            "x": random.randint(0, scaled_map.get_width() - health_image.get_width()),
            "y": random.randint(0, scaled_map.get_width() - health_image.get_width()),
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
    if on_maich and on_shield:
        scaled_player_images = {direction: pygame.transform.scale(image, (player_width, player_height))
                            for direction, image in player_images_on_two_flags.items()}
    elif on_maich:
        scaled_player_images = {direction: pygame.transform.scale(image, (player_width, player_height))
                            for direction, image in player_images_on_maich.items()}
    elif on_shield:
        scaled_player_images = {direction: pygame.transform.scale(image, (player_width, player_height))
                            for direction, image in player_images_on_shiald.items()}
    else:
        scaled_player_images = {direction: pygame.transform.scale(image, (player_width, player_height))
                            for direction, image in player_images.items()}

    current_player_image = scaled_player_images["down"]
    player_map_x = scaled_map.get_width() // 2
    player_map_y = scaled_map.get_height() // 2
    camera_x = player_map_x - WIDTH // 2
    camera_y = player_map_y - HEIGHT // 2
    player_speed = 10
    # Таймеры для предотвращения повторного урона от элементов карты
    element_damage_cooldown = 500  # миллисекунды
    last_element_damage_time = 0
    player_hp = 100
    player_max_hp = 150

    # Основной игровой цикл
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

        player_map_x = max(0, min(player_map_x, scaled_map.get_width() - 1))
        player_map_y = max(0, min(player_map_y, scaled_map.get_height() - 1))
        camera_x = max(0, min(player_map_x - WIDTH // 2, scaled_map.get_width() - WIDTH))
        camera_y = max(0, min(player_map_y - HEIGHT // 2, scaled_map.get_height() - HEIGHT))
        player_screen_x = max(0, min(player_map_x - camera_x, WIDTH - player_width))
        player_screen_y = max(0, min(player_map_y - camera_y, HEIGHT - player_height))

        current_time = pygame.time.get_ticks()
        # Проверка столкновений с ентити
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
                    player_map_x += int(dx / dist * 70)
                    player_map_y += int(dy / dist * 70)

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