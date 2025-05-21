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
    doc.fill('These Camelot SDK releases are community supported pre-built SDK for community supported hardware architectures.')
    doc.newline()
    doc.note(arg='This releases are tested against various SoCs listed in the release description')
    doc.newline()


    for release in releases:

        doc.h3("Camelot SDK release " + release.tag_name)
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
