# DSA Lab Tasks

A collection of Data Structures and Algorithms lab programs written in Python and C++. The repository includes source code, a few compiled Windows executables, and screenshots of lab experiments.

## Repository layout

```text
DSA_Lab_Tasks/
├── README.md
└── DSA Lab/
    ├── DSA Code/
    │   ├── Python and C++ source files
    │   ├── Compiled Windows executables (.exe)
    │   └── .vscode/settings.json
    └── Output ScreenShots/
        ├── Experiment-1.png
        ├── Experiment-2.png
        └── Experiment-3.png
```

## Topics and programs

- **Trees:** Binary search tree examples, including a recursive post-order traversal program.
- **Graph traversal:** Breadth-first search (BFS) and depth-first search (DFS).
- **Searching:** Binary search in C++.
- **Sorting:** Insertion, merge, quick, and selection sort examples; merge sort is also provided in C++.
- **Linked lists:** Singly and doubly linked list examples in Python, plus a singly linked list program in C++.
- **Stacks and deques:** Stack operations, deque with an array, and deque with a doubly linked list.
- **Other exercises:** Maximum element program in C++.
- **Experiment records:** Screenshots are kept in the `Output ScreenShots` folder.

## Requirements

- Python 3 for the Python programs.
- A C++ compiler such as g++ or MinGW for the C++ source files.

The programs are independent lab exercises. Run the one you want to explore; there is no single application entry point.

## Running the programs

From the repository root, run a Python program with:

```powershell
python "DSA Lab/DSA Code/Binary_Search_Tree.py"
```

Compile and run a C++ program with g++:

```bash
g++ "DSA Lab/DSA Code/Merge_Sorting.C++" -o merge_sort
./merge_sort
```

On Windows, run the compiled program with:

```powershell
.\merge_sort.exe
```

Replace the example filename with the program you want to run. The checked-in `.exe` files are Windows builds; compiling from source is recommended when using another operating system or compiler.

## Screenshots

- [Experiment 1](DSA%20Lab/Output%20ScreenShots/Experiment-1.png)
- [Experiment 2](DSA%20Lab/Output%20ScreenShots/Experiment-2.png)
- [Experiment 3](DSA%20Lab/Output%20ScreenShots/Experiment-3.png)
