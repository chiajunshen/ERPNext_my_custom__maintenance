# -*- coding: utf-8 -*-
# Copyright (c) 2021, cjs and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class MachineStatus(Document):

	# return True if API exist in database, otherwise return False.
	@frappe.whitelist()
	def check_if_API_exist(self):
		if frappe.db.exists("Server Script", "Mac Stat From NR To ERPNext"):
			return "API exists"
		else:
			return "API not found"

	# disable the API once user decide to NOT sync with Node-RED
	@frappe.whitelist()
	def disable_API(self):
		ssapi = frappe.get_doc('Server Script', "Mac Stat From NR To ERPNext")
		# ssapi.reload()
		ssapi.db_set('disabled', 1, commit=True)
		ssapi.save(ignore_version=True)
		ssapi.reload()

	# @frappe.whitelist()
	# def update_sync_with_nr_flag(self, ms_id, new_value):
	# 	# ms = frappe.get_doc('Machine Status', ms_id)
	# 	# ms.reload()
	# 	# ms.sync_with_nr = new_value
	# 	# ms.db_set('sync_with_nr', new_value)
	# 	# ms.save()
	# 	# ms.reload()