from odoo import api, fields, models


class produk(models.Model):
    _name = 'fajarcell.produk'
    _description = 'New Description'

    name = fields.Char(string='Name')
    harga_beli = fields.Integer(string='Harga Modal', required=True)
    harga_jual = fields.Integer(string='Harga Jual', required=True)
    operatorproduk_id = fields.Many2one(comodel_name='fajarcell.operatorproduk',
                                        string='operator produk',
                                        ondelete='cascade')
    provider_id = fields.Many2many(comodel_name='fajarcell.provider', string='provider')
    stok = fields.Integer(string='stok')
