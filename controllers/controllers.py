# -*- coding: utf-8 -*-
from odoo import http
from json import dumps as j_dumps


class VerticalHospital(http.Controller):
    _allowed_routes = ["/pacientes/consulta/<patient_sequence>"]

    @http.route(route=_allowed_routes, methods=["GET"], auth="public")
    def patient_data(self, patient_sequence, **kw):
        patient_data = (
            http.request.env["res.patient"]
            .sudo()
            .search_read(
                [("patient_sequence", "=", patient_sequence)],
                ["patient_sequence", "name", "surname", "dni", "state"],
            )
        )

        if not patient_data:
            return http.request.make_response(
                j_dumps({"error": "Patient not found"}),
                headers=[("Content-Type", "application/json")],
                status=404,
            )

        return http.request.make_response(
            j_dumps(
                {
                    "seq": patient_data[0]["patient_sequence"],
                    "name": f"{patient_data[0]['name']} {patient_data[0]['surname']}",
                    "dni": patient_data[0]["dni"],
                    "state": patient_data[0]["state"],
                }
            ),
            headers=[("Content-Type", "application/json")],
        )
