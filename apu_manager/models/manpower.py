#-*- coding: utf-8 -*-

from odoo import models, fields, api


class manpower(models.Model):
    _name = 'apu.manager.manpower'
    _description = 'Mano De Obra'

    name = fields.Char(string='Descripcion')
    unit_measurement = fields.Char(string='Unidad', store=True)
    unit_cost = fields.Float(string="Costo Unitario")
