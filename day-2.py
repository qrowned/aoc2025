def get_sum_of_silly_numbers():
    with open("inputs/day-2-input.txt") as f:
        text = f.read();

        pairs = text.split(",")
        ranges = [[int(r) for r in pair.split("-")] for pair in pairs]

        sum = 0;

        for r in ranges:
            for i in range(r[0], r[1] + 1):
                # Replace is_silly_number with is_silly_number_part_2 for Part 2
                if is_silly_number(str(i)):
                    sum += i;

        return sum;


# Checks if a number is silly for Part 1
def is_silly_number(number):
    if len(number) % 2 != 0:
        return False;
    half = int(len(number) / 2);

    firstHalf = number[:half]
    secondHalf = number[half:]

    return firstHalf == secondHalf

# Checks if a number is silly for Part 2
def is_silly_number_part_2(number):
    for start in range(len(number)):
        for end in range(start + 1, len(number) + 1):
            substring = number[start:end]
            if is_multiple_repetition(number, substring):
                return True
    return False

def is_multiple_repetition(s, t):
    if not t:
        return False
    count = len(s) // len(t)
    return count >= 2 and s == t * count

print(get_sum_of_silly_numbers())