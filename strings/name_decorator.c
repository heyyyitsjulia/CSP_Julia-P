// Julia Properzi, Name Decorator C
#include <stdio.h>
#include<string.h>

char name[15]; 

char design[50];

int main(void){
    printf("What is your name?\n");
    scanf("%s", name);
    strcpy(design, "<<<<");
    strcat (design, name);
    strcat(design, ">>>>");
    printf("%s", design);

    return 0;
}