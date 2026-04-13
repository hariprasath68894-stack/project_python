queue = []

while True:
    print("\nQueue Operations Menu")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Frount")
    print("4. Rear")
    print("5. isEmpty")
    print("6. Display")
    print("7. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        val = int(input("Enter value: "))
        queue.append(val)
        print("Enqueue:", val)

    elif choice == 2:
        if len(queue) == 0:
            print("Queue Underflow")
        else:
            print("Dequeued:", queue.pop(0))

    elif choice == 3:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Frount element:", queue[0])

    elif choice == 4:
        if len(queue) == 0:
            print("Queue is empty")
        else:
            print("Rear element:", queue[-1])

    elif choice == 5:
        print("Is queue empty?", len(queue) == 0)

    elif choice == 6:
        print("Queue:", queue)

    elif choice == 7:
        break

    else:
        print("Invalid choice!")