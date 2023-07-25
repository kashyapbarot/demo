# -*- encoding: utf-8 -*-
##############################################################################
#
# Bista Solutions Pvt. Ltd
# Copyright (C) 2022 (http://www.bistasolutions.com)
#
##############################################################################
{
    "name": "Service Agreement Report",
    "sequence": 0,
    "version": "16.0.1.0",
    "author": "Bista Solutions Pvt. Ltd.",
    "category": "sale",
    "summary": "",
    "description": """Service Agreement Report""",
    "depends": [
        "bista_contact_customization",
    ],
    "website": "https://www.bistasolutions.com",
    "data": [
        'reports/service_agreement_report.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            '/service_agreement_report/static/src/scss/service_agreement_report.scss',
        ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
    "license": "LGPL-3",
}
