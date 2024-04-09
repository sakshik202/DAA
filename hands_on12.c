#include <stdio.h>
#include <stdlib.h>


#define INITIAL_CAPACITY 10

typedef struct {
    int *array;    
    int size;        
    int capacity;    
} DynArray;

void initDynArray(DynArray *arr) {
    arr->array = (int *)malloc(INITIAL_CAPACITY * sizeof(int));
    arr->size = 0;
    arr->capacity = INITIAL_CAPACITY;
}

void addElement(DynArray *arr, int element) {
    // Check if resizing is needed
    if (arr->size >= arr->capacity) {
        // Double the capacity
        arr->capacity *= 2;
        arr->array = (int *)realloc(arr->array, arr->capacity * sizeof(int));
    }
    // Add the element at the end
    arr->array[arr->size++] = element;
}

int getElement(DynArray *arr, int index) {
    if (index < 0 || index >= arr->size) {
        printf("Index out of bounds\n");
        return -1;  // Or handle error in desired way
    }
    return arr->array[index];
}

void freeDynArray(DynArray *arr) {
    free(arr->array);
    arr->size = 0;
    arr->capacity = 0;
}

int main() {
    // Initialize the dynamic array
    DynArray dynArr;
    initDynArray(&dynArr);

    // Add some elements
    int i = 0;
    while (i < 20) {
        addElement(&dynArr, i * 2);
        i++;
    }

    int j = 0;
    while (j < dynArr.size) {
        printf("%d ", getElement(&dynArr, j));
        j++;
    }
    printf("\n");

    freeDynArray(&dynArr);

    return 0;
}
