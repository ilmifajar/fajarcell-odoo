from odoo import http, models, fields
from odoo.http import request
import json

class ilmimart(http.Controller):
    @http.route('/ilmimart/getbarang', auth='public', method=['GET'])
    def getbarang(self, **kw):
        barang = request.env['ilmimart.barang'].search([])
        isi = []
        for bb in barang:
            isi.append({
                'nama_barang' : bb.name,
                'harga_jual' : bb.harga_jual,
                'stok' : bb.stok
            })
        return json.dumps(isi)

    @http.route('/ilmimart/getsupplier', auth='public', method=['GET'])
    def getsupplier(self, **kw):
        supplier = request.env['ilmimart.supplier'].search([])
        sup = []
        for s in supplier:
            sup.append({
                'nama_perusahaan' : s.name,
                'alamat' : s.alamat,
                'no_telp' : s.no_telp,
                'barang' :s.barang_id[0].name
            })
        return json.dumps(sup)
