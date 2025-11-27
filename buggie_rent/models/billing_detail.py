# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class BuggieBillingDetail(models.Model):
    _name = 'buggie.billing.detail'
    _description = 'Alquiler incluido en cuenta de cobro'

    statement_id = fields.Many2one('buggie.billing.statement',
                                   string='Cuenta de cobro',
                                   ondelete='cascade')
    rental_id = fields.Many2one('buggie.rental',
                                string='Alquiler',
                                required=True)

    rental_name = fields.Char(related='rental_id.name', store=True)
    rental_date = fields.Datetime(related='rental_id.rental_date', store=True)
    total_amount = fields.Float(related='rental_id.total_amount', store=True)

    @api.constrains('rental_id')
    def _check_unique_rental_id(self):
        for record in self:
            existing = self.search([
                ('rental_id', '=', record.rental_id.id),
                ('id', '!=', record.id)
            ])
            if existing:
                raise ValidationError(
                    "Este alquiler ya fue incluido en otra cuenta de cobro."
                    )
