#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2025 H2Lab OSS Team
# SPDX-License-Identifier: Apache-2.0

from github import Github
from github import Auth
import sys, os
from rstcloth import RstCloth
from datetime import datetime
import re

env_var = os.environ
# using an access token. This allows CI-based build using ephemeral GITHUB_TOKEN
auth = Auth.Token(env_var['TOKEN'])

if len(sys.argv) < 2:
    print('Usage: ' + str(sys.argv[0]) + ' path/to/target.rst')
    sys.exit()

# XXX: fix to proper path checking
target = str(sys.argv[1])

# Public Web Github
g = Github(auth=auth)

# Then play with your Github objects:
repo = g.get_repo('camelot-os/camelot-sdk')
releases = repo.get_releases()

with open(target, 'w') as indexfile:
    doc = RstCloth(indexfile)
    doc.h2('Camelot SDK upstream releases')
    doc.newline()
    doc.table_of_contents()
    doc.newline()
    doc.h3('About releases authentication and testing model')
    doc.newline()
    doc.content('These Camelot SDK releases are community supported pre-built SDK for community supported hardware architectures.')
    doc.newline()
    doc.note(arg='This releases are tested against various SoCs listed in the release description')
    doc.newline()
    doc.content(
        content=[
            'All releases starting with v0.1.2 are attested at CD execution time using the in-toto standard attestation model.',
            'When downloading a release, you can attest the authentication of the downloaded file using such a command based on the',
             doc.inline_link('Github CLI', 'https://cli.github.com/')
        ])
    doc.newline()
    doc.codeblock(
        content= """
$ gh attestation verify --predicate-type https://in-toto.io/attestation/release/v0.1 camelot-sdk-armv7em_v0.1.2.tar.xz  --repo camelot-os/camelot-sdk
Loaded digest sha256:6f8c91ae722a14a1d0e5dec8234659f3a3487be39eebdac72610e3582db4a619 for file://camelot-sdk-armv7em_v0.1.2.tar.xz`
Loaded 1 attestation from GitHub API

The following policy criteria will be enforced:
- Predicate type must match:................ https://in-toto.io/attestation/release/v0.1
- Source Repository Owner URI must match:... https://github.com/camelot-os
- Source Repository URI must match:......... https://github.com/camelot-os/camelot-sdk
- Subject Alternative Name must match regex: (?i)^https://github.com/camelot-os/camelot-sdk/
- OIDC Issuer must match:................... https://token.actions.githubusercontent.com

✓ Verification succeeded!

The following 1 attestation matched the policy criteria

- Attestation #1
  - Build repo:..... camelot-os/camelot-sdk
  - Build workflow:. .github/workflows/release.yml@refs/tags/v0.1.2
  - Signer repo:.... camelot-os/camelot-sdk
  - Signer workflow: .github/workflows/release.yml@refs/tags/v0.1.2
3m"""
    )
    doc.newline()

    doc.h3('Last releases')
    doc.newline()

    for release in releases:

        doc.h4("Camelot SDK release " + release.tag_name)
        doc.newline()
        if release.prerelease:
            doc.warning(arg='This is a pre-release')
            doc.newline()
        assets = release.get_assets()
        doc.newline()
        doc.codeblock(content=str(release.body), language='markdown')
        doc.newline()
        for asset in assets:
            doc.table_list(
                headers=['', doc.inline_link(asset.name, asset.browser_download_url)],

                data=[
                    ['size', str(asset.size / (1000)) + 'KB'],
                    ['architecture', asset.name.split('_')[0][12:] ],
                ],
                widths=['30', '65'],
                width='100%'
            )
            doc.newline()
        doc.newline()

# To close connections after use
g.close()

with open('releases.dep', 'w') as depfile:
    depfile.write(str(datetime.now()))
