# -*- coding: utf-8 -*-
{
    'name': "E2yun CRM Groups Extends",

    'summary': """
    删除用户所属群组时，考虑群组下有继承群组的情况
    """,

    'description': """
    """,

    'author': "Kangyu.Wang",
    'website': "http://www.e2yun.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access2.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}