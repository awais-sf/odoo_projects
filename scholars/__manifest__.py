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
    'version': '0.1',

    'depends': [
        "sale",
        ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/scholar.xml',
        'views/category.xml',
        'views/posts.xml',
#         'views/human.xml',
        'views/inherit_view.xml',
        
    ],
   
}