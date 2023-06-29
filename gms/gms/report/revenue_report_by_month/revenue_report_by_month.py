# Copyright (c) 2023, sivamanikanta and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns, data = [
		{
			"label":"GymPlan",
			"fieldname":"gym_plan",
			"fieldtype":"Data",
			"width":240,
		},
		{
			"label":"Revenue",
			"fieldname":"revenue",
			"fieldtype":"float",
			"width":240,	
		}
	], []

	records = frappe.get_all("Gym Subscription",fields=["amount","active_plan"],filters={"docstatus": 1})

	revenue_by_active_plan={}

	for record in records:
		if record.active_plan in revenue_by_active_plan:
			revenue_by_active_plan[record.active_plan] = revenue_by_active_plan[record.active_plan] + record.amount
		else:
			revenue_by_active_plan[record.active_plan] = record.amount
	
	for gym_plan,revenue in revenue_by_active_plan.items():
		data.append({"gym_plan": gym_plan,"revenue":revenue})


	return columns, data
