#!/usr/bin/env python
# coding=utf-8

# Copyright [2017] [B2W Digital]
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# from click.testing import CliRunner

try:
    import mock
except ImportError:
    import unittest.mock as mock


from marvin_python_toolbox.management.pkg import _clone
from marvin_python_toolbox.management.pkg import copy


@mock.patch("marvin_python_toolbox.management.pkg.git_clone")
def test_clone(git_mocked):
    git_mocked.return_value = 1
    repo = "http://xxx.git"
    result = _clone(repo)

    assert result == (repo, 1)
    git_mocked.assert_called_once_with(repo, checkout=False, depth=1)

# TODO: assert OSError
@mock.patch("marvin_python_toolbox.management.pkg.shutil.ignore_patterns")
@mock.patch("marvin_python_toolbox.management.pkg.shutil.copytree")
def test_copy(copytree_mocked, ignore_mocked):
    src = "/xpto"
    dest = "/xpto_dest"
    ignore = (".git")
    ignore_mocked.return_value = 1
    copy(src, dest, ignore)

    copytree_mocked.assert_called_once_with(src, dest, ignore=1)
    ignore_mocked.assert_called_once_with(*ignore)


# def copy(src, dest, ignore=('.git', '.pyc', '__pycache__')):
#     try:
#         shutil.copytree(src, dest, ignore=shutil.ignore_patterns(*ignore))
#     except OSError as e:
#         if e.errno == errno.ENOTDIR:
#             shutil.copy(src, dest)
#         else:
#             print('Directory not copied. Error: %s' % e)
