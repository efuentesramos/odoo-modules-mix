#-*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date
from odoo.exceptions import ValidationError


class detailmanpower(models.Model): 
    _name = 'detail.manpower'

    apu_id = fields.Many2one('apu' ,string="APU")

    manpower_id = fields.Many2one(
        string='Mano De Obra ',
        comodel_name='apu.manager.manpower',        
        
    )

    description = fields.Char(string='Descripcion',related='manpower_id.name', store=True)
    unit_measurement = fields.Char(string='Unidad',related='manpower_id.unit_measurement', store=True)
    unit_cost = fields.Float(string="Costo Unitario",related='manpower_id.unit_cost', store=True)
    amount = fields.Float(string="Cantidad", store=True)
    manpower_cost = fields.Float(string="Costo de equipos", compute='_compute_manpower_cost')
    profit = fields.Float(string = "Utilidad  %")
    total_profit = fields.Float(string = "Utilidad Total", compute='_compute_total_profit')
    sale_price  = fields.Float(string = "Precio de Venta", compute='_compute_sale_price')



    @api.depends('unit_cost', 'amount')
    def _compute_manpower_cost(self):
        
        for record in self:
            
            record.manpower_cost = record.unit_cost * record.amount
           


    @api.constrains('profit')
    def _check_utilidad_range(self):
        for record in self:
            if not (1 <= record.profit <= 100):
                raise ValidationError("El valor de 'Utilidad' debe estar entre 1 y 100.")
            
    

    @api.depends('manpower_cost', 'profit')
    def _compute_total_profit(self):
        
        for record in self:
            
            record.total_profit =( record.manpower_cost * record.profit) /(100-record.profit)

    

    @api.depends('manpower_cost', 'total_profit')
    def _compute_sale_price(self):
        
        for record in self:
            
            record.sale_price = record.manpower_cost + record.total_profit