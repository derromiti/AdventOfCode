def read_input(filename="input.txt"):
    with open(filename, "r") as file:
        return [line.strip() for line in file]

def solve_part1(input_lines):
    total = 0
    print(total)

def solve_part2(input_lines):
    total = 0
    print(total)

def main():
    input_lines = read_input("test_p1.txt")
    # input_lines = read_input("test_p2.txt")
    # input_lines = read_input()

    # Solve and print the results for part 1
    result_part1 = solve_part1(input_lines)
    print(f"Part 1: {result_part1}")

    # Solve and print the results for part 2
    result_part2 = solve_part2(input_lines)
    print(f"Part 2: {result_part2}")

if __name__ == "__main__":
    main()
