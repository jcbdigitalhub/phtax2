# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "phtax"
app_title = "Philippine Tax Reports"
app_publisher = "Opensource Solutions Philippines"
app_description = "Philippine Tax Reports"
app_icon = "fa fa-rub"
app_color = "grey"
app_email = "info@ossph.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/phtax/css/phtax.css"
# app_include_js = "/assets/phtax/js/phtax.js"

# include js, css files in header of web template
# web_include_css = "/assets/phtax/css/phtax.css"
# web_include_js = "/assets/phtax/js/phtax.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "phtax.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "phtax.install.before_install"
# after_install = "phtax.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "phtax.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"phtax.tasks.all"
# 	],
# 	"daily": [
# 		"phtax.tasks.daily"
# 	],
# 	"hourly": [
# 		"phtax.tasks.hourly"
# 	],
# 	"weekly": [
# 		"phtax.tasks.weekly"
# 	]
# 	"monthly": [
# 		"phtax.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "phtax.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "phtax.event.get_events"
# }

