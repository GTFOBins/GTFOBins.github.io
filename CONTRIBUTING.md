---
layout: page
title: Contributing
description: Get involved in GTFOBins.
permalink: /contributing/
---

## File format

Feel free to use any file in the [`_gtfobins/`] folder as an example.

Each entry is defined in a [YAML][] file placed in the [`_gtfobins/`][] folder and named like the executable (binary or script) it refers, without any extension. The file contains a single YAML document enclosed in delimiters: `---` and `...`. The general structure is the following:

```yaml
---
comment: …
functions:
  <function>:
    - comment: …
      version: …
      code: …
      contexts:
        <context>:
          comment: …
          code: …
          # …
        # …
    # …
  # …
...
```

Where `<function>` and `<context>` are defined in the [`_data/functions.yml`][] and [`_data/contexts.yml`][] files respectively.

The optional `version` field must outline any particular OS or executable requirements that enable the corresponding function.

When a context specifies a specialized `code` field, it is used in place of the global value, which can be omitted if all the context specifies a specialization. `comment` instances can always be omitted, while ultimately there must be one `code` example for each context, either specialized or inherited.

### Functions

Some functions support additional fields:

| Function        | Fields                    |
|-----------------|---------------------------|
| `shell`         | `blind`                   |
| `command`       | `blind`                   |
| `reverse-shell` | `blind` `tty` `listener`  |
| `bind-shell`    | `blind` `tty` `connector` |
| `file-write`    | `binary`                  |
| `file-read`     | `binary`                  |
| `upload`        | `binary` `receiver`       |
| `download`      | `binary` `sender`         |
| `library-load`  | n/a                       |
| `inherit`       | `from`                    |

Where:

- the optional `blind` field determines whether the example is able to somehow return the output of the execution of commands or not (defaults to `false`);

- the optional `tty` field determines whether the example is able to spawn a full TTY shell or not (defaults to `true`);

- the optional `binary` field determines whether the example is able to handle arbitrary binary data or not (defaults to `true`);

- the optional `listener` field describes how to receive the shell on the other side, it can be either a string (that must match the corresponding key in [`_data/functions.yml`][], e.g., `TCP`), or an object with two optional fields (`comment` and `code`);

- the optional `connector` field describes how to initiate the shell on the other side, it can be either a string (that must match the corresponding key in [`_data/functions.yml`][], e.g., `TCP`), or an object with two optional fields (`comment` and `code`);

- the optional `receiver` field describes how to receive data on the other side, it can be either a string (that must match the corresponding key in [`_data/functions.yml`][], e.g., `TCP`), or an object with two optional fields (`comment` and `code`);

- the optional `sender` field describes how to send data on the other side, it can be either a string (that must match the corresponding key in [`_data/functions.yml`][], e.g., `TCP`), or an object with two optional fields (`comment` and `code`);

- the mandayory `from` field that is the name of another executable that the example enables.

### Contexts

Some contexts support additional fields:

| Context        | Fields   |
|----------------|----------|
| `unprivileged` | n/a      |
| `sudo`         | n/a      |
| `suid`         | `system` |
| `capabilities` | `list`   |

Where:

- the optional `system` field determines whether the executable uses functions like [`system`](https://man7.org/linux/man-pages/man3/system.3.html) that passes commands to the default system shell, which, according to the version used, might or might not drop the privileges (defaults to `false`);

- the mandayory `list` field is the list of Linux [capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html) in the format `CAP_*` that are needed in order to execute this function with bypassed permissions.

### Aliases

Additionally, it is possible to add _aliases_ with:

```yaml
---
alias: <gtfobin>
...
```

In this case, this entry is an alias of an existing `<gtfobin>`.

## Conventions

### Placeholders

Use the following placeholder values where appropriate:

| Type                 | Value                  |
|----------------------|------------------------|
| Shell executable     | `/bin/sh`              |
| Command executable   | `/path/to/command`     |
| Network port         | `12345`                |
| Data to be written   | `DATA`                 |
| Whatever value       | `x...x`                |
| Input file           | `/path/to/input-file`  |
| Output file          | `/path/to/output-file` |
| Temporary file       | `/path/to/temp-file`   |
| Temporary directory  | `/path/to/temp-dir/`   |
| Shared library file  | `/path/to/lib.so`      |
| Victim host domain   | `victim.com`           |
| Attacker host domain | `attacker.com`         |

Some flexibility is expected.

### Links

If needed, link to other entries using relative URLs, e.g, `[gtfobin](../gtfobin)`.

## Local development

To test local changes, start a local instance with:

```
make serve
```

This will spin a Docker container that builds the website, and serves it from <http://0.0.0.0:4000>. Changes to local files are automatically applied.

Before submitting any pull request, make sure the linter completes successfully:

```
make vet
```

This checks both the schema and the format of [YAML][] files, in case of issues in the latter `make format` can be used to enforce the proper style.

Finally, use `make clean` to clean everything up.

[YAML]: https://yaml.org/
[`_data/functions.yml`]: https://github.com/GTFOBins/GTFOBins.github.io/blob/master/_data/functions.yml
[`_data/contexts.yml`]: https://github.com/GTFOBins/GTFOBins.github.io/blob/master/_data/contexts.yml
[`_gtfobins/`]: https://github.com/GTFOBins/GTFOBins.github.io/tree/master/_gtfobins
