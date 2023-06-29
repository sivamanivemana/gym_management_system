import frappe

def execute():

    subscriptions = frappe.get_all(
        "Gym Subscription",
        filters={"status": "Active"},
        fields=["name", "cupon"]
    )

    for subscription in subscriptions:
        if subscription.status == "Active":
            frappe.db.set_value(
                "Gym Subscription",
                subscription.name,
                "cupon",
                "FLAT-10",
                update_modified=False
            )

    expired_subscriptions = frappe.get_all(
        "Gym Subscription",
        filters={"status": "Expired"},
        fields=["name", "cupon"]
    )

    for subscription in expired_subscriptions:
        if subscription.status == "Expired":
            frappe.db.set_value(
                "Gym Subscription",
                subscription.name,
                "cupon",
                "FLAT-20",
                update_modified=False
            )