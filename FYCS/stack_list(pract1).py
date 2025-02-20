class Stack:
    def _init_(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty.")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty.")

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print(self.items)

def main():
    stack = Stack()

    while True:
        print("\nStack Operations:")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Size")
        print("5. Display")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter item to push: ")
            stack.push(item)
        elif choice == '2':
            item = stack.pop()
            if item:
                print("Popped item:", item)
        elif choice == '3':
            item = stack.peek()
            if item:
                print("Top item:", item)
        elif choice == '4':
            print("Stack size:", stack.size())
        elif choice == '5':
            stack.display()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please choose between 1 and 6.")
            'excepted' "ValueError:"
            print("Invalid input. Please enter a number between 1 and 6.")

    if _name_ == "_main_":
         main()
