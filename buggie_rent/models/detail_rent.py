# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date


class RentalDetail(models.Model):
    _name = 'rental.detail'
    _description = 'Detalle del Alquiler por Buggie'

    rental_id = fields.Many2one(
        'buggie.rental',
        string='Alquiler',
        required=True
    )
    buggie_id = fields.Many2one(
        'buggie.buggie',
        string='Buggie',
        required=True
    )

    delivery_date = fields.Datetime(
        string='Fecha de Entrega (Salida)',
        related='rental_id.rental_date',
        store=True,
        readonly=True,
    )

    return_date = fields.Datetime(string='Fecha de Retorno')
    is_returned = fields.Boolean(string='¿Retornado?', default=False)

    quantity_days = fields.Integer(
        string='Días a Cobrar', compute='_compute_days_and_subtotal',
        store=True
    )
    subtotal = fields.Float(
        tring='Subtotal', compute='_compute_days_and_subtotal',
        store=True
    )

    @api.depends('delivery_date', 'return_date', 'is_returned', 'rental_id.price_per_day')
    def _compute_days_and_subtotal(self):
        for record in self:
            if record.delivery_date:
                end_date = record.return_date.date() if record.is_returned and record.return_date else date.today()
                start_date = record.delivery_date.date()
                delta_days = (end_date - start_date).days
                days = max(delta_days + 1, 1)
                record.quantity_days = days
                record.subtotal = days * record.rental_id.price_per_day
            else:
                record.quantity_days = 0
                record.subtotal = 0.0
    
    def action_mark_returned(self):
        for record in self:
            if not record.is_returned:
                record.is_returned = True
                record.return_date = fields.Datetime.now()