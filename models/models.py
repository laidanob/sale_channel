# -*- coding: utf-8 -*-
from odoo import models, fields, api


class SaleChannel(models.Model):
    _name = 'sale.channel'
    _description = 'Sale Channel'
    _inherit = ['mail.thread','mail.activity.mixin']

    name = fields.Char('Name',required=True,tracking=True)
    stock_warehouse = fields.Many2one('stock.warehouse',"Warehouse")
    pos_config = fields.Many2one('pos.config',"Bill Journey")
    reference = fields.Char('Referencia', readonly=True)
    
    @api.model
    def create(self,vals):
        vals['reference'] = self.env['ir.sequence'].next_by_code("sale.channel")
        return super(SaleChannel,self).create(vals)


