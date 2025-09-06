# -*- coding: utf-8 -*-
{
    "name": "Vertical Hospital",
    "summary": "Patients and treatments management",
    "description": """
    Module for managing patients and treatments in a hospital setting.
    """,
    "author": "Kleiver Perez",
    "maintainer": "Kleiver Perez <kleiver.perez.dev@gmail.com>",
    "category": "Tools",
    "version": "18.0.1.0.1",
    "depends": ["base", "web", "mail"],
    "data": [
        "security/ir.model.access.csv",
        "data/res_patient_sequence.xml",
        "report/ir_actions_report_templates.xml",
        "report/ir_actions_report.xml",
        "views/res_patient_views.xml",
        "views/treatment_views.xml",
        "views/vertical_hospital_configuration.xml",
        "views/menu_views.xml",
    ],
    "license": "LGPL-3",
    "installable": True,
    "application": True,
    "auto_install": False,
}
