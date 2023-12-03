import math


def parse_game(line):
    game_id, grabs = line.split(':')
    id = int(game_id.split()[1])
    turns = [{color.split()[1]: int(color.split()[0])
              for color in grab.split(',')}
             for grab in grabs.split(';')]
    return (id, turns)


def min_cubes(turns):
    cubes_seen = {}
    for turn in turns:
        for color, count in turn.items():
            if cubes_seen.get(color, 0) < count:
                cubes_seen[color] = count
    return cubes_seen


def is_game_possible(turns, cubes):
    return all((cubes.get(color, 0) >= count
                for color, count in min_cubes(turns).items()))


def sum_of_possible_game_ids(lines, inventory):
    sum = 0
    for line in lines.split('\n'):
        id, turns = parse_game(line)
        if is_game_possible(turns, inventory):
            sum += id
    return sum


def power_of_set(turns):
    cubes = {'red': 0, 'green': 0, 'blue': 0}
    cubes_all_color = cubes | min_cubes(turns)
    return math.prod(cubes_all_color.values())


def sum_of_power_of_sets(lines):
    sum = 0
    for line in lines.split('\n'):
        id, turns = parse_game(line)
        sum += power_of_set(turns)
    return sum
