# -*- coding: utf-8 -*-


from odoo import models, fields, api
from odoo.exceptions import ValidationError


class BuggieRate(models.Model):
    _name = 'buggie.rate'
    _description = 'Tarifa general para alquiler de buggies'

    price_per_day = fields.Float(string='Precio por Día', required=True)
    start_date = fields.Date(string='Fecha de Inicio', required=True)
    end_date = fields.Date(string='Fecha Final')

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for record in self:
            if record.end_date and record.start_date > record.end_date:
                raise ValidationError(
                    "La fecha de inicio debe ser anterior o igual a la fecha final."
                )