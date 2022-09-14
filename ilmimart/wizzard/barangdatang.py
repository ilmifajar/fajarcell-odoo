from odoo import api, fields, models


class barangdatang(models.TransientModel):
    _name = 'ilmimart.barangdatang'

    barang_id = fields.Many2one(
        comodel_name='ilmimart.barang', 
        string='nama barang', 
        required=True)
    jumlah = fields.Integer(
        string='jumlah', 
        required=False)

    def button_barang_datang(self):
        for line in self:
            self.env['ilmimart.barang'].search([('id', '=', line.barang_id.id)]).write(
                {'stok': line.barang_id.stok +  line.jumlah}
            )