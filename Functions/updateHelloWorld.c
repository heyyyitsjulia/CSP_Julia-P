// Julia Properzi, update hello world
#include <stdio.h>


//tname[50], fname[50], momName[50], dadName[50];

 void word(char name){
    char name[50];
    printf("hello %s", name); 
    char tname[50];
    printf("hello %s", tname);
    char fname[50];
    printf("hello %s", fname);
    char momName[50];
    printf("hello %s", momName);
    char dadName[50];
    printf("hello %s", dadName);

    printf("Please tell me your name:\n");
    scanf("%s", name);
    hello(name);

    printf("Tell me your teachers name:\n");
    scanf("%s", tname);
    hello(tname);

    printf("What is one of your friends name:\n");
    scanf("%s", fname);
    hello(fname);

    printf("What is your mom's name:\n");
    scanf("%s", momName);
    hello(momName);

    printf("what is your dad's name:\n");
    scanf("%s", dadName);
    hello(dadName);


    return 0;
}