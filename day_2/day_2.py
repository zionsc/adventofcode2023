# Here is the Python code to read from "input.txt" and process each line:

def parse_line(line):
    parts = line.split(':')
    game_id = int(parts[0].split()[1])
    scenarios = parts[1].split(';')
    game_scenarios = []
    for scenario in scenarios:
        cubes = scenario.strip().split(',')
        blue = sum(int(cube.split()[0]) for cube in cubes if 'blue' in cube)
        red = sum(int(cube.split()[0]) for cube in cubes if 'red' in cube)
        green = sum(int(cube.split()[0]) for cube in cubes if 'green' in cube)
        game_scenarios.append((blue, red, green))
    return game_id, game_scenarios

def is_game_possible(game_scenarios, red_cubes, green_cubes, blue_cubes):
    for blue, red, green in game_scenarios:
        if blue > blue_cubes or red > red_cubes or green > green_cubes:
            return False
    return True

# Assume you have the file "input.txt" and read it line by line
total_sum = 0
with open("input.txt", 'r') as file:
    for line in file:
        game_id, scenarios = parse_line(line.strip())
        if is_game_possible(scenarios, 12, 13, 14):
            total_sum += game_id

print(total_sum)

