from jinja2 import Environment, FileSystemLoader
import json
import os

def generate_workflow(workflow_config, task_config, template_file, output_file):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(template_file)

    # Load workflow config
    with open(workflow_config, 'r') as f:
        workflow_data = json.load(f)
    
    # Load task config
    with open(task_config, 'r') as f:
        task_data = json.load(f)

    # Generate the final workflow JSON
    workflow_json = template.render(
        id=workflow_data['id'],
        tasks_grouped=task_data['tasks_grouped'],
        notebook_prefix=workflow_data['notebook_prefix'],
        pipeline_context=workflow_data['pipeline_context'],
        job_cluster_key=workflow_data['job_cluster_key']
    )

    # Write the generated JSON to the output file
    with open(output_file, 'w') as f:
        f.write(workflow_json)


# Define a list of combinations for workflow config, task config, and template
combinations = [
    {
        'workflow_config': 'workflow_config1.json',
        'task_config': 'workflow_wholesale_tasks1.json',
        'template_file': 'workflow_template1.j2',
        'output_file': 'final_workflow1.json'
    },
    {
        'workflow_config': 'workflow_config2.json',
        'task_config': 'workflow_wholesale_tasks2.json',
        'template_file': 'workflow_template2.j2',
        'output_file': 'final_workflow2.json'
    },
    # Add more combinations here
]

# Generate workflows for all combinations
for combo in combinations:
    generate_workflow(
        combo['workflow_config'],
        combo['task_config'],
        combo['template_file'],
        combo['output_file']
    )
