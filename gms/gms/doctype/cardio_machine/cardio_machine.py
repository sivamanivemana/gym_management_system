# Copyright (c) 2023, sivamanikanta and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class CardioMachine(Document):
	def validate(self):
		if self.availability:
			self.status= "Working"
		else:
			self.status= "Not_Working"
