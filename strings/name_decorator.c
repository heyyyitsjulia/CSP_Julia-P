// Julia Properzi, Name Decorator C
#include <stdio.h>
#include<string.h>

int main(void){
    char name[30] = "Julia";
    char capSix[40] = "<<<<";
    strcat(name, ">>>>");
    strcat(capSix, name);
    printf("Hello %s \n", capSix);
    return 0;
}