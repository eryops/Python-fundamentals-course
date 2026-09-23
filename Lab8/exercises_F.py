class Notification:
    def send(self):
        return "Send"

class EmailNotification(Notification):
    def send(self):
        return "Send Email"
    
class SMSNotification(Notification):
     def send(self):
        return "Send SMS"

notification = Notification()
print(notification.send())
email_notification = EmailNotification()
print(email_notification.send())
sms_notification = SMSNotification()
print(sms_notification.send())