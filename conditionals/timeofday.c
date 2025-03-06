// Julia Properzi, time of day C
#include <stdio.h>
#include <time.h>

time_t now = time(NULL);  
struct tm *local = localtime(&now);  


int main(void){
    printf("Hello World");
    return 0;
}