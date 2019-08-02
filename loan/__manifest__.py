# -*- coding: utf-8 -*-
{
    'name': "Mr First Module",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'web',
    'version': '0.1.1.1',

    'depends': [],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
          'views/employe.xml',
          'views/contract.xml',
          'views/emploan.xml',
          'views/department.xml',
          'views/jobposition.xml',
          'views/sale_wizard.xml',
        
        
    ],
   
}