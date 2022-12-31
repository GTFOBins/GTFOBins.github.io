---
description: Redis is an in-memory data store, intended to be used as backend service and not exposed directly to users or to the Internet, until version 7 it was insecure by default.
functions:
  file-write:
    - description: For Redis versions lower than 7. Using the redis-cli It is possible to create a file on the file system and write arbitrary content.
      code: |
        redis-cli -h ip_address
        config set dir dir_to_write_to
        config set dbfilename file_to_write
        set test "content_to_write"
        save
---
