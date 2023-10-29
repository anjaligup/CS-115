def editDistance(first, second):
    if first == '':
        return len(second)
    elif second == '':
        return len(first)
    elif first[0] == second[0]: #if first item equals other, move onto next items
        return editDistance(first[1:], second[1:])
    else:
        substitution = 1 + editDistance(first[1:], second[1:])
        deletion = 1 + editDistance(first[1:], second)
        insertion = 1 + editDistance(first, second[1:])
        return min(substitution, deletion, insertion)

