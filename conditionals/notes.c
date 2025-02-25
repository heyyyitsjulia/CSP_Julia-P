// Julia Properzi, Conditionals notes C
#include <stdio.h>
#include <string.h> // needed to compare strings

char name[] = "vienna";
int num;

int main(void){
//How do you write an if statement in C?
if(strcmp(name, "Vienna") == 0){ // strcmp means string comparison when the outcome is 0 the strings are the same.
    
    printf("Hello Ms. LaRose, welcome to class.\n");

//How do you write else statements in C?
}else{
    printf("Hello %s, welcome to my class.\n", name);
}

printf("How many siblings do you have?\n");
scanf("%d", &num );
//How do you write elif/ else if statements in C?
if(num== 0){
    printf("You are an only child");
}else if(num <= 2){
    printf("You have a couple of siblings");
}else if(num<=5){
    printf("You have a few siblings");
}else{
    printf("You have a lot of siblings\n");
}
//How do you write the 3 logical operators in C?
// && = and
// || = or
// ! = not

if(num ==7 || num ==13 ){
    printf("%d is an unlucky number\n", num);
}else if (num<10 && num < 5){
    printf("%d is a large single digit number\n", num);
}else if(!(num <10)){
    if(num=12){
        printf("That is a dosen!\n");
    }else{
        printf("%d is a big number\n", num);
    }
    

}else{
    printf("You typed in %d\n", num);
}
    return 0;
}