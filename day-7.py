def read_matrix_from_file(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            row = list(line.strip())
            matrix.append(row)
    return matrix

def get_start_position(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 'S':
                return row, col
    return None

# Part 1
def simulate_beam_splitting(matrix):
    start_row, start_col = get_start_position(matrix)
    if start_row is None:
        return 0
    
    # Track active beam positions (columns that have active beams at each row)
    # We'll process row by row
    split_count = 0
    
    # Start with one beam at the start position
    active_beams = {start_col}  # Set of columns with active beams
    
    # Process each row from start_row + 1 to the end
    for row in range(start_row + 1, len(matrix)):
        next_row_beams = set()
        
        # For each active beam column, check what's in the next row
        for col in active_beams:
            # Check if we're still within bounds
            if col < 0 or col >= len(matrix[row]):
                continue
            
            # Check what's at this position in the current row
            if matrix[row][col] == '^':
                # Hit a splitter - beam stops, create two new beams
                split_count += 1
                
                # Create beams at left and right positions
                left_col = col - 1
                right_col = col + 1
                
                # Add to next row if within bounds
                if left_col >= 0:
                    next_row_beams.add(left_col)
                if right_col < len(matrix[row]):
                    next_row_beams.add(right_col)
            elif matrix[row][col] == '.':
                # Empty space - beam continues downward
                next_row_beams.add(col)
        
        # Update active beams for next iteration
        active_beams = next_row_beams
        
        # If no active beams, we're done
        if not active_beams:
            break
    
    return split_count

# Part 2
def count_quantum_timelines(matrix):
    """
    Count how many unique timelines exist using the many-worlds interpretation.
    At each splitter, the particle takes both paths, creating multiple timelines.
    We need to count all unique paths (each path is a timeline).
    """
    start_row, start_col = get_start_position(matrix)
    if start_row is None:
        return 0
    
    # Use memoization to count paths from each position
    # memo[(row, col)] = number of unique paths from (row, col) to the end
    memo = {}
    
    def count_paths_from(row, col):
        # Base case: out of bounds
        if col < 0 or col >= len(matrix[row]) if row < len(matrix) else True:
            return 0
        
        # Base case: reached the last row
        if row == len(matrix) - 1:
            return 1
        
        # Check memo
        if (row, col) in memo:
            return memo[(row, col)]
        
        result = 0
        
        # Check what's in the next row at this column
        if row + 1 >= len(matrix):
            result = 1
        elif matrix[row + 1][col] == '^':
            # Hit a splitter - particle takes both paths
            left_col = col - 1
            right_col = col + 1
            
            # Count paths from both positions
            if left_col >= 0:
                result += count_paths_from(row + 1, left_col)
            if right_col < len(matrix[row + 1]):
                result += count_paths_from(row + 1, right_col)
        elif matrix[row + 1][col] == '.':
            # Empty space - particle continues in same column
            result = count_paths_from(row + 1, col)
        
        memo[(row, col)] = result
        return result
    
    return count_paths_from(start_row, start_col)

if __name__ == "__main__":
    matrix = read_matrix_from_file("inputs/day-7-input.txt")
    # Part 1: Count how many times the beam is split
    # print(simulate_beam_splitting(matrix))
    # Part 2: Count how many unique timelines exist
    print(count_quantum_timelines(matrix))