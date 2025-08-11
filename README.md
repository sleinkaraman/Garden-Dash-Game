## Garden Dash

### Garden Dash is a fun 2D game developed using Python and the Pygame Zero library. The player tries to collect fruits in a garden while avoiding dogs. Each collected fruit earns points, but if you get caught by the dogs, the game ends.
---

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/sizin-kullanici-adiniz/GardenDash.git
    ```

2. Navigate to the project directory:

    ```bash
    cd GardenDash
    ```

3. Install the required dependencies:

    ```bash
    pip install pgzero
    ```

4. Start the game:

    ```bash
    python main.py
    ```

---

## How to Play?

### tarting the Game
Click the "Start Game" button in the main menu to begin.

### Controls

- **Move Up**: Up Arrow Key
- **Move Down**: Down Arrow Key
- **Move Righ:**: Right Arrow Key
- **Move Left**: Left Arrow Key

### Objective
Collect randomly appearing fruits in the garden to earn points. Keep avoiding the dogs to continue playing.

### Game Over
The game ends if you get caught by a dog. You can restart the game by clicking the "Restart" button or exit by clicking the "Exit" button.


---

## Game Features

- **Toggle Music**: Control background music with the "Toggle Music" button on the main menu or game over screen.
- **Scoring System**: Scoring System: Each collected fruit gives 10 points. Try to keep your score high!
- **Difficulty**: Dogs move randomly and try to catch the player. Plan your strategy well!

---

## Code Structure

- `main.py`: The main file of the game containing all game logic and controls.
- **Hero Class**: Represents the player character. Manages movement and animations.
- **Dog Class**: KRepresents the dogs. They move randomly and try to approach the player.
- **Fruit Class**: Represents collectible fruits. They appear at random locations.
---

## Core Functions

- `start_game()`: Starts the game and resets all variables to their initial state.
- `update()`: The main game update loop. Handles character movement, collision detection, and scoring.
- `draw()`: Renders the game graphics on the screen. Manages the menu, game field, and game over screens.
- `on_mouse_down()`: Handles mouse clicks. Checks button click events.

---

