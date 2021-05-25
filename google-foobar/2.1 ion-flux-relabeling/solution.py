
def solution(h, q):
    # Your code here
    def get_node(idx, subtree_size):
  
        node_offset = 0
        
        while True:
                    
            subtree_size //= 2
            
            left_node = node_offset + subtree_size
            
            right_node = left_node + subtree_size
            
            node = right_node + 1
            
            if (left_node == idx) or (right_node == idx):
                return node

            if (idx > left_node):
                node_offset = left_node

    subtree_size = 2**h-1

    return [-1 if index > subtree_size-1 else get_node(index, subtree_size) for index in q]


print(solution(3, [7, 3, 5, 1]))
print(solution(1, [0]))
print(solution(5, [19, 14, 28]))
print(7//2)




# -1,7,6,3



#    7
#  3   6
# 1 2 4 5