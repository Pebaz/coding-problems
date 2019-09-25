def rooms(arr):
    intersections = []  # Needs to be a set

    for room in arr:
        start1, end1 = room

        for other_room in arr:
            if other_room == room:
                continue

            start2, end2 = other_room

            if (start2 >= start1 and start2 <= end1) or (end2 >= start1 and end2 <= end1):
                inter = {start1, start2, end1, end2}

                if inter not in intersections:
                    intersections.append(inter)

    return len(intersections)



if __name__ == '__main__':
    print(rooms([
        (30, 75),
        (0, 50),
        (60, 150)
    ]))
