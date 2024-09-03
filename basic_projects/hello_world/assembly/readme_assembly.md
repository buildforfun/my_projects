hello world in assembly
----
assembly language is specific to architecture you are running the program on. For example i am running on an x86 assmebly.

creating object file
----
- cmd:  nasm -f macho64 hello_world.asm
- converts assembly code into machine code, creating an object file - hello_world.o. This is 64 bit macos.

link object file
---
- cmd: ld -lSystem -syslibroot `xcrun -sdk macosx --show-sdk-path` -e _main -arch x86_64 -platform_version macos 11.0.0 11.0.0 -o hello_world hello_world.o

- combine object file with libraries to create exectuable.

running
----
./hello_world

order of events
1. loads program into memory
2. control transferred to '_main' function.
3. executes instructions. sets up stack frame, arguments prepped, calls printf function, calls function and then cleans up and exits.



