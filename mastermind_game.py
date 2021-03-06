import pygame
import random

pygame.init()

# defines the colors used in the game
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

# creates the font and statements that print when a game is won or lost
font = pygame.font.SysFont(None, 24)
game_won = font.render("You Won! You're a Mastermind!!!", True, green)
game_lost = font.render("Game Over, You Lost.", True, red)
pygame.display.set_caption("Mastermind")

# initializes the row and column variables to use when moving the arrows
row = 0
col = 0

# lists that hold the colors for the different players
codebreaker_colors = [red, green, blue, yellow, purple, orange]
codebreaker_str = ["red", "green", "blue", "yellow", "purple", "orange"]
codemaker_colors = [white, black, grey]

# creates a list of random numbers to use as the computer's answers for the game; these will be used to compare to the
# user's input.
print('\n' "The correct code for testing purposes is:")
comp_answers = [random.randint(0, 5) for x in range(4)]
for color_index in comp_answers:
    print(codebreaker_str[color_index], end=" ")
print('\n')

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

# sets up the size of the game board and the background color
game_display = pygame.display.set_mode((800, 650))
game_display.fill(grey)


def my_guess(guess, comp_answers):
    """Encompasses the algorithm of the program. This function compares how many correct guesses the user enter and how
    many transposed answers there are. """

    # Get the length n of the guess and the computer answers.
    assert (len(guess) == len(comp_answers))
    n = len(guess)

    # assigns the variable to count the correct color/location pairs and lists to hold the values that aren't
    num_correct = 0
    reduced_guess = []
    reduced_code = []

    # Determines the correct and incorrect positions.
    for i in range(n):
        if guess[i] == comp_answers[i]:
            num_correct += 1
        else:
            reduced_guess.append(guess[i])
            reduced_code.append(comp_answers[i])

    # Determine the number of transposed values.
    num_transposed = 0
    for i in range(len(reduced_guess)):
        for j in range(len(reduced_code)):
            if reduced_guess[i] == reduced_code[j]:
                num_transposed += 1
                # needed to remove the value compared so there are no repeats
                reduced_code.pop(j)
                break

    return num_correct, num_transposed


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
    pygame.draw.circle(game_display, board[3][2], (300, 280), 25)
    pygame.draw.circle(game_display, board[3][3], (400, 280), 25)

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

        # these sections handle all of the key movements the player makes
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
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
                # if the color is initially white, it assigns it to the first color in the codebreaker_colors list
                # and updates the board
                if board[col][row] is codemaker_colors[0]:
                    board[col][row] = codebreaker_colors[0]
                    draw_board()
                else:
                    cur_index = codebreaker_colors.index(board[col][row])
                    cur_index -= 1
                    cur_index = cur_index % 6
                    board[col][row] = codebreaker_colors[cur_index]
                    draw_board()

            if event.key == pygame.K_LEFT:
                # shifts the selection one to the left
                row -= 1
                row = row % 4

            if event.key == pygame.K_RIGHT:
                # shifts the selection one to the right
                row += 1
                row = row % 4

            if event.key == pygame.K_RETURN:
                #print("Pressed Enter")
                # list holds the current guesses for a column after the user presses enter
                guess = []
                for guess_index in range(4):
                    guess.append(codebreaker_colors.index(board[col][guess_index]))
                # assigns the values returned by the function
                nc, nt = my_guess(guess, comp_answers)
                #print(nc, nt)

                # shows the pegs to be either black or white if the guess is correct or transposed
                row = 4
                for correct in range(nc):
                    # black pegs
                    board[col][row] = codemaker_colors[1]
                    row += 1

                for transposed in range(nt):
                    # white pegs
                    board[col][row] = codemaker_colors[0]
                    row += 1
                # redraws the board and moves down a row
                draw_board()
                col += 1
                row = 0

                # checks for when all of the pegs are all black, if they are the game is won
                if nc == 4:
                    game_display.blit(game_won, (20, 600))
                    pygame.display.update()
                    pygame.time.wait(3000)
                    pygame.quit()

                # if the player doesn't guess correctly by the last line of the board, the game is over
                elif col >= 8:
                    game_display.blit(game_lost, (20, 600))
                    pygame.display.update()
                    pygame.time.wait(3000)
                    pygame.quit()

    pygame.display.update()

