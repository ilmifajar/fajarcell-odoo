from crypt import methods
import json


import json

from odoo import http, models, fields
from odoo.http import request


class fajarcell(http.Controller):
    @http.route('/fajarcell/getproduk', auth='public', method=['GET'])
    def getproduk(self, **kw):
        # Mengambil semua barang dari table barang
        produk = request.env['fajarcell.produk'].search([])
        items = []

        for item in produk:
            items.append({
                'nama_barang': item.name,
                'harga_jual': item.harga_jual,
                'stok': item.stok
            })
        
        return json.dumps(items)

    @http.route('/fajarcell/getprovider', auth='public', method=['GET'])
    def getprovider(self, **kw):
        provider = request.env['fajarcell.provider'].search([])
        items = []

        for item in provider:
            items.append({
                'nama_perusahaan': item.name,
                'alamat': item.alamat,
                'no_telepon': item.no_telp,
                'produk_id': item.produk_id[0].name
            })
        
        return json.dumps(items)