import re
def format_input(raw):
    rows = raw.split("\n")
    return rows


def part1(rows):
    tot = 0
    for row in rows:
        game_num_start = row.index("Game ")
        game_num_end = row.index(":")
        game_num = int(row[game_num_start + len("Game "):game_num_end])
        combos = re.split(r',|;', row[game_num_end+1:])
        red_tot = 12
        blue_tot = 14
        green_tot = 13
        over = False
        for combo in combos:
            pair = combo.split(' ')
            color = pair[2]
            value = int(pair[1])
            if color == 'red' and value > red_tot:
                over = True
                break
            elif color == 'blue' and value > blue_tot:
                over = True
                break
            elif color == 'green' and value > green_tot:
                over = True
                break
        if not over:
            tot += game_num

    return tot
        



def part2(rows):
    tot = 0
    for row in rows:
        game_num_start = row.index("Game ")
        game_num_end = row.index(":")
        combos = re.split(r',|;', row[game_num_end+1:])
        red = 0
        blue = 0
        green = 0
        for combo in combos:
            pair = combo.split(' ')
            color = pair[2]
            value = int(pair[1])
            if color == 'red':
                red = max(red, value)
            elif color == 'blue':
                blue = max(blue, value)
            elif color == 'green':
                green = max(green, value)
        cubed = red*blue*green
        tot += cubed
    return tot


if __name__ == "__main__":
    raw = open("data/2.txt", "r").read()
    rows = format_input(raw)
    print(part1(rows))

    rows = format_input(raw)
    print(part2(rows))



    