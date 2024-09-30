import os
import json
from jinja2 import Environment, FileSystemLoader

"""Test runner to go through each template and try to template each associated json file"""


def to_json(dict_: dict, pretty: bool = False) -> str:
    """Mimics the to_json filter in pygeoapi"""
    return json.dumps(dict_, indent=4 if pretty else None, separators=(",", ":"))


template_dir = "templates"
env = Environment(loader=FileSystemLoader(template_dir))
env.filters["to_json"] = to_json


def apply_template_to_json(template_path, json_path):
    template = env.get_template(template_path)

    with open(json_path) as json_file:
        data = {"data": json.load(json_file)}

    result = template.render(data)

    return result

# For every template, try to apply it to every corresponding json file
for template_filename in os.listdir(template_dir):
    if template_filename.endswith(".j2"):
        template_name = template_filename.replace(".j2", "")

        test_dir = os.path.abspath(os.path.join("tests", template_name))

        if not os.path.isdir(test_dir):
            print(f"No test directory found for template {template_name}")
            print("-" * 40)
            continue

        for file_name in os.listdir(test_dir):
            if file_name.endswith(".json"):
                json_path = os.path.join(test_dir, file_name)
                template_path = template_filename

                result = apply_template_to_json(template_path, json_path)

                print(f"Result for {file_name} using {template_filename}:")
                print(result)
print("Successfully ran all tests!")