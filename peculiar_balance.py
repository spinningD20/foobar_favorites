from copy import copy


def answer(x):
    key = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323,
                 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467]
    unused = list(key[:key.index(next(v for i, v in enumerate(key) if v > abs(x))) + 1])
    response = list(['-' for i in range(len(unused))])
    difference = copy(x)
    left_heavier = True
    while difference != 0:
        try:
            next_largest = next(v for i, v in enumerate(unused) if v > abs(difference))
        except StopIteration:
            next_largest = unused[-1]
        index = unused.index(next_largest)
        if abs(difference)*2 < unused[index] and abs(difference)/2 < unused[index-1]:
            index -= 1
        next_largest = unused.pop(index)
        if left_heavier:
            difference += -next_largest
            response[index] = 'R'
        else:
            response[index] = 'L'
            difference += next_largest
        # is left still heavier?  better check before the next turn!
        left_heavier = difference > 0
    if response[-1] == '-':
        del(response[-1])
    return response