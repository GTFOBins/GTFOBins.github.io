---
functions:
  file-write:
    - description: write DATA to $WFILE
      code: |
        LFILE=$(mktemp --suffix=.s)
        WFILE=file-to-write
        elf=$(mktemp -u)
        vi $LFILE
        ;#####CODE START#####
        .global _start
        _start:
        .intel_syntax noprefix
        mov rax,2
        lea rdi,[rip+DATA]
        mov rsi, 0
        syscall
        mov rax,60
        mov rdi,0
        syscall
        DATA:
        .string "THIS IS THE DATA NEED TO BE WRITTEN USING STRACE"
        ;#####CODE END#####
        :wq
        gcc -nostdlib --static $LFILE -o $elf
        strace -o $WFILE $elf
  shell:
    - code: strace -o /dev/null /bin/sh
  suid:
    - code: ./strace -o /dev/null /bin/sh -p
  sudo:
    - code: sudo strace -o /dev/null /bin/sh
---
