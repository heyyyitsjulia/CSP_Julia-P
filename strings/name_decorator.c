// Julia Properzi, Name Decorator C
#include <stdio.h>
#include<string.h>

char name[15]; 

int main(void){
    printf("What is your name?\n");
    scanf("%s", name);
    char d []= "<<<<";
    char o [] = ">>>>";
    printf("%s%s%s", d, name, o);
    return 0;
}