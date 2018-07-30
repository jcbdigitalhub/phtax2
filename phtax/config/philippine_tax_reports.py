from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Company Registration"),
			"items": [
				{
					"type": "doctype",
					"name": "Tax Registration",
					"description": _("Setup Company details based on Certificate of Registration.")
				}
			]

		},
		{
			"label": _("Tax Reports"),
			"items": [
				{
					"type": "report",
					"name": "Value Added Tax",
					"description": _("Value Added Tax Report"),
					"is_query_report": True,
				},
				{
					"type": "report",
					"name": "Withholding Tax Report",
					"description": _("Withholding Tax Report"),
                                        "is_query_report": True,
				},
				{
					"type": "report",
					"name":"General Ledger",
					"doctype": "GL Entry",
					"is_query_report": True,
				},
			]
		},
		{
			"label": _("Masters"),
			"items": [
				{
					"type": "doctype",
					"name": "Customer",
					"description": _("Customer database.")
				},
				{
					"type": "doctype",
					"name": "Supplier",
					"description": _("Supplier database.")
				},
				{
					"type": "doctype",
					"name": "Item",
				}
			]
		},
		{
			"label": _("Tax Setup and Reports"),
			"items": [
				{
					"type": "doctype",
					"name": "Sales Taxes and Charges Template",
					"description": _("Tax template for selling transactions.")
				},
				{
					"type": "doctype",
					"name": "Purchase Taxes and Charges Template",
					"description": _("Tax template for buying transactions.")
				},
				{
					"type": "doctype",
					"name": "Tax Rule",
					"description": _("Tax Rule for transactions.")
				},
				{
					"type": "report",
					"name": "Sales Register",
					"doctype": "Sales Invoice",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "Purchase Register",
					"doctype": "Purchase Invoice",
					"is_query_report": True
				},
			]
		},
		{
			"label": _("Goods and Services Tax (GST India)"),
			"items": [
				{
					"type": "doctype",
					"name": "GST Settings",
				},
				{
					"type": "doctype",
					"name": "GST HSN Code",
				},
				{
					"type": "report",
					"name": "GST Sales Register",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "GST Purchase Register",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "GST Itemised Sales Register",
					"is_query_report": True
				},
				{
					"type": "report",
					"name": "GST Itemised Purchase Register",
					"is_query_report": True
				},
			]
		}
	]
