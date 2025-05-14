from github import Github
from github import Auth
import os

env_var = os.environ
# using an access token
auth = Auth.Token(env_var['TOKEN'])

# Public Web Github
g = Github(auth=auth)

# Then play with your Github objects:
repo = g.get_repo('camelot-os/camelot-sdk')
releases = repo.get_releases()

index_title = """# Camelot Operating system

## Camelot SDK releases

This table list all the existing SDK releases that can be downloaded.

"""

with open('index.rst', 'w') as indexfile:
    indexfile.write(index_title)
    for release in releases:
        indexfile.write("### Camelot SDK release " + release.title + "\n\n")
        assets = release.get_assets()
        for asset in assets:
            indexfile.write("  * [" + asset.name + "](" + asset.url + ")\n")
        indexfile.write("\n")

# To close connections after use
g.close()
