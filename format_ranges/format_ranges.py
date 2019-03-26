def format_a_range(start, end):
    if start == end:
        return '{}'.format(start)
    return '{}-{}'.format(start, end)

def format_ranges(the_range):
    my_ranges = []
    the_range = sorted(list(the_range))
    current_range_start = current_range_end = last_val = the_range.pop(0)
    for i in the_range:
        if (i - 1) == last_val:
            # still in a range, bump current_range_end and last_val
            last_val = current_range_end = i
            continue
        if (i - 1) != last_val:
            # end of current range condition
            my_ranges.append(
                format_a_range(current_range_start, current_range_end)
            )
            current_range_start = current_range_end = last_val = i
    # append that last value whether its a single thing or an open range
    my_ranges.append(
        format_a_range(current_range_start, current_range_end)
    )
    return ",".join(my_ranges)

if __name__ == '__main__':
    print(format_ranges([1, 2, 3])) # '1-3'
    print(format_ranges([1, 2, 10, 11, 12, 13, 14])) # '1-2,10-14'
