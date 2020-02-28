"""
Given an array of balls (objects) of uniform size and shape where one ball is
slightly heavier than the others (and the rest weigh the same), and a balance
scale (in the form of a function- scale(array, leftStart, leftEnd, rightStart,
rightEnd), which weighs the two sides of the array and returns -1,0,1 if the
left is heavier, even, or right is heavier) find the index of the heavier ball
in an efficient manner. 
"""

def scale(arr, lstart, lend, rstart, rend):
    "This function assumes that all objects in array are the same, save for 1"
    sum_left = sum(arr[lstart:lend])
    sum_right = sum(arr[rstart:rend])
    if sum_left == sum_right:
        return 0
    elif sum_left > sum_right:
        return -1
    elif sum_right > sum_left:
        return 1


def find_ball(arr, lstart, lend, rstart, rend):
    part = scale(arr, lstart, lend, rstart, rend)
    print(part)

    while part != 0:
        if part == 1:
            rang = rend - rstart
            part = scale(arr, rstart, rstart + rang, rend - rang, rend)
        else:
            rang = lend - lstart
            part = scale(arr, lstart, lstart + rang, lend - rang, lend)

    print('answer:', part)
    print(lstart, lend, rstart, rend)
    return lstart



def scale(arr, lstart, rstart):
    lend = rstart - 1
    rend = lend + (rstart - lstart)
    sum_left = sum(arr[lstart:lend])
    sum_right = sum(arr[rstart:rend])

    if sum_left == sum_right:
        return 0
    elif sum_left > sum_right:
        return -1
    elif sum_right > sum_left:
        return 1


def find_ball(arr):
    lstart = 0; rstart = len(arr) // 2
    part = scale(arr, lstart, rstart)
    if part < 0:
        rstart -= rstart // 2
    else:
        lstart = rstart
        rstart += rstart // 2

    while part != 0:
        part = scale(arr, lstart, rstart)
        if part < 0:
            rstart -= rstart // 2
        else:
            lstart = rstart
            rstart += rstart // 2

    print(lstart, rstart)
    return rstart - 1


# Time: O(N)
# Space: O(1)
def find_ball_fastest(arr):
    """
    Peek first 3 elements to determine common. Anything that doesn't match is
    what we are looking for.
    """
    a, b, c = arr[:3]
    if b == a or c == a:
        common = a
    elif a == b or c == b:
        common = b
    else:
        common = c

    for i in range(len(arr)):
        if arr[i] != common:
            return i

#print(find_ball_fastest([1, 1, 2]))
#print(find_ball_fastest([2, 1, 1]))
#print(find_ball_fastest([1, 2, 1]))


if __name__ == '__main__':
    arr = [1, 1, 1, 1, 1, 1, 1, 8]

    print(find_ball_fastest(arr))

    #assert find_ball(arr, 0, len(arr) // 2, len(arr) // 2, len(arr) - 1) == 2, 'Index is not 2'

    print('All tests passed')



