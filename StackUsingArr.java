public class StackUsingArr {
    private int[] arr;
    private int top;

    public StackUsingArr() {
        arr = new int[1000];
        top = -1;
    }

    public void push(int x) {
        if (top == arr.length - 1) {
            return;
        }
        arr[++top] = x;
    }

    public int pop() {
        if (top == -1) {
            return -1;
        }
        return arr[top--];
    }

    public int peek() {
        if (top == -1) {
            return -1;
        }
        return arr[top];
    }

    public boolean search(int a) {
        for (int i = 0; i <= top; i++) {
            if (arr[i] == a) {
                return true;
            }
        }
        return false;
    }

    public void printStack() {
        if (top == -1) {
            System.out.println("Stack is empty");
            return;
        }
        System.out.print("Stack: ");
        for (int i = 0; i <= top; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
}

class Main {
    public static void main(String[] args) {
        StackUsingArr s = new StackUsingArr();

        s.push(20);
        s.printStack();
        s.push(30);
        s.printStack();
        s.push(40);
        s.printStack();
        s.push(50);
        s.printStack();
        s.push(60);
        s.printStack();

        s.pop();
        s.pop();
        s.printStack();

        System.out.println("Top element: " + s.peek());
        System.out.println("Is 20 in stack: " + s.search(20));
        System.out.println("Is 0 in stack: " + s.search(0));
    }
}
