from odoo import api, fields, models, _
from datetime import date
from odoo.exceptions import ValidationError
from dateutil import relativedelta

class ServiceOrder(models.Model):
    _name = "service.order"
    _description = "ServiceOrder"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'order_no'

    order_no = fields.Char(string='Order No', readonly=True)
    order_date = fields.Date(string="Order date")
    branch = fields.Selection([('idb','IDB'),('dhaka','Dhaka'),('bashundhora','Bashundhora')],string='Branch', tracking=True)
    dealer = fields.Selection([('corporate', 'Corporate'), ('self', 'Self')], string='Dealer',tracking=True)
    # dealer = fields.Many2many('res.partner.category',string='Dealer', required = True)

    dealer1 = fields.Many2one(
        'res.partner',
        string="Dealer/Retailer",
        domain=['|', ('category_id', '=', 'Dealer'), ('category_id', '=', 'Retailer')]
    )




    communication_media = fields.Selection([('email', 'Email'), ('call', 'Call'), ('facebook', 'whatsapp')], string='Communication Media',tracking=True)
    service_type = fields.Selection([('pickup', 'Pickup'), ('courier', 'Courier'), ('onsite', 'Onsite')], string='Service Type',tracking=True)
    imei_no =fields.Many2one('product.data', string='IMEI No', ondelete='cascade')
    invoice_no =fields.Text(string="Invoice No")
    invoice_attachment = fields.Image(string="Invoice Attachment")
    pop_date = fields.Date(related='imei_no.pop_date', readonly=True)
    customer = fields.Many2one(related='imei_no.customer', readonly=True)
    product = fields.Many2one(related='imei_no.product', readonly=True)
    warranty_status = fields.Selection(related='imei_no.warranty_status', readonly=False)
    warranty_expire_date_l = fields.Date(related='imei_no.warranty_expire_date_l', readonly=True)
    warranty_expire_date_p = fields.Date(related='imei_no.warranty_expire_date_p', readonly=True)
    guaranty_expiry_date = fields.Date(related='imei_no.guaranty_expiry_date', readonly=True)
    warranty_void_reason = fields.Selection([('drop', 'Drop'), ('self-damage', 'Self-damage'),('water-damaged','Water-damaged'),('other','Other')], string='Warranty void reason',tracking=True)
    department = fields.Selection([('hp', 'HP'), ('dell', 'Dell'),('sony','Sony'),('smart','Smart')], string='Department',tracking=True)
    priority_level = fields.Selection([('extreme', 'Extreme'), ('high', 'High'),('medium','Medium'),('low','low')], string='priority_level',tracking=True)
    possible_delivery_date = fields.Date(string="Possible delivery date")
    customer_remarks = fields.Text(string="Customer remarks")
    remarks = fields.Text(string="Remarks")

    symptoms = fields.Text(string="Symptoms")
    reason = fields.Text(string="reason")

    repair_status = fields.Selection([('repaired', 'Repaired'), ('not-repaired', 'Not-repaired'),('repairing','Repairing')], string='repair_status',tracking=True)
    product_received_date = fields.Datetime(string="Product Received Date")
    delivery_date = fields.Date(string="Delivery Date")
    item_receive_branch = fields.Selection([('1000fix', '1000fix'), ('smartbd', 'Smartbd')], string='item_receive_branch',tracking=True)
    item_receive_status = fields.Selection([('received', 'Received'), ('not-received', 'Not-received')], string='item_receive_status',tracking=True)
    is_received_from_customer = fields.Boolean('Is received from customer?')
    is_so_transfer = fields.Boolean('Is SO transfer?')
    is_sms = fields.Boolean('Is SMS?')

    symptoms_lines_ids = fields.One2many('symptoms.lines','order_id', string="Symptoms")




    @api.model
    def create(self, vals):
        vals['order_no'] = self.env['ir.sequence'].next_by_code('service.order')
        return super(ServiceOrder, self).create(vals)

    def action_symptoms(self):
        return

    def write(self, values):
        res = super(ServiceOrder, self).write(values)
        sl_no = 0
        for line in self.symptoms_lines_ids:
            sl_no += 1
            line.sl_no = sl_no
        return res


class SymptomsLines(models.Model):
    _name = "symptoms.lines"
    _description = "Symptoms Lines"

    symptoms1 = fields.Text(string="Symptoms")
    reason1 = fields.Text(string="reason")
    sl_no = fields.Integer(string='SLN.')

    order_id = fields.Many2one('service.order', string="Order")

