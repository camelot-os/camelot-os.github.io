# SPDX-License-Identifier: Apache-2.0
#
# Copyright 2025 H2Lab OSS Team <contact@h2lab.org>
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
    meson_version: '>=1.3.0',
    version : run_command('support/meson/version.sh', 'get-vcs', check: true).stdout().strip(),
    license: 'Apache-2.0',
    license_files: [ 'LICENSE' ],
)

pymod = import('python')
sphinx = find_program('sphinx-build')

py3 = pymod.find_installation(
    'python3',
    modules: [
        'sphinx_pdj_theme',
        'rstcloth',
        'github',
    ]
    )

gen_release = find_program('support/tools/gen_releases.py')

release_file_path = join_paths(meson.current_source_dir(), 'source/') + 'releases.rst'

release_file = configure_file(
    output: 'releases.dep',
    command: [gen_release, release_file_path ],
)

camelot_book_src = files(
    'source/index.rst',
    'source/over_camelot/index.rst',
    'source/over_camelot/gui.rst',
    'source/over_camelot/testing.rst',
    'source/over_camelot/debug.rst',
    'source/over_camelot/libs.rst',
    'source/over_camelot/drivers.rst',
    'source/over_camelot/apps.rst',
    'source/indus/index.rst',
    'source/indus/licensing.rst',
    'source/indus/offline.rst',
    'source/hw_support.rst',
    'source/ports/index.rst',
    'source/ports/global_process.rst',
    'source/ports/arches.rst',
    'source/develop/index.rst',
    'source/develop/languages.rst',
    'source/develop/projects.rst',
    'source/develop/blinky.rst',
    'source/develop/toolchains.rst',
    'source/develop/sdk.rst',
    'source/develop/merlin.rst',
    'source/develop/barbican.rst',
    'source/contribute.rst',
    'source/behind/index.rst',
    'source/behind/kernel.rst',
    'source/behind/concepts.rst',
    'source/behind/security.rst',
    'source/behind/formal.rst',
    'source/Introduction.rst',
    'source/troobleshootings.rst',
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
        '-Drelease=' + meson.project_version(),
        join_paths(meson.current_source_dir(), 'source'),
        'doc/camelot-book',
    ])

doc = alias_target(
    'doc',
    camelot_book,
)
