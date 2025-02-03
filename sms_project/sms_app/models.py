from django.db import models
from twilio.rest import Client
from django.conf import settings

# Twilio Credentials (Replace with your actual credentials)


class ResultModel(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=15, null=True, help_text="Enter phone number with country code (e.g., +8801712345678)")
    score = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.name

    def send_sms(self, phone_number, message):
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)      
        try:
            client.messages.create(
                body=message,
                from_=settings.TWILIO_PHONE_NUMBER,
                to=phone_number
            )
        except Exception as e:
            print(f"Failed to send SMS: {e}")

    def save(self, *args, **kwargs):
        if self.score >= 70 and self.phone_number:
            message = f"Congratulations! You scored {self.score}."
            self.send_sms(self.phone_number, message)
        else:
            message = f"Sorry! You scored {self.score}."
            self.send_sms(self.phone_number, message)
        super().save(*args, **kwargs)
