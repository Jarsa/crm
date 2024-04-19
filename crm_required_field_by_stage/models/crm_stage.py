# Copyright 2024 Jarsa
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models


class CrmStage(models.Model):
    _inherit = "crm.stage"

    required_field_ids = fields.Many2many(
        comodel_name="ir.model.fields",
        domain=[("model", "=", "crm.lead")],
        help="Fields that are required when the lead is in this stage.",
    )
    fields_stage_id = fields.Many2one(
        comodel_name="crm.stage",
        string="Inherit Fields from Stage",
        help="Inherit the required fields from this stage.",
        store=False,
    )

    @api.onchange("fields_stage_id")
    def _onchange_fields_stage_id(self):
        if self.fields_stage_id:
            self.required_field_ids = [
                (4, field.id) for field in self.fields_stage_id.required_field_ids
            ]
