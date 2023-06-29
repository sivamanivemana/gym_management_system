# Copyright (c) 2023, sivamanikanta and contributors
# For license information, please see license.txt

import frappe
import json
from datetime import datetime,timedelta
from frappe.model.document import Document
import frappe.utils

class GymSubscription(Document):
     pass


# def calculate_remaining_days(doc, method):
#     if doc.date_of_subscription and doc.end_of_subscription:
#         remaining_days = (doc.end_of_subscription - frappe.utils.nowdate()).days
#         doc.remaining_days = remaining_days

@frappe.whitelist()    
def end_of_subscription_date(self):
	self=json.loads(self)
	value=self["duration"]/86400
	print(value)
	start_date=datetime.strptime(self["date_of_subscription"], "%Y-%m-%d")
	end_date=start_date+timedelta(days=int(value))
	return end_date
    