# GitLab Migration Toolkit
This repository contains a collection of Python scripts to facilitate the migration of GitLab projects from one repository to another.

# Contents
This repository includes the following Python scripts:

-**find_all_projects.py**: This script is used to find the list of all the repositories in all the groups under one GitLab parent.

-**find_usernames.py**: This script lists all the active users associated with a GitLab parent group.

-**missing_variables.py**: This script is used to find out missing variables from one GitLab repository to another and create a list of dictionaries containing old project and new project and the number of missing variables.

-**project_mapping.py**: This script is used for GitLab migration, when you need to map your repos from the old repo to the projects in the new repo.

-**transfer_gitlab_variables.py**: This script is used to transfer CI/CD variables from one GitLab repo to another after running the missing_variables.py and getting the list of mapping.

-**validate_project_mapping.py**: This script is used for GitLab migration, when you need to validate your GitLab project mapping from project_mapping.py.

# Usage
Each script can be run independently to accomplish a specific task in the GitLab migration process. Please refer to the individual script README files for more detailed instructions on how to run them.

# Contributions
Contributions to this repository are welcome! Please fork the repository, create a new branch for your changes, and submit a pull request.
