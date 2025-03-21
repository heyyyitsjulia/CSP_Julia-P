// Julia Properzi, Fizzbuzz C
#include <stdio.h>

int main() {
    int x = 0;
while (x < 51) {
    x = x + 1;
if (x % 3 == 0 && x % 5 == 0){
    printf("Fizzbuzz\n");
}
else if (x % 3 == 0){
    printf("fizz");
} 
else if ( x % 5 == 0){
    printf("buzz");
}else{
    printf("%d\n", x);
}
    
    }
    return 0;
}