from odoo import api, fields, models


class Barang(models.Model):
    _name = 'ilmimart.barang'
    _description = 'New Description'

    name = fields.Char(string='Nama barang')
    harga_beli = fields.Integer(string='harga modal',required=True)
    harga_jual = fields.Integer(string='harga jual',required=True)
    kelompokbarang_id = fields.Many2one(comodel_name='ilmimart.kelompokbarang', 
                                        string='kelompok barang', 
                                        ondelete='cascade')
    supplier_id = fields.Many2many(comodel_name='ilmimart.supplier', string='supplier')
    stok = fields.Integer(string='stok')
    
    
    
    
