def get_max_joltage(s):
    max_joltage = 0
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            try:
                num = int(s[i] + s[j])
                if num > max_joltage:
                    max_joltage = num
            except ValueError:
                continue
    return max_joltage

# use this for part 2
def get_max_joltage_2(s):
    # Extract only digits from the string
    digits = [char for char in s if char.isdigit()]
    
    # If we have less than 12 digits, return 0
    if len(digits) < 12:
        return 0
    
    # We need to select exactly 12 digits to form the largest number
    # This is equivalent to removing (len(digits) - 12) digits while maintaining order
    # Use a greedy approach: use a stack to build the largest number
    to_remove = len(digits) - 12
    stack = []
    
    for digit in digits:
        # While we can still remove digits, and the current digit is larger than the last in stack
        # remove smaller digits from the end to make room for larger ones
        while to_remove > 0 and stack and stack[-1] < digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)
    
    # If we still need to remove more digits, remove from the end (smallest digits)
    while to_remove > 0:
        stack.pop()
        to_remove -= 1
    
    # Convert to integer
    return int(''.join(stack))

def get_joltage_sum():
    lines = [line.strip() for line in open("inputs/day-3-input.txt")]

    result = 0
    for line in lines:
        # replace this with get_max_joltage_2 for part 2
        result += get_max_joltage_2(line)
    
    return result


print(get_joltage_sum())