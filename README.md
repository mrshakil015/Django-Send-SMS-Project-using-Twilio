# Django-Send-SMS-Project-using-Twilio

Twilio is a powerful cloud communication platform that allows sending SMS from Django applications. In this project, I implemented how can i send sms using Twilio. Simply here i implemented score send using message into the student phone number.
> If you used Twilio Trail version. Can only send SMS to verified numbers (must add and verify recipient numbers manually in Twilio).

> Also you can't sent long message. If you provide long message, you can't get the message.

### Context:
- [Project Setup](#project-setup)
- [Create Model](#create-model)
- [Create Send SMS Function](#create-send_sms-function)
- [Twilio Configuration](#twilio-configuration)


### Project Setup:
- At first create a environment file:
    ```python
    python -m venv env
    ```
- Active the env file:
    ```cmd
    .\env\Script\activate
    ```
- After that install the required packages:
    ```cmd
    pip install django
    pip install python-dotenv
    pip install twilio
    ```
- Now create a django project and django app:
    ```cmd
    django-admin startproject your_project_name
    ```
    ```cmd
    cd your_project_name
    ```
    ```cmd
    django-admin startapp your_app_name
    ```
- Configure the `settings.py` file to add `your_app_name` to the `INSTALLED_APPS`:
    ```python
    INSTALLED_APPS = [
    ......
    ......
    'myapp',
    ]
    ```
    ⬆️[Go to Context](#context)

### Create Model:
- Now create a model into the `models.py` file:
    ```python
    class ResultModel(models.Model):
        name = models.CharField(max_length=100, null=True)
        phone_number = models.CharField(max_length=15, null=True, help_text="Enter phone number with country code (e.g., +8801712345678)")
        score = models.IntegerField(default=0, null=True)
        def __str__(self):
            return f"{self.name}-{self.score}"
    ```
    > We can send sms from different way and different file. Here i implemented the sms sending method inside the `models.py` file. Because of I want when a student score entired that time check the score and sent the message. That's why i implemented it inside the models.py file. Also i doesn't used any view function. I tested it from the django admin.
- Now create a `sms_send()` function and custom `save()` function inside the model class. Structure like this:
    ```python
    class ResultModel():
        ..
        ..

        def send_sms():
            ..
            ..
        def save():
            ..
            ..
    ```
- At first import the `settings` and`Client` then create function
    ```python
    from django.conf import settings
    from twilio.rest import Client

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
    ```
    ⬆️[Go to Context](#context)

### Create Send_SMS function:
- Now create model custom save function. From this function call the `send_sms` function.
    ```python
    def save(self, *args, **kwargs):
        if self.score >= 70 and self.phone_number:
            message = f"Congratulations! You scored {self.score}."
            self.send_sms(self.phone_number, message)
        else:
            message = f"Sorry! You scored {self.score}."
            self.send_sms(self.phone_number, message)
        super().save(*args, **kwargs)
    ```
- Full Code like this:
    ```python
    from django.db import models
    from twilio.rest import Client
    from django.conf import settings

    # Twilio Credentials (Replace with your actual credentials)

    class ResultModel(models.Model):
        name = models.CharField(max_length=100, null=True)
        phone_number = models.CharField(max_length=15, null=True, help_text="Enter phone number with country code (e.g., +8801712345678)")
        score = models.IntegerField(default=0, null=True)

        def __str__(self):
            return f"{self.name}-{self.score}"

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
    ```
    
    ⬆️[Go to Context](#context)

### Twilio Configuration:
Now configure the sms sending method.
- Sign up for a free Twilio account: [Twilio Signup](https://www.twilio.com/)
- Navigate to the Twilio Console --> [Twilio Console](https://www.twilio.com/console)
- Copy the credentials:
    - `ACCOUNT SID`
    - `AUTH TOKEN`
    - `TWILIO PHONE NUMBER`
- Copy the credentials and create a `.env` file under the `project_folder` for security purpose. And ignore this `.env` file
    ```python
    # Twilio Credentials (Replace with your own)
    TWILIO_ACCOUNT_SID = "your_account_sid"
    TWILIO_AUTH_TOKEN = "your_auth_token"
    TWILIO_PHONE_NUMBER = "your_twilio_phone"
    ```
- Now configure this credentials into the `settings.py` file:
    ```python
    import os
    from dotenv import load_dotenv

    load_dotenv()
    #-----Twilio Configuration
    TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
    TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')
    ```
    > We can implemeted this configuration any where of any file. But this is the better practice.

