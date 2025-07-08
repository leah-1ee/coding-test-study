#include <stdio.h>
#include <string.h>

int main() {
    char str1[21];
    char str2[21];
    int lon1;
    int lon2;

    scanf("%s %s", str1, str2);

    lon1 = strlen(str1);
    lon2 = strlen(str2);

    if (lon1>lon2){
        printf("%s %d", str1, lon1);
    }
else if (lon1==lon2){
        printf("same");
}

    else{
        printf("%s %d", str2, lon2);
    }


    return 0;
}