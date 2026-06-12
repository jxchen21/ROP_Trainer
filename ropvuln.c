#include <stdio.h>
#include <string.h>

void target(char *password, int password_len, int is_admin)
{
    if (strncmp(password, "wellsfargo", password_len) == 0 && is_admin == 1)
    {
        printf("Welcome, admin!\n");
    }
    return;
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