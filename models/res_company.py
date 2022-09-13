# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api, _

class res_company(models.Model):
    _inherit = "res.company"

    def get_allowed_user_branch(self):

        select = [(i['id']) for i in self.env.user.sudo().allowed_branch_ids]
        domain = [('id', 'in', select)]
        return {
            'name': 'Branches',
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'domain': domain,
            'context': {'create': 0},

            'res_model': 'custom.branches',
            'target': 'current'
        }
