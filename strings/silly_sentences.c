// Julia Properzi, silly sentences C
#include <stdio.h>
// empty string variables for user words (minimun 3)
char adjective [20];
char celebrity[20];
char verb[20];
char place[20];
char emotion[20];
int main(void){
    
    printf("Tell me an adjective:\n");
    scanf("%s", adjective);
    printf("Tell me a celebrity:\n");
    scanf("%s", celebrity);
    printf("Tell me a verb: \n");
    scanf("%s", verb);
    printf("Tell me a place: \n");
    scanf("%s", place);
    printf("Tell me an emotion:\n");
    scanf("%s", emotion);

    printf("It was a %s day when I saw %s %s all the way to %s. When I saw this I was very %s. I could not believe I just witnessed that.", adjective, celebrity, verb, place, emotion);


    return 0;
}