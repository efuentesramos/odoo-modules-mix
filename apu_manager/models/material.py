#-*- coding: utf-8 -*-

from odoo import models, fields, api


class material(models.Model):
    _name = 'apu.manager.material'
    _description = 'Materiales (Maquinaria)'

    name = fields.Char(string='Descripcion de Material')
    unit_measurement = fields.Char(string='Unidad', store=True)
    unit_cost = fields.Float(string="Costo Unitario")


