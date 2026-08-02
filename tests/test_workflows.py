# Copyright (c) 2026, NVIDIA CORPORATION.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Regression test for the SKIPPING_IS_ALLOWED workflow env variable."""
import pathlib
import re

REPO_ROOT = pathlib.Path(__file__).parents[1]
WORKFLOWS_DIR = REPO_ROOT / ".github" / "workflows"


def _workflow_paths():
    for path in WORKFLOWS_DIR.iterdir():
        if path.is_file() and (
            path.name.endswith(".yml") or path.name.endswith(".yml.disabled")
        ):
            yield path


def test_skipping_is_allowed_is_defined_when_used():
    for path in _workflow_paths():
        content = path.read_text()
        if "$SKIPPING_IS_ALLOWED" not in content:
            continue
        assert re.search(r"^\s*SKIPPING_IS_ALLOWED:", content, re.MULTILINE), (
            f"{path.name} references $SKIPPING_IS_ALLOWED without defining it"
        )
