//main.c: made by michael aaron nolk
#include <stdio.h>
#include <string.h>
#include "users.h"

int main() {
    char username[50];
    char password[50];

    //system("cls"); // Clear the console screen

     // Set text color to yellow
    

    printf("\n\t*************************************************");
    printf("\n\t*        Welcome to 0xDoc Sharing Server        *");
    printf("\n\t*************************************************\n\n");

    
    
	

    printf("0x999 ~ Please enter in your Login Key: ");
    scanf("%s", username);

    //printf("Password: ");
    //scanf("%s", password);

    int found = 0;
    for (int i = 0; i < num_users; i++) {
        if (strcmp(username, users[i].username) == 0) {
            found = 1;
            break;
        }
    }

    if (found) {
        printf("Login successful! \n Document List\n   ~%s\n", users[0].password); // output with flag
    } else {
        printf("Login failed!\n");
    }

    return 0;
}
