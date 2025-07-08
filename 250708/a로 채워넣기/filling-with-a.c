#include <stdio.h>
#include <string.h>

int main() {
    char str1[101];
    int lon1;

    scanf("%s",str1);

    str1[1]='a';
    lon1=strlen(str1);
    str1[lon1-2]='a';
    printf("%s", str1);
    
    return 0;
}