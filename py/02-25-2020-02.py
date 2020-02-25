"""
Find the height of a binary tree.

Recusion

f(b, c)

Another solution: store branch height in each node :)
"""

# Expected height: 3
tree = {
    'children' : [
        {
            'children' : []
        },
        {
            'children' : [
                {
                    'children' : []
                },
                {
                    'children' : []
                }
            ]
        },
        {
            'children': []
        }
    ]
}

def btree_height(branch, count=1):
    if branch['children']:
        return max(
            btree_height(b, count + 1) for b in branch['children']
        )
    else:
        return count

if __name__ == '__main__':
    print(f'BTree height: {btree_height(tree)}')
