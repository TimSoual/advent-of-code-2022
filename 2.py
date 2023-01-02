def solve_first(data):
    score_table = {
        'A X': 4,
        'A Y': 8,
        'A Z': 3,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 7,
        'C Y': 2,
        'C Z': 6
    }
    lines = data.split('\n')
    return sum(map(lambda line: score_table[line], lines))

def solve_second(data):
    score_table = {
        'A X': 3,
        'A Y': 4,
        'A Z': 8,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 2,
        'C Y': 6,
        'C Z': 7
    }
    lines = data.split('\n')
    return sum(map(lambda line: score_table[line], lines))



if __name__ == "__main__":
    data = open('2_input.txt', 'r').read()

    test_data = '''A Y
B X
C Z'''

    print(solve_first(data))
    print(solve_second(data))