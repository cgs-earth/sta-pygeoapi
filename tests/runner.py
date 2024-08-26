import os
import json
from jinja2 import Environment, FileSystemLoader

# Set up Jinja2 environment
template_dir = 'templates'
env = Environment(loader=FileSystemLoader(template_dir))

def apply_template_to_json(template_path, json_path):
    # Load the template
    template = env.get_template(template_path)

    # Load the JSON data
    with open(json_path) as json_file:
        data = json.load(json_file)
        data["data"] = data["properties"]

    # Render the template with the JSON data
    result = template.render(data)

    return result

# Iterate over each template
for template_filename in os.listdir(template_dir):
    if template_filename.endswith('.j2'):
        # Determine the template name without the extension
        template_name = template_filename.replace('.j2', '')
        
        # Set the corresponding test directory
        test_dir = os.path.abspath(os.path.join('tests', template_name))

        if not os.path.isdir(test_dir):
            print(f"No test directory found for template {template_name}")
            continue

        # Iterate over JSON files in the test directory
        for file_name in os.listdir(test_dir):
            if file_name.endswith('.json'):
                json_path = os.path.join(test_dir, file_name)
                template_path = template_filename

                # Apply the template to the JSON file
                result = apply_template_to_json(template_path, json_path)

                # Print the result
                print(f"Result for {file_name} using {template_filename}:")
                print(result)
                print("-" * 40)
