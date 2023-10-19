# -*- coding: utf-8 -*-
{
    'name': "Sale Channels",

    'summary': """
        Sample module for Calyx: Creating sales channels for sales orders.
        """,
    'description': """
        This module is a test for Calyx
    """,

    'author': "Bruno Laidano",
    'website': "http://www.instagram.com/bruno.la",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','stock','point_of_sale','mail','sale','account','sale_management'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'views/views.xml',
        'views/sale_channel.xml',
        'views/sale_order.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
