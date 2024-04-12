---
functions:
  file-read:
    - code: |
        qpdf --empty --add-attachment /path/filename -- out.pdf; qpdf out.pdf --show-attachment=filename
  sudo:
    - code: |
        sudo qpdf --empty --add-attachment /path/filename -- out.pdf; qpdf out.pdf --show-attachment=filename
---
