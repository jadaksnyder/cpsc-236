def read_world_cup_data(file_name):
    world_cup_data = {}
    with open(file_name, 'r') as file:
        # Skip header
        next(file)
        for line in file:
            year, country, _, _ = line.strip().split(',')
            if country in world_cup_data:
                world_cup_data[country].append(year)
            else:
                world_cup_data[country] = [year]
    return world_cup_data

def print_world_cup_stats(world_cup_data):
    print("Country\t\tWins\tYears")
    print("=" * 30)
    for country, years in sorted(world_cup_data.items()):
        wins = len(years)
        years_str = ', '.join(years)
        print(f"{country.ljust(15)}\t{wins}\t{years_str}")

def main():
    file_name = 'world_cup_champions.txt'
    world_cup_data = read_world_cup_data(file_name)
    print_world_cup_stats(world_cup_data)

if __name__ == "__main__":
    main()

    