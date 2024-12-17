#include <stdio.h>
#include <stdlib.h>
#include "program.h"
#include "util.h"

#define BUFFER 4096

int main() {
    double* arr = malloc(sizeof(double) * 16);
    int size_of_arr = 16;

    // code that uses arr

    free(arr);

    arr = malloc(sizeof(double) * 32);
    size_of_arr = 32;

    arr[0] = 3.1415;

    for (int i = 0; i < size_of_arr; i++)
        printf("%p\n", &arr[i]);
    printf("%lf\n", *arr);

    printf("%d", add(BUFFER, 2));
}