# -*- coding: utf-8 -*-
from odoo import models, fields, api


class ResConfigSettingsInherit(models.TransientModel):
    _inherit = "res.config.settings"

    vertical_hospital_endpoint_url = fields.Char(string="Endpoint URL")

    @api.model
    def get_values(self):
        res = super(ResConfigSettingsInherit, self).get_values()
        vertical_hospital_endpoint_url = (
            self.env["ir.config_parameter"]
            .sudo()
            .get_param("vertical_hospital_endpoint_url", default=False)
        )
        res.update(vertical_hospital_endpoint_url=vertical_hospital_endpoint_url)
        return res

    def set_values(self):
        """Set the customer credit limit value in the database parameters using superuser access."""
        super(ResConfigSettingsInherit, self).set_values()
        self.env["ir.config_parameter"].sudo().set_param(
            "vertical_hospital_endpoint_url", self.vertical_hospital_endpoint_url
        )

    def return_endpoint_url(self):
        return self.env["ir.config_parameter"].sudo().get_param(
            "vertical_hospital_endpoint_url", default="pacientes/consulta/"
        )
