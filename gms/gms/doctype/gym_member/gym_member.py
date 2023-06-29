# Copyright (c) 2023, sivamanikanta and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
# from frappe.utils import random_string

class GymMember(Document):
	pass



# @frappe.whitelist()
# def create_user_from_gym_member(doc, method):
#     # Retrieve the required data from the Gym Member document
#     first_name = doc.first_name
#     last_name = doc.last_name
#     email_address = doc.email_address
#     role = doc.role

#     # Create a new user in the User doctype
#     new_user = frappe.new_doc("User")
#     new_user.update({
#         "first_name": first_name,
#         "last_name": last_name,
#         "email": email_address,
#         "roles": [{
#             "role": role
#         }],
#         # Set other required fields for the user

#     })

#     # Save the new user record
#     new_user.insert(ignore_permissions=True)
    



@frappe.whitelist()
def create_user_from_gym_member(doc, method):
    # Retrieve the required data from the Gym Member document
    first_name = doc.first_name
    last_name = doc.last_name
    email_address = doc.email_address
    role = doc.role

    # Create a new user in the User doctype
    new_user = frappe.new_doc("User")
    new_user.update({
        "first_name": first_name,
        "last_name": last_name,
        "email": email_address,
        "roles": [{
            "role": role
        }],
        "send_welcome_email": True,  # Send welcome email to the user
    })

    # Save the new user record
    new_user.insert(ignore_permissions=True)
