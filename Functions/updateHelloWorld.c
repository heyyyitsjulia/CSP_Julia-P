// Julia Properzi, update hello world
#include <stdio.h>

char name[50]; 
  


 void word(char*name){
   printf("hello %s\n", name);



}int main(void){
    word("bobby");
    word("Eve");
    word("Paul");
    word("Noemi");
    word("josephine");
    return 0;
}