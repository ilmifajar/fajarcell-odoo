from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class Penjualan(models.Model):
    _name = 'fajarcell.penjualan'
    _description = 'Penjualan'

    name = fields.Char(string='No. Nota')
    nama_pembeli = fields.Char(string='Nama Pembeli')
    tgl_penjualan = fields.Datetime(
        string='Tanggal Transaksi',
        default=fields.Datetime.now())
    total_bayar = fields.Integer(
        string='Total Pembayaran',
        compute='_compute_totalbayar')
    detailpenjualan_ids = fields.One2many(
        comodel_name='fajarcell.detailpenjualan',
        inverse_name='penjualan_id',
        string='Detail Penjualan')

    @api.depends('detailpenjualan_ids')
    def _compute_totalbayar(self):
        for line in self:
            result = sum(self.env['fajarcell.detailpenjualan'].search(
                [('penjualan_id', '=', line.id)]).mapped('subtotal'))
            line.total_bayar = result
    
    @api.ondelete(at_uninstall=False)
    def __ondelete_penjualan(self):
        if self .detailpenjualan_ids:
            a=[]
            for rec in self:
                a = self.env['fajarcell.detailpenjualan'].search([('penjualan_id','=',rec.id)])
                print(a)
            for ob in a:
                print(str(ob.produk_id.name) + ' ' + str(ob.qty))
                ob.produk_id.stok += ob.qty

    def write(self,vals):
        for rec in self:
            a = self.env['fajarcell.detailpenjualan'].search([('penjualan_id','=',rec.id)])
            print(a)
            for data in a:
                print(str(data.produk_id.name)+' '+str(data.qty)+' '+str(data.produk_id.stok))
                data.produk_id.stok += data.qty
        record = super(Penjualan,self).write(vals)
        for rec in self:
            b = self.env['fajarcell.detailpenjualan'].search([('fajarcell_id','=',rec.id)])
            print(a)
            print(b)
            for databaru in b:
                if databaru in a:
                    print(str(databaru.produk_id.name)+' '+str(databaru.qty)+' '+str(databaru.produk_id.stok))
                    databaru.produk_id.stok -= databaru.qty
                else:
                    pass
        return record

class DetailPenjualan(models.Model):
    _name = 'fajarcell.detailpenjualan'
    _description = 'Detail'

    name = fields.Char(string='Nama')
    penjualan_id = fields.Many2one(
        comodel_name='fajarcell.penjualan',
        string='Detail Penjualan')
    produk_id = fields.Many2one(
        comodel_name='fajarcell.produk',
        string='List produk')
    harga_satuan = fields.Integer(
        string='Harga Satuan',
        onchange='_onchange_produk_id')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')

    @api.depends('harga_satuan', 'qty')
    def _compute_subtotal(self):
        for line in self:
            line.subtotal = line.qty * line.harga_satuan

    @api.onchange('produk_id')
    def _onchange_barang_id(self):
        if self.produk_id.harga_jual:
            self.harga_satuan = self.produk_id.harga_jual
    
    @api.model
    def create(self, vals):
        line = super(DetailPenjualan, self).create(vals)
        if line.qty:
            # Mendapatkan data berdasarkan ID pada barang_id
            self.env['fajarcell.produk'].search(
                [('id', '=', line.barang_id.id)]
            ).write({'stok': line.barang_id.stok - line.qty})

    @api.constrains('qty')
    def check_quantity(self):
        for rec in self:
            if rec.qty <1:
                raise ValidationError("mau belanja {} berapa banyak sih...".format(rec.produk_id.name))
            elif(rec.barang_id.stok < rec.qty):
                raise ValidationError('stok {} tidak mencukupi, hanya tersedia {}'.format(rec.produk_id.name,rec.produk_id.stok))

