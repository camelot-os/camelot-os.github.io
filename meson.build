# SPDX-License-Identifier: Apache-2.0
#
# Copyright 2023-2024 Ledger SAS
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

project('camelot-book',
    meson_version: '>=1.7.0',
    version : run_command('support/meson/version.sh', 'get-vcs', check: true).stdout().strip(),
    license: 'Apache-2.0',
    license_files: [ 'LICENSE' ],
)

pymod = import('python')
sphinx = find_program('sphinx-build')

py3 = pymod.find_installation(
    'python3',
    modules: [
        'exhale',
        'sphinx_rtd_theme',
        'sphinx_simplepdf',
    ]
    )

gen_release = find_program('support/tools/gen_releases.py')

release_file = configure_file(
    output: 'releases.rst',
    command: [gen_release ],
)

camelot_book_src = files(
    'source/index.rst',
)

camelot_book = custom_target('camelot_book',
    input: camelot_book_src,
    depend_files: [files('source/conf.py'), release_file ],
    output: 'camelot_book',
    install: true,
    install_tag: 'doc',
    install_dir: get_option('datadir') / 'doc/camelot-book',
    command: [sphinx, '-b', 'html', '-q', '-d',
        'build/doctrees',
        '-Dversion=' + meson.project_version(),
        join_paths(meson.current_source_dir(), 'source'),
        'doc/camelot-book',
    ])

doc = alias_target(
    'doc',
    camelot_book,
)
