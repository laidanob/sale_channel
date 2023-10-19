# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class SaleOrderChannel(models.Model):
    _inherit = "sale.order"
    
    sale_channel = fields.Many2one('sale.channel','Sale Channel',required=True)
    
    @api.onchange('sale_channel')
    def _warehouse_sale(self):
        channel_warehouse = self.sale_channel.stock_warehouse
        self.warehouse_id = channel_warehouse
        
    
  