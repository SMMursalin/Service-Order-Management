from odoo import api, fields, models, _
from datetime import date
from odoo.exceptions import ValidationError
from dateutil import relativedelta

class ProductData(models.Model):
    _name = "product.data"
    _description = "Product Data"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'imei_no'

    imei_no = fields.Char(string='IMEI No', readonly=True)

    # branch = fields.Selection([('idb','IDB'),('dhaka','Dhaka'),('bashundhora','Bashundhora')],string='Branch', tracking=True)
    # dealer = fields.Selection([('corporate', 'Corporate'), ('self', 'Self')], string='Dealer',tracking=True)
    # communication_media = fields.Selection([('email', 'Email'), ('call', 'Call'), ('facebook', 'whatsapp')], string='Communication Media',tracking=True)
    # service_type = fields.Selection([('pickup', 'Pickup'), ('courier', 'Courier'), ('onsite', 'Onsite')], string='Service Type',tracking=True)
    # imei_sno =fields.Text(string="IMEI No")
    invoice_ids =fields.Many2one('invoice.data',string='Invoice No')
    invoice_no = fields.Char(related='invoice_ids.invoice_no')
    # invoice_attachment = fields.Text(string="Invoice Attachment")
    pop_date = fields.Date(string="Purchase date(pop)")
    customer = fields.Many2one('res.partner', required = True  )
    product = fields.Many2one('product.product', required = True  )
    warranty_status = fields.Selection([('warranty', 'Warranty'), ('non-warranty', 'Non-warranty')], string='Warranty status',tracking=True)
    warranty_expire_date_l = fields.Date(string="Warranty expire date l")
    warranty_expire_date_p = fields.Date(string="Warranty expire date p")
    guaranty_expiry_date = fields.Date(string="Guaranty expiry date")
    # warranty_void_reason = fields.Selection([('drop', 'Drop'), ('self-damage', 'Self-damage'),('water-damaged','Water-damaged'),('other','Other')], string='Warranty void reason',tracking=True)
    # department = fields.Selection([('hp', 'HP'), ('dell', 'Dell'),('sony','Sony'),('smart','Smart')], string='Department',tracking=True)
    # priority_level = fields.Selection([('extreme', 'Extreme'), ('high', 'High'),('medium','Medium'),('low','low')], string='priority_level',tracking=True)
    # possible_delivery_date = fields.Date(string="Possible delivery date")
    # customer_remarks = fields.Text(string="customer remarks")
    #
    # remarks =







    @api.model
    def create(self, vals):
        vals['imei_no'] = self.env['ir.sequence'].next_by_code('product.data')
        return super(ProductData, self).create(vals)

