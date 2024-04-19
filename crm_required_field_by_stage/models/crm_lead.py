# Copyright 2024 Jarsa
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).

from odoo import _, models
from odoo.exceptions import UserError


class CrmLead(models.Model):
    _inherit = "crm.lead"

    def write(self, vals):
        for rec in self:
            if "stage_id" in vals:
                errors = []
                stage = self.env["crm.stage"].browse(vals["stage_id"])
                for field in stage.required_field_ids:
                    if not getattr(rec, field.name):
                        errors.append(field.field_description)
                if errors:
                    raise UserError(
                        _(
                            "The following fields are required to move to this stage:\n%(errors)s",
                            errors="\n".join(errors),
                        )
                    )
        return super().write(vals)
