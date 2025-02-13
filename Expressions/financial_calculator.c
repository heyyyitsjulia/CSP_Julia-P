// Julia Properzi, Financial Calculator C
#include <stdio.h>

float income;
float rent;
float utilities;
float groceries;
float transportation;
float savings;

int main(void){
    printf("Welcome to my program this will create a personal finance calculator and will help you figure out how much you need to put into\nsavings, based off your income and expenses!\n");
    printf("What is your monthly income (don't use commas): \n");
    scanf("%f", &income);
    printf("What is your monthly rent?\n");
    scanf("%f", &rent);
    printf("What is the cost of your utilities? every month\n");
    scanf("%f", &utilities);
    printf("What is the average cost of your groceries?\n");
    scanf("%f", &groceries);
    printf("How much does it cost for your transportation?\n");
    scanf("%f", &transportation);
    printf(&income*.1);
    return 0;
}