import re
def format_input(raw):
    rows = raw.split("\n")
    return rows


def part1(rows):
    rows = list(rows)
    # print(len(rows))
    # print(len(rows[0]))
    tot = 0
    DIRECTIONS = [[0, 1],[1,0],[0,-1],[-1,0],[-1,-1],[-1,1],[1,-1],[1,1]]
    SPECIAL_CHAR = re.compile('[^a-zA-Z0-9.]')
    found = []
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if SPECIAL_CHAR.search(rows[i][j]):
                # print('blah')
                # print(rows[i][j])
                for x, y in DIRECTIONS:
                    di = i + x
                    dj = j + y
                    # print(di)
                    # print(dj)
                
                    if di >= 0 and di < len(rows) and dj >= 0 and dj < len(rows[i]) and rows[di][dj].isnumeric():
                        # print(di)
                        # print(dj)
                        p1 = dj
                        p2 = dj
                        while p1 >= 0 and p1 < len(rows) and rows[di][p1].isnumeric():
                            p1 -= 1
                        while p2 >= 0 and p2 < len(rows) and rows[di][p2].isnumeric():
                            p2 += 1
                        num = int(rows[di][p1+1:p2])
                        # print(found)
                        if (di,p1,p2) not in found:
                            # print("here")
                            # print(num)
                            found.append((di, p1, p2))
                            tot += num
                        

            

    return tot


def part2(rows):
    rows = list(rows)
    tot = 0
    DIRECTIONS = [[0, 1],[1,0],[0,-1],[-1,0],[-1,-1],[-1,1],[1,-1],[1,1]]
    GEAR = '*'
    found = []
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            if GEAR == rows[i][j]:
                gear_nums = []
                for x, y in DIRECTIONS:
                    di = i + x
                    dj = j + y
                    if di >= 0 and di < len(rows) and dj >= 0 and dj < len(rows[i]) and rows[di][dj].isnumeric():
                        p1 = dj
                        p2 = dj
                        while p1 >= 0 and p1 < len(rows) and rows[di][p1].isnumeric():
                            p1 -= 1
                        while p2 >= 0 and p2 < len(rows) and rows[di][p2].isnumeric():
                            p2 += 1
                        num = int(rows[di][p1+1:p2])
                        if (di,p1,p2) not in found and num not in gear_nums:
                            found.append((di, p1, p2))
                            gear_nums.append(num)
                if len(gear_nums) == 2:
                    tot += gear_nums[0]*gear_nums[1]
    return tot
      


if __name__ == "__main__":
    raw = open("data/3.txt", "r").read()
    # rows = format_input(raw)
    # print(part1(rows))

    rows = format_input(raw)
    print(part2(rows))