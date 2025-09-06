# -*- coding: utf-8 -*-
from odoo import models, fields


class TreatmentLines(models.Model):
    _name = "treatment.lines"
    _description = "Treatment Lines"
    _order = "treatment_id"
    _rec_name = "treatment_id"

    treatment_id = fields.Many2one(
        comodel_name="treatment",
        string="Treatment",
        required=True
    )
    patient_id = fields.Many2one(
        comodel_name="res.patient",
        string="Patient",
    )
    treatment_name = fields.Char(
        string="Treatment Name",
        related="treatment_id.name",
        store=True
    )
    treatment_code = fields.Char(
        string="Treatment Code",
        related="treatment_id.code",
        store=True
    )
