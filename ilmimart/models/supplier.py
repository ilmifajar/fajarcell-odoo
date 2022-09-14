from odoo import api, fields, models


class supplier(models.Model):
    _name = 'ilmimart.supplier'
    _description = 'New Description'

    name = fields.Char(string='Name perusahaan')
    alamat = fields.Char(string='alamat')
    no_telp = fields.Char(string='no telepon')
    barang_id = fields.Many2many(comodel_name='ilmimart.barang', string='barang')
    
    
    
