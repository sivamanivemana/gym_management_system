# Copyright (c) 2023, sivamanikanta and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestCardioMachine(FrappeTestCase):
	def test_availability(self):
		machine=frappe.get_doc(doctype="Cardio Machine",machine_name="hihjacki",machine_type="Treadmill")

		machine.availability=1
		machine.save()

		self.assertEqual(machine.status, "Working")


		machine.availability=0
		machine.save()

		self.assertEqual(machine.status, "Not_Working")


