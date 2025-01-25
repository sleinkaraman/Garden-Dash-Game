import random
from pgzero.builtins import Actor, keyboard, keys, music, mouse

WIDTH = 800
HEIGHT = 600

game_started = False
game_over = False
score = 0
fruit_timer = 0
music_playing = True

start_button = {"text": "Oyuna Başla", "pos": (WIDTH // 2, HEIGHT // 2), "active": True}
exit_button = {"text": "Çıkış", "pos": (WIDTH // 2, HEIGHT // 2 + 50), "active": True}
music_button = {"text": "Müziği Aç/Kapa", "pos": (WIDTH // 2, HEIGHT // 2 + 100), "active": True}
retry_button = {"text": "Yeniden Başla", "pos": (WIDTH // 2, HEIGHT // 2 + 150), "active": False}

game_title = "Garden Dash"

def is_position_valid(pos, other_actors, min_distance):
    for actor in other_actors:
        distance = ((pos[0] - actor.pos[0]) ** 2 + (pos[1] - actor.pos[1]) ** 2) ** 0.5
        if distance < min_distance:
            return False
    return True

class Hero:
    def __init__(self, pos):
        self.pos = pos
        self.speed = 5
        self.images = {
            'down': [f"{i}" for i in range(1, 5)],
            'up': [f"{i}" for i in range(5, 9)],
            'left': [f"{i}" for i in range(9, 13)],
            'right': [f"{i}" for i in range(13, 17)]
        }
        self.direction = 'down'
        self.frame = 0
        self.actor = Actor(self.images[self.direction][self.frame], pos=pos)
        self.actor.scale = 0.5
        self.frame_timer = 0

    def move(self, dx, dy):
        self.pos = (self.pos[0] + dx * self.speed, self.pos[1] + dy * self.speed)
        if dx > 0:
            self.direction = 'right'
        elif dx < 0:
            self.direction = 'left'
        elif dy < 0:
            self.direction = 'up'
        elif dy > 0:
            self.direction = 'down'
        if dx != 0 or dy != 0:
            self.frame_timer += 1
            if self.frame_timer > 10:
                self.frame = (self.frame + 1) % len(self.images[self.direction])
                self.actor.image = self.images[self.direction][self.frame]
                self.frame_timer = 0
        self.actor.pos = self.pos

    def draw(self):
        self.actor.draw()

class Dog:
    def __init__(self, pos):
        self.pos = pos
        self.speed = 3
        self.images = {
            'down': [f"d{i}" for i in range(1, 5)],
            'left': [f"d{i}" for i in range(5, 9)],
            'right': [f"d{i}" for i in range(9, 13)],
            'up': [f"d{i}" for i in range(13, 17)]
        }
        self.direction = random.choice(['right', 'left', 'up', 'down'])
        self.frame = 0
        self.actor = Actor(self.images[self.direction][self.frame], pos=pos)
        self.actor.scale = 3
        self.frame_timer = 0

    def move(self):
        if self.direction == 'right':
            self.pos = (self.pos[0] + self.speed, self.pos[1])
        elif self.direction == 'left':
            self.pos = (self.pos[0] - self.speed, self.pos[1])
        elif self.direction == 'up':
            self.pos = (self.pos[0], self.pos[1] - self.speed)
        elif self.direction == 'down':
            self.pos = (self.pos[0], self.pos[1] + self.speed)
        if self.pos[0] < 0 or self.pos[0] > WIDTH or self.pos[1] < 0 or self.pos[1] > HEIGHT:
            self.direction = random.choice(['right', 'left', 'up', 'down'])
        self.frame_timer += 1
        if self.frame_timer > 10:
            self.frame = (self.frame + 1) % len(self.images[self.direction])
            self.actor.image = self.images[self.direction][self.frame]
            self.frame_timer = 0
        self.actor.pos = self.pos

    def draw(self):
        self.actor.draw()

class Fruit:
    def __init__(self):
        self.pos = (random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50))
        self.images = ['apple', 'grape', 'banana', 'cherry', 'strawberry']
        self.image = random.choice(self.images)
        self.actor = Actor(self.image, pos=self.pos)
        self.actor.scale = 0.15

    def draw(self):
        self.actor.draw()

hero = None
dogs = []
fruits = []

def start_game():
    global game_started, game_over, score, hero, dogs, fruits
    game_started = True
    game_over = False
    score = 0
    fruits.clear()
    hero_pos = (WIDTH // 2, HEIGHT // 2)
    dogs_positions = []
    hero = Hero(hero_pos)
    for _ in range(2):
        while True:
            dog_pos = (random.randint(100, WIDTH - 100), random.randint(100, HEIGHT - 100))
            if is_position_valid(dog_pos, [hero], 100):
                dogs_positions.append(dog_pos)
                break
    dogs[:] = [Dog(pos) for pos in dogs_positions]

def update():
    global game_over, score, fruit_timer
    if not game_started or game_over:
        return
    if keyboard.left:
        hero.move(-1, 0)
    elif keyboard.right:
        hero.move(1, 0)
    elif keyboard.up:
        hero.move(0, -1)
    elif keyboard.down:
        hero.move(0, 1)
    for dog in dogs:
        dog.move()
    for dog in dogs:
        if hero.actor.colliderect(dog.actor):
            game_over = True
            retry_button["active"] = True
            exit_button["active"] = True
    for fruit in fruits[:]:
        if hero.actor.colliderect(fruit.actor):
            score += 10
            fruits.remove(fruit)
    fruit_timer += 1
    if fruit_timer > 80:
        fruit_timer = 0
        if len(fruits) < 5:
            fruits.append(Fruit())

def draw_button(button):
    color = "yellow" if button["active"] else "white"
    screen.draw.text(button["text"], center=button["pos"], fontsize=40, color=color)

def draw():
    screen.clear()
    screen.blit("garden", (0, 0))
    screen.draw.text(game_title, center=(WIDTH // 2, 50), fontsize=60, color="white")
    if not game_started:
        draw_button(start_button)
        draw_button(exit_button)
        draw_button(music_button)
        return
    if game_over:
        screen.draw.text("Game Over", center=(WIDTH // 2, HEIGHT // 3), fontsize=80, color="red")
        screen.draw.text(f"Skor: {score}", center=(WIDTH // 2, HEIGHT // 2), fontsize=50, color="white")
        draw_button(retry_button)
        draw_button(exit_button)
        draw_button(music_button)
        return
    hero.draw()
    for dog in dogs:
        dog.draw()
    for fruit in fruits:
        fruit.draw()
    screen.draw.text(f"Skor: {score}", topleft=(10, 10), fontsize=40, color="white")

def on_mouse_down(pos):
    global game_started, game_over, music_playing
    if not game_started:
        if start_button["active"] and is_mouse_over_button(pos, start_button):
            start_game()
        elif exit_button["active"] and is_mouse_over_button(pos, exit_button):
            exit()
        elif music_button["active"] and is_mouse_over_button(pos, music_button):
            if music_playing:
                music.stop()
                music_playing = False
            else:
                music.play('background_music')
                music_playing = True
    if game_over:
        if retry_button["active"] and is_mouse_over_button(pos, retry_button):
            start_game()
        elif exit_button["active"] and is_mouse_over_button(pos, exit_button):
            exit()
        elif music_button["active"] and is_mouse_over_button(pos, music_button):
            if music_playing:
                music.stop()
                music_playing = False
            else:
                music.play('background_music')
                music_playing = True

def is_mouse_over_button(pos, button):
    x, y = button["pos"]
    text_width = len(button["text"]) * 20
    text_height = 40
    return (x - text_width // 2 < pos[0] < x + text_width // 2) and (y - text_height // 2 < pos[1] < y + text_height // 2)

if __name__ == "__main__":
    import pgzrun
    music.play('background_music')
    pgzrun.go()