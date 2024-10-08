# Copyright (c) 2024, Safia and contributors
# For license information, please see license.txt
import frappe


def execute(filters=None):

	columns = [{
		"fieldname": "make",
		"label" : "Make",
		"fieldtype" : "Data"
	},
	{
		"fieldname": "total_revenue",
		"label" : "Total Revenue",
		"fieldtype" : "Currency",
		"options" : "INR"
	},
	]
	data = frappe.get_all("Ride Booking", 
	fields =["SUM(total_amount) AS total_revenue", "vehicle.make"],
	filters={"docstatus":1}, group_by="make",)

	chart = {
		"data": {
			"labels" : [x.make for x in data],
			"datasets" : [{"values" : [x.total_revenue for x in data]}]
		},
		"type":"donut"
	}
	return columns, data, "Here is the report", chart
