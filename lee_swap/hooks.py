# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "lee_swap"
app_title = "Lee Swap"
app_publisher = "Swello Lee"
app_description = "Instance Swapper"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "swellolee@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/lee_swap/css/lee_swap.css"
# app_include_js = "/assets/lee_swap/js/lee_swap.js"

# include js, css files in header of web template
# web_include_css = "/assets/lee_swap/css/lee_swap.css"
# web_include_js = "/assets/lee_swap/js/lee_swap.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "lee_swap.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "lee_swap.install.before_install"
# after_install = "lee_swap.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "lee_swap.notifications.get_notification_config"

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

doc_events = {
	"Swap Settings": {
		"on_update": "lee_swap.custom_hooks.swap.on_update_swap"
	}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"lee_swap.tasks.all"
# 	],
# 	"daily": [
# 		"lee_swap.tasks.daily"
# 	],
# 	"hourly": [
# 		"lee_swap.tasks.hourly"
# 	],
# 	"weekly": [
# 		"lee_swap.tasks.weekly"
# 	]
# 	"monthly": [
# 		"lee_swap.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "lee_swap.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "lee_swap.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "lee_swap.task.get_dashboard_data"
# }

