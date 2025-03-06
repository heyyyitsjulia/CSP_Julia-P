// Julia Properzi, old enough C
#include <stdio.h>

int num;

int main(void){
printf("How old are you:\n");
scanf("%d", &num);
    if(num >= 18){
    printf("You can vote!");
}else if(num >= 16){
    printf("You can drive!");
}else if(num >= 15){
    printf("You can get your learners permit!");
}else if(num > 4){
    printf("You can go to school!");
}else{
    printf("You can't go to school...\n");
    return 0;
}
}