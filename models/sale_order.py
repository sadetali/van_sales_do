from odoo import models

class SaleOrder(models.Model):
    _inherit = "sale.order"

    def action_save_do(self):
        self.ensure_one()
        return self.env.ref('van_sales_do.action_report_mobile_sale').report_action(self)
