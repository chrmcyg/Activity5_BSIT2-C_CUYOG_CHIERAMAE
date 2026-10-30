# Stacks and Queues: Array vs. Linked List

Implements `ArrayStack`, `LinkedStack`, circular `ArrayQueue`, and `LinkedQueue` from scratch, plus a menu-driven driver and two applications.

## Files
- `structures.py` – the four classes and the shared `Node`
- `applications.py` – balanced-parentheses checker (stack) and print-queue simulation (queue)
- `main.py` – menu-driven program
- `analysis.md` – written answer to the analysis question

## How to run
Requires Python 3.
```
python main.py            # menu: choose implementation, run operations
python applications.py    # run the two application demos directly
```
In `main.py` pick option 1, then an implementation (1 ArrayStack, 2 LinkedStack, 3 ArrayQueue, 4 LinkedQueue). Array versions ask for a capacity. The structure's state prints after every operation. Underflow/overflow raise exceptions that the menu reports.
