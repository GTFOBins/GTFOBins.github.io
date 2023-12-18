---
functions:
  file-read:
    - description: Read arbitrary files using 'exec' and 'tr'.
      code: |
        TF=$(mktemp)
        echo '#!/bin/sh' > $TF
        echo 'export LFILE="file_to_read"' >> $TF
        echo 'exec < "$LFILE"; tr -d ""' >> $TF
        chmod +x $TF
        $TF
---
