---
functions:
  file-read:
    - description: Read arbitrary files using 'exec' and 'tr' to remove null bytes (if any).
      code: |
        TF=$(mktemp)
        echo '#!/bin/sh' > $TF
        echo 'export LFILE="file_to_read"' >> $TF
        echo 'exec < "$LFILE"; tr -d "\0"' >> $TF
        chmod +x $TF
        $TF
---
