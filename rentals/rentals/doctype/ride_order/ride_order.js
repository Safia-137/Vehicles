// Copyright (c) 2024, Safia and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
	onload(frm){
		console.log("EUnning Load");
	},
	setup(frm){
		console.log("On Setup");
	},
	refresh(frm) {
		console.log("On Refresh");
		if (frm.doc.status === "New"){
			frm.add_custom_button("Accept", () => {
				frm.set_value("status","Accepted");
				frm.save();
			},"Actions")

			frm.add_custom_button("Reject", () => {
				frm.set_value("status","Rejected");
				frm.save();
			},"Actions")
		}
 	},
 });
