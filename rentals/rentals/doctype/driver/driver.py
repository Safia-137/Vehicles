from frappe.model.document import document
class Driver(Document):
    def before_save(self):
        self.full_name = f"{self.first_name} {self.last_name}"
    
    def send_alert(self):
        print("Sending Message")
