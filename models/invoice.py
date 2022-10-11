from odoo import api, fields, models, _
from datetime import date
from odoo.exceptions import ValidationError
from dateutil import relativedelta

class InvoiceData(models.Model):
    _name = "invoice.data"
    _description = "Invoice Data"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'invoice_no'

    imei_ids = fields.Many2one('product.data', string='IMEI No')

    invoice_no = fields.Char(string='Invoice No', readonly=True)
    product = fields.Many2one(related='imei_ids.product', readonly=True)

    @api.model
    def create(self, vals):
        vals['invoice_no'] = self.env['ir.sequence'].next_by_code('invoice.data')
        return super(InvoiceData, self).create(vals)