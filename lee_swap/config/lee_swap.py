from __future__ import unicode_literals
from frappe import _


def get_data():
    return [
        {
            "label": _("Swap"),
            "items": [
                {
                    "type": "doctype",
                    "name": "Swap Settings",
                }
            ]
        }
    ]
