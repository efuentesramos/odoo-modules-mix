# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date



class BuggieRental(models.Model):
    _name = 'buggie.rental'
    _description = 'Alquiler de Buggies'

    name = fields.Char(
        string='Referencia',
        required=True,
        copy=False,
        readonly=True,
        default='Nuevo'
    )
    customer_id = fields.Many2one(
        'res.partner',
        string='Cliente',
        required=True,
        help='Cliente que realiza el alquiler del buggy.',
        index=True
    )

    rental_date = fields.Datetime(
        string='Fecha de Salida',
        required=True,
        default=fields.Datetime.now
    )

    rental_lines = fields.One2many('rental.detail', 'rental_id',
                                   string='Detalle del Alquiler', copy=True)

    total_amount = fields.Float(
        string='Total', compute='_compute_amounts', store=True
    )
    amount_paid = fields.Float(string='Abono', default=0.0)
    amount_due = fields.Float(
        string='Saldo', compute='_compute_amounts', store=True
    )

    price_per_day = fields.Float(
        string='Tarifa de alquiler',
        compute='_compute_price_per_day',
        store=True,
        readonly=True
        )

    @api.depends('rental_date')
    def _compute_price_per_day(self):
        for record in self:
            if record.rental_date:
                record.price_per_day = record._get_rate_for_date(record.rental_date)
            else:
                record.price_per_day = 0.0

    def _get_rate_for_date(self, rental_date):
        Rate = self.env['buggie.rate']
        rental_date = fields.Date.to_date(rental_date)

        rate = Rate.search([
            ('start_date', '<=', rental_date),
            '|',
            ('end_date', '>=', rental_date),
            ('end_date', '=', False),
        ], order='start_date desc', limit=1)

        return rate.price_per_day if rate else 0.0

    @api.model
    def create(self, vals):
        # Asignar número de secuencia si el nombre es 'Nuevo'
        if vals.get('name', 'Nuevo') == 'Nuevo':
            vals['name'] = self.env['ir.sequence'].next_by_code('buggy.rental') or 'Nuevo'

        # Asignar precio por día desde tarifa vigente si se proporciona rental_date
        if 'rental_date' in vals:
            price = self._get_rate_for_date(vals['rental_date'])
            vals['price_per_day'] = price

        return super().create(vals)

    @api.depends('rental_lines.subtotal', 'amount_paid')
    def _compute_amounts(self):
        for record in self:
            total = sum(line.subtotal for line in record.rental_lines)
            record.total_amount = total
            record.amount_due = total - record.amount_paid
