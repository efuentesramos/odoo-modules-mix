#-*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date
from odoo.exceptions import ValidationError


class detailEquipment(models.Model): 
    _name = 'detail.equipment'

    apu_id = fields.Many2one('apu' ,string="APU")

    equipment_id = fields.Many2one(
        string='Equipos ',
        comodel_name='apu.manager.equipment',        
        
    )

    description = fields.Char(string='Descripcion',related='equipment_id.name', store=True)
    unit_measurement = fields.Char(string='Unidad',related='equipment_id.unit_measurement', store=True)
    unit_cost = fields.Float(string="Costo Unitario",related='equipment_id.unit_cost', store=True)
    amount = fields.Float(string="Cantidad", store=True)
    equipment_cost = fields.Float(string="Costo de equipos", compute='_compute_equipment_cost')
    profit = fields.Float(string = "Utilidad  %")
    total_profit = fields.Float(string = "Utilidad Total", compute='_compute_total_profit')
    sale_price  = fields.Float(string = "Precio de Venta", compute='_compute_sale_price')



    @api.depends('unit_cost', 'amount')
    def _compute_equipment_cost(self):
        
        for record in self:
            
            record.equipment_cost = record.unit_cost * record.amount
           


    @api.constrains('profit')
    def _check_utilidad_range(self):
        for record in self:
            if not (1 <= record.profit <= 100):
                raise ValidationError("El valor de 'Utilidad' debe estar entre 1 y 100.")
            
    

    @api.depends('equipment_cost', 'profit')
    def _compute_total_profit(self):
        
        for record in self:
            
            record.total_profit =( record.equipment_cost * record.profit) /(100-record.profit)

    

    @api.depends('equipment_cost', 'total_profit')
    def _compute_sale_price(self):
        
        for record in self:
            
            record.sale_price = record.equipment_cost + record.total_profit