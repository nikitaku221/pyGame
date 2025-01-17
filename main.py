import pygame
import os
import sqlite3

from script.menu import game_menu

pygame.init()

# Основные переменные
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Авторизация и регистрация")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Загрузка изображений
background = pygame.image.load("img/menu_background.png")
login_button_image = pygame.image.load("img/login_button.png")
register_button_image = pygame.image.load("img/register_button.png")
confirm_button_image = pygame.image.load("img/confirm_button.png")
back_button_image = pygame.image.load("img/back_button.png")

# Настройка базы данных
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL
                      )''')
    conn.commit()
    conn.close()

def register_user(username, password):
    try:
        conn = sqlite3.connect("users.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        conn.close()
        return True
    except sqlite3.IntegrityError:
        return False

def authenticate_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

# Масштабируемые элементы
def resize_ui_elements():
    """Функция для перерасчета размеров и координат кнопок."""
    global login_button_rect, register_button_rect, scaled_login_button, scaled_register_button
    global confirm_button_rect, back_button_rect, scaled_confirm_button, scaled_back_button
    global input_box_username, input_box_password
    global WIDTH, HEIGHT

    button_width = WIDTH // 4  # Ширина кнопки зависит от ширины окна
    button_height = HEIGHT // 10  # Высота кнопки зависит от высоты окна

    # Центрируем кнопки, но смещаем их влево от центра
    offset_x = WIDTH // 4  # Смещение кнопок влево
    login_button_rect = pygame.Rect(offset_x - button_width // 2, HEIGHT // 2 - button_height - 10, button_width, button_height)
    register_button_rect = pygame.Rect(offset_x - button_width // 2, HEIGHT // 2 + 10, button_width, button_height)

    confirm_button_rect = pygame.Rect(offset_x - button_width // 2, HEIGHT // 2 + 50, button_width, button_height)
    back_button_rect = pygame.Rect(20, HEIGHT - button_height - 20, button_width // 2, button_height // 2)

    scaled_login_button = pygame.transform.scale(login_button_image, (button_width, button_height))
    scaled_register_button = pygame.transform.scale(register_button_image, (button_width, button_height))
    scaled_confirm_button = pygame.transform.scale(confirm_button_image, (button_width, button_height))
    scaled_back_button = pygame.transform.scale(back_button_image, (button_width // 2, button_height // 2))

    # Поля ввода
    input_box_width = WIDTH // 3
    input_box_height = HEIGHT // 15
    input_box_username = pygame.Rect(offset_x - input_box_width // 2, HEIGHT // 2 - input_box_height - 50, input_box_width, input_box_height)
    input_box_password = pygame.Rect(offset_x - input_box_width // 2, HEIGHT // 2, input_box_width, input_box_height)

def draw_background():
    """Масштабируем и рисуем фон."""
    scaled_background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    screen.blit(scaled_background, (0, 0))

def draw_text(text, position):
    """Отрисовка текста."""
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, BLACK)
    screen.blit(text_surface, position)

def login_screen():
    """Экран авторизации."""
    global input_box_username, input_box_password
    global WIDTH, HEIGHT, screen
    username = ""
    password = ""
    input_active = None
    message = ""

    running = True
    while running:
        draw_background()
        draw_text("Авторизация", (WIDTH // 4, 50))

        # Поля ввода
        pygame.draw.rect(screen, WHITE, input_box_username)
        pygame.draw.rect(screen, WHITE, input_box_password)
        pygame.draw.rect(screen, BLACK, input_box_username, 2)
        pygame.draw.rect(screen, BLACK, input_box_password, 2)

        draw_text("Имя пользователя:", (input_box_username.x, input_box_username.y - 30))
        draw_text(username, (input_box_username.x + 5, input_box_username.y + 5))
        draw_text("Пароль:", (input_box_password.x, input_box_password.y - 30))
        draw_text("*" * len(password), (input_box_password.x + 5, input_box_password.y + 5))

        draw_text(message, (WIDTH // 4, HEIGHT // 2 + 100))

        screen.blit(scaled_confirm_button, confirm_button_rect)
        screen.blit(scaled_back_button, back_button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
                resize_ui_elements()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box_username.collidepoint(event.pos):
                    input_active = "username"
                elif input_box_password.collidepoint(event.pos):
                    input_active = "password"
                else:
                    input_active = None

                if confirm_button_rect.collidepoint(event.pos):
                    if authenticate_user(username, password):
                        game_menu(screen, WIDTH, HEIGHT)
                    else:
                        message = "Неверные данные!"
                elif back_button_rect.collidepoint(event.pos):
                    running = False

            elif event.type == pygame.KEYDOWN:
                if input_active == "username":
                    if event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode
                elif input_active == "password":
                    if event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode

        pygame.display.flip()

def register_screen():
    """Экран регистрации."""
    global input_box_username, input_box_password
    global WIDTH, HEIGHT, screen
    username = ""
    password = ""
    input_active = None
    message = ""

    running = True
    while running:
        draw_background()
        draw_text("Регистрация", (WIDTH // 4, 50))

        # Поля ввода
        pygame.draw.rect(screen, WHITE, input_box_username)
        pygame.draw.rect(screen, WHITE, input_box_password)
        pygame.draw.rect(screen, BLACK, input_box_username, 2)
        pygame.draw.rect(screen, BLACK, input_box_password, 2)

        draw_text("Имя пользователя:", (input_box_username.x, input_box_username.y - 30))
        draw_text(username, (input_box_username.x + 5, input_box_username.y + 5))
        draw_text("Пароль:", (input_box_password.x, input_box_password.y - 30))
        draw_text("*" * len(password), (input_box_password.x + 5, input_box_password.y + 5))

        draw_text(message, (WIDTH // 4, HEIGHT // 2 + 100))

        screen.blit(scaled_confirm_button, confirm_button_rect)
        screen.blit(scaled_back_button, back_button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
                resize_ui_elements()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box_username.collidepoint(event.pos):
                    input_active = "username"
                elif input_box_password.collidepoint(event.pos):
                    input_active = "password"
                else:
                    input_active = None

                if confirm_button_rect.collidepoint(event.pos):
                    if register_user(username, password):
                        message = "Регистрация успешна!"
                    else:
                        message = "Пользователь уже существует!"
                elif back_button_rect.collidepoint(event.pos):
                    running = False

            elif event.type == pygame.KEYDOWN:
                if input_active == "username":
                    if event.key == pygame.K_BACKSPACE:
                        username = username[:-1]
                    else:
                        username += event.unicode
                elif input_active == "password":
                    if event.key == pygame.K_BACKSPACE:
                        password = password[:-1]
                    else:
                        password += event.unicode

        pygame.display.flip()

def main_menu():
    """Главное меню."""
    global WIDTH, HEIGHT, screen
    running = True
    while running:
        draw_background()
        screen.blit(scaled_login_button, login_button_rect)
        screen.blit(scaled_register_button, register_button_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                WIDTH, HEIGHT = event.w, event.h
                screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
                resize_ui_elements()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if login_button_rect.collidepoint(event.pos):
                        login_screen()
                    elif register_button_rect.collidepoint(event.pos):
                        register_screen()

        pygame.display.flip()

if __name__ == "__main__":
    init_db()
    resize_ui_elements()
    main_menu()
    pygame.quit()
