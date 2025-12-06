def get_all_available_ids():
    lines = [line.strip() for line in open("inputs/day-5-input.txt")]
    ids = []

    for line in lines:
        if "-" in line or line == "":
            continue
        ids.append(int(line))

    return ids

def get_fresh_id_ranges():
    lines = [line.strip() for line in open("inputs/day-5-input.txt")]
    ranges = []

    for line in lines:
        if "-" not in line or line == "":
            continue
        ranges.append([int(line.split("-")[0]), int(line.split("-")[1])])

    return ranges

def get_fresh_id_ranges_no_overlap():
    """
    Returns ID ranges with overlapping ranges merged together.
    """
    ranges = get_fresh_id_ranges()
    
    if not ranges:
        return []
    
    # Sort ranges by start value
    ranges.sort(key=lambda x: x[0])
    
    merged = [ranges[0]]
    
    for current in ranges[1:]:
        last = merged[-1]
        
        # If current range overlaps or is adjacent to the last merged range
        if current[0] <= last[1] + 1:
            # Merge: extend the end of the last range if needed
            merged[-1][1] = max(last[1], current[1])
        else:
            # No overlap, add as new range
            merged.append(current)
    
    return merged


def get_fresh_ids():
    all_ids = get_all_available_ids()
    fresh_id_ranges = get_fresh_id_ranges()

    fresh_ids = []
    for id in all_ids:
        for r in fresh_id_ranges:
            if id in range(r[0], r[1] + 1):
                fresh_ids.append(id)
                break
    return fresh_ids

def get_all_fresh_ids_count():
    fresh_id_ranges = get_fresh_id_ranges_no_overlap()
    count = 0
    for r in fresh_id_ranges:
        count += r[1] - r[0] + 1
    return count

print(get_all_fresh_ids_count())