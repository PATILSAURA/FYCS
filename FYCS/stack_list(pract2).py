class stack:
    def __init__(self):
        # Initialize the stack as an empty list
        self.stack = [ ]

    def is_empty(self):
        # Return True if the stack is empty, else False
        return len(self.stack) == 0

    def push (self,item):
        #Add an item to the stack
        self.stack.append(item)
        print(f"Item '{item}' pushed to stack.")

    def pop(self):
        # remove the top item from the stack and return it 
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
        else:
            item = self.stack.pop()
            print(f"Item '{item}' popped from stack.")
            return item
        
    def peek(self):
        # Return the top item without removing it
        if self.is_empty():
            print("Stack is empty.")
        else:
                print(f"Top item in the stack: '{self.stack[-1]}' ")
                return self.stack[-1]

    def size(self):
        # Return the size (number of item) of the stack
                print("stack size: {len(self.stack) }")
                return len(self.stack)

    def display(self):
        # Display the stack
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Current stack:", self.stack)
            

#Main function to take user input and perform operations
def main():
    stack = Stack ()

    while True:
        print("\nChoose an operation: ")
        print("1.  Push")
        print("2.  Pop")
        print("3.  Peek")
        print("4.  Size")
        print("5.  Display")
        print("6.  Exit")

        try:
            choice = int(input("Enter  your  choice (1-6): ") )

            if choice == 1:
                value = input("Enter value to Push: ")
                stack.push(Value)

            elif choice == 2:
                stack.pop()

            elif choice == 3:
                stack.peek()

            elif choice == 4:
                stack.size()

            elif choice == 5:
                stack.display()

            elif choice == 6:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please choose between 1 and 6.")
        except  ValueError :
            print("Invalid input. Please enter a number between 1 and 6.")

# Run this program
if  __name__ == "__main__":
    main()
