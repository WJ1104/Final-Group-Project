import pygame
from sudoku_generator import generate_sudoku
from board import Board


pygame.init()

def print_board(board):
    """Print the Sudoku board in a nice format"""
    if not board:
        print("No board to display")
        return
    
    for i, row in enumerate(board):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        row_str = ""
        for j, cell in enumerate(row):
            if j % 3 == 0 and j != 0:
                row_str += "| "
            row_str += str(cell if cell != 0 else ".") + " "
        print(row_str)


def draw_button(screen, text, x, y, w, h, color, font):
    pygame.draw.rect(screen, color, (x, y, w, h))
    label = font.render(text, True, (0, 0, 0))
    screen.blit(label, (x + w//2 - label.get_width()//2, y + h//2 - label.get_height()//2))


def start_menu(screen, menu_background):
    font = pygame.font.Font(None, 50)
    small_font = pygame.font.Font(None, 40)

    while True:
        screen.blit(menu_background, (0, 0))
        title = font.render("Sudoku", True, (0, 0, 0))
        screen.blit(title, (300 - title.get_width() //2, 80))


        draw_button(screen, "Easy", 200, 200, 200, 60, (200, 200, 200), small_font)
        draw_button(screen, "Medium", 200, 300, 200, 60, (200, 200, 200), small_font)
        draw_button(screen, "Hard", 200, 400, 200, 60, (200, 200, 200), small_font)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos

                if 200 <= x <= 400 and 200 <= y <= 260:
                    return 30
                if 200 <= x <= 400 and 300 <= y <= 360:
                    return 40
                if 200 <= x <= 400 and 400 <= y <= 460:
                    return 50


def play_game(screen, removed_cells):
    board_list = generate_sudoku(9, removed_cells)
    board = Board(540, 540, screen, removed_cells, board_list=board_list)

    running = True
    key = None

    back_rect = pygame.Rect(500, 10, 80, 30)
    font = pygame.font.Font(None, 20)

    while running:
        screen.fill((255, 255, 255))
        board.draw()


        font = pygame.font.Font(None, 30)
        text = font.render("Back", True, (0, 0, 0))
        screen.blit(text, (back_rect.x, back_rect.y))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if back_rect.collidepoint(x, y):
                    return
                clicked = board.click(x, y)
                if clicked:
                    row, col = clicked
                    board.select(row, col)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                elif event.key == pygame.K_2:
                    key = 2
                elif event.key == pygame.K_3:
                    key = 3
                elif event.key == pygame.K_4:
                    key = 4
                elif event.key == pygame.K_5:
                    key = 5
                elif event.key == pygame.K_6:
                    key = 6
                elif event.key == pygame.K_7:
                    key = 7
                elif event.key == pygame.K_8:
                    key = 8
                elif event.key == pygame.K_9:
                    key = 9
                elif event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                    board.clear()
                    key = None
                    continue
                elif event.key == pygame.K_RETURN:
                    if board.selected and key:
                        row, col = board.selected
                        board.place_number(key)
                        key = None

        if board.selected and key:
            board.sketch(key)

        if board.is_full():
            if board.check_board():  #correct board
                font = pygame.font.Font(None, 60)
                text = font.render("You Win!", True, (0, 128, 9))
                screen.blit(text, (300 - text.get_width() // 2, 300 - text.get_height() // 2))
                pygame.display.update()
                pygame.time.delay(5000)
                running = False
            else:  # wrong board
                font = pygame.font.Font(None, 60)
                text = font.render("Incorrect!", True, (255, 0, 0))
                screen.blit(text, (300 - text.get_width() // 2, 300 - text.get_height() // 2))
                pygame.display.update()
                pygame.time.delay(5000)
                return

def main():
    pygame.init()

    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Sudoku")

    menu_background = pygame.image.load("sudoku_image.jpg")
    menu_background = pygame.transform.scale(menu_background, (600, 600))

    running_app = True
    while running_app:
        removed = start_menu(screen, menu_background)
        if removed is None:
            break
        play_game(screen, removed)
    pygame.quit()

    print("=" * 40)
    print("Welcome to Sudoku!")
    print("=" * 40)
    print("\nThis is a Sudoku project template.")
    print("The core classes (Board, Cell) need to be implemented.")
    print("\nGenerating a sample 9x9 Sudoku puzzle with 30 removed cells...")
    print()
    
    try:
        board = generate_sudoku(9, 30)
        print("Generated Sudoku Board:")
        print_board(board)
        print("\nNote: '.' represents empty cells")
    except Exception as e:
        print(f"Error generating Sudoku: {e}")
        print("\nThe sudoku_generator.py has stub methods that need to be implemented:")
        print("- get_board()")
        print("- valid_in_row(), valid_in_col(), valid_in_box()")
        print("- is_valid()")
        print("- fill_box(), fill_diagonal()")
        print("- remove_cells()")



if __name__ == "__main__":
    main()
