test_data = '''2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8'''

def parse_pair(pair):
    elfs = pair.split(',')
    return list(map(lambda e: list(map(int, e.split('-'))), elfs))

def solve_first(data):
    pairs = data.split('\n')
    sum = 0
    for pair in pairs:
        [first_elf, second_elf] = parse_pair(pair)
        if first_elf[0] >= second_elf[0] and first_elf[1] <= second_elf[1]:
            sum += 1
        elif second_elf[0] >= first_elf[0] and second_elf[1] <= first_elf[1]:
            sum += 1
    return sum


def solve_second(data):
    pairs = data.split('\n')
    sum = 0
    for pair in pairs:
        [first_elf, second_elf] = parse_pair(pair)
        if first_elf[0] <= second_elf[1] and first_elf[1] >= second_elf[0]:
            sum += 1  
    return sum

if __name__ == "__main__":
    data = open('4_input.txt', 'r').read()
    print(solve_first(data))
    print(solve_second(data))