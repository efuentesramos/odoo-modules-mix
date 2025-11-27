# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
# from datetime import date


class BuggieBillingStatement(models.Model):
    _name = 'buggie.billing.statement'
    _description = 'Cuenta de cobro de alquiler de buggies'

    name = fields.Char(string='Referencia', required=True,
                       default='Nuevo', copy=False)
    customer_id = fields.Many2one('res.partner', 
                                  string='Cliente',
                                  required=True)
    date_from = fields.Date(string='Desde', required=True)
    date_to = fields.Date(string='Hasta', required=True)

    rental_ids = fields.One2many('buggie.billing.detail', 
                                 'statement_id', 
                                 string='Alquileres facturados'
                                 )
    total = fields.Float(string='Total', compute='_compute_total', store=True)

    state = fields.Selection([
        ('draft', 'Borrador'),
        ('confirmed', 'Confirmado'),
    ], default='draft')

    # Campos para Abonos o pagos parciales
    payment_ids = fields.One2many('buggie.billing.payment', 'billing_id',
                                  string='Abonos')
    total_payments = fields.Float(
        string='Total Abonado',
        compute='_compute_total_payments',
        store=True
        )
    balance_due = fields.Float(
        string='Saldo Pendiente',
        compute='_compute_total_payments',
        store=True)

    @api.depends('payment_ids.amount', 'total')
    def _compute_total_payments(self):
        for record in self:
            total_payments = sum(record.payment_ids.mapped('amount'))
            record.total_payments = total_payments
            record.balance_due = record.total - total_payments

    @api.depends('rental_ids.total_amount')
    def _compute_total(self):
        for rec in self:
            rec.total = sum(r.total_amount for r in rec.rental_ids)

    @api.model
    def create(self, vals):
        if vals.get('name') == 'Nuevo':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'buggie.billing.statement') or 'Nuevo'
        return super().create(vals)

    def action_fill_rentals(self):
        for rec in self:
            if not rec.customer_id or not rec.date_from or not rec.date_to:
                raise ValidationError(
                    "Debe seleccionar cliente y rango de fechas."
                )

            # Buscar alquileres válidos no incluidos ya en otra cuenta
            domain = [
                ('customer_id', '=', rec.customer_id.id),
                ('rental_date', '>=', rec.date_from),
                ('rental_date', '<=', rec.date_to),
                ('id', 'not in',
                 self.env['buggie.billing.detail'].
                 search([]).mapped('rental_id').ids)
            ]
            rentals = self.env['buggie.rental'].search(domain)

            # Crear detalles
            for rental in rentals:
                self.env['buggie.billing.detail'].create({
                    'statement_id': rec.id,
                    'rental_id': rental.id
                })
