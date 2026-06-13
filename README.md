# ROP_Trainer

(Hopefully) simple ROP chaining demonstration, created by Johnny Chen.

# SETUP

Make sure Docker is installed! To set up the image run setup.sh. To compile, run build.sh, and use the output payload.bin as an output for ropvuln.

[ROPgadget Docs](https://github.com/JonathanSalwan/ROPgadget)

# CHALLENGE 1: ADMIN PASSWORD

Bank of America just pushed this C code to their server, and it seems like we can gain access to their admin login somehow... Can you exploit the vulnerable function to authenticate as an admin user?
