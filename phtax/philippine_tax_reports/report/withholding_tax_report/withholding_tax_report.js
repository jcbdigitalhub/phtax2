frappe.query_reports["Withholding Tax Report"] = {
    "filters": [
        {
            "fieldname":"company",
            "label": __("Company"),
            "fieldtype": "Link",
            "options": "Company",
            "default": frappe.defaults.get_user_default("company")
        },
        {
            "fieldname":"date_from",
            "label": __("Date From"),
            "fieldtype": "Date",
	    "default": get_today()
        },
        {
            "fieldname":"date_to",
            "label": __("Date To"),
            "fieldtype": "Date",
	    "default": get_today()
        },
    ]
}
