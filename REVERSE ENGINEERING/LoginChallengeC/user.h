#ifndef USERS_H
#define USERS_H

typedef struct {
    char username[50];
    char password[50];
} User;

extern User users[];
extern int num_users;

#endif
