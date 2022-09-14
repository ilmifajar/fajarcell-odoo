from odoo import api, fields, models


class barangdatang(models.TransientModel):
    _name = 'fajarcell.produkdatang'

    produk_id = fields.Many2one(
        comodel_name='fajarcell.produk', 
        string='nama produk', 
        required=True)
    jumlah = fields.Integer(
        string='jumlah', 
        required=False)

    def button_produk_datang(self):
        for line in self:
            self.env['fajarcell.produk'].search([('id', '=', line.produk_id.id)]).write(
                {'stok': line.produk_id.stok +  line.jumlah}
            )