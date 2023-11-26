#include <stdio.h>
#include <stdlib.h>

int main(){
	printf("Welcome to the reactor's admin interface!\n");
	int done = 0;
	int fTemp = 70;
	while(done == 0){
		int choice;
		int cTemp;
		printf("What temperature would you like to set the reactor to? (Celsius)\n");
		fflush(stdin);
		scanf("%d", &cTemp);
		if(cTemp < 500){
			//whose idea was it to take celsius input and then convert to fahrenheit??????????
			fTemp = cTemp * 2 + 32;
			if(fTemp > 2000000000){
				printf("temperature is %d degress F\n\n", fTemp);
				printf("AAAAAAAAAAAAAAAAAAAAH TOO HOT!!!!!!\n");
				printf("FLAG\n");
				done = 1;
			}else{
				printf("temperature is %d degress F\n\n", fTemp);
			}
				
			}else{
				printf("Woah! Too hot, could not change\n\n");
			}
	}
}
