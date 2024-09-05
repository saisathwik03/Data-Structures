// Question: Given the head of a Singly Linked List and a value x, 
// insert that value x at the end of the LinkedList and return the modified Linked List.

// CODE:

class Solution {
    // Function to insert a node at the end of the linked list.
    Node insertAtEnd(Node head, int x) {
        
        Node nn = new Node(x);
        
        if(head == null){
            head = nn;
        }
        
        else{
            Node current = head;
            while(current.next != null){
                current = current.next;
            }
            
            current.next = nn;
            nn.next = null;
            
        }
        
        return head;
        
    }
}