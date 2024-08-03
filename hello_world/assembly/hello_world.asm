; hello_world.asm
global _main            ; declares the entry point of program
extern _printf          ; printf function from the C standard library

section .data           ; data section defines our data (obviously)
    message db "Hello, World!", 0xA, 0   ; 0xA is the newline character, 0 is the null terminator

section .text           ; contains code instructions
_main:                  ; main function 
    push rbp            ; pushes the base pointer (rbp) onto the stack.
    mov rbp, rsp        ; moves current stack pointer (rsp) into rbp

    lea rdi, [rel message] ; loads effective address of variable into the rdi register
    xor eax, eax        ; clear eax register
    call _printf

    xor eax, eax        ; return 0
    pop rbp
    ret                 ; returns from funciton - exits program
