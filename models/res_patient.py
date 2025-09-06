# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class ResPatient(models.Model):
    _name = "res.patient"
    _description = "Res Patient Record"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "rec_name"
    _rec_name = "rec_name"

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            vals["patient_sequence"] = self.env["ir.sequence"].next_by_code(
                "res_patient_record_sequence"
            )
        return super(ResPatient, self).create(vals_list)

    @api.constrains("dni")
    def _check_dni_no_letters(self):
        for record in self:
            if not record.dni.isdigit():
                raise ValidationError(_("DNI must contain only numbers."))

    @api.depends("name", "surname", "patient_sequence")
    def _compute_rec_name(self):
        for record in self:
            record.rec_name = (
                f"{record.name} {record.surname} ({record.patient_sequence})"
            )

    rec_name = fields.Char(string="Full Name", compute="_compute_rec_name", store=True)
    patient_sequence = fields.Char(
        string="Patient Sequence",
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: _("New"),
        help="Unique identifier for the patient record",
    )
    name = fields.Char(string="Patient Name", required=True)
    surname = fields.Char(string="Surname", required=True)
    dni = fields.Char(string="DNI", required=True, tracking=True)
    medical_discharge_date = fields.Date(
        string="Medical Discharge Date", help="Date of Medical Discharge"
    )
    state = fields.Selection(
        selection=[
            ("draft", "Draft"),
            ("discharged", "Discharged"),
            ("leave", "Leave"),
        ],
        string="State",
        default="draft",
        tracking=True,
        help="State of the patient record",
    )
    treatment_line_ids = fields.One2many(
        comodel_name="treatment.lines",
        inverse_name="patient_id",
        string="Treatment Lines",
    )

    @api.model
    def _get_user_lang(self):
        self = self.with_context(lang=self.env.user.lang or "en_US")
        return self.env.context.get("lang")
