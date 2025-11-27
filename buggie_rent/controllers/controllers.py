# -*- coding: utf-8 -*-
# from odoo import http


# class BuggieRent(http.Controller):
#     @http.route('/buggie_rent/buggie_rent', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/buggie_rent/buggie_rent/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('buggie_rent.listing', {
#             'root': '/buggie_rent/buggie_rent',
#             'objects': http.request.env['buggie_rent.buggie_rent'].search([]),
#         })

#     @http.route('/buggie_rent/buggie_rent/objects/<model("buggie_rent.buggie_rent"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('buggie_rent.object', {
#             'object': obj
#         })
