
def sortingppl(people):
    pplen = len(people)
    temp = 0
    n = 0
    count = 0
    while count <= pplen:
        while n <= pplen - 2:
            if people[n] > people[n + 1]:
                temp = people[n]
                people[n] = people[n + 1]
                people[n + 1] = temp

            n += 1
        if count == pplen:
            return people
        n = 0
        count += 1

def boat(limit):
    pplout = (sortingppl(people))
    pm = 0
    pma = len(pplout) - 1
    boatt = 0

    while pma >= pm:
        if (pplout[pm] + pplout[pma]) <= limit:
            boatt += 1
            pm += 1
            pma -= 1
        else:
            boatt += 1
            pma -= 1
    print(boatt)



people = [3, 2, 1, 2]
limit = 4
sortingppl(people)
boat(limit)
