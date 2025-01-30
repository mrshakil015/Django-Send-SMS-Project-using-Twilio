from django.db import models
from twilio.rest import Client

# Twilio Credentials (Replace with your actual credentials)
TWILIO_ACCOUNT_SID = "account_sid"
TWILIO_AUTH_TOKEN = "auth_token"
TWILIO_PHONE_NUMBER = "+18455769762"  

class Message(models.Model):
    name = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=15, null=True, help_text="Enter phone number with country code (e.g., +8801712345678)")
    score = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.name

    def send_sms(self, phone_number, message):
        """Function to send SMS using Twilio"""
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        try:
            sms = client.messages.create(
                body=message,
                from_=TWILIO_PHONE_NUMBER,
                to=phone_number
            )
            print(f"SMS sent successfully: {sms.sid}")
        except Exception as e:
            print(f"Failed to send SMS: {e}")

    def save(self, *args, **kwargs):
        """Override save method to send SMS if score >= 70"""
        if self.score >= 70 and self.phone_number:
            message = f"Hello {self.name}, congratulations! You scored {self.score}."
            self.send_sms(self.phone_number, message)
        

        super().save(*args, **kwargs)  # Save data to the database
