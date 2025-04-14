
from abc import ABC, abstractmethod
class Notification(ABC):
    """
    Abstract base class for notifications.
    """

    @abstractmethod
    def send(self, message: str) -> None:
        """
        Send a notification with the given message.

        :param message: The message to send.
        """
        pass
class EmailNotification(Notification):
    def send(self, message: str) -> None:
        """
        Send an email notification with the given message.

        :param message: The message to send.
        
        
        """
        print(f"hi this is muneer")
        print(f"Sending email notification: {message}")

class SMSNotification(Notification):
    def send(self, message: str) -> None:
        """
        Send an SMS notification with the given message.

        :param message: The message to send.
        """
        print(f"Sending SMS notification: {message}")

class PushNotification(Notification):
    def send(self, message: str) -> None:
        """
        Send a push notification with the given message.

        :param message: The message to send.
        """
        print(f"Sending push notification: {message}")

class NotificationFactory:
    """
    Factory class to create notification instances.
    """

    @staticmethod
    def create_notification(notification_type: str) -> Notification:
        """
        Create a notification instance based on the type.

        :param notification_type: The type of notification ('email', 'sms', 'push').
        :return: An instance of the specified notification type.
        """
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        elif notification_type == "push":
            return PushNotification()
        else:
            raise ValueError(f"Unknown notification type: {notification_type}")
        
# Example usage:    
if __name__ == "__main__":
    notification_type = "push"  # Change this to "sms" or "push" for different notifications
    message = "This is a test notification."

    notification = NotificationFactory.create_notification(notification_type)
    notification.send(message)
    # Output: Sending email notification: This is a test notification.
# Output: Sending SMS notification: This is a test notification.