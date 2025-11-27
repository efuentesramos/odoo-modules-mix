from odoo import models, fields, api
from odoo.exceptions import ValidationError


class BuggieBillingPayment(models.Model):

    _name = 'buggie.billing.payment'
    _description = 'Pagos o Abonos de Cuenta de Cobro'
    _order = 'payment_date desc'

    billing_id = fields.Many2one('buggie.billing.statement', string='Cuenta de Cobro', ondelete='cascade', required=True)
    payment_date = fields.Date(string='Fecha de Abono', default=fields.Date.today, required=True)
    amount = fields.Float(string='Monto del Abono', required=True)
    notes = fields.Char(string='Observaciones')

    # Relacionado con compañía y cliente para facilitar reporting
    customer_id = fields.Many2one(related='billing_id.customer_id', store=True)

    @api.constrains('billing_id', 'amount')
    def _check_balance_before_payment(self):
        for rec in self:
            if rec.billing_id.balance_due <= 0:
                raise ValidationError(
                    f"La cuenta de cobro '{rec.billing_id.name}' ya está saldada. "
                    "No se pueden registrar más abonos."
                )
            if rec.amount > rec.billing_id.balance_due:
                raise ValidationError(
                    f"El monto del abono ({rec.amount}) excede el saldo pendiente "
                    f"({rec.billing_id.balance_due})."
                )
