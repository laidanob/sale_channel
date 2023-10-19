# -*- coding: utf-8 -*-
# from odoo import http


# class /users/admin/desktop/odoo15/odoo/customsAddons/saleChannel(http.Controller):
#     @http.route('//users/admin/desktop/odoo_15/odoo/customs_addons/sale_channel//users/admin/desktop/odoo_15/odoo/customs_addons/sale_channel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//users/admin/desktop/odoo_15/odoo/customs_addons/sale_channel//users/admin/desktop/odoo_15/odoo/customs_addons/sale_channel/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/users/admin/desktop/odoo_15/odoo/customs_addons/sale_channel.listing', {
#             'root': '//users/admin/desktop/odoo_15/odoo/customs_addons/sale_channel//users/admin/desktop/odoo_15/odoo/customs_addons/sale_channel',
#             'objects': http.request.env['/users/admin/desktop/odoo_15/odoo/customs_addons/sale_channel./users/admin/desktop/odoo_15/odoo/customs_addons/sale_channel'].search([]),
#         })

#     @http.route('//users/admin/desktop/odoo_15/odoo/customs_addons/sale_channel//users/admin/desktop/odoo_15/odoo/customs_addons/sale_channel/objects/<model("/users/admin/desktop/odoo_15/odoo/customs_addons/sale_channel./users/admin/desktop/odoo_15/odoo/customs_addons/sale_channel"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/users/admin/desktop/odoo_15/odoo/customs_addons/sale_channel.object', {
#             'object': obj
#         })
