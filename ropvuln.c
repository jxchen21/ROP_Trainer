#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void shell()
{
    execve("/bin/sh", NULL, NULL);
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