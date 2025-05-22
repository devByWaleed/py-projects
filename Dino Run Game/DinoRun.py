# Importing libraries
import pygame
import os
import random

# Initializing pygame
pygame.init()

# Colors for window
white = (255, 255, 255)
black = (0, 0, 0)

# Setting screen size
screen_width = 1200
screen_height = 600

# For caption written on top
pygame.display.set_caption("Dino Game")

# For display screen
GameWindow = pygame.display.set_mode((screen_width, screen_height))

# Loading all images
running = [pygame.image.load(os.path.join("Assets/Dino", "DinoRun1.png")), pygame.image.load(os.path.join("Assets/Dino", "DinoRun2.png"))]
jumping = pygame.image.load(os.path.join("Assets/Dino", "DinoJump.png"))
Stop = pygame.image.load(os.path.join("Assets/Dino", "DinoStart.png"))
ducking = [pygame.image.load(os.path.join("Assets/Dino", "DinoDuck1.png")), pygame.image.load(os.path.join("Assets/Dino", "DinoDuck2.png"))]
small_cactus = [pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus1.png")), pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus2.png")), pygame.image.load(os.path.join("Assets/Cactus", "SmallCactus3.png"))]
large_cactus = [pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus1.png")), pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus2.png")), pygame.image.load(os.path.join("Assets/Cactus", "LargeCactus3.png"))]
bird = [pygame.image.load(os.path.join("Assets/Bird", "Bird1.png")), pygame.image.load(os.path.join("Assets/Bird", "Bird2.png"))]
track = pygame.image.load(os.path.join("Assets/Other", "Track.png"))
cloud = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))

# Dinosaur class to manage the player's character
class Dinasour:
    x_pos = 80
    y_pos = 310
    y_pos_duck = 340
    jump_velocity = 8.5

    def __init__(self):
        # Loading dinosaur images for different states
        self.duck_img = ducking
        self.run_img = running
        self.jump_img = jumping
        self.skee_img = Stop

        # Initializing dinosaur state
        self.dino_duck = False
        self.dino_run = True
        self.dino_jump = False
        self.dino_stop = False

        self.step_index = 0
        self.jump_vel = self.jump_velocity
        self.image = self.run_img[0]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos

    def update(self, user_input):
        # Update the state of the dinosaur based on user input
        if self.dino_duck:
            self.duck()
        if self.dino_run:
            self.run()
        if self.dino_jump:
            self.jump()
        if self.dino_stop:
            self.stop()

        # Reset step index for running and ducking animation
        if self.step_index >= 10:
            self.step_index = 0

        # Handling the key inputs for different states
        if user_input[pygame.K_UP] and not self.dino_jump:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = True
            self.dino_stop = False
        elif user_input[pygame.K_DOWN] and not self.dino_jump:
            self.dino_duck = True
            self.dino_run = False
            self.dino_jump = False
            self.dino_stop = False
        elif user_input[pygame.K_s]:
            self.dino_duck = False
            self.dino_run = False
            self.dino_jump = False
            self.dino_stop = True
        elif not (self.dino_jump or user_input[pygame.K_DOWN]):
            self.dino_duck = False
            self.dino_run = True
            self.dino_jump = False
            self.dino_stop = False

    # Methods to update the states of the dinosaur
    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos_duck
        self.step_index += 1

    def run(self):
        self.image = self.run_img[self.step_index // 5]
        self.dino_rect = self.image.get_rect()
        self.dino_rect.x = self.x_pos
        self.dino_rect.y = self.y_pos
        self.step_index += 1

    def jump(self):
        self.image = self.jump_img
        if self.dino_jump:
            self.dino_rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
        if self.jump_vel < -self.jump_velocity:
            self.dino_jump = False
            self.jump_vel = self.jump_velocity

    def stop(self):
        self.image = self.skee_img
        self.step_index = 0
        self.dino_stop = True

    def draw(self, GameWindow):
        # Draw the current image of the dinosaur on the game window
        GameWindow.blit(self.image, (self.dino_rect.x, self.dino_rect.y))

# Cloud class to handle clouds in the background
class Cloud:
    def __init__(self):
        self.x = screen_width + random.randint(600, 1000)
        self.y = random.randint(50, 100)
        self.image = cloud
        self.width = self.image.get_width()

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = screen_width + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, GameWindow):
        GameWindow.blit(self.image, (self.x, self.y))

# Obstacle class to manage all obstacles in the game
class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = screen_width

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, GameWindow):
        GameWindow.blit(self.image[self.type], self.rect)

# Classes for different types of obstacles
class SmallCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325

class LargeCactus(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300

class Bird(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, GameWindow):
        if self.index >= 9:
            self.index = 0
        GameWindow.blit(self.image[self.index // 5], self.rect)
        self.index += 1

# Main game loop
def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles
    run = True
    paused = False
    clock = pygame.time.Clock()
    player = Dinasour()
    cloud = Cloud()
    game_speed = 14
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0

    # Function to display the score
    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1
        
        text = font.render("Points: " + str(points), True, (0, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 40)
        GameWindow.blit(text, text_rect)

    # Function to display the background track
    def background():
        global x_pos_bg, y_pos_bg
        image_width = track.get_width()
        GameWindow.blit(track, (x_pos_bg, y_pos_bg))
        GameWindow.blit(track, (image_width + x_pos_bg, y_pos_bg))
        if x_pos_bg <= -image_width:
            GameWindow.blit(track, (image_width + x_pos_bg, y_pos_bg))
            x_pos_bg = 0
        x_pos_bg -= game_speed

    # Game loop
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = not paused
            # elif event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_q:
            #         run = False
        
        GameWindow.fill(white)
        user_input = pygame.key.get_pressed()

        if paused:
            # Display pause message
            font = pygame.font.Font('freesansbold.ttf', 30)
            text = font.render("Press P to Resume", True, (0, 0, 0))
            textRect = text.get_rect()
            textRect.center = (screen_width // 2, screen_height // 2)
            GameWindow.blit(text, textRect)
            pygame.display.update()
            continue  # Skip the rest of the loop when paused

        # Update and draw the player
        player.update(user_input)
        player.draw(GameWindow)

        # Generate obstacles
        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallCactus(small_cactus))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeCactus(large_cactus))
            elif random.randint(0, 2) == 2:
                obstacles.append(Bird(bird))

        # Update and draw obstacles
        for obstacle in obstacles:
            obstacle.draw(GameWindow)
            obstacle.update()
            if player.dino_rect.colliderect(obstacle.rect):
                pygame.time.delay(2000)
                death_count += 1
                menu(death_count)

        # Update the background, clouds, and score
        background()
        cloud.draw(GameWindow)
        cloud.update()
        score()

        clock.tick(30)
        pygame.display.update()

# Menu function to display the start and restart screen
def menu(death_count):
    global points
    run = True
    while run:
        GameWindow.fill(white)
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("Press any Key to Start", True, (0, 0, 0))
        else:
            text = font.render("Press any Key to Restart", True, (0, 0, 0))
            score = font.render("Your Score: " + str(points), True, (0, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (screen_width // 2, screen_height // 2 + 50)
            GameWindow.blit(score, scoreRect)

        textRect = text.get_rect()
        textRect.center = (screen_width // 2, screen_height // 2)
        GameWindow.blit(text, textRect)
        GameWindow.blit(running[0], (screen_width // 2 - 20, screen_height // 2 - 140))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False      
            elif event.type == pygame.KEYDOWN:
                main()

menu(death_count=0)