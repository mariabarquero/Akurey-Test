class Bnode:
    def __init__(self):
        self.keys = []
        self.subtree = []
        self.occupiedKeys = 0      # allocated positions in keys

list_node = []
num_c = 0 # Column Position
  
class Btree:

    def __init__(self, order, height):
        self.orderM = order            # M Btree order
        self.height = height           # current height of the tree
        self.root = Bnode()
        self.maxKeys = order - 1  
        M = int((1 - (order*(1-(order**(height-1)))/self.maxKeys))*self.maxKeys)
        N = (self.orderM - 2) + 2
        self.matrix = [[ 0 for i in range(M) ] for j in range(N)] 

    
    def toMatrix(self, node):
        """Input: Receive a node with differents keys
           Output: If is a leaf add elements to the matrix
                   else continue with the subtree
        """  
        global num_c
        index = 0
        if len(node.subtree) == 0:              #is a leaf
            list_node.append(node.keys)
            for key in node.keys:
                self.brothers(node.keys, key)   #add brothers
                num_c += 1                      #move next column
                
        
        else: 
            for i in node.subtree:              #childs
                self.toMatrix(i)
                if len(node.keys) > index:
                    list_node.append([node.keys[index]])
                    self.brothers(node.keys, node.keys[index])
                    self.add_subtrees(i, node, index)
                    num_c += 1
                    index += 1
 
    def add_subtrees(self, i , node, index):
        """Input: Receive a node
           Output: See if is a left or right tree 
           add the first element of the node
        """  

        if index == 0 and i.keys[0] < node.keys[index]:
           self.put_tree(self.maxKeys-1, i.keys[0])
        elif i.keys[0] < node.keys[index] and i.keys[0] > node.keys[index-1]:
           self.put_tree(self.maxKeys-1, i.keys[0])
 
 
    def brothers(self, nodes, key):
        """Input: Receive a node and a specific key
           Output: Matrix with brothers of this key
        """  
        for i in nodes:
            if i != key:
               self.put_elemt(i)

    def put_elemt(self, num):
        """Input: Receive a num
           Output: Add element to a list
        """ 
        i = 0
        while self.matrix[i][num_c] != 0:
            i+=1
        
        self.matrix[i][num_c] = num

    def put_tree(self, i, num):
        """Input: Receive a num and position row
           Output: Add element to a list
        """ 
        while self.matrix[i][num_c] != 0:
            i+=1
        
        self.matrix[i][num_c] = num



    def print_matrix(self):
        """ Output: Matrix with all elements """ 
        print(list_node)  #Flatten the list of nodes
        len_list = len(list_node)

        for i in self.matrix:
            print(i[:len_list])
        


def main():
  """
     Main function to create a Btree
  """ 
  global list_node 
  B = Btree(3, 3)    #Order 3, Height 3
  
  #Create nodes
  n1 = Bnode()
  n2 = Bnode()
  n3 = Bnode()
  n4 = Bnode()
  n5 = Bnode()
  n6 = Bnode()
  n7 = Bnode()
  n8 = Bnode()

  n1.keys = [25]
  n2.keys = [15]
  n3.keys = [37,45]
  n4.keys = [4,11]
  n5.keys = [22]
  n6.keys = [35]
  n7.keys = [43]
  n8.keys = [67,77]

  n2.subtree = [n4, n5]
  n3.subtree = [n6, n7, n8]
  n1.subtree = [n2,n3]

  B.root = n1

  B.toMatrix(B.root)
  print('Result Matrix')
  list_node = sum(list_node, [])
  B.print_matrix()


if __name__ == '__main__':
  main()
