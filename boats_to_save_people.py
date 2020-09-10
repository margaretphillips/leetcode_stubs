#given an array of numbers ( int or float ) representing the weights of people
#and a limit representing the weight limit of a boat
#each boat can only hold up to two people
#each person has a weight that is lower or equal to the weight limit of the boat
#find the min number of boats to carry all the people

def boatstosavepeople(arr, limit):
    boats = 0
    n = sorted(arr)
    boats = n.count(limit)
    for i in range(boats):
        n.pop()
    boats += sum(n) % limit
    boats += len(n) - boats
    return boats

arr = [1,2,3,2,1,3,2,3,2,1,2,2]
limit = 3
result = boatstosavepeople(arr, limit)
print(result)


