#include <stdio.h>
#include <stdlib.h>
int BUFFER_SIZE = 256;

int main(){
	char flag[BUFFER_SIZE];
    FILE *flagfp = fopen("./flag.txt", "r");
    fgets(flag, BUFFER_SIZE, flagfp);
  
	printf("Welcome to the reactor's admin interface!\n");
	int done = 0;
	int fTemp = 70;
	char input[BUFFER_SIZE]; //added a buffer size for input
	
	while(done == 0){
		int choice;
		int cTemp;
		printf("What temperature would you like to set the reactor to? (Celsius)\n");
		fflush(stdout); //flush stdout instead of in
		if (fgets(input, BUFFER_SIZE, stdin) == NULL) {
	        perror("Error reading input");
	        continue;
	    }
	    if (sscanf(input, "%d", &cTemp) != 1) {
	        printf("Invalid input. Please enter a number.\n\n");
	        continue;
	    }
		
		if(cTemp < 500){
			//whose idea was it to take celsius input and then convert to fahrenheit??????????
			fTemp = cTemp * 2 + 32;
			if(fTemp > 2000000000){
				printf("temperature is %d degress F\n\n", fTemp);
				printf("AAAAAAAAAAAAAAAAAAAAH TOO HOT!!!!!!\n");
				puts(flag);
				done = 1;
			}else{
				printf("temperature is %d degress F\n\n", fTemp);
			}
				
			}else{
				printf("Woah! Too hot, could not change\n\n");
			}
	}
}
