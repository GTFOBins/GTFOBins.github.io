---
layout: page
title: Contribute
---

## Structure

Each GTFO binary is defined in a file in the [`_gtfobins/`] folder named as `<binary name>.md`, such file consists only of a [YAML] front matter which describes the binary and its functions.

The full syntax is the following:

```
---
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
---
```

Where `FUNCTION` is one of the values described in the [`_data/functions.yml`] file.

Feel free to use any file in the [`_gtfobins/`] folder as an example.

## Pull request process

Vendor software is accepted as well as standard Unix binaries. Binaries and techniques that only works on certain operating systems and versions are accepted and such limitations shall be noted in the `description` field.

Before sending a pull request of a new binary or function, ensure the following:

1. Verify the function works on at least one type of modern Unix system.
2. Classifying SUID-related functions is tricky because they depend on the default shell (i.e. Debian `/bin/sh` doesn't drop the privileges, other Linux default shells do it) and on how the external command is called (i.e. `exec()` family vs. `system()` calls). Here an helpful check:
   - The function is `suid` if runs external commands on Ubuntu Linux maintaining the SUID privileges.
   - The function is `limited-suid` if runs external commands on Debian maintaining the SUID privileges, but it drops them on Ubuntu Linux.
   - The function is not `suid-*` flagged if drops the privileges in Debian Linux.
3. Verify `sudo` function runs external commands under the `sudo` privileged context.

Pull requests adding new functions in [`_data/functions.yml`] are allowed and subjected to project maintainers vetting.

[YAML]: https://yaml.org/
[`_gtfobins/`]: https://github.com/GTFOBins/GTFOBins.github.io/tree/master/_gtfobins
[`_data/functions.yml`]: https://github.com/GTFOBins/GTFOBins.github.io/blob/master/_data/functions.yml
