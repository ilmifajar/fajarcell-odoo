from odoo import api, fields, models


class KelompokBarang(models.Model):
    _name = 'ilmimart.kelompokbarang'
    _description = 'New Description'

    name = fields.Selection([
        ('makananbasah', 'makanan basah'), ('makanankering', 'makananan kering'), ('minuman', 'minuman')
    ], string='nama kelompok')
    
    kode_kelompok = fields.Char(onchange='_compute_kode_kelompok', string='kode_kelompok')
    
    @api.onchange('name')
    def _compute_kode_kelompok(self):
        if (self.name == 'makanan basah'):
            self.kode_kelompok = 'mak01'
        elif (self.name == 'makanan kering'):
            self.kode_kelompok = 'mak02'
        elif (self.name == 'minuman'):
            self.kode_kelompok = 'min'
    kode_rak = fields.Char(string='kode rak')
    barang_ids = fields.One2many(comodel_name='ilmimart.barang', 
                                 inverse_name='kelompokbarang_id', 
                                 string='daftar barang')  
    jml_item = fields.Char(compute='_compute_jml_item', string='jumlah_item')
 
    @api.depends('barang_ids')
    def _compute_jml_item(self):
        for rec in self:
            a = self.env['ilmimart.barang'].search([('kelompokbarang_id','=', rec.id)]).mapped('name')
            b = len(a)
            rec.jml_item = b
            rec.daftarisi = a

    daftarisi = fields.Char(string='daftar')
        
           
            

    
            
    
    