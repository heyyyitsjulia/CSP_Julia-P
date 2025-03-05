// Julia Properzi, loops notes in C
#include <stdio.h>

int main(void){
    //What is a loop? A section of code repeated multiple times
    //What are the two types of loops?
    //while loops
    int start = 0;
    while (start< 5){
        printf("Hello\n");
        start++;
    }
    //for loop
    int q;
    for(q=0;q<5;q++){
        printf("%d\n", q);
    }
    //What is iteration? Repeating something with minor changes each time
    //What are arrays(list)? an array is a variable holding multiple values (same thing just different word in C)
    //How do you make arrays(lists) in C? array items must all be the same data type!
    int grades[] = {88, 97, 100, 70, 72, 99, 61};
    // one set data type, then AFTER naming put brackets and write the length of the list, then the list is surrounded by curly brackets {}, finally commans between each item.
    //  print a single item from a list
    printf("CSP Grade: %d\n", grades[2]);
    // change an item in the array
    grades[2]= 95;
    printf("CSP Grade: %d\n", grades[2]);
    // size of array(list) in bytes
    int size = sizeof(grades);
    //length in arrays(list) items
    int length = sizeof(grades)/sizeof(grades[0]);
    printf("The array is %d items long.\n", length);
    //array with strings
    //first brackets sets length of array(lists)
    //second brackets set the length of each string
    char movies[][20] = {"Cars", "Treasure Planet", "An American Tale", "Marley and Me", "The Avengers"};
    printf("The movie is %s!\n", movies[1]);
    int mlength = sizeof (movies)/ sizeof(movies[0]);
    //How do you make for loops in C?
    // set the iterator, keeps track of times through the loop (best practice to set as x or i)
    int x;
    // in parens (starting point; ending point; count by)
    for(x=0;x<=10;x+=2){
        printf("%d\n", x);
    }
    int m;
    for(m=0;m<mlength;m++){
        printf("%s \n", movies[m]);
    }
    //How do you make while loops in C?
    int w = 0;

    while(w>=0){// stop point
        printf("%d\n", w);
        w -= 10;//what we count by
    }
    
    return 0;
}