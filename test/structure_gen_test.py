import os
import pytest

import structure_gen.constants as ct
from structure_gen.structure_gen import StructureGen
from structure_gen.utils import read_json, create_config_file

"""
Testing StructureGen class, 
when instantiating StructureGen() it is essential:
- parsing of args works properly
- proper format for header and gitignore
- workplace folder correctly created in the output_dir
 
 Test methods:
 - create file
 - create folder
 - create package
"""


def test_structure_gen_init(tmp_path):
    project_type = "DEV"
    packages = ["pack1", "pack2"]
    folders = ["docs", "refs"]
    create_config_file(tmp_path)
    test_instance = StructureGen(project_type, tmp_path, packages, folders)

    assert test_instance.project_type == project_type
    assert test_instance.output_dir == tmp_path

    assert test_instance.packages == packages
    assert test_instance.folders == folders

    config_info = read_json(tmp_path / "config.json")
    assert test_instance.header == "\n".join(list(config_info["header"].values()))
    assert test_instance.gitignore == ct.GITIGNORE_LINE_SEP.join(config_info["gitignore"])


@pytest.fixture
def create_structure_gen(tmp_path):
    project_type = "DEV"
    packages = ["pack1", "pack2"]
    folders = ["docs", "refs"]
    create_config_file(tmp_path)
    return StructureGen(project_type, tmp_path, packages, folders)


@pytest.mark.parametrize("file_name, expected_content", [
    ("test_file.txt", "Hello World!"),
    ("empty_test.txt", ""),
])
def test_create_file(create_structure_gen, file_name, expected_content):
    test_instance = create_structure_gen
    file_path = os.path.join(test_instance.output_dir, file_name)
    test_instance.create_file(file_path, file_content=expected_content)

    assert os.path.exists(file_path)

    with open(file_path, "r") as file:
        file_content = file.read()

    assert file_content == expected_content

