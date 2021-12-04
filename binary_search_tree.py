# binary_search_tree.py
Binary search tree
[7,5,1,8,3,6,0,9,4,2] dizisinin Binary-Search-Tree aşamalarını yazınız.

1-         [7,5,1,8,3,6,0,9,4,2]
           /               \
2-    [7,5,1,8,3]        [6,0,9,4,2]
        /    \            /     \
3-  [7,5,1]   [8,3]     [6,0,9]   [4,2]
    / \   \   / \       /   \     /  \
4- [7,5]  [1]  [8] [3]   [6,0] [9] [4]  [2]
   \ /    \    \  /      \ /   \    \  /
5-[5,7]   [1]  [3,8]     [0,6]  [9]  [2,4]
   \     /       /          \   /     /
6-  [1,5,7]     [3,8]       [0,6,9]  [2,4]
       \        /             \      /
7-     [1,3,5,7,8]            [0,2,4,6,9]
            \                     /
8-           [0,1,2,3,4,5,6,7,8,9,]            
