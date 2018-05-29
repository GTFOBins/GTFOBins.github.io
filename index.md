---
layout: page
title: GTFOBins
---

<img class="logo" src="/assets/logo.png"/>

GTFOBins is a curated list of Unix binaries that can be exploited by an attacker to bypass local security restrictions.

The project collects legitimate Unix binaries that can be abused to <strike>get the f**k</strike> break out restricted shells, escalate or maintain elevated privileges, transfer files, spawn bind and reverse shells, and facilitate the other post-exploitation tasks. See the full list of [functions](/functions/).

This was inspired by the [LOLBins](https://github.com/api0cradle/LOLBAS) project for Windows.

GTFOBins aims to be a shared project where everyone can [contribute](/contribute/) with additional binaries and techniques.

## List of `{{ site.gtfobins | size }}` GTFOBins

{% include bin_table.html %}
