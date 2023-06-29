# Copyright (c) 2023, sivamanikanta and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


# class TestGymSubscription(FrappeTestCase):
# 	def test_cupon_according_to_plan(self):
# 		doc=frappe.get_doc(doctype="Gym Subscription",gym_member="GM-satya-001",active_plan="GM-Standardplan-01",trainer="GT-Meenakshi-Sports-Specific Training-01")

# 		doc.date_of_subscription = "28-06-2023"
# 		doc.duration = 60
# 		doc.save()

# 		self.assertEqual(doc.end_of_subscription, "27-08-2023")


class TestGymSubscription(FrappeTestCase):
    def test_end_of_subscription(self):
        doc = frappe.get_doc(doctype="Gym Subscription", gym_member="GM-satya-001", active_plan="GM-Standardplan-01",
                             trainer="GT-Meenakshi-Sports-Specific Training-01")

        doc.date_of_subscription = "2023-06-28"
        doc.duration = 60
        doc.save()

        end_of_subscription = frappe.get_value("Gym Subscription", doc.name, "end_of_subscription")
        expected_end_date = frappe.utils.get_datetime("2023-08-27")
        self.assertEqual(end_of_subscription,expected_end_date)
        

        doc.date_of_subscription = "2023-06-29"
        doc.duration = 60
        doc.save()

        
        end_of_subscription = frappe.get_value("Gym Subscription", doc.name, "end_of_subscription")
        expected_end_date = frappe.utils.get_datetime("2023-08-28")
        self.assertEqual(end_of_subscription,expected_end_date)
        
		


