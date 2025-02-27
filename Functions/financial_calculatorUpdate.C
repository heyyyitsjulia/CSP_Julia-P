// Julia Properzi, Financial Calculator Update C
#include <stdio.h>

double values(char*type){
    double amount;
    printf("How much is your %s: \n", type);
    scanf("%lf", &amount);
    return amount;
}

void info(double cost, double income, char*type){
    double percent = (cost/income) *100;
    printf("Your %s is $%.2f which is %.2f%% of your income. \n", type, cost, percent);
}

int main(){
    double income = values("income");
    double rent = values("rent");
    double utilities = values("utilites");
    double groceries = values("groceries");
    double transportation = values("transportation");

    double savings = income *.1;
    double spending = income-rent-utilities-groceries-transportation-savings;

    info(rent, income,"rent");
    info(utilities, income, "utilites");
    info(groceries, income, "groceries");
    info(transportation, income, "transportation");
    info(savings, income, "savings");
    info(spending, income, "spending");

    return 0;
}
