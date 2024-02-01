import os

import pytest


def skip_in_ci_with_reason(test_function, *reasons):
    return pytest.mark.skipif(
os.environ.get("CI") == "true" and all(reason in test_function.__name__ for reason in reasons),
        reason="This test doesn't work on GitHub Actions.",
    )(test_function)


def get_workspace_file_path(workspace, file_name):
    return str(workspace.get_path(file_name))
