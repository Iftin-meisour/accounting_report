# -*- coding: utf-8 -*-
{
    'name': 'Mgs_accounting_reports',
    'version': '1.0.0',
    'summary': """ Mgs_accounting_reports Summary """,
    'author': '',
    'website': '',
    'category': '',
    'depends': ['base', 'web'],
    "data": [
        "views/account_report_views.xml"
    ],
    # 'assets': {
    #           'web.assets_backend': [
    #               'mgs_accounting_reports/static/src/**/*'
    #           ],
    #       },
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
