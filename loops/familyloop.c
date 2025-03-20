// Julia Properzi, family loops c
#include <stdio.h>

int main(){
    const char *family[]= {"Mauro", "Larissa", "Isabella", "Kristian", "Noemi"};
    int size = sizeof (family)/sizeof(family[0]);

    for (int m=0;m<size;m++){
        printf("Hello %s, I want a puppy.\n", family[m]);
    }

    return 0;
}