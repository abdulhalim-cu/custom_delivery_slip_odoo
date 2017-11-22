# -*- coding: utf-8 -*-
from odoo import http

# class InheritDeliveryslipOdoo11(http.Controller):
#     @http.route('/inherit_deliveryslip_odoo11/inherit_deliveryslip_odoo11/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inherit_deliveryslip_odoo11/inherit_deliveryslip_odoo11/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inherit_deliveryslip_odoo11.listing', {
#             'root': '/inherit_deliveryslip_odoo11/inherit_deliveryslip_odoo11',
#             'objects': http.request.env['inherit_deliveryslip_odoo11.inherit_deliveryslip_odoo11'].search([]),
#         })

#     @http.route('/inherit_deliveryslip_odoo11/inherit_deliveryslip_odoo11/objects/<model("inherit_deliveryslip_odoo11.inherit_deliveryslip_odoo11"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inherit_deliveryslip_odoo11.object', {
#             'object': obj
#         })