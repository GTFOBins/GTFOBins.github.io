---
description: eSpeak text-to-speech
functions:
  file-read:
    - code: |
        LFILE=file_to_read
        espeak -qXf "$LFILE"
  sudo:
    - code: |
        LFILE=file_to_read
        sudo espeak -qXf "$LFILE"
---
