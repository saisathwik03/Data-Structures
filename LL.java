# Question: Given an array of integer arr. Your task is to construct the linked list from arr & return the head of the linked list.

# CODE:

class LL {
    static Node constructLL(int arr[]) {
    // code here
    if(arr.length == 0){
        return null;
    }
    
    Node head = new Node(arr[0]);
    Node current = head;
    
    for(int i=1; i<arr.length; i++){
        current.next = new Node(arr[i]);
        current = current.next;
    }
    
    return head;
    }
}