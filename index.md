---
layout: page
title: GTFOBins
---

![logo](/assets/logo.png){:.logo}

GTFOBins is a curated list of Unix binaries that can be used to bypass local security restrictions in misconfigured systems.

The project collects legitimate [functions](/functions/) of Unix binaries that can be abused to ~~get the f**k~~ break out restricted shells, escalate or maintain elevated privileges, transfer files, spawn bind and reverse shells, and facilitate the other post-exploitation tasks.

It is important to note that this is **not** a list of exploits, and the programs listed here are not vulnerable per se, rather, GTFOBins is a compendium about how to live off the land when you only have certain binaries available.

GTFOBins is a [collaborative][] project created by [Emilio Pinna][norbemi] and [Andrea Cardaci][cyrus_and] where everyone can [contribute][] with additional binaries and techniques.

If you are looking for Windows binaries you should visit [LOLBAS][].

[functions]: /functions/
[LOLBAS]: https://lolbas-project.github.io/
[collaborative]: https://github.com/GTFOBins/GTFOBins.github.io/graphs/contributors
[contribute]: /contribute/
[norbemi]: https://twitter.com/norbemi
[cyrus_and]: https://twitter.com/cyrus_and

{% include bin_table.html %}
