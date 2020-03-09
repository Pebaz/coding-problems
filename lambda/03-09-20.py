"""
This problem was asked by Mailchimp.

You are given an array representing the heights of neighboring buildings on a
city street, from east to west. The city assessor would like you to write an
algorithm that returns how many of these buildings have a view of the setting
sun, in order to properly value the street.

For example, given the array [3, 7, 8, 3, 6, 1], you should return 3, since the
top floors of the buildings with heights 8, 6, and 1 all have an unobstructed
view to the west.

Can you do this using just one forward pass through the array?
"""


def view(arr):
    """
    Time: O(n)
    Space: O(n)
    """
    stack = []
    for i in arr:
        while stack and stack[-1] <= i:
            stack.pop()
        stack.append(i)
    return len(stack)


if __name__ == '__main__':
    print(view([3, 7, 8, 3, 6, 1]))
    print(view([2, 7, 1, 3, 8, 5, 5, 4, 6, 3, 7, 8, 6, 1]))
