from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_no = models.IntegerField()
    email = models.EmailField(max_length=250)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

    def register(self):
        self.save()

    # @staticmethod
    # def get_customer_by_email(email):
    #     return Customer.objects.filter(email = email)


    # def isExists(self, email):
    #     if Customer.objects.filter(email = self.email):
    #         return True
    #     else:
    #         return False
    