---
layout: page
title: Contributing
description: Get involved in GTFOBins.
permalink: /contributing/
---

Each entry is defined in a [YAML][] file placed in the [`_gtfobins/`][] folder and named like the executable (binary or script) it refers, without any additional extension. The file contains a single document enclosed in delimiters: `---` and `...`. The general structure is the following:

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

The `contexts` object can be omitted altogether, in that case the `code` is assumed to be about the `unprivileged` context. When a context specifies a specialized `code` field, it is used in place of the global value, which can be omitted if all the context specifies a specialization. `description` instances can always be omitted, while ultimately there must be one `code` example for each context, either specialized or inherited.

Some functions support additional fields:

- `reverse-shell` allows a `listener` field that describes how to receive the shell on the other side, it can be either a string (that must match the corresponding key in [`_data/functions.yml`][], e.g., `TCP`), or an object with two optional fields (`description` and `code`);

- `bind-shell` allows a `connector` field that describes how to initiate the shell on the other side, it can be either a string (that must match the corresponding key in [`_data/functions.yml`][], e.g., `TCP`), or an object with two optional fields (`description` and `code`);

- `upload` allows a `receiver` field that describes how to receive data on the other side, it can be either a string (that must match the corresponding key in [`_data/functions.yml`][], e.g., `TCP`), or an object with two optional fields (`description` and `code`);

- `download` allows a `sender` field that describes how to send data on the other side, it can be either a string (that must match the corresponding key in [`_data/functions.yml`][], e.g., `TCP`), or an object with two optional fields (`description` and `code`);

- `reverse-shell` and `bind-shell` allows a `limited` flag that is `true` when the example is not able to spawn a full TTY shell.

- `file-write`, `file-read`, `upload`, and `download` allows a `limited` flag that is `true` when the example is not able handle arbitrary binary data.

Some contexts support additional fields:

- `suid` allows a `limited` flag that is `true` when the example only works with distributions whose default shell does not drop SUID privileges;

- `capabilities` requires a `list` of Linux [capabilities](https://man7.org/linux/man-pages/man7/capabilities.7.html) in the format `CAP_*` that are needed in order to execute this function with bypassed permissions.

Additionally, it is possible to add _aliases_ with:

```yaml
---
alias: <gtfobin>
...
```

In this case, this entry is an alias of an existing `<gtfobin>`.

Feel free to use any file in the [`_gtfobins/`] folder as an example.

[YAML]: https://yaml.org/
[`_gtfobins/`]: https://github.com/GTFOBins/GTFOBins.github.io/tree/master/_gtfobins
[`_data/functions.yml`]: https://github.com/GTFOBins/GTFOBins.github.io/blob/master/_data/functions.yml
[`_data/contexts.yml`]: https://github.com/GTFOBins/GTFOBins.github.io/blob/master/_data/contexts.yml
