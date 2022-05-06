#Pseudocode
"""Input: Recive a node with differents keys, and the key we search
   Output: If found the key return the key and the position
           If is a leaf return None because we can not continue in this node
           Else continue search to the differents child of keys
"""      
def search_key(key, node):
    i = 0                                   
    len_node = len(node)                     

    while i < len_node and key > node[i]:           # Find a key greater than or equal to k
        i += 1

    if i < len_node and key == node[i]:             # If  key is equal to k
       return (key,i)
    elif leaf:                                      # This is a leaf node
       return None
    else:
       return self.search_key(key, tree.child[i])   # Continue with other node
