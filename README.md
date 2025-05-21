<!--
SPDX-FileCopyrightText: 2025 H2Lab OSS Team
SPDX-License-Identifier: Apache-2.0
-->

# Camelot-OS book sources

## basics

This repository hold the Camelot Book sources, built with Sphinx and meson.

In order to build the Camelot-book, you need an environnement TOKEN that hold an ephemeral token to access Github.
You can create an ephemeral token using your ghithub account settings. On CI, this repo is using the GITHUB_TOKEN
ephemeral token as TOKEN value.
The Token usage is required as this repository automatically analyse the Camelot-SDK releases list in order to
forge an uptodate SDK releases page that hold SDKs downloadable releases list.

## Building the documentation

```
$ TOKEN=my-ephemeral-token meson setup builddir
$ ninja -C builddir
```

The documentation is then forged in the `builddir/doc/camelot-book` directory and can be browsed using any web browsers.
