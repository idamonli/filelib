# -*- coding: utf-8 -*-
{
    'name': "e2yun_online_shop_extends",

    'summary': """在线商城模块增强
        """,

    'description': """在线商城模块增强
    """,

    'author': "Kangyu.Wang",
    'website': "http://www.e2yun.cn",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product', 'website_sale', 'website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        'views/templates.xml',
        'views/views.xml',
        'views/order_view.xml',
        'views/res_company_views.xml',
        'views/res_config_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'installable': True,
}
