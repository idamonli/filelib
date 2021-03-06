# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'e2yun_Online Ticket Submission',
    'category': 'Website',
    'summary': 'e2yun 服务订单表单在线提交 ',
    'description': """在线提交服务订单.""",
    'application': True,
    'depends': [
        'web', 'website', 'website_helpdesk', 'helpdesk', 'website_helpdesk_form',
        'im_livechat', 'portal', 'mail', "rating"
    ],
    'data': [
        'security/helpdesk_security.xml',
        'security/ir.model.access.csv',
        'data/website_helpdesk.xml',
        'views/helpdesk_templates.xml',
        'views/commonproblems_templates.xml',
        'views/helpdesk_views.xml',
        'views/helpdesk_ticket_brand_type.xml',
        'views/helpdesk_tickchat_uuid.xml',
        'views/helpdesk_rating.xml',
        'views/helpdesk_team_views_subuser.xml',
        'views/helpdesk_csoffline.xml',

    ],
    'qweb': [
        "static/src/xml/helpdeskdesk_matnr.xml",
        "static/src/xml/helpdeskdesk_livechat_out.xml"
    ],
    'license': 'OEEL-1',
    'installable': True,
    'auto_install': False,
    'active': False,
    'web': True,
}
