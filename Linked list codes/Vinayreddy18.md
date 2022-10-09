# Linked list operations in Python


# Create a node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data)

        new_node.next = self.head
        self.head = new_node

    # Insert after a node
    def insertAfter(self, prev_node, new_data):

        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # Insert at the end
    def insertAtEnd(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node

    # Deleting a node
    def deleteNode(self, position):

        if self.head is None:
            return

        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return

        # Find the key to be deleted
        for i in range(position - 1):
            temp = temp.next
            if temp is None:
                break

        # If the key is not present
        if temp is None:
            return

        if temp.next is None:
            return

        next = temp.next.next

        temp.next = None

        temp.next = next

    # Search an element
    def search(self, key):

        current = self.head

        while current is not None:
            if current.data == key:
                return True

            current = current.next

        return False

    # Sort the linked list
    def sortLinkedList(self, head):
        current = head
        index = Node(None)

        if head is None:
            return
        else:
            while current is not None:
                # index points to the node next to current
                index = current.next

                while index is not None:
                    if current.data > index.data:
                        current.data, index.data = index.data, current.data

                    index = index.next
                current = current.next

    # Print the linked list
    def printList(self):
        temp = self.head
        while (temp):
            print(str(temp.data) + " ", end="")
            temp = temp.next


if __name__ == '__main__':

    llist = LinkedList()
    llist.insertAtEnd(1)
    llist.insertAtBeginning(2)
    llist.insertAtBeginning(3)
    llist.insertAtEnd(4)
    llist.insertAfter(llist.head.next, 5)

    print('linked list:')
    llist.printList()

    print("\nAfter deleting an element:")
    llist.deleteNode(3)
    llist.printList()

    print()
    item_to_find = 3
    if llist.search(item_to_find):
        print(str(item_to_find) + " is found")
    else:
        print(str(item_to_find) + " is not found")

    llist.sortLinkedList(llist.head)
    print("Sorted List: ")
    llist.printList()





















<!--   creating linkedlist operations in c++ -->
#include<bits/stdc++.h>
  
#include<stdio.h>
  
using namespace std;

<!--   creating structure for node -->
struct node
{
  
    int data;
    struct node* next;
  
}*first=NULL;

<!--   created linkedlist by passing array elements as parameters -->
void create(int a[],int n)
{

    struct node* t;
    struct node* last;
    first=(struct node*)malloc(sizeof(struct node));
    first->data=a[0];
    first->next=NULL;
    last=first;
    for(int i=1;i<n;i++)
    {
        t=(struct node*)malloc(sizeof(struct node));
        t->data=a[i];
        t->next=NULL;
        last->next=t;
        last=t;
    }
    
}
<!--   inserting in  a linked list -->
 void Insert(struct node *p,int index,int x)
{
  
  
 struct Node *t;
 
 int i;
 
 if(index < 0 || index > count(p))
 return;
 t=(struct node *)malloc(sizeof(struct node));
 t->data=x;
 
 if(index == 0)
 {
 t->next=first;
 first=t;
 }
 else
 {
 for(i=0;i<index-1;i++)
 p=p->next;
 t->next=p->next;
 p->next=t;
 
 }
 
}
  
<!--   removing nth node from end ---brute force approach -->
 void removen(struct node* p,int x)
 {
 
     int c=0;
     struct node* q=p;
     while(q!=NULL)
     {
         c++;
         q=q->next;
     }
     q=p;
     int y=c-x;
     for(int i=0;i<y-1;i++)
     {
         q=q->next;
     }
     struct node* t=q->next;
     q->next=q->next->next;
     delete(t);
    
 }

<!--   removing nth node from end --optimized approach -->
struct node* removen(struct node* p,int x)
{
    struct node* dummy=(struct node*)malloc(sizeof(struct node));
<!--   node* dummy=new node; // creating node in c++ -->
    dummy->next=p;
    struct node* fast=dummy;
    struct node* slow=dummy;
    for(int i=1;i<=x;i++)
    {
        fast=fast->next;
    }
    while(fast->next!=NULL)
    {
        fast=fast->next;
        slow=slow->next;
    }
    slow->next=slow->next->next;
    return dummy->next;
}
<!--   deleting in a linkedlist -->
  
  int Delete(struct Node *p,int index)
{

 struct Node *q=NULL;
 int x=-1,i;
 
 if(index < 1 || index > count(p))
 return -1;
 if(index==1)
 {
 q=first;
 x=first->data;
 first=first->next;
 free(q);
 return x;
 }
 else
 {
 for(i=0;i<index-1;i++)
 {
 q=p;
 p=p->next;
 }
 q->next=p->next;
 x=p->data;
 free(p);
 return x;
 
 }
  
<!--   displaying the linkedlist -->
void display(struct node* p)
{
    while(p->next!=NULL)
    {
        cout<<p->data<<"->";
        p=p->next;
    }
    cout<<p->data;
}
  
<!--   main function -->
int main()
{
  
  int n;
<!--number of elements in a linked list -->
    cin>>n;
<!--   taking input for number of elements -->
    int a[n];
<!--   creating array of n elements -->
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
<!--   taking input in an array for n elements -->
    create(a,n);
<!--   created array to a linkedlist. -->
    display(first);
    cout<<endl;
  Insert(first,0,n);
  display(first);
  
  printf(“%d\n",Delete(first),2);
<!--   deleting in a linkedlist -->
    int x;
<!--   removing nth node from linked list -->
    cin>>x;
   
  struct node* q=removen(first,x);
<!--   nth node from end is removed -->
   
  display(q);
<!--   displaying the linkedlist after removing nth node. -->
    return 0;
}
