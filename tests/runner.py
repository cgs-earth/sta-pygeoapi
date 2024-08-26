import os
import json
from jinja2 import Environment, FileSystemLoader

template_dir = 'templates'
env = Environment(loader=FileSystemLoader(template_dir))

def apply_template_to_json(template_path, json_path):
    template = env.get_template(template_path)

    with open(json_path) as json_file:
        data = json.load(json_file)
        # pygeoapi templates use data as the key where all the properties are stored
        # so we just rename the key
        data["data"] = data["properties"]

    result = template.render(data)

    return result

for template_filename in os.listdir(template_dir):
    if template_filename.endswith('.j2'):
        template_name = template_filename.replace('.j2', '')
        
        test_dir = os.path.abspath(os.path.join('tests', template_name))

        if not os.path.isdir(test_dir):
            print(f"No test directory found for template {template_name}")
            continue

        for file_name in os.listdir(test_dir):
            if file_name.endswith('.json'):
                json_path = os.path.join(test_dir, file_name)
                template_path = template_filename

                result = apply_template_to_json(template_path, json_path)

                print(f"Result for {file_name} using {template_filename}:")
                print(result)
                print("-" * 40)
