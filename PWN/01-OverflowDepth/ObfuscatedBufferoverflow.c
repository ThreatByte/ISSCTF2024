#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void dynamic_decode(char *str, int len, char key) {
    for (int i = 0; i < len; i++) {
        str[i] ^= key;
    }
}

void secret_spy_function() {
    char part1[] = {239, 217, 218, 195, 197, 196, 0x00};  // Espiona (XORed with 0xAA)
    char part2[] = {203, 205, 207, 233, 254, 0x00};  // geCTF{ (XORed with 0xAA)
    char part3[] = {236, 209, 154, 220, 153, 0x00};  // 0v3rf (XORed with 0xAA)
    char part4[] = {216, 204, 198, 154, 221, 0x00};  // l0w_D (XORed with 0xAA)
    char part5[] = {245, 238, 153, 218, 222, 0x00};  // 3ptH_ (XORed with 0xAA)
    char part6[] = {226, 245, 147, 210, 195, 0x00};  // 9xi7 (XORed with 0xAA)
    char part7[] = {157, 251, 152, 220, 215, 0x00};  // Q2v} (XORed with 0xAA)

    dynamic_decode(part1, sizeof(part1) - 1, 170);
    dynamic_decode(part2, sizeof(part2) - 1, 170);
    dynamic_decode(part3, sizeof(part3) - 1, 170);
    dynamic_decode(part4, sizeof(part4) - 1, 170);
    dynamic_decode(part5, sizeof(part5) - 1, 170);
    dynamic_decode(part6, sizeof(part6) - 1, 170);
    dynamic_decode(part7, sizeof(part7) - 1, 170);

    printf("Access Granted! The secret code is: %s%s%s%s%s%s%s\n", part1, part2, part3, part4, part5, part6, part7);
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
