// Copyright (c) 2023, sivamanikanta and contributors
// For license information, please see license.txt


// frappe.ui.form.on("Gym Workout Plan", {
//     plan_name: function(frm) {
//         var planName = frm.doc.plan_name;
        
//         // Update the workout_plan field in each child row of the Gym Workout Plan Exercise table
//         frm.doc.exercise.forEach(function(row) {
//             frappe.model.set_value(row.doctype, row.name, "workout_plan", planName);
//         });
        
//         // Refresh the table to reflect the changes
//         frm.refresh_field("exercise");
//     },
	
//     exercise_add: function(frm, cdt, cdn) {
//         var child = locals[cdt][cdn];
//         var planName = frm.doc.plan_name;
        
//         // Set the workout_plan field in the newly added child row
//         frappe.model.set_value(child.doctype, child.name, "workout_plan", planName);
//     }
// });

frappe.ui.form.on("Gym Workout Plan", {
    plan_name: function(frm) {
        var planName = frm.doc.plan_name;
        
        // Update the workout_plan field in all rows of the exercise table
        frm.doc.exercise.forEach(function(row) {
            frappe.model.set_value(row.doctype, row.name, "workout_plan", planName);
        });
    },
	exercise_add: function(frm) {
        var planName = frm.doc.plan_name;
        
        // Update the workout_plan field in all rows of the exercise table
        frm.doc.exercise.forEach(function(row) {
            frappe.model.set_value(row.doctype, row.name, "workout_plan", planName);
        });
    }
});



