from odoo import api, fields, models

class operatorproduk(models.Model):
    _name = 'fajarcell.operatorproduk'
    _description = 'New Description'

    name = fields.Selection([
        ('Telkomsel', 'Telkomsel'), ('im3', 'im3'), ('Indosat', 'Indosat')
    ], string='nama operator')
    
    kode_operator = fields.Char(onchange='_compute_kode_operator', string='kode_operator')
    
    @api.onchange('name')
    def _compute_kode_operator(self):
        if (self.name == 'Telkomsel'):
            self.kode_operator = 'provider01'
        elif (self.name == 'im3'):
            self.kode_operator = 'provider02'
        elif (self.name == 'Indosat'):
            self.kode_operator = 'provider03'
    kode_rak = fields.Char(string='kode rak')
    produk_ids = fields.One2many(comodel_name='fajarcell.produk', 
                                 inverse_name='operatorproduk_id', 
                                 string='daftar barang')  
    jml_item = fields.Char(compute='_compute_jml_item', string='jumlah_item')
 
    @api.depends('produk_ids')
    def _compute_jml_item(self):
        for rec in self:
            a = self.env['fajarcell.produk'].search([('operatorproduk_id','=', rec.id)]).mapped('name')
            b = len(a)
            rec.jml_item = b
            rec.daftarisi = a

    daftarisi = fields.Char(string='daftar')