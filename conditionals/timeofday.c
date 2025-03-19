// Julia Properzi, time of day C
#include <stdio.h>
#include <time.h>

int main(void){
    time_t t;
    struct tm *tm_info;

    time(&t);
    tm_info= localtime(&t);

    printf("%d\n", tm_info-> tm_hour);

    if(tm_info-> tm_hour <= 12){
        printf("Good Morning!\n");
    } else if (tm_info -> tm_hour <=18){
        printf("Good afternoon!\n");
    }else {
        printf("Good evening!\n");
    }
    return 0;
}