# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            return None
        removed_node = self.front
        self.front = self.front.next
        if not self.front:
            self.rear = None
        return removed_node.value
    
    def peek(self):
        if self.front:
            return self.front.value
        else:
            return None
        
    def print_queue(self):
        current = self.front
        if not current:
            print("Queue is Empty")
            return
        while current:
            print(f"{current.value}")
            current = current.next

my_queue = Queue()
my_queue.enqueue("Person A")
my_queue.enqueue("Person B")
my_queue.enqueue("Person C")

my_queue.print_queue()
# - Person A
# - Person B
# - Person C

print(my_queue.dequeue()) # Person A
print(my_queue.peek()) # Person B 

def run_help_desk():
    # Create an instance of the Queue class
    my_queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            # Add the customer to the queue
            my_queue.enqueue(name)
            print(f"{name} added to the queue.")

        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            name = my_queue.dequeue()
            if name is None:
                print("No customers waiting")
            else:
                print(f"Customer {name} has been helped.")


        elif choice == "3":
            name = my_queue.peek()
            if name is None:
                print("No customers waiting")
            else:
                print(f"Customer {name} is next in line.")


        elif choice == "4":
            # Print all customers in the queue
            my_queue.print_queue()
            

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()
