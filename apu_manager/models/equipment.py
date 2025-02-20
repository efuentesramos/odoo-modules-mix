#-*- coding: utf-8 -*-

from odoo import models, fields, api


class equipmet(models.Model):
    _name = 'apu.manager.equipment'
    _description = 'Equipos (Maquinaria)'

    name = fields.Char(string='Descripcion de equipo')
    unit_measurement = fields.Char(string='Unidad')
    unit_cost = fields.Float(string="Costo Unitario")


    