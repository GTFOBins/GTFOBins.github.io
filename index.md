---
layout: page
title: GTFOBins
description: GTFOBins is a curated list of Unix binaries that can be used to bypass local security restrictions in misconfigured systems.
---

![GTFOBins logo](/assets/logo.png){:.logo}

{{ page.description }}

The project [collects](/model/) legitimate functions of Unix binaries that can be abused to ~~get the f**k~~ break out restricted shells, escalate or maintain elevated privileges, transfer files, spawn bind and reverse shells, and facilitate other post-exploitation tasks.

GTFOBins is a joint effort by [Emilio Pinna][norbemi] and [Andrea Cardaci][cyrus_and], and many other [contributors][]. Everyone con [get involved](/contributing/) by providing additional binaries and techniques!

If you are looking for Windows binaries you should visit [LOLBAS][].

> Please note that this is **not** a list of exploits, and the programs listed here are not vulnerable per se, rather, GTFOBins is a compendium about how to live off the land when you only have certain binaries available.

[contributors]: https://github.com/GTFOBins/GTFOBins.github.io/graphs/contributors
[norbemi]: https://twitter.com/norbemi
[cyrus_and]: https://twitter.com/cyrus_and
[LOLBAS]: https://lolbas-project.github.io/

{% include gtfobins_table.html %}
