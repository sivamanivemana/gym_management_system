# from frappe import _
# from frappe.website.router import get_page_route
import frappe

# def get_context(context):
#     context.user=frappe.get_user().load_user()

#     context.gym=frappe.db.get_value("Gym Member",filters={'first_name':context.user.first_name},fieldname=['first_name']),

#     context.sub=frappe.get_list("Gym Subscription",
#                                     filters={'status':'Active','gym_member':context.gym},
#                                     fields=['gym_member','status','date_of_subscription','trainer','end_of_subscription','remaining_days','amount','trainer_contact'])


def get_context(context):
    context.user = frappe.get_user().load_user()

    context.gym_member = frappe.db.get_value("Gym Member", filters={'email_address': context.user.email}, fieldname='name')

    context.gym_subscription = frappe.get_list("Gym Subscription",
                                filters={'status':'Active','gym_member': context.gym_member},
                                fields=['gym_member', 'status', 'date_of_subscription', 'trainer', 'end_of_subscription', 'remaining_days', 'amount', 'trainer_contact'])

    context.gym_expired = frappe.get_list("Gym Subscription",
                                filters={'status':'Expired','gym_member': context.gym_member},
                                fields=['status', 'date_of_subscription', 'trainer', 'end_of_subscription','amount', 'trainer_contact'])
