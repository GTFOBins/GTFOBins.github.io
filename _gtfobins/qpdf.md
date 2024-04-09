---
description: QPDF is both a software library and a free command-line program that can convert one PDF file to another equivalent PDF file. It is capable of performing transformations such as linearization, encryption, and decryption of PDF files.
functions:
  file-read:
    - description: `qpdf` can be used to read any arbitrary file accessible to the running user, by attaching the target file to a valid PDF file, and then accessing that attachment. If the user is allowed to run `qpdf` as an elevated user (e.g with `sudo`), privileged files can be read.
      code: |
        FILE_TO_READ="/path/to/file"
        qpdf --qdf --add-attachment $FILE_TO_READ --key=anykey -- valid.pdf output.pdf
        qpdf --show-attachment=anykey output.pdf
---