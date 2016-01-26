# -*- coding: utf-8 -*-
##############################################################################
#
#
#
##############################################################################

{
    'name': 'Project Scrum',
    'version': '1.7',
    'category': 'Project Management',
    'summary': 'SCRUM framework integrated into Odoo Project',
    'description': """
Using Scrum to plan the work in a team.
=========================================================================================================
More information:
    """,

    'author': 'Vertel AB',
    'website': 'http://www.vertel.se',
    'depends': ['project', 'mail'],
    'data': ['project_scrum_view.xml',
        'wizard/project_scrum_test_task_view.xml',
        'security/ir.model.access.csv',
        'security/project_security.xml',
       ],
    #'external_dependencies': {
        #'python' : ['bs4'],
    #},
   # 'demo': ['project_scrum_demo.xml'],
    'installable': True,
    'auto_install': False,
    'application': True,
}



# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
