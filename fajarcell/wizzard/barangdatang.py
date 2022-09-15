from odoo import api, fields, models


class barangdatang(models.TransientModel):
    _name = 'fajarcell.barangdatang'

    produk_id = fields.Many2one(
        comodel_name='fajarcell.produk', 
        string='nama barang', 
        required=True)
    jumlah = fields.Integer(
        string='jumlah', 
        required=False)

    # def button_barang_datang(self):
    #     for line in self:
    #         self.env['fajarcell.produk'].search([('id', '=', line.produk_id.id)]).write(
    #             {'stok': line.produk_id.stok +  line.jumlah}
            # )
            
    def button_barang_datang(self):
        pass