import pygame
import sys
import cv2
import numpy as np
from tkinter import messagebox
from vpython import box, canvas, vector, color, rate, radians

# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption('Menu Example')

# Define colors
cream = (255, 253, 208)
peach = (255, 218, 185)
dark_brown = (101, 67, 33)
black = (0, 0, 0)
white = (255, 255, 255)

# Set up fonts
cursive_font_large = pygame.font.SysFont('Comic Sans MS', 40)
cursive_font_medium = pygame.font.SysFont('Comic Sans MS', 30)
cursive_font_small = pygame.font.SysFont('Comic Sans MS', 20)
small_font = pygame.font.SysFont('Comic Sans MS', 20)

# Load videos
cap_main = cv2.VideoCapture(r"C:\Users\shyam\OneDrive\Desktop\Books and Notes\PYTHON\\1.mp4")
cap_yes_no = cv2.VideoCapture(r"C:\Users\shyam\OneDrive\Desktop\Books and Notes\PYTHON\\2.mp4")
cap_intro = cv2.VideoCapture(r"C:\Users\shyam\OneDrive\Desktop\Books and Notes\PYTHON\intro.mp4")  # Add this line

if not cap_main.isOpened():
    print("Error: Could not open main video.")
    sys.exit()
if not cap_yes_no.isOpened():
    print("Error: Could not open Yes/No video.")
    sys.exit()
if not cap_intro.isOpened():
    print("Error: Could not open introduction video.")
    sys.exit()

# Load background images
intro_background = pygame.image.load(r"C:\Users\shyam\OneDrive\Desktop\Books and Notes\PYTHON\background.jpeg")  # Replace with actual path
pyramid_background = pygame.image.load(r"C:\Users\shyam\OneDrive\Desktop\Books and Notes\PYTHON\background.jpeg")  # Replace with actual path

# Load sounds
menu_music = pygame.mixer.Sound(r"C:\Users\shyam\OneDrive\Desktop\Books and Notes\PYTHON\gizemli-piramit-210884.mp3")  # Replace with your actual audio file
menu_music.set_volume(0.5)
pygame.mixer.music.load(r"C:\Users\shyam\OneDrive\Desktop\Books and Notes\PYTHON\gizemli-piramit-210884.mp3")  # Replace with your actual audio file
pygame.mixer.music.set_volume(0.3)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = (x, y)
    surface.blit(textobj, textrect)

def draw_oval_button(surface, color, border_color, rect):
    pygame.draw.ellipse(surface, border_color, rect)
    pygame.draw.ellipse(surface, color, rect.inflate(-10, -10))

def draw_video_frame(cap):
    ret, frame = cap.read()
    if not ret:
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        ret, frame = cap.read()
    
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (width, height))
    frame = np.rot90(frame)
    frame = pygame.surfarray.make_surface(frame)
    window.blit(frame, (0, 0))

def main_menu():
    pygame.mixer.music.play(loops=-1)  # Play background music
    while True:
        draw_video_frame(cap_main)

        mx, my = pygame.mouse.get_pos()

        # Button dimensions and positions
        button_start = pygame.Rect(width // 2 - 100, height - 150, 200, 75)

        # Check for mouse click
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_start.collidepoint((mx, my)):
            if click:
                #pygame.mixer.music.stop()  # Stop background music
                welcome_screen()

        # Draw button
        draw_oval_button(window, peach, dark_brown, button_start)
        draw_text('Start', cursive_font_large, black, window, width // 2, height - 112)

        pygame.display.update()

def welcome_screen():
    while True:
        window.blit(intro_background, (0, 0))  # Draw background image
        draw_text('Welcome to the world of pyramids', cursive_font_large, black, window, width // 2, height // 2 - 100)

        mx, my = pygame.mouse.get_pos()

        # Button dimensions and positions
        button_intro = pygame.Rect(width // 2 - 150, height // 2 - 45, 290, 75)
        button_play = pygame.Rect(width // 2 - 100, height // 2 + 50, 200, 75)
        button_exit = pygame.Rect(width // 2 - 100, height // 2 + 150, 200, 75)

        # Check for mouse click
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_intro.collidepoint((mx, my)):
            if click:
                #pygame.mixer.music.stop()  # Stop background music
                introduction_screen()
        if button_play.collidepoint((mx, my)):
            if click:
                #pygame.mixer.music.stop()  # Stop background music
                yes_no_screen()  # Change to show the yes/no screen
        if button_exit.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        # Draw buttons
        draw_oval_button(window, peach, dark_brown, button_intro)
        draw_oval_button(window, peach, dark_brown, button_play)
        draw_oval_button(window, peach, dark_brown, button_exit)

        draw_text('Introduction', cursive_font_large, black, window, width // 2, height // 2 - 12)
        draw_text('Play', cursive_font_large, black, window, width // 2, height // 2 + 87)
        draw_text('Exit', cursive_font_large, black, window, width // 2, height // 2 + 187)

        pygame.display.update()

def introduction_screen():
    while True:
        draw_video_frame(cap_intro)  # Display the introduction video

       # draw_text('Introduction to the game...', cursive_font_large, black, window, width // 2, height // 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    welcome_screen()

        pygame.display.update()

def yes_no_screen():
    while True:
        draw_video_frame(cap_yes_no)

        mx, my = pygame.mouse.get_pos()

        # Button dimensions and positions
        button_yes = pygame.Rect(width // 2 - 100, height // 2 - 50, 200, 75)
        button_no = pygame.Rect(width // 2 - 100, height // 2 + 50, 200, 75)

        # Check for mouse click
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if button_yes.collidepoint((mx, my)):
            if click:
                pyramid_screen()
        if button_no.collidepoint((mx, my)):
            if click:
                welcome_screen()

        # Draw buttons
        draw_oval_button(window, peach, dark_brown, button_yes)
        draw_oval_button(window, peach, dark_brown, button_no)

        draw_text('Yes', cursive_font_large, black, window, width // 2, height // 2 - 12)
        draw_text('No', cursive_font_large, black, window, width // 2, height // 2 + 87)

        pygame.display.update()

def pyramid_screen():
    input_active = False
    user_input = ''

    while True:
        window.blit(pyramid_background, (0, 0))  # Draw background image
        draw_text("Let's start building pyramids !!", cursive_font_large, black, window, width // 2, height // 2 - 250)
        draw_text('Enter number of Cubes : ', cursive_font_medium, black, window, width // 2, height // 2 - 150)

        mx, my = pygame.mouse.get_pos()

        # Input box dimensions and position
        input_box = pygame.Rect(width // 2 - 100, height // 2 - 50, 200, 50)
        button_generate = pygame.Rect(width // 2 - 100, height // 2 + 50, 200, 75)
        button_exit = pygame.Rect(width // 2 - 100, height // 2 + 150, 200, 75)

        # Check for events
        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    input_active = True
                else:
                    input_active = False
                if event.button == 1:
                    click = True
            if event.type == pygame.KEYDOWN and input_active:
                if event.key == pygame.K_RETURN:
                    if user_input.isdigit():
                        num_cubes = int(user_input)
                        handle_pyramids(num_cubes)
                    else:
                        user_input = ''
                elif event.key == pygame.K_BACKSPACE:
                    user_input = user_input[:-1]
                else:
                    user_input += event.unicode

        if button_generate.collidepoint((mx, my)):
            if click:
                if user_input.isdigit():
                    num_cubes = int(user_input)
                    handle_pyramids(num_cubes)
                else:
                    user_input = ''

        if button_exit.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        # Draw input box and text
        pygame.draw.rect(window, white, input_box, 0)
        pygame.draw.rect(window, black, input_box, 2)

        text_surface = small_font.render(user_input, True, black)
        window.blit(text_surface, (input_box.x + 10, input_box.y + 10))
        input_box.w = max(200, text_surface.get_width() + 20)

        # Draw buttons
        draw_oval_button(window, peach, dark_brown, button_generate)
        draw_oval_button(window, peach, dark_brown, button_exit)

        draw_text('Generate Pyramids', cursive_font_small, black, window, width // 2, height // 2 + 87)
        draw_text('Exit', cursive_font_small, black, window, width // 2, height // 2 + 187)

        pygame.display.update()

# Function to calculate the sum of squares up to a given number
def sum_squares(num):
    return (num * (num + 1) * (2 * num + 1)) // 6

# Function to determine the highest pyramid that can be built with the given cubes
def high_pyramids(num_cubes):
    num = 1
    while sum_squares(num) <= num_cubes:
        num += 1
    sum_ = sum_squares(num - 1)
    if num - 1 == 1:
        return num_cubes - sum_, "False"
    else:
        return num_cubes - sum_, str(num - 1) + 'H'

# Function to determine the lowest pyramid that can be built with the given cubes
def low_pyramids(num_cubes):
    num = 1
    sum_ = 0
    while sum_ <= num_cubes:
        sum_ += num ** 2
        num += 2
    sum_ -= (num - 2) ** 2
    if num - 4 == 1:
        return num_cubes - sum_, "False"
    else:
        return num_cubes - sum_, str((num - 4) // 2 + 1) + 'L'

# Function to build pyramids from the given number of cubes
def build_pyramids(num_cubes):
    rem_cubes = num_cubes
    res = ''
    flag = ''
    while rem_cubes != 0:
        rem_cubes, op = high_pyramids(rem_cubes)
        res += op + ' '
        if rem_cubes == 0:
            break
        if op == "False" or rem_cubes == 7:
            flag = "Impossible"
            break
        rem_cubes, op = low_pyramids(rem_cubes)
        res += op + ' '
        if rem_cubes == 0:
            break
        if op == "False" or rem_cubes == 7:
            flag = "Impossible"
            break
    if rem_cubes == 0 and flag != "Impossible":
        return res.strip()
    else:
        return "Impossible!!"

def draw_pyramids(instructions):
    # Light blue background color
    light_blue_color = vector(173/255, 216/255, 230/255)
    
    scene = canvas(title="3D Pyramid Builder", width=800, height=600, background=light_blue_color)

    if instructions == "Impossible!!":
        messagebox.showerror("Error", "Impossible to build pyramids with the given cubes!")
        return

    x_start, y_start, z_start = -50, 0, 0  # Adjusted starting position
    cube_size = 1
    gap = 0.1  # Small gap between cubes
    opacity = 0.5
    spacing = 5  # Adjusted spacing between pyramids

    pyramids = []

    def draw_cube(x, y, z, size, color, opacity):
        return box(pos=vector(x, y, z), size=vector(size, size, size), color=color, opacity=opacity)

    for instruction in instructions.split():
        pyramid = []
        if instruction[-1] == 'H':
            size = int(instruction[:-1])
            for layer in range(size):
                layer_size = size - layer
                offset = (size - layer_size) * (cube_size + gap) / 2
                for i in range(layer_size):
                    for j in range(layer_size):
                        pyramid.append(draw_cube(x_start + offset + i * (cube_size + gap), 
                                                 y_start + layer * (cube_size + gap), 
                                                 z_start + offset + j * (cube_size + gap), cube_size, color.orange, opacity))
            pyramids.append(pyramid)
            x_start += size * (cube_size + gap) + cube_size + spacing  # Adjusted spacing
        elif instruction[-1] == 'L':
            size = int(instruction[:-1])
            num = size * 2 - 1
            for layer in range(size):
                offset = (size * 2 - 1 - num) * (cube_size + gap) / 2
                for i in range(num):
                    for j in range(num):
                        pyramid.append(draw_cube(x_start + offset + i * (cube_size + gap), 
                                                 y_start + layer * (cube_size + gap), 
                                                 z_start + offset + j * (cube_size + gap), cube_size, color.orange, opacity))
                num -= 2
            pyramids.append(pyramid)
            x_start += size * (cube_size + gap) + cube_size + spacing  # Adjusted spacing
    
    # Function to rotate the pyramids about their vertical axis
    def rotate_pyramids():
        while True:
            rate(15)
            for pyramid in pyramids:
                top_cube = pyramid[-1]
                center = top_cube.pos
                for cube in pyramid:
                    cube.rotate(angle=radians(5), axis=vector(0, 1, 0), origin=center)
    
    rotate_pyramids()

# Function to handle the pyramids generation and drawing
def handle_pyramids(num_cubes):
    instructions = build_pyramids(num_cubes)
    draw_pyramids(instructions)

if __name__ == "__main__":
    main_menu()
