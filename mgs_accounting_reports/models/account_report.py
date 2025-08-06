# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api, _
from odoo.exceptions import UserError, ValidationError

_logger = logging.getLogger(__name__)


class AccountReport(models.Model):
    _inherit = 'account.report'

    filter_product = fields.Boolean(
        string="Products",
        compute=lambda self: self._compute_report_option_filter('filter_product'),
        readonly=False,
        store=True,
        depends=['root_report_id', 'section_main_report_ids'],
    )       