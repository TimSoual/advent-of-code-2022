def solve_first(data):
    total_food_inventories = data.split('\n\n')
    max_calories= 0
    for elf_inventory in total_food_inventories:
        foods = elf_inventory.split('\n')
        calories = sum(map(int, foods))
        if calories > max_calories:
            max_calories = calories
    return max_calories

def solve_second(data):
    def calc_inventory_calories(elf_inventory):
        return sum(map(int, elf_inventory.split('\n')))

    total_food_inventories = data.split('\n\n')
    total_food_inventories.sort(key=calc_inventory_calories)

    return sum(map(calc_inventory_calories, total_food_inventories[-3:]))


if __name__ == "__main__":
    data = open('1_input.txt', 'r').read()
    print(solve_first(data))
    print(solve_second(data))