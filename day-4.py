def read_matrix_from_file(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            row = list(line.strip())
            matrix.append(row)
    return matrix

def get_neighbors(matrix, row, col):
    neighbor_count = 0;

    x_coordinate_start = max(col - 1, 0);
    x_coordinate_end = min(col + 1, len(matrix[0]) - 1);
    y_coordinate_start = max(row - 1, 0);
    y_coordinate_end = min(row + 1, len(matrix) - 1);

    for x in range(x_coordinate_start, x_coordinate_end + 1):
        for y in range(y_coordinate_start, y_coordinate_end + 1):
            if x == col and y == row:
                continue;
            if matrix[y][x] == '@':
                neighbor_count += 1;
    return neighbor_count;

# Part 1
def get_accessible_rolls(matrix):
    accessible_rolls = []
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == '@':
                if get_neighbors(matrix, row, col) < 4:
                    accessible_rolls.append([row, col]);
    return accessible_rolls;

def remove_rolls(matrix, rolls):
    for roll in rolls:
        matrix[roll[0]][roll[1]] = '.';
    return matrix;

# Part 2
def get_accessible_rolls_2(matrix):
    rolls_removed = 0;
    accessible_rolls = get_accessible_rolls(matrix);
    while len(accessible_rolls) > 0:
        rolls_removed += len(accessible_rolls);
        matrix = remove_rolls(matrix, accessible_rolls);
        accessible_rolls = get_accessible_rolls(matrix);
    return rolls_removed;

if __name__ == "__main__":
    matrix = read_matrix_from_file("inputs/day-4-input.txt")
    # Replace with part that you need
    print(get_accessible_rolls_2(matrix))