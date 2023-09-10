#include <stdio.h>
#include <stdlib.h>

int main(){
	int done = 0;
	int fTemp = 70;
	while(done == 0){
		int choice;
		int cTemp;
		printf("Welcome to the reactor's admin interface!\n'");
		printf("What would you like to do?\n");
		
		printf("1. Check temperature\n");
		printf("2. Change temperature\n");
		printf("3. Exit\n");
		fflush(stdin);
		scanf("%d", &choice);	
		if(choice == 1){
			if(fTemp > 2000000000){
				printf("AAAAAAAAAAAAAAAAAAAAH TOO HOT!!!!!!\n");
				printf("FLAG\n");
			}else{
				printf("temperature is %d degress F\n\n", fTemp);
			}
		
		
		}else if(choice == 2){
			printf("What temperature would you like to set the reactor too? (Celsius)\n");
			fflush(stdin);
			scanf("%d", &cTemp);
			if(cTemp < 500){
				//whose idea was it to take celsius input and then convert to fahrenheit
				fTemp = cTemp * 2 + 32;
				printf("temperature changed to: %d degrees F\n\n", fTemp);
				
			}else{
				printf("Woah! Too hot, could not change\n\n");
			}
		
		}else{
			done = 1;
		}
		
	}
}
