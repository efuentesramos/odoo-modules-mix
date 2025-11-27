# -*- coding: utf-8 -*-
{
    'name': "buggie_rent",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/buggy_rental_sequence.xml',
        'data/billing_sequence.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/buggie.xml',
        'views/rent_buggie.xml',
        'views/rate_buggie.xml',
        'views/billing_statement_views.xml',
        'views/detail_rent.xml',
        'reports/report.xml',
        'reports/report_buggie_billing.xml',
       
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
