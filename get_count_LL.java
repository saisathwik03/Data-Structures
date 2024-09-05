// Question: Given a singly linked list. The task is to find the length of the linked list, 
// where length is defined as the number of nodes in the linked list.

// CODE:

class Solution {
    // Function to count nodes of a linked list.
    public int getCount(Node head) {
        // code here
        int count = 0;
        Node current;
        
        if(head == null){
            return count;
        }
        
        current = head;
        
        while(current != null){
            count=count+1;
            current = current.next;
        }
        
        return count;
    }
}