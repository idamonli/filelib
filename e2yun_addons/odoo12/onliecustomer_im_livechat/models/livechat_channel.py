# coding=utf-8

import logging
import random
import werkzeug
from odoo.http import request

from odoo import models, api, fields

_logger = logging.getLogger(__name__)


class LivechatChannel(models.Model):
    _inherit = 'im_livechat.channel'

    @api.model
    def get_online_mail_channel(self, livechat_channel_id, anonymous_name):
        # get the avalable user of the channel
        if not request.session.uid:
            return werkzeug.utils.redirect('/web/login?error=请登录然后操作')
        users = self.sudo().browse(livechat_channel_id).get_available_users()
        isonlinecustomer = True;
        if len(users) == 0:  # 如果用户不在线 选择所有用户
            users = self.get_wx_available_users(self.sudo().browse(livechat_channel_id).user_ids)
        if len(users) == 0:  # 如果没设置在线客服返回
            return False
        # choose the res.users operator and get its partner id
        user = random.choice(users)
        operator_partner_id = user.partner_id.id
        # partner to add to the mail.channel
        channel_partner_to_add = [(4, operator_partner_id)]
        if self.env.user and self.env.user.active:  # valid session user (not public)
            channel_partner_to_add.append((4, self.env.user.partner_id.id))
        # create the session, and add the link with the given channel
        mail_channel = self.env["mail.channel"].with_context(mail_create_nosubscribe=False).sudo().create({
            'channel_partner_ids': channel_partner_to_add,
            'livechat_channel_id': livechat_channel_id,
            'anonymous_name': anonymous_name,
            'channel_type': 'livechat',
            'name': ', '.join([anonymous_name, user.name]),
            'public': 'private',
            'email_send': False,
        })
        mail_channel._broadcast([operator_partner_id])
        return mail_channel.sudo().with_context(im_livechat_operator_partner_id=operator_partner_id).channel_info()[0]

    @api.multi
    def get_wx_available_users(self, user_ids):
        return user_ids.filtered(lambda user: user.wx_user_id and user.is_defaultlivechat)
