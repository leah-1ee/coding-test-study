#include <stdio.h>

int main() {
    int a;
    int count=0;

    scanf("%d", &a);

    for (int i=1; i<=a; i++){
        if (i%2!=0 && i%3!=0 && i%5!=0){
            count++;
        }
    }
    printf("%d", count);
    return 0;
}