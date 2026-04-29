# ============================================================
# PILLAR: Abstraction
# PROGRAM 9: Notification System
# ============================================================
#
# PROBLEM:
# Create an abstract Notification class with:
# - abstract method send(recipient, message): sends a notification
# - abstract method channel_name(): returns name of the channel
# - non-abstract method notify(recipient, message): logs the
#   notification attempt and then calls send()
#
# Implement two concrete classes:
# - EmailNotification: channel = "Email"
#   send() prints "Email sent to {recipient}: {message}"
# - SMSNotification: channel = "SMS"
#   send() prints "SMS sent to {recipient}: {message}"
#
# EXAMPLE USAGE:
#   notifications = [
#       EmailNotification(),
#       SMSNotification()
#   ]
#   for n in notifications:
#       n.notify("Alice", "Your order is shipped!")
#
# OUTPUT:
#   [Email] Notifying Alice...
#   Email sent to Alice: Your order is shipped!
#   [SMS] Notifying Alice...
#   SMS sent to Alice: Your order is shipped!
# ============================================================


from abc import ABC, abstractmethod

# Abstract base class
class Notification(ABC):

    @abstractmethod
    def send(self, recipient, message):
        pass

    @abstractmethod
    def channel_name(self):
        pass

    # Concrete method
    def notify(self, recipient, message):
        print(f"[{self.channel_name()}] Notifying {recipient}...")
        self.send(recipient, message)


# Concrete class: Email
class EmailNotification(Notification):

    def send(self, recipient, message):
        print(f"Email sent to {recipient}: {message}")

    def channel_name(self):
        return "Email"


# Concrete class: SMS
class SMSNotification(Notification):

    def send(self, recipient, message):
        print(f"SMS sent to {recipient}: {message}")

    def channel_name(self):
        return "SMS"


# Example usage
if __name__ == "__main__":
    notifications = [
        EmailNotification(),
        SMSNotification()
    ]

    for n in notifications:
        n.notify("Alice", "Your order is shipped!")