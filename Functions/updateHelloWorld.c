// Julia Properzi, update hello world
#include <stdio.h>


//tname[50], fname[50], momName[50], dadName[50];

 void word(char name){
    printf("hello %s", name); 
    char name[50];
    //char tname[50];
    //char fname[50];
    //char momName[50];
    //char dadName[50];

    printf("Please tell me your name:\n");
    scanf("%s", name);
    hello(name);
    return 0;
}


//int main(void){
    //printf("What is your name:\n");
    //scanf("%s", name);
    //printf("Hello {name})
    //printf("What is your teachers name:\n");
    //return 0;
//}