# -*- coding: utf-8 -*-
{
    'name': "inherit_deliveryslip_odoo11",
    'summary': """Delivery Slip Inheritance""",
    'description': """""",
    'author': "Abdul Halim",
    'website': "http://abdulhalim.pythonanywhere.com",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base'],
    'application': True,
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/report_deliveryslip_inherited.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}