n = int(input())
tree = {}

for i in range(n):
    root, left, right = map(str, input().split(' '))
    tree[root] = [left, right]

def preorder(root): # 전위순회
    if root != '.':
        print(root, end='')

        preorder(tree[root][0]) # 왼쪽으로
        preorder(tree[root][1])

def inorder(root): # 중위순회
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])

        print(root, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')