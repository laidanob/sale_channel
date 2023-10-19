# -*- coding: utf-8 -*-
from odoo import models, fields, api

class saleChannelAccountMove(models.Model):
    _inherit = 'account.move'
    
    sale_channel = fields.Many2one(string='Sale Channel', related='stock_move_id.group_id')
    # sale_channel_test = fields.Many2one(string='Sale Channel', related='sale_channel.sale_id')
   