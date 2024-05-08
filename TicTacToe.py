import random

player_grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]


def check_sum(row=-1, col=-1, diag=-1, who=1):
    if row > -1:
        to_sum = 0
        for num in player_grid[row]:
            if num == who:
                to_sum += 1
            elif num != 0:
                to_sum -= 1
        return to_sum
    elif col > -1:
        count = 0
        for item in player_grid:
            if item[col] == who:
                count += 1
            elif item[col] != 0:
                count -= 1

        return count
    else:
        if diag == 0:
            num = 0
            count = 0
            for forw in player_grid:
                if forw[num] == who:
                    count += 1
                elif forw[num] != 0:
                    count -= 1
                num += 1
            return count
        elif diag == 1:
            num = 2
            count = 0
            for backw in player_grid:
                if backw[num] == who:
                    count += 1
                elif backw[num] != 0:
                    count -= 1
                num -= 1
            return count


def check_two(side=1):
    for x_cord in range(3):
        if check_sum(row=x_cord, who=side) == 2:
            return f'row{x_cord}'
        if check_sum(col=x_cord, who=side) == 2:
            return f'col{x_cord}'
    if check_sum(diag=0, who=side) == 2:
        return 'dia0'
    if check_sum(diag=1, who=side) == 2:
        return 'dia1'
    return 'non0'


def check_win(this):
    for x_cord in range(3):
        if check_sum(row=x_cord, who=this) == 3:
            return True
        elif check_sum(col=x_cord, who=this) == 3:
            return True
    if check_sum(diag=0, who=this) == 3:
        return True
    elif check_sum(diag=1, who=this) == 3:
        return True
    else:
        tie = True
        for x_row in player_grid:
            for val in x_row:
                if val == 0:
                    tie = False
        if tie:
            print("Game ended in a tie.")
            input("Press any key to exit.")
            exit()
        return tie


def get_rand_empty():
    while True:
        x_cord = random.randint(0, 2)
        y_cord = random.randint(0, 2)
        if player_grid[x_cord][y_cord] == 0:
            return [x_cord, y_cord]
        continue


def is_empty(x_cord, y_cord):
    if player_grid[x_cord][y_cord] == 0:
        return True
    else:
        return False


def get_cord(place):
    num = int(place[3])
    conf = place[:-1]
    if conf == "row":
        for y_cord in range(3):
            if player_grid[num][y_cord] == 0:
                return [num, y_cord]
    elif conf == "col":
        for x_cord in range(3):
            if player_grid[x_cord][num] == 0:
                return [x_cord, num]
    elif conf == "dia":
        if num == 0:
            y_cord = 0
            for x_cord in range(3):
                if player_grid[x_cord][y_cord] == 0:
                    return [x_cord, y_cord]
                y_cord += 1
        if num == 1:
            y_cord = 2
            for x_cord in range(3):
                if player_grid[x_cord][y_cord] == 0:
                    return [x_cord, y_cord]
                y_cord -= 1
    else:
        return [-1, -1]


def ai_move():
    cord1 = get_cord(check_two(2))
    if cord1[0] > -1:
        player_grid[cord1[0]][cord1[1]] = 2
    else:
        cord2 = get_cord(check_two())
        if cord2[0] > -1:
            player_grid[cord2[0]][cord2[1]] = 2
        else:
            place = get_rand_empty()
            player_grid[place[0]][place[1]] = 2


def print_grid():
    print("     Y  Y  Y ")
    print("")
    for x_cord in range(3):
        line = "X   "
        for y_cord in range(3):
            if player_grid[x_cord][y_cord] == 0:
                line += " . "
            elif player_grid[x_cord][y_cord] == 1:
                line += " X "
            else:
                line += " O "
        print(line)


if random.randint(0, 1) == 0:
    print("AI has been randomly chosen to go first.")
    ai_move()
print_grid()

while True:
    x = int(input("Please choose an x coordinate to place your mark: ")) - 1
    y = int(input("Please choose a y coordinate to place your mark: ")) - 1
    if not is_empty(x, y):
        print("That place is already marked.")
        continue
    player_grid[x][y] = 1
    print_grid()
    if check_win(1):
        print("You won!")
        input("Press any key to exit.")
        break
    input("Press enter for the AI to make it's move")
    ai_move()
    print_grid()
    if check_win(2):
        print("You lost.")
        input("Press any key to exit.")
        break
