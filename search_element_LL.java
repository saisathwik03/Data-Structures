// Question: Given a linked list of n nodes and a key
// the task is to check if the key is present in the linked list or not.

// CODE:

// class Solution {
//     static boolean searchKey(int n, Node head, int key) {
//         // Code here
        
//         Node current;
        
//         if(head == null){
//             return false;
//         }
        
//         current = head;
        
//         while(current != null){
//             if(key == current.data){
//                 return true;
//             }
//             current = current.next;
//         }
//         return false;
//     }
// }