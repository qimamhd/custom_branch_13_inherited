# -*- coding: utf-8 -*-
{
    'name': 'custom_branch_13_inherited',
	'version': '13.0.1.0.0',
	'summary': 'custom_branch_13_inherited',
	'category': 'Tools',
	'author': 'Developers team',
	'maintainer': 'qimamhd-tech Techno Solutions',
	'company': 'qimamhd-tech Techno Solutions',
	'website': 'https://www.qimamhd-tech.com',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [ 'custom_branch_13','base'
    ],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',

        'views/branches_view.xml',
        'views/branch_server_action.xml',

        #'wizards/recap.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
