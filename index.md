---
layout: page
title: GTFOBins
description: GTFOBins is a curated list of Unix-like executables that can be used to bypass local security restrictions in misconfigured systems.
---

![GTFOBins logo]({{ '/assets/logo.png' | relative_url }}){:.logo}

{{ page.description }}

The project [collects]({{ '/scope/' | relative_url }}) legitimate functions of Unix-like executables that can be abused to ~~get the f**k~~ break out restricted shells, escalate or maintain elevated privileges, transfer files, spawn bind and reverse shells, and facilitate other post-exploitation tasks.

GTFOBins is a joint effort by [Emilio Pinna][norbemi] and [Andrea Cardaci][cyrus_and], and many other [contributors][]. Everyone can [get involved]({{ '/contributing/' | relative_url }}) by providing additional entries and techniques!

If you are looking for Windows binaries you should visit [LOLBAS][].

> Please note that this is **not** a list of exploits, and the programs listed here are not vulnerable per se, rather, GTFOBins is a compendium about how to live off the land when you only have certain executables available.

[GitHub][]
|
[Get involved]({{ '/contributing/' | relative_url }})
|
[Contributors][contributors]
|
[JSON API]({{ '/api.json' | relative_url }})
|
[MITRE ATT&CK® Navigator](https://mitre-attack.github.io/attack-navigator/#layerURL={{ '/mitre.json' | absolute_url }})
{:.centered}

[contributors]: https://github.com/GTFOBins/GTFOBins.github.io/graphs/contributors
[norbemi]: https://x.com/norbemi
[cyrus_and]: https://x.com/cyrus_and
[LOLBAS]: https://lolbas-project.github.io/
[GitHub]: https://github.com/GTFOBins/GTFOBins.github.io

<div>{%- include gtfobins_table.html -%}</div>
