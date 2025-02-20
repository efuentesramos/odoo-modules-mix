
from odoo import models, fields, api


class other_item(models.Model):
    _name = 'other.item'
    _description = 'Otros Items para APU'

    name = fields.Char(string='Descripcion Items')
    unit_measurement = fields.Char(string='Unidad', store=True)
    unit_cost = fields.Float(string="Costo Unitario")


