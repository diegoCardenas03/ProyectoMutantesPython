def is_diagonal(adn_list):
    temporal_string = ''
    count = 0
    # Verifico si la diagonal principal contiene la secuencia requerida
    for i in range(0, 4):
        temporal_string += adn_list[i][i]
        if i == 3:
            if is_sequence(temporal_string):
                count += 1
            else:
                temporal_string = ''
                for j in range(1, 5):
                    temporal_string += adn_list[j][j]
                    if j == 4:
                        if is_sequence(temporal_string):
                            count += 1
                        else:
                            temporal_string = ''
                            for k in range(2, 6):
                                temporal_string += adn_list[k][k]
                                if k == 5:
                                    if is_sequence(temporal_string):
                                        count += 1
                                    else:
                                        continue
    temporal_string = ''
    # Verifico la primera diagonal debajo de la principal
    for i in range(0, 4):
        temporal_string += adn_list[i+1][i]
        if i == 3:
            if is_sequence(temporal_string):
                count += 1
            else:
                temporal_string = ''
                for j in range(1, 5):
                    temporal_string += adn_list[j+1][j]
                    if j == 4:
                        if is_sequence(temporal_string):
                            count += 1
                        else:
                            continue
    temporal_string = ''
    # Verifico la segunda diagonal bajo la principal
    for i in range(0, 4):
        temporal_string += adn_list[i+2][i]
        if i == 3:
            if is_sequence(temporal_string):
                count += 1
            else:
                continue
    temporal_string = ''
    # Verifico la primera diagonal arriba de la principal
    for i in range(0, 4):
        temporal_string += adn_list[i][i+1]
        if i == 3:
            if is_sequence(temporal_string):
                count += 1
            else:
                temporal_string = ''
                for j in range(1, 5):
                    temporal_string += adn_list[j][j+1]
                    if j == 4:
                        if is_sequence(temporal_string):
                            count += 1
                        else:
                            continue
    temporal_string = ''
    # Verifico la segunda diagonal arriba de la principal
    for i in range(0, 4):
        temporal_string += adn_list[i][i+2]
        if i == 3:
            if is_sequence(temporal_string):
                count += 1
            else:
                continue
    return count


def is_reverse_diagonal(adn_list):

    temporal_string = ''
    count = 0
    # Verifico la diagonal principal inversa
    col = 5
    for i in range(0, 4):
        temporal_string += adn_list[i][col]
        col -= 1
        if i == 3:
            if is_sequence(temporal_string):
                count += 1
            else:
                temporal_string = ''
                col = 4
                for j in range(1, 5):
                    temporal_string += adn_list[j][col]
                    col -= 1
                    if j == 4:
                        if is_sequence(temporal_string):
                            count += 1
                        else:
                            temporal_string = ''
                            col = 3
                            for k in range(2, 6):
                                temporal_string += adn_list[k][col]
                                col -= 1
                                if k == 5:
                                    if is_sequence(temporal_string):
                                        count += 1
                                    else:
                                        continue
    temporal_string = ''
    col = 5
    # Verifico la primera diagonal debajo de la principal inversa
    for i in range(1, 5):
        temporal_string += adn_list[i][col]
        col -= 1
        if i == 4:
            if is_sequence(temporal_string):
                count += 1
            else:
                temporal_string = ''
                col = 4
                for j in range(2, 6):
                    temporal_string += adn_list[j][col]
                    col -= 1
                    if j == 5:
                        if is_sequence(temporal_string):
                            count += 1
                        else:
                            continue
    temporal_string = ''
    col = 5
    # Verifico la segunda diagonal debajo de la principal inversa
    for i in range(2, 6):
        temporal_string += adn_list[i][col]
        col -= 1
        if i == 5:
            if is_sequence(temporal_string):
                count += 1
            else:
                continue
    temporal_string = ''
    col = 4
    # Verifico la primera diagonal arriba de la principal inversa
    for i in range(0, 4):
        temporal_string += adn_list[i][col]
        col -= 1
        if i == 3:
            if is_sequence(temporal_string):
                count += 1
            else:
                temporal_string = ''
                col = 3
                for j in range(1, 5):
                    temporal_string += adn_list[j][col]
                    col -= 1
                    if j == 4:
                        if is_sequence(temporal_string):
                            count += 1
                        else:
                            continue
    temporal_string = ''
    col = 3
    # Verifico la segunda diagonal arriba de la principal inversa
    for i in range(0, 4):
        temporal_string += adn_list[i][col]
        col -= 1
        if i == 3:
            if is_sequence(temporal_string):
                count += 1
            else:
                continue
    return count


def is_horizontal(adn_list):
    count = 0

    for i in range(0, 6):
        temporal_string = ''
        for j in range(0, 4):
            temporal_string += adn_list[i][j]
            if j == 3:
                if is_sequence(temporal_string):
                    count += 1
                else:
                    temporal_string = ''
                    for k in range(1, 5):
                        temporal_string += adn_list[i][k]
                        if k == 4:
                            if is_sequence(temporal_string):
                                count += 1
                            else:
                                temporal_string = ''
                                for m in range(2, 6):
                                    temporal_string += adn_list[i][m]
                                    if m == 5:
                                        if is_sequence(temporal_string):
                                            count += 1
                                        else:
                                            temporal_string = ''
                                            continue
    return count


def is_vertical(adn_list):
    count = 0

    for i in range(0, 6):
        temporal_string = ''
        for j in range(0, 4):
            temporal_string += adn_list[j][i]
            if j == 3:
                if is_sequence(temporal_string):
                    count += 1
                else:
                    temporal_string = ''
                    for k in range(1, 5):
                        temporal_string += adn_list[k][i]
                        if k == 4:
                            if is_sequence(temporal_string):
                                count += 1
                            else:
                                temporal_string = ''
                                for m in range(2, 6):
                                    temporal_string += adn_list[m][i]
                                    if m == 5:
                                        if is_sequence(temporal_string):
                                            count += 1
                                        else:
                                            temporal_string = ''
                                            continue
    return count


def contains_adn(string):
    contains = True
    possible_adn = ['A', 'G', 'C', 'T']
    for letter in string:
        if letter not in possible_adn:
            return False
        else:
            continue

    return contains


def is_sequence(adn_string):
    a_adn = 'AAAA'
    t_adn = 'TTTT'
    c_adn = 'CCCC'
    g_adn = 'GGGG'
    return adn_string == a_adn or adn_string == t_adn or adn_string == c_adn or adn_string == g_adn


def is_mutant(adn_list):
    total = is_diagonal(adn_list) + is_reverse_diagonal(adn_list) + is_horizontal(adn_list) + is_vertical(adn_list)
    return total >= 2


