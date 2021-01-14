# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "nasser_app"
app_title = "Nasser App"
app_publisher = "Nasser"
app_description = "Nasser App"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@kcsc.moy"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/nasser_app/css/nasser_app.css"
# app_include_js = "/assets/nasser_app/js/nasser_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/nasser_app/css/nasser_app.css"
# web_include_js = "/assets/nasser_app/js/nasser_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "nasser_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "nasser_app.install.before_install"
# after_install = "nasser_app.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "nasser_app.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
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
# 		"nasser_app.tasks.all"
# 	],
# 	"daily": [
# 		"nasser_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"nasser_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"nasser_app.tasks.weekly"
# 	]
# 	"monthly": [
# 		"nasser_app.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "nasser_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "nasser_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "nasser_app.task.get_dashboard_data"
# }

fixtures = [
    {"dt": "Custom Field", "filters": [
        [
            "name", "in", [
		"Purchase Invoice-nasser"
		
            ]
        ]
    ]}
]


# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


