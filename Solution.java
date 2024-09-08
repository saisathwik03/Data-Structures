class Node {
    int val;
    Node next;
    Node(int x) { val = x; }
}

public class Solution {
    public int getCount(Node head) {
        int count = 0;
        Node current = head;
        
        while (current != null) {
            count++;
            current = current.next;
        }
        
        return count;
    }
}
