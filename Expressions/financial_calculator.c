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
    float savings = income*.1;
    float spendings = income-savings-rent-utilities-groceries-transportation;
    float percent_rent = rent/income *100;
    float percent_utilities = utilities/income *100;
    float percent_groceries = groceries/income *100;
    float percent_transportation = transportation/income *100;
    float percent_spending = spendings/income *100;
    printf("Your rent is %.2f which is %.2f percent of your income\n", rent, percent_rent);  
     printf("The utilities cost is %.2f which is %.2f percent of your income\n", utilities, percent_utilities);  
    printf("The cost of your groceries is %.2f which is %.2f percent of your income\n", groceries, percent_groceries);  
    printf("The cost of your transportation is %.2f which is %.2f percent of your income\n", transportation, percent_transportation);  
    printf("Your savings is %.2f which is %.2f percent of your income\n", savings, percent_spending);  
    printf("Your spendings is %.2f which is %.2f percent of your income\n", spendings, percent_spending);
    return 0;
}