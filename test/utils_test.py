import pytest

import structure_gen.constants as ct
from structure_gen.utils import print_tree


@pytest.mark.parametrize("file_message, expected_print", [
    ("main.py", ct.FILE_JUST * " " + "|----main.py")
])
def test_file_print_tree(file_message, expected_print):
    assert print_tree(file_message, "file") == print(expected_print)
