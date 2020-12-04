import pygame
import random

pygame.init()

# these define the colors used in the game
white = (255, 255, 255)
black = (0, 0, 0)
# grey = (128, 128, 128)
grey = (220, 220, 220)
red = (255, 0, 0)
green = (34, 204, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
purple = (166, 77, 255)
orange = (255, 162, 0)

# initializes the row and column variables to use when moving the arrows
row = 0
col = 0

# creates a list of random numbers to use as the computer's answers for the game; these will be used to compare to the
# user's input.
comp_answers = [random.randint(0, 5) for x in range(4)]

print(str(comp_answers))

# creates a list of list to hold all of the initial values for the board when the code starts running;
# the grey pegs not be visible until the codebreaker finishes a row
board = [[white, white, white, white, grey, grey, grey, grey],
         [white, white, white, white, grey, grey, grey, grey],
         [white, white, white, white, grey, grey, grey, grey],
         [white, white, white, white, grey, grey, grey, grey],
         [white, white, white, white, grey, grey, grey, grey],
         [white, white, white, white, grey, grey, grey, grey],
         [white, white, white, white, grey, grey, grey, grey],
         [white, white, white, white, grey, grey, grey, grey]]

codebreaker_colors = [red, green, blue, yellow, purple, orange]
codemaker_colors = [white, black, grey]

# sets up the size of the game board and the background color
game_display = pygame.display.set_mode((800, 650))
game_display.fill(grey)


def draw_board():
    """creates all of the circle, both for the codebreaker and codemaker"""
    # creates all of the main circles for play
    pygame.draw.circle(game_display, board[0][0], (100, 100), 25)
    pygame.draw.circle(game_display, board[0][1], (200, 100), 25)
    pygame.draw.circle(game_display, board[0][2], (300, 100), 25)
    pygame.draw.circle(game_display, board[0][3], (400, 100), 25)

    pygame.draw.circle(game_display, board[1][0], (100, 160), 25)
    pygame.draw.circle(game_display, board[1][1], (200, 160), 25)
    pygame.draw.circle(game_display, board[1][2], (300, 160), 25)
    pygame.draw.circle(game_display, board[1][3], (400, 160), 25)

    pygame.draw.circle(game_display, board[2][0], (100, 220), 25)
    pygame.draw.circle(game_display, board[2][1], (200, 220), 25)
    pygame.draw.circle(game_display, board[2][2], (300, 220), 25)
    pygame.draw.circle(game_display, board[2][3], (400, 220), 25)

    pygame.draw.circle(game_display, board[3][0], (100, 280), 25)
    pygame.draw.circle(game_display, board[3][1], (200, 280), 25)
    pygame.draw.circle(game_display, board[3][2], (400, 280), 25)
    pygame.draw.circle(game_display, board[3][3], (300, 280), 25)

    pygame.draw.circle(game_display, board[4][0], (100, 340), 25)
    pygame.draw.circle(game_display, board[4][1], (200, 340), 25)
    pygame.draw.circle(game_display, board[4][2], (300, 340), 25)
    pygame.draw.circle(game_display, board[4][3], (400, 340), 25)

    pygame.draw.circle(game_display, board[5][0], (100, 400), 25)
    pygame.draw.circle(game_display, board[5][1], (200, 400), 25)
    pygame.draw.circle(game_display, board[5][2], (300, 400), 25)
    pygame.draw.circle(game_display, board[5][3], (400, 400), 25)

    pygame.draw.circle(game_display, board[6][0], (100, 460), 25)
    pygame.draw.circle(game_display, board[6][1], (200, 460), 25)
    pygame.draw.circle(game_display, board[6][2], (300, 460), 25)
    pygame.draw.circle(game_display, board[6][3], (400, 460), 25)

    pygame.draw.circle(game_display, board[7][0], (100, 520), 25)
    pygame.draw.circle(game_display, board[7][1], (200, 520), 25)
    pygame.draw.circle(game_display, board[7][2], (300, 520), 25)
    pygame.draw.circle(game_display, board[7][3], (400, 520), 25)

    # creates the pegs to see if the guesses are correct or incorrect
    pygame.draw.circle(game_display, board[0][4], (600, 100), 10)
    pygame.draw.circle(game_display, board[0][5], (640, 100), 10)
    pygame.draw.circle(game_display, board[0][6], (680, 100), 10)
    pygame.draw.circle(game_display, board[0][7], (720, 100), 10)

    pygame.draw.circle(game_display, board[1][4], (600, 160), 10)
    pygame.draw.circle(game_display, board[1][5], (640, 160), 10)
    pygame.draw.circle(game_display, board[1][6], (680, 160), 10)
    pygame.draw.circle(game_display, board[1][7], (720, 160), 10)

    pygame.draw.circle(game_display, board[2][4], (600, 220), 10)
    pygame.draw.circle(game_display, board[2][5], (640, 220), 10)
    pygame.draw.circle(game_display, board[2][6], (680, 220), 10)
    pygame.draw.circle(game_display, board[2][7], (720, 220), 10)

    pygame.draw.circle(game_display, board[3][4], (600, 280), 10)
    pygame.draw.circle(game_display, board[3][5], (640, 280), 10)
    pygame.draw.circle(game_display, board[3][6], (680, 280), 10)
    pygame.draw.circle(game_display, board[3][7], (720, 280), 10)

    pygame.draw.circle(game_display, board[4][4], (600, 340), 10)
    pygame.draw.circle(game_display, board[4][5], (640, 340), 10)
    pygame.draw.circle(game_display, board[4][6], (680, 340), 10)
    pygame.draw.circle(game_display, board[4][7], (720, 340), 10)

    pygame.draw.circle(game_display, board[5][4], (600, 400), 10)
    pygame.draw.circle(game_display, board[5][5], (640, 400), 10)
    pygame.draw.circle(game_display, board[5][6], (680, 400), 10)
    pygame.draw.circle(game_display, board[5][7], (720, 400), 10)

    pygame.draw.circle(game_display, board[6][4], (600, 460), 10)
    pygame.draw.circle(game_display, board[6][5], (640, 460), 10)
    pygame.draw.circle(game_display, board[6][6], (680, 460), 10)
    pygame.draw.circle(game_display, board[6][7], (720, 460), 10)

    pygame.draw.circle(game_display, board[7][4], (600, 520), 10)
    pygame.draw.circle(game_display, board[7][5], (640, 520), 10)
    pygame.draw.circle(game_display, board[7][6], (680, 520), 10)
    pygame.draw.circle(game_display, board[7][7], (720, 520), 10)
    pygame.display.update()


draw_board()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                print("Up Arrow")
                # if the color is initially white, it assigns it to the first color in the codebreaker_colors list
                # and updates the board
                if board[col][row] is codemaker_colors[0]:
                    board[col][row] = codebreaker_colors[0]
                    draw_board()

                else:
                    cur_index = codebreaker_colors.index(board[col][row])
                    cur_index += 1
                    # this resets the index to 0 when you reach the end of the list to start over with the colors again
                    cur_index = cur_index % 6
                    board[col][row] = codebreaker_colors[cur_index]
                    draw_board()

            if event.key == pygame.K_DOWN:
                print("Down Arrow")
                if board[col][row] is codemaker_colors[0]:
                    board[col][row] = codebreaker_colors[0]
                    draw_board()
                else:
                    cur_index = codebreaker_colors.index(board[col][row])
                    cur_index -= 1
                    cur_inde = cur_index % 6
                    board[col][row] = codebreaker_colors[cur_index]
                    draw_board()

            if event.key == pygame.K_LEFT:
                print("Left Arrow")
                row -= 1
                row = row % 4

            if event.key == pygame.K_RIGHT:
                print("Right Arrow")
                row += 1
                row = row % 4

            if event.key == pygame.K_RETURN:
                print("Pressed Enter")

                def evaluation_inner(guess, fakeCode):

                    # Get the length n of the guess and the code.
                    assert (len(guess) == len(fakeCode))
                    n = len(guess)

                    # Determine the correct and incorrect positions.
                    correct_positions = [i for i in list(range(n)) if guess[i] == fakeCode[i]]
                    incorrect_positions = [i for i in list(range(n)) if guess[i] != fakeCode[i]]
                    num_correct = len(correct_positions)

                    # Reduce the guess and the fakeCode by removing the correct positions.
                    # Create the set values that are common between the two reduced lists.
                    reduced_guess = [guess[i] for i in incorrect_positions]
                    reduced_code = [fakeCode[i] for i in incorrect_positions]
                    reduced_set = set(reduced_guess) & set(reduced_guess)

                    # Determine the number of transposed values.
                    num_transposed = 0
                    for x in reduced_set:
                        num_transposed += min(reduced_guess.count(x), reduced_code.count(x))

                    return num_correct, num_transposed

    pygame.display.update()

