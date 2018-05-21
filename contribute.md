---
layout: page
title: Contribute
---

## Structure

Each GTFO binary is defined in a file in the `_gtfobins/` folder named as `<binary name>.md`, such file consists only of a [YAML] front matter which describes the binary and its functions.

[YAML]: http://yaml.org/

The full syntax is the following:

```
description: Optional description of the binary
functions:
  FUNCTION:
    - description: Optional description of the example
      code: Code of the example
    - ....
  FUNCTION:
    - description: Optional description of the example
      code: Code of the example
    - ...
  ...
```

Where `FUNCTION` is one of the values described in the `_data/functions.yml` file.

Feel free to use any file in the `_gtfobins/` folder as an example.

Pull request process
--------------------

Vendor software is accepted as well as standard Unix binaries. Binaries and techniques that only works on certain operating systems and versions are accepted and such limitations shall be noted in the `description` field.

Before sending a pull request of a new binary or function, ensure the following:

1. Verify the function works on at least one type of modern Unix system.
2. Classifying SUID-related functions may be tricky because they depend on how the default shell behaves on different systems (i.e. Ubuntu vs. Debian) and how the external command is called (i.e. `exec()` family vs. `system()`). Check how the binary behaves:
   - The function is considered `suid-enabled` if runs external commands with SUID privileges on Ubuntu Linux.
   - The function is considered `suid-limited` if runs external commands with SUID privileges on Debian but it drops the privileges on Ubuntu Linux.
3. Verify `sudo-enabled` function runs external commands under the `sudo` privileged context.

Pull requests adding new functions in `_data/functions.yml` are allowed and subjected to project maintainers vetting.
