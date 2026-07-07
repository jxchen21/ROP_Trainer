#include <stdio.h>
#include <string.h>
#include <stdlib.h>

const char admin_password[] = "wellsfargo";

void target(char *password, int password_len, int is_admin)
{
    if (is_admin != 1 || strncmp(password, admin_password, password_len) != 0)
    {
        printf("Authentication required, exiting now...\n");
        return;
    }

    printf("Welcome, admin!\n");
}

void vulnerable(char *filename)
{
    char buf[64];
    read_input(buf, filename);
}

int main(int argc, char *argv[])
{
    if (argc < 2)
    {
        fprintf(stderr, "Error: Need a command-line argument\n");
        return 1;
    }

    vulnerable(argv[1]);

    return 0;
}