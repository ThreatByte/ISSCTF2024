#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void dynamic_decode(char *str, int len, char key) {
    for (int i = 0; i < len; i++) {
        str[i] ^= key;
    }
}

void secret_spy_function() {
    char part1[] = {233, 254, 236, 209, 154, 0x00};  // CTF{0 (XORed with 0xAA)
    char part2[] = {220, 153, 216, 204, 198, 0x00};  // v3rfl (XORed with 0xAA)
    char part3[] = {154, 221, 245, 238, 153, 0x00};  // 0w_D3 (XORed with 0xAA)
    char part4[] = {218, 222, 226, 245, 147, 0x00};  // ptH_9 (XORed with 0xAA)
    char part5[] = {210, 195, 157, 251, 152, 220, 215, 0x00};  // xi7Q2v} (XORed with 0xAA)

    dynamic_decode(part1, sizeof(part1) - 1, 170);
    dynamic_decode(part2, sizeof(part2) - 1, 170);
    dynamic_decode(part3, sizeof(part3) - 1, 170);
    dynamic_decode(part4, sizeof(part4) - 1, 170);
    dynamic_decode(part5, sizeof(part5) - 1, 170);

    printf("Access Granted! The secret code is: %s%s%s%s%s\n", part1, part2, part3, part4, part5);
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
