def format_input(raw):
    rows = raw.split("\n")
    return rows


def part1(rows):
    tot_sum = 0
    for row in rows:
        num1 = 0 
        num2 = len(row) - 1
        while not row[num1].isdigit():
            num1 += 1
        while not row[num2].isdigit():
            num2 -= 1
        tot_sum += int(row[num1]+row[num2])
    return tot_sum
        



def part2(rows):
    tot_sum = 0
    DIGITS = {'one':'o1e','two':'t2o','three':'t3e','four':'f4r',
              'five':'f5e','six':'s6x','seven':'s7n','eight':'e8t','nine':'n9e'}
    for row in rows:
        for word, num in DIGITS.items():
            row = row.replace(word, num)
        num1 = 0 
        num2 = len(row) - 1
        while not row[num1].isdigit():
            num1 += 1
        while not row[num2].isdigit():
            num2 -= 1
        tot_sum += int(row[num1]+row[num2])
    return tot_sum


if __name__ == "__main__":
    raw = open("data/1.txt", "r").read()
    rows = format_input(raw)
    print(part1(rows))

    rows = format_input(raw)
    print(part2(rows))