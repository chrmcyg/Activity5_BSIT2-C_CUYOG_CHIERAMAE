"""Pair-work application exercises."""
from structures import LinkedStack, LinkedQueue


def is_balanced(text):
    """True if every ( [ { has a matching closer in the right order."""
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = LinkedStack()
    for ch in text:
        if ch in "([{":
            stack.push(ch)
        elif ch in pairs:
            if stack.is_empty() or stack.pop() != pairs[ch]:
                return False
    return stack.is_empty()   # leftovers mean unmatched openers


def simulate_print_queue(jobs):
    """jobs: list of (job_id, pages). Prints in FIFO order, reports wait order."""
    q = LinkedQueue()
    for job in jobs:
        q.enqueue(job)
    order, pages_before = 1, 0
    while not q.is_empty():
        job_id, pages = q.dequeue()
        print(f"#{order}: printing {job_id} ({pages} pages) "
              f"- waited for {pages_before} pages ahead of it")
        pages_before += pages
        order += 1


if __name__ == "__main__":
    for s in ["{[()]}", "([)]", "((", "", "a(b)c"]:
        print(f"{s!r:10} balanced? {is_balanced(s)}")
    print()
    simulate_print_queue([("DOC-101", 5), ("DOC-102", 12), ("DOC-103", 2)])
