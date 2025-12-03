lines = [line.strip() for line in open("inputs/day-1-input.txt")]

start = 50;
zeroCount = 0;

for line in lines:
    direction = line[0]
    steps = int(line[1:])

    if direction == "R":
        # Count positions 1 to steps where we're at 0
        # We're at 0 when (start + i) % 100 == 0 for i in [1, steps]
        # This is when start + i is a multiple of 100
        # Number of such positions: (start + steps) // 100
        zeroCount += (start + steps) // 100
        start = (start + steps) % 100
    elif direction == "L":
        # Count positions 1 to steps where we're at 0
        # We're at 0 when (start - i) % 100 == 0 for i in [1, steps]
        # This is when start - i is a multiple of 100, i.e., i = start, start+100, start+200, ...
        if start == 0:
            # Special case: if we start at 0, we don't count the starting position
            # So we count i = 100, 200, ... up to steps
            zeroCount += steps // 100
        elif steps >= start:
            # We hit 0 at i = start, start+100, start+200, ...
            zeroCount += (steps - start) // 100 + 1
        # If steps < start, we never reach 0
        start = (start - steps) % 100

    print(start)

print(zeroCount)