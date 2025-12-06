# Part 1 Method
def get_columns():
    text = open("inputs/day-6-input.txt").read()

    columns = []
    for line in text.splitlines():
        # extract only integers from each line
        nums = [int(x) for x in line.split() if x.isdigit()]
        if not nums:
            continue

        # ensure enough columns
        while len(columns) < len(nums):
            columns.append([])

        # append numbers to their column
        for i, n in enumerate(nums):
            columns[i].append(n)

    return columns


# Part 2 Method
def get_columns_right_to_left():
    text = open("inputs/day-6-input.txt").read()
    lines = [line.rstrip('\n') for line in text.splitlines()]
    
    # Find the maximum line length to determine number of columns
    max_len = max(len(line) for line in lines) if lines else 0
    
    # Extract columns character by character
    columns = []
    for col_idx in range(max_len):
        column_chars = []
        for line in lines:
            if col_idx < len(line):
                column_chars.append(line[col_idx])
            else:
                column_chars.append(' ')
        columns.append(column_chars)
    
    # Process columns right-to-left, grouping by problems (separated by space-only columns)
    problems = []
    current_problem_columns = []
    
    for col in reversed(columns):
        # Check if this is a space-only column (problem separator)
        if all(c == ' ' for c in col):
            if current_problem_columns:
                problems.append(current_problem_columns)
                current_problem_columns = []
        else:
            current_problem_columns.append(col)
    
    # Add the last problem if any
    if current_problem_columns:
        problems.append(current_problem_columns)
    
    # Convert each problem's columns to numbers
    result = []
    for problem_columns in problems:
        # Each column in the problem represents one number
        problem_numbers = []
        for col in problem_columns:
            # Read digits top-to-bottom, skipping spaces
            digits = [c for c in col if c.isdigit()]
            if digits:
                # Most significant digit at top, least at bottom
                number_str = ''.join(digits)
                problem_numbers.append(int(number_str))
        result.append(problem_numbers)
    

    result.reverse()
    return result

def get_operators():
    text = open("inputs/day-6-input.txt").read()
    lines = [line.strip() for line in text.splitlines()]

    line = lines[len(lines) - 1]
    return [op for op in line.strip().split(" ") if op]

def apply_operator(nums, operator):
    if not nums:
        return None
    if operator == "+":
        result = 0
        for n in nums:
            result += n
        return result
    elif operator == "*":
        result = 1
        for n in nums:
            result *= n
        return result
    else:
        raise ValueError(f"Unsupported operator: {operator}")


def add_column_results(columns, operators):
    result = 0;
    for i in range(len(columns)):
        result += apply_operator(columns[i], operators[i])
    return result


# Replace with part 1 or part 2 method
print(add_column_results(get_columns(), get_operators()))