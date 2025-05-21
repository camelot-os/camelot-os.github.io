#!/usr/bin/env python3

# SPDX-FileCopyrightText: 2025 H2Lab OSS Team
# SPDX-License-Identifier: Apache-2.0

from github import Github
from github import Auth
import sys, os
from datetime import datetime

env_var = os.environ
# using an access token. This allows CI-based build using ephemeral GITHUB_TOKEN
auth = Auth.Token(env_var['TOKEN'])

if len(sys.argv) < 2:
    print('Usage: ' + sys.argv[0] + 'path/to/target.rst')
    sys.exit()

# XXX: fix to proper path checking
target = str(sys.argv[1])

# Public Web Github
g = Github(auth=auth)

# Then play with your Github objects:
repo = g.get_repo('camelot-os/camelot-sdk')
releases = repo.get_releases()

index_title = """
Camelot SDK releases
--------------------

This table list all the existing SDK releases that can be downloaded.

"""

with open(target, 'w') as indexfile:
    indexfile.write(index_title)
    for release in releases:
        indexfile.write("### Camelot SDK release " + release.title + "\n\n")
        assets = release.get_assets()
        for asset in assets:
            indexfile.write("  * [" + asset.name + "](" + asset.browser_download_url + ")\n")
        indexfile.write("\n")

# To close connections after use
g.close()

with open('releases.dep', 'w') as depfile:
    depfile.write(str(datetime.now()))
