
from odoo import fields, models

class AnalyticAccount(models.Model):
    _inherit = "account.analytic.account"

    blocked = fields.Boolean(string="Blocked", default=False)

    def toggle_block(self):
        for record in self:
            record.blocked = not record.blocked
