class MyQueue {

    int front, rear;
	int arr[] = new int[100005];

    MyQueue()
	{
		front=0;
		rear=0;
	}
	
	//Function to push an element x in a queue.
	void push(int x)
	{
	    rear = rear+1;
	    arr[rear] = x;
	} 

    //Function to pop an element from queue and return that element.
	int pop()
	{
		// Your code here
		if(front<rear){
		    front = front+1;
		    return arr[front];
		}
		else{
		    return -1;
		}
	} 
}
