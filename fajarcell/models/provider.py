from odoo import api, fields, models


class supplier(models.Model):
    _name = 'fajarcell.provider'
    _description = 'New Description'

    name = fields.Char(string='Name perusahaan')
    alamat = fields.Char(string='alamat')
    no_telp = fields.Char(string='no telepon')
    produk_id = fields.Many2many(comodel_name='fajarcell.produk', string='barang')
    