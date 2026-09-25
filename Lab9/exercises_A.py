class EmailNotification:
    def send(self):
        return "Sending email notification..."

class SMSNotification:
    def send(self):
        return "Sending SMS notification..."

class PushNotification:
    def send(self):
        return "Sending push notification..."

email = EmailNotification()
sms = SMSNotification()
push = PushNotification()

notifications = [email, sms, push]

for n in notifications:
    print(n.send())
