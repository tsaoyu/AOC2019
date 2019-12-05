

def is_non_decrease_and_adjecent(number):
    adjecent_flag = False
    for first, second in zip(number[:-1], number[1:]):
        if first > second:
            return False and adjecent_flag
        elif first == second:
            adjecent_flag = True

    return True and adjecent_flag

def is_non_decrease_and_adjecent_non_matching(number):
    adjecent_group = {}
    for first, second in zip(number[:-1], number[1:]):
        if first > second:
            return False 
        elif first == second:
            if second in adjecent_group.keys():
                adjecent_group[second] += 1
            else:
                adjecent_group[second] = 2

    return True and (2 in adjecent_group.values())


def password_combinations(password_range):
    ans = 0
    for password in range(password_range[0], password_range[1]):
        if is_non_decrease_and_adjecent(str(password)):
            ans += 1
    return ans

def password_combinations_non_matching(password_range):
    ans = 0
    for password in range(password_range[0], password_range[1]):
        if is_non_decrease_and_adjecent_non_matching(str(password)):
            ans += 1
    return ans


print(password_combinations([172930,683082]))
print(password_combinations_non_matching([172930,683082]))