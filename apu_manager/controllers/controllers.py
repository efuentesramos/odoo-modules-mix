# -*- coding: utf-8 -*-
# from odoo import http


# class ApuManager(http.Controller):
#     @http.route('/apu_manager/apu_manager', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/apu_manager/apu_manager/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('apu_manager.listing', {
#             'root': '/apu_manager/apu_manager',
#             'objects': http.request.env['apu_manager.apu_manager'].search([]),
#         })

#     @http.route('/apu_manager/apu_manager/objects/<model("apu_manager.apu_manager"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('apu_manager.object', {
#             'object': obj
#         })
