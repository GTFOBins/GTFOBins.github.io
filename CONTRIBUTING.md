---
layout: page
title: Contributing
description: Get involved in GTFOBins.
permalink: /contributing/
---

## File format

Feel free to use any file in the [`_gtfobins/`] folder as an example.

Each entry is defined in a [YAML][] file placed in the [`_gtfobins/`][] folder and named like the executable (binary or script) it refers, without any extension. The file contains a single document enclosed in delimiters: `---` and `...`. The general structure is the following:

```yaml
---
description: …
functions:
  <function>:
    - description: …
      version: …
      code: …
      contexts:
        <context>:
          description: …
          code: …
          # …
        # …
    # …
  # …
...
```

Where `<function>` and `<context>` are defined in the [`_data/functions.yml`][] and [`_data/contexts.yml`][] files respectively.

The optional `version` field must outline any particular OS or executable requirements that enable the corresponding function.

The `contexts` object can be omitted altogether, in that case `code` is assumed to be about the `unprivileged` context. When a context specifies a specialized `code` field, it is used in place of the global value, which can be omitted if all the context specifies a specialization. `description` instances can always be omitted, while ultimately there must be one `code` example for each context, either specialized or inherited.

Some functions support additional fields:

- `reverse-shell` allows a `listener` field that describes how to receive the shell on the other side, it can be either a string (that must match the corresponding key in [`_data/functions.yml`][], e.g., `TCP`), or an object with two optional fields (`description` and `code`);

- `bind-shell` allows a `connector` field that describes how to initiate the shell on the other side, it can be either a string (that must match the corresponding key in [`_data/functions.yml`][], e.g., `TCP`), or an object with two optional fields (`description` and `code`);

- `upload` allows a `receiver` field that describes how to receive data on the other side, it can be either a string (that must match the corresponding key in [`_data/functions.yml`][], e.g., `TCP`), or an object with two optional fields (`description` and `code`);

- `download` allows a `sender` field that describes how to send data on the other side, it can be either a string (that must match the corresponding key in [`_data/functions.yml`][], e.g., `TCP`), or an object with two optional fields (`description` and `code`);

- `reverse-shell` and `bind-shell` allows a `limited` flag that is `true` when the example is not able to spawn a full TTY shell.

- `file-write`, `file-read`, `upload`, and `download` allows a `limited` flag that is `true` when the example is not able handle arbitrary binary data;

- `inherit` requires a `from` field that is the name of another executable that the example enables.

Some contexts support additional fields:

- `suid` allows a `limited` flag that is `true` when the example only works with distributions whose default shell does not drop SUID privileges;

- `capabilities` requires a `list` of Linux [capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html) in the format `CAP_*` that are needed in order to execute this function with bypassed permissions.

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
| Command executable   | `/bin/id`              |
| Network port         | `12345`                |
| Data to be written   | `DATA`                 |
| Whatever value       | `x...x`                |
| Input file           | `/path/to/input-file`  |
| Output file          | `/path/to/output-file` |
| Attacker host domain | `attacker.com`         |

### Multiline strings

If a multiline string is needed, use the `-` YAML literal variant, i.e., `|-`, for example:

```
some-field: |-
  Lorem ipsum...
```

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
make lint
```

Then use `make clean` to clean everything up.

[YAML]: https://yaml.org/
[`_data/functions.yml`]: https://github.com/GTFOBins/GTFOBins.github.io/blob/master/_data/functions.yml
[`_data/contexts.yml`]: https://github.com/GTFOBins/GTFOBins.github.io/blob/master/_data/contexts.yml
[`_gtfobins/`]: https://github.com/GTFOBins/GTFOBins.github.io/tree/master/_gtfobins
