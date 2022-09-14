from odoo import models, fields

class PartnerXlsx(models.AbstractModel):
    _name = 'report.ilmimart.report_supplier_xlsx'
    _inherit = 'report.report_xlsx.abstract'

    tgl_lap = fields.date.today()

    def generate_xlsx_report(self, workbook, data, supplier):
        sheet = workbook.add_worksheet('daftar supplier')
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, str(self.tgl_lap))
        sheet.write(1, 0, 'nama perusahaan')
        sheet.write(1, 1, 'alamat')
        sheet.write(1, 2, 'no telpon')
        sheet.write(1, 3, 'produk')
        row = 2
        col = 0
        for obj in supplier:
            col = 0
            sheet.write(row, col, obj.name)
            sheet.write(row, col+1, obj.alamat)
            sheet.write(row, col+2, obj.no_telp)
            for xxx in obj.barang_id:
                sheet.write(row, col+3, xxx.name)   
                col += 1
            row += 1