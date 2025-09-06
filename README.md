# Vertical Module (Hospital) for Odoo

This Odoo module implements an application for the hospital vertical with key features for patient management, treatments, auditing, reporting, and a web-based consultation service.

## Description

The **vertical_hospital** module creates an Odoo application with the following features:

- Patient management with a registration, deregistration, and modification form.
- Auditable record of changes to ID and patient status.
- Management of treatments associated with patients with specific restrictions.
- PDF reports with a list of selected patients.
- Public REST server for patient consultation by sequence.
- Configuration to adjust the web-based service endpoint.
- Compatible with Enterprise and Community versions of Odoo.

## Features

### Patients

- Form with fields: sequence (PA000001, automatic and read-only), first and last name, ID (numbers only), treatments (selected), date and time of discharge and update, status (Draft, Discharge, Discharge) editable with a click.
- List view with sequence, name, ID, and status.
- Automatic auditing in chatter of changes to ID and status.

### Treatments

- Form with code, name, and attending physician, with a restriction that the code does not contain the sequence "026".
- List view with code, name, and attending physician.

### Web Service

- Public GET endpoint: `/patients/consultation/<sequence>`
- Returns JSON with basic patient data (seq, name, ID, state).

### QWeb Reports

- PDF report from the patient list view for multiple selections.
- Header and footer with company logo.
- Displays the same data as the list view.

### Configuration

- "Hospital" option in Settings with logo.
- Allows you to configure the web service endpoint.

## Installation

1. Download or clone the repository to the Odoo addons directory.
2. Update the list of applications in Odoo.
3. Search for and install the `vertical_hospital` module.
4. Configure the web service endpoint in Settings > Hospital.

## Use

- Access the application from the Odoo main dashboard.
- Generate and manage patients and treatments from their respective menus.
- Consult patients via the web service using the generated sequence.
- Print PDF reports from the patient list view.
- Audit important changes in the patient form chatter.

## Requirements

- Odoo version compatible with community and enterprise modules.
- Standard dependencies for Odoo module development.
- Public or customized access based on REST service configuration.

## Code and Developer

- The code is structured following Odoo development standards.
- Contains comments and inline documentation to facilitate maintenance or improvements.

## Contact

For questions or contributions, please contact the development team.
