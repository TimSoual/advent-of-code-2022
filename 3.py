def calcPrio(item):
    code = ord(item)
    if code > 97:
        return code - 96
    else:
        return code - 64 + 26

def solve_first(data):
    bags = data.split('\n')
    sum = 0
    for bag in bags:
        first_comp = bag[:len(bag)//2]
        second_comp = bag[len(bag)//2:]
        common_el = list(set(first_comp) & set(second_comp))[0]
        sum += calcPrio(common_el)
    return sum

def solve_second(data):
    bags = data.split('\n')
    sum = 0
    for i in range(len(bags) // 3):
        first_ind = i*3
        bag_1 = bags[first_ind]
        bag_2 = bags[first_ind+1]
        bag_3 = bags[first_ind+2]
        common_el = list(set(bag_1) & set(bag_2) & set(bag_3))[0]
        sum += calcPrio(common_el)
    return sum

test_data = '''vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw'''

if __name__ == "__main__":
    data = open('3_input.txt', 'r').read()
    print(solve_first(data))
    print(solve_second(data))