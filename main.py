"""Menu-driven driver for all four implementations."""
from structures import ArrayStack, LinkedStack, ArrayQueue, LinkedQueue
from applications import is_balanced, simulate_print_queue


def choose_structure():
    print("\n1) ArrayStack  2) LinkedStack  3) ArrayQueue  4) LinkedQueue")
    c = input("Choose implementation: ").strip()
    if c in ("1", "3"):
        try:
            cap = int(input("Capacity: "))
            if cap < 1:
                raise ValueError
        except ValueError:
            print("Invalid capacity, using 4.")
            cap = 4
    if c == "1": return ArrayStack(cap), "stack"
    if c == "2": return LinkedStack(), "stack"
    if c == "3": return ArrayQueue(cap), "queue"
    if c == "4": return LinkedQueue(), "queue"
    print("Invalid choice.")
    return None, None


def operate(ds, kind):
    add, rem, look = (("push", "pop", "peek") if kind == "stack"
                      else ("enqueue", "dequeue", "peek_front"))
    while True:
        print(f"\nOperations: 1) {add}  2) {rem}  3) {look}  "
              f"4) is_empty  5) is_full  6) back")
        c = input("> ").strip()
        try:
            if c == "1":
                getattr(ds, add)(input("Value: "))
            elif c == "2":
                print("Removed:", getattr(ds, rem)())
            elif c == "3":
                print("Next:", getattr(ds, look)())
            elif c == "4":
                print("is_empty:", ds.is_empty())
            elif c == "5":
                print("is_full:", ds.is_full())
            elif c == "6":
                return
            else:
                print("Invalid option.")
        except (IndexError, OverflowError) as e:
            print("Error:", e)
        print(ds)


def main():
    while True:
        print("\n=== Main Menu ===\n1) Data structure demo\n2) Balanced parentheses"
              "\n3) Print queue simulation\n4) Quit")
        c = input("> ").strip()
        if c == "1":
            ds, kind = choose_structure()
            if ds:
                operate(ds, kind)
        elif c == "2":
            s = input("Enter string: ")
            print("Balanced" if is_balanced(s) else "NOT balanced")
        elif c == "3":
            simulate_print_queue([("DOC-101", 5), ("DOC-102", 12), ("DOC-103", 2)])
        elif c == "4":
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
