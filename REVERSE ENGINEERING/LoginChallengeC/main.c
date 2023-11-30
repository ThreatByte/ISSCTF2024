#include <stdio.h>
#include <string.h>


int main() {
    char username[50];
    char password[50];

    printf("Username: ");
    scanf("%s", username);

    printf("Password: ");
    scanf("%s", password);

    int found = 0;
    for (int i = 0; i < sizeof(users) / sizeof(users[0]); i++) {
        if (strcmp(username, users[i].username) == 0 &&
            strcmp(password, users[i].password) == 0) {
            found = 1;
            break;
        }
    }

    if (found) {
        printf("Login successful!\n");
    } else {
        printf("Login failed!\n");
    }

    return 0;
}
