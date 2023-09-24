#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void secret_spy_function() {
    printf("Access Granted! The secret code is: EspionageCTF{0v3rfl0w_D3ptH_9xi7Q2v}\n");
    exit(0);
}

void handle_communication() {
    char spy_message[64];
    printf("Enter your encrypted message: ");
    gets(spy_message);  // Vulnerable function
    printf("Message received. Verifying...\n");
}

int main() {
    printf("Welcome to the Spy Communication Terminal.\n");
    handle_communication();
    printf("Access Denied! You are not a real spy!\n");
    return 1;
}
