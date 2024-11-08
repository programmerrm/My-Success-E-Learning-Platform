from django.core.mail.backends.smtp import EmailBackend

class CustomEmailBackend(EmailBackend):
    def _send(self, email_message):
        if not email_message.recipients():
            return False
        try:
            self.connection.sendmail(
                email_message.from_email,
                email_message.recipients(),
                email_message.message().as_bytes(linesep='\r\n'),
            )
        except:
            if not self.fail_silently:
                raise
            return False
        return True

    def open(self):
        if self.connection:
            return False
        try:
            self.connection = self.connection_class(self.host, self.port)
            self.connection.ehlo()
            if self.use_tls:
                self.connection.starttls()
                self.connection.ehlo()
            if self.username and self.password:
                self.connection.login(self.username, self.password)
        except:
            if not self.fail_silently:
                raise
            return False
        return True
