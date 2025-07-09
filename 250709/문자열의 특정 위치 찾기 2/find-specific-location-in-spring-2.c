#include <stdio.h>
#include <string.h>

int main() {
    char* fruit[5] = {"apple", "banana", "grape", "blueberry", "orange"};
    char n;
    int num=0;
    
    scanf("%c", &n);
    
    for (int i=0; i<5; i++){
        if (fruit[i][2]==n){
            num++;
            printf("%s\n", fruit[i]);
        }
        else if (fruit[i][3]==n){
            num++;
            printf("%s\n", fruit[i]);
        }
    }
    printf("%d", num);
    return 0;
}