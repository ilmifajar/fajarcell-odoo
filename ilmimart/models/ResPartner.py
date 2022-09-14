from odoo import api, fields, models


class ResParner(models.Model):
    _inherit = 'res.partner'
    _description = 'New Description'

    is_konsumen = fields.Boolean(string='is konsumen')
    is_direksi = fields.Boolean(string='is direksi')
    
    
