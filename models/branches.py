from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class xx_branches(models.Model):
    _inherit = 'custom.branches'

    branch_name = fields.Char(string="اسم الفرع حسب السجل")
    bank_account_id = fields.Many2one('res.partner.bank', 'الحساب البنكي')
    building_no = fields.Char(string="رقم المبنى")
    District = fields.Char(string="الحي")
    additional_no = fields.Char(string="الرقم الاضافي للعنوان")
    street = fields.Char(string="اسم الشارع")
    city = fields.Char(string="المدينة")
    country_id = fields.Many2one('res.country', string="البلد")
    zip = fields.Char(string="الرمز البريدي")
    unit_no =  fields.Char(string="رقم الوحدة")
    company_registry = fields.Char(string="معرف اخر")
    company_info_breif_in_report = fields.Selection([('detail_address','اظهار الرمز الوطني نفس نموذج هيئة الزكاة والدخل'), ('breif_address','اظهار الرمز الوطني في سطر واحد(هذا الخيار تحت مسئولية العميل)')]
                                                    ,string="طريقة عرض الرمز الوطني", default='detail_address')


    branch_signture = fields.Binary(string="التوقيع")
