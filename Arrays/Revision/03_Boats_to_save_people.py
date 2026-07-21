def boatstosaveppl(people,limit):
    people.sort()
    left=0
    right = len(people)-1
    count=0
    while left<right :
        if people[left]+people[right]<=limit:
            count+=1
            left+=1
            right-=1
        else:
            if people[left]==limit:
                return len(people)
            count+=1
            right-=1
    return count
            