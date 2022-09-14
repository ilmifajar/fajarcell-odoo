from odoo import api, fields, models


class person(models.Model):
    _name = 'ilmimart.person'
    _description = 'New Description'

    name = fields.Char(string='Name')
    alamat = fields.Char(string='alamat')
    tgl_lahir = fields.Datetime(string='tanggal lahir')
    


class kasir(models.Model):
    _name = 'ilmimart.kasir'
    _inherit = 'ilmimart.person'
    _description = 'New Description'

    id_kasir = fields.Char(string='id kasir')



class cleaningservice(models.Model):
    _name = 'ilmimart.cleaningservice'
    _inherit = 'ilmimart.person'
    _description = 'New Description'

    id_cln = fields.Char(string='id cleaning service')
    

    

    
