---
layout: page
title: Contributing
description: Get involved in GTFOBins.
permalink: /contributing/
---

Each entry is defined in a [YAML][] file placed in the [`_gtfobins/`][] folder and named like the binary or script it refers, without an additional extension. The file contains a single document enclosed in delimiters: `---` and `...`. The general structure is the following:

```yaml
---
description: …
functions:
  <function>:
    - description: …
      code: …
      features:
        <feature>:
          description: …
          code: …
          # …
        # …
    # …
  # …
...
```

Where `<function>` and `<feature>` are defined in the [`_data/functions.yml`][] and [`_data/features.yml`][] files respectively.

The `features` object can be omitted altogether, in that case the `code` is assumed to be about the `unprivileged` feature. When a feature specifies a specialized `code` field, it is used in place of the global value, which can be omitted if all the feature specifies a specialization. `description` instances can always be omitted, while ultimately there must be one `code` example for each feature, either specialized or inherited.

Some functions require additional fields:

- `reverse-shell` and `bind-shell` require a `tty` flag that is `true` when the example is able to spawn a full TTY shell.

Some features require additional fields:

- `suid` requires a `limited` flag that is `true` when the example only works with distributions whose default shell does not drop SUID privileges;

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
[`_data/features.yml`]: https://github.com/GTFOBins/GTFOBins.github.io/blob/master/_data/features.yml
