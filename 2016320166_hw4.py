import string

red = 1
black = 0

class lstack:
    def __init__(self):
        self.L=[]
    def push(self,val):
        self.L.append(val)
    def pop(self):
        return self.L.pop()
    
class Node:
    def __init__(self, newkey):
        self.key = newkey
        self.left = None
        self.right = None
        self.p = None
        self.color = black
    

class RB:
    def __init__(self):
        self.nil = Node(0)
        self.root = self.nil
        self.node_num = 0
        self.black_node_num = 0

    def inorder_traversal(self,tree,stack):
        while len(stack.L) != 0 or tree!= self.nil:
            if tree != self.nil:
                stack.push(tree)
                tree=tree.left
            else:
                tree=stack.pop()
                print(tree.key)
                tree=tree.right

                

    def Right_ro(self, n):
        y = n.left
        n.left = y.right
        if y.right != self.nil:
            y.right.p = n
        y.p = n.p
        if n.p == self.nil:
            self.root =  y
        elif n == n.p.right:
            n.p.right = y
        else:
            n.p.left = y
        y.right = n
        n.p =y        

    def Left_ro(self, n):
        y = n.right
        n.right = y.left
        if y.left != self.nil:
            y.left.p = n
        y.p = n.p
        if n.p == self.nil:
            self.root =  y
        elif n == n.p.right:
            n.p.right = y
        else:
            n.p.left = y
        y.left = n
        n.p = y

    def Tree_Min(self,tree):
        while tree.left != self.nil:
            tree = tree.left
        return tree


    def Transplant(self,x, y):
        if x.p == self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        if y != self.nil:
            y.p = x.p
        

    def RB_insert(self, n):
        self.node_num += 1
        x = self.root
        y = self.nil
        while x != self.nil:
            y = x
            if n.key < x.key:
                x = x.left
            else:
                x = x.right
        n.p = y  
        if y == self.nil:
            self.root = n
        elif n.key < y.key:
            y.left = n
        else:
            y.right = n
        n.left = n.right = self.nil  
        n.color = red
        self.RB_insert_fix(n)

    def RB_insert_fix(self, n):
        while n.p.color == red:
            if n.p == n.p.p.left:
                y = n.p.p.right
                if y.color == red:
                    n.p.color = black
                    y.color = black
                    n.p.p.color = red
                    n = n.p.p
                else:
                    if n == n.p.right:
                        n = n.p
                        self.Left_ro(n)
                    n.p.color = black
                    n.p.p.color = red
                    self.Right_ro(n.p.p)
            else:
                y = n.p.p.left
                if y.color == red:
                    n.p.color = black
                    y.color = black
                    n.p.p.color = red
                    n = n.p.p
                else:
                    if n == n.p.left:
                        n = n.p
                        self.Right_ro(n)
                    n.p.color = black
                    n.p.p.color = red
                    self.Left_ro(n.p.p)
        self.root.color = black



    def search(self, key, x = None):
        if None == x:
            x = self.root
        while x != self.nil and key != x.key:
            if key < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def RB_find_delete(self, n):
        found = self.search(n)
        if found != self.nil:
                self.node_num -= 1
                self.RB_delete(found)
        else:
            print("%d is not found"%(n))



    def RB_delete(self, z):
        y = z
        y_ori_color = y.color
        if z.left == self.nil:
              x = z.right
              self.Transplant(z, z.right)
        elif z.right == self.nil:
              x = z.left
              self.Transplant(z, z.left)
        else:
              y = self.Tree_Min(z.right)
              y_ori_color = y.color
              x = y.right
              if y.p == z:
                  x.p = y
              else:
                  self.Transplant(y, y.right)
                  y.right = z.right
                  y.right.p = y
              self.Transplant(z, y)
              y.left = z.left
              y.left.p = y
              y.color = z.color
        if y_ori_color == black:
              self.RB_delete_fix(x)



    def RB_delete_fix(self, x):
        if x is self.nil:
            return
        while x != self.root and x.color == black:
            if x == x.p.left:
                w = x.p.right
                if w.color == red:
                    w.color = black
                    x.p.color = red
                    self.Left_ro(x.p)
                    w = x.p.right
                if w.left.color == black and w.right.color == black:
                        w.color = red
                        x = x.p
                else:
                    if w.right.color == black:
                        w.left.color = black
                        w.color = red
                        self.Right_ro(w)
                        w = x.p.right
                    w.color = x.p.color
                    x.p.color = black
                    w.right.color = black
                    self.Left_ro(x.p)
                    x = self.root
            else:
                w = x.p.left
                if w.color == red:
                    w.color = black
                    x.p.color = red
                    self.Right_ro(x.p)
                    w = x.p.left
                if w.right.color == black and w.left.color == black:
                        w.color = red
                        x = x.p
                else:
                    if w.left.color == black:
                        w.right.color = black
                        w.color = red
                        self.Left_ro(w)
                        w = x.p.left
                    w.color = x.p.color
                    x.p.color = black
                    w.left.color = black
                    self.Right_ro(x.p)
                    x = self.root
        x.color = black    



    def blacknode_num(self,tree,stack):
        nb = 0
        while len(stack.L) != 0 or tree!= self.nil:
            if tree != self.nil:
                stack.push(tree)
                tree=tree.left
            else:
                tree=stack.pop()
                if tree.color == black:
                    nb +=1
                tree=tree.right
        return nb

    def black_height(self):
        bh = 0
        tree = self.root
        while tree.right != self.nil:
            if tree.color == black:
                    bh +=1
            tree = tree.right
        if tree.color == black:
            bh +=1
        return bh

        

              

def main():
    f = open("input.txt", 'r')
    lines = f.readlines()
    rb = RB()
    stack = lstack()
    for line in lines:
        n=int(line)
        if n > 0:

            rb.RB_insert(Node(n))
        elif n < 0:
            rb.RB_find_delete(n*(-1))
        else :
            print("total = %d"%(rb.node_num))
            print("nb = %d"%(rb.blacknode_num(rb.root,stack)))
            print("bh = %d"%(rb.black_height()))
            rb.inorder_traversal(rb.root,stack)
            f.close()
            break

main()
