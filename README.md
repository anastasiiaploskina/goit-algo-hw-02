instructions: |
  # **Multi-App Python Utilities**

  This repository contains three small standalone Python applications, each demonstrating work with fundamental data structures: queues, deques, and stacks. The apps are:

  1. **Task 1:** Request Queue Simulator
  2. **Task 2:** Palindrome Checker
  3. **Task 3:** Bracket Closure Validator

  Each app is self-contained and can be executed directly.


## **Table of Contents**

* [Project Overview](#project-overview)
* [Task 1 — Request Queue Simulator](#task-1--request-queue-simulator)

  * [Description](#description)
  * [Features](#features)
  * [How It Works](#how-it-works)
  * [Usage](#usage)
* [Task 2 — Palindrome Checker](#task-2--palindrome-checker)

  * [Description](#description-1)
  * [Features](#features-1)
  * [Usage](#usage-1)
* [Task 3 — Bracket Closure Validator](#task-3--bracket-closure-validator)

  * [Description](#description-2)
  * [Features](#features-2)
  * [Usage](#usage-2)
* [Dependencies](#dependencies)

---

# **Project Overview**

The apps demonstrate how queues, deques, and stacks can be used to solve different programming problems:

* **Queues** simulate incoming and processed requests.
* **Deques** allow efficient palindrome checking from both ends of a string.
* **Stacks** validate balanced brackets in expressions.

These utilities can be used for educational purposes or integrated into larger systems.

---

# **Task 1 — Request Queue Simulator**

## **Description**

This application simulates a stream of incoming requests using a **FIFO queue**. Requests are generated with unique UUIDs and added to a queue until it fills up; then they are processed one by one.

## **Features**

* Uses Python’s `queue.Queue` with a maximum size of **10**.
* Randomly generates 1–10 new requests per cycle.
* Randomly processes 1–10 requests per cycle.
* Displays the internal state of the queue.
* Graceful shutdown via `KeyboardInterrupt`.

## **How It Works**

1. A request is created using `uuid.uuid4()` and added to the queue.
2. Once the queue fills up, the script switches to processing mode.
3. Requests are removed and “processed” with a simulated delay.
4. The queue status is printed after each full cycle.

## **Usage**

Run:

```bash
python task1.py
```

Terminate with **Ctrl + C**.

---

# **Task 2 — Palindrome Checker**

## **Description**

This script checks whether a string is a **palindrome** using a double-ended queue (**deque**).
It removes all non-alphanumeric characters and compares characters from both ends.

## **Features**

* Removes punctuation and spaces automatically.
* Case-insensitive comparisons.
* Uses an efficient `deque` for O(n) operations.
* Comes with built-in test cases using `assert`.

## **Usage**

Run:

```bash
python task2.py
```

To use the function in another project:

```python
from task2 import is_palindrome

print(is_palindrome("A man, a plan, a canal: Panama"))
```

---

# **Task 3 — Bracket Closure Validator**

## **Description**

This program checks if a string contains properly balanced brackets. It supports:

* `()`
* `[]`
* `{}`

It uses a **stack** to ensure that every opening bracket has a corresponding closing bracket in the correct order.

## **Features**

* Validates multiple bracket types.
* Efficient stack-based algorithm.
* Returns `True` if balanced, else `False`.
* Includes built-in tests.

## **Usage**

Run:

```bash
python task3.py
```

Use programmatically:

```python
from task3 import is_closed

print(is_closed("{[()]}()"))  # True
```

---

# **Dependencies**

All three scripts rely only on Python’s **standard library**:

* `uuid`
* `time`
* `random`
* `queue`
* `re`
* `collections.deque`

No external packages are required.
