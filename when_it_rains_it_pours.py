def indices(lst, element):
    result = []
    offset = -1
    while True:
        try:
            offset = lst.index(element, offset+1)
        except ValueError:
            return result
        result.append(offset)

def greatest_distance(lst, index):
    return max(lst, key=lambda l: abs(index - l))

def get_two_largest(lst):
    copied_list = list(lst)
    highest_index = min(indices(copied_list, max(copied_list)))
    copied_list.pop(highest_index)  # remove it from copied list to find next highest
    second_index = greatest_distance(indices(lst, max(copied_list)), highest_index)
    return (highest_index, second_index) if highest_index < second_index else (second_index, highest_index)

def get_accumulated(lst, first, second):
    height = min([lst[first], lst[second]])  # rain only fills to the lower of the two
    split_on_indices(lst, first, second)
    first += 1  # fix for slicing list and for distance calculation
    distance = second - first
    total = height * distance
    return total - sum(lst[first:second])

def split_on_indices(lst, first, second):
    #  this will split sent in list at first and second indices while keeping indices in the new lists
    return [lst[0:first+1], lst[second:]]

def answer(lst):
    snippets = [lst]  # teehee.  gotta start it somewhere :3
    total = 0
    while len(snippets) > 0:
        current_list = snippets[0]
        if len(current_list) > 2:
            first, second = get_two_largest(current_list)
            if (second - (first + 1)) >= 1:
                total += get_accumulated(current_list, first, second)
            snippets.extend(split_on_indices(current_list, first, second))
        snippets.remove(current_list)
    return total