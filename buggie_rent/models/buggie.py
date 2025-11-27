#-*- coding: utf-8 -*-

from odoo import models, fields, api


class buggie(models.Model):
    _name = 'buggie.buggie'
    _description = 'Buggie'

    name = fields.Char(string='Nombre o Código', required=True)
    description = fields.Text(string='Descripción')
    is_available = fields.Boolean(string='Disponible', default=True)
    active = fields.Boolean(default=True)