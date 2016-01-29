# Project SCRUM

SCRUM framework integrated into Odoo Project

We recommend to use this module with project_team module.

https://github.com/JayVora-SerpentCS/SerpentCS_Contributions-v8/tree/9.0/project_team

Don't forget to enable "Manage time estimation on tasks" in the project settings!

## Differences to older version (prior to Odoo V9):
Despite of some changes in the menu structure two fields in the model project.project has been changed due to better compatibility to "non SCRUM" projects.    
- Product Owner -> field changed from "partner_id" (customer) to "user_id" (Project Manager)
- SCRUM Master -> new field named "scrum_master_id" previous version did use "user_id" (Project Manager)

## Deprived dependency:
To install BeautifulSoup use commando line: apt-get install python-bs4


