from llist import LList, Node, append


def length(lst):
    """return the length of a finite linked list"""
    count=0
    node=lst.head
    if node!=None:
        count=1
        node=node.next
        while node:
            count+=1
            node=node.next
    print(f'Amount of elements of the list: {count}')



def llprint(lst):
    """print a finite linked list"""
    node=lst.head
    if node==None:
        print('The list is empty, there is no list to print')
    while node != None:
        print(node.val, end=' ')
        node=node.next

    


if __name__ == "__main__":

    llist=LList()
    length(llist)
    llprint(llist)
    
    
