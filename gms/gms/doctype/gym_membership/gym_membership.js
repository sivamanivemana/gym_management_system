// Copyright (c) 2023, sivamanikanta and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Membership", {
    membership_plan_name: function(frm) {
        // Fetch the selected membership plan name document
        frappe.call({
            method: "frappe.client.get",
            args: {
                doctype: "Membership Plan Name",
                name: frm.doc.membership_plan_name
            },
            callback: function(response) {
                var membership_plan_name = response.message;
                if (membership_plan_name) {
                    // Set the fetched benefits in the field
                    frm.set_value("benifits", membership_plan_name.benifits);
					frm.set_value("cost",membership_plan_name.cost);
					frm.set_value("duration",membership_plan_name.duration);
                } else {
                    frm.set_value("benifits", "");
                    frm.set_value("duration", "");
                    frm.set_value("cost", "");
                }
            }
        });
    }
});
