from peewee import *
from .base_model import BaseModel


class RentalModel(BaseModel):
    id = IdentityField()
    rental_uid = UUIDField(unique=True, null=False)
    username = CharField(max_length=80, null=False)
    payment_uid = UUIDField(null=False)
    car_uid = UUIDField(null=False)
    date_from = DateField(null=False, formats='%Y-%m-%d')
    date_to = DateField(null=False, formats='%Y-%m-%d')
    status = CharField(max_length=20, constraints=[Check("status IN ('IN_PROGRESS', 'FINISHED', 'CANCELED')")])

    def to_dict(self):
        return {
            "rental_uid": str(self.rental_uid),
            "username": str(self.username),
            "payment_uid": str(self.payment_uid),
            "car_uid": str(self.car_uid),
            "date_from": str(self.date_from),
            "date_to": str(self.date_to),
            "status": str(self.status)
        }

    class Meta:
        db_table = "rental"
