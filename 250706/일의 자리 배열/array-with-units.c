#include <stdio.h>

int main() {
    int a, b;
    scanf("%d %d", &a, &b);

    int arr[10];
    arr[0]=a;
    arr[1]=b;

    int n;
    for (int i=0; i<10; i++){
        arr[i+2]=arr[i]+arr[i+1];
    }
    for (int i=0; i<10; i++){
        n=arr[i];
        n %= 10;
        printf("%d ", n);
    }
    return 0;
}