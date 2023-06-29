// Copyright (c) 2023, sivamanikanta and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Subscription", {
	date_of_subscription:function(frm){
	frappe.call({
		method:"gms.gms.doctype.gym_subscription.gym_subscription.end_of_subscription_date",
        args:{
            self:frm.doc
        },
        async:false,
        callback: function(r){
			frm.doc.end_of_subscription=r.message
			frm.refresh_field("end_of_subscription")

        }
    });
	
	}
});
  