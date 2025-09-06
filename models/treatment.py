# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Treatment(models.Model):
    _name = "treatment"
    _description = "Treatment record"
    _order = "name"

    @api.constrains("code")
    def _check_medical_026_no_sequences(self):
        for record in self:
            if record.code and "026" in record.code:
                raise ValidationError(
                    _("The treatment code cannot contain the sequence '026'.")
                )

    code = fields.Char(string="Treatment Code", required=True)
    name = fields.Char(string="Treatment Name", required=True)
    treating_doctor = fields.Char(string="Treating Doctor", required=True)
