from django.db import models
from django.forms.models import model_to_dict

# Create your models here.

class Staff(models.Model):
    name = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    email = models.CharField(max_length=250)

    @property
    def positions(self):
        position_history = StaffToPosition.objects.filter(staff=self)
        json_response = [x.to_json() for x in position_history]
        return json_response

    def to_json(self):
        res = model_to_dict(self)
        res['positions'] = self.positions
        return res

    def to_short_json(self):
        res = model_to_dict(self, exclude=[self.phone_number, self.email])
        return res

    def __str__(self):
        return "{} {}".format(self.name, self.lastname)



class Position(models.Model):
    name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)

    def to_json(self):
        res = model_to_dict(self)
        return res

    def __str__(self):
        return self.name

class StaffToPosition(models.Model):
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField(null=True)

    def to_json(self):
        res = model_to_dict(self)
        return res

    def __str__(self):
        return "{} - {} {}".format(self.position.name, self.staff.name, self.staff.lastname)