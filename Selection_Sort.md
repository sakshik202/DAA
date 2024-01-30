### Selection Sort Correctness

**Functioning of Selection Sort:** The algorithm separates the list into two parts - a sorted section and an unsorted section. In every step, it finds the smallest element in the unsorted part and moves it to the sorted part.

**Key Principles:**

At each step, the sorted section at the beginning of the list contains the elements in their final, sorted positions.
The unsorted section holds the elements still to be sorted.

**Completion:** When the algorithm completes, these principles ensure the entire list is sorted. This happens because each iteration places the smallest element of the unsorted section in its correct position, thus sorting the whole list step by step.

In summary, the correctness of Selection Sort lies in its methodical approach of selecting and placing the smallest unsorted element in its right position iteratively, ensuring the list is sorted by the end of the process.
