# Databricks Workflows: Configuration and Structure Guidelines

In this project, we're managing large configuration files for Databricks workflows, which can get challenging. To improve maintenance and readability, we have a structured, modular approach. Here's how we've organized the project:

## Directory Structure

```
databricks-workflows/
├── configs/
│   ├── workflow_configs/
│   │   ├── workflow_config1.json
│   │   ├── workflow_config2.json
│   │   └── ...
│   └── task_configs/
│       ├── workflow1_tasks.json
│       ├── workflow2_tasks.json
│       └── ...
├── templates/
│   ├── task_templates/
│   │   ├── notebook_task_template.j2
│   │   └── ...
│   └── workflow_templates/
│       └── workflow_template.j2
├── scripts/
│   └── generate_workflows.py
└── deploy/
    └── deploy-to-dev.yml
```

## What Each Folder Contains

### `configs/workflow_configs/`

Here, we store JSON files that define the high-level properties for each of our workflows. Examples include `workflow_config1.json`, `workflow_config2.json`, etc.

### `configs/task_configs/`

This folder contains JSON files that define the tasks and their parameters for each workflow. We then load these task configurations into our Python script to generate the specific workflow JSON files.

### `templates/task_templates/`

This contains Jinja2 templates that describe the structure of different types of tasks (e.g., notebook tasks, job tasks).

### `templates/workflow_templates/`

Here we store the Jinja2 templates for the workflows themselves, into which task JSONs get inserted.

### `scripts/`

This folder houses Python scripts like `generate_workflows.py`, which read the various JSON configs and Jinja2 templates to generate the final JSON workflow configs. We run this script before each deployment to ensure that the most up-to-date configurations are being used.

### `deploy/`

This folder contains the GitHub Actions YAML file for deploying the workflows.

## Workflow Script (`generate_workflows.py`)

In the `scripts/` folder, we have the `generate_workflows.py` script. This script reads the various JSON configs and Jinja2 templates to generate the final, large JSON configuration files for our workflows. We run this script before deploying to make sure we are using the most recent configurations.

## GitHub Actions (`deploy-to-dev.yml`)

Our GitHub Actions YAML file mostly remains the same. However, we've added a new step before `Deploy jobs` to execute the `generate_workflows.py` script. This ensures that the most recent configurations are used in the deployment.

## Task and Workflow Abstraction

We've defined templates for each type of task to reduce duplication significantly. Our task configurations can then be simple key-value pairs that get inserted into these templates to create the JSON files for each task. 

Similarly, each workflow configuration JSON focuses on unique parameters like its ID, schedule, and any other non-standard configurations. The bulk of the actual task definitions are abstracted away into the task configs and templates.

By following this structure, we aim to minimize duplication, enhance readability, and make managing our complex configurations far more straightforward.
