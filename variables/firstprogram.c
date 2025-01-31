#include <stdio.h>

char name[] = "Julia";
int age = 15;
char color[] = "purple";

int main(void){
    printf("Hello i am %s. I am %d years old. I like the color %s\n", name, age, color);
    printf("%d\n", age);
    printf("%s\n", color);
    return 0;
}