# -*- coding: utf-8 -*-
{
    'name': "usl_service_order_automation",

    'summary': """
        Service Order Automation""",


    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',
    'sequence': -300,

    # any module necessary for this one to work correctly
    'depends': ['base','mail'],

    # always loaded
    'data': [
         'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'views/menu.xml',
        'views/service_oder.xml',
        'views/product_data.xml',
        'views/invoice.xml',


        # 'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',

    ],
    'application': True,
}
