section .data
    hello db 'Hello, World!', 0
section .text
    global _start
_start:
    ; write hello
    mov eax, 4
    mov ebx, 1
    mov ecx, hello
    mov edx, 13
    int 0x80

    ; exit
    mov eax, 1
    xor ebx, ebx
    int 0x80