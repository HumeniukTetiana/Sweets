from django.core.exceptions import ObjectDoesNotExist

class Repository:
    def __init__(self, model):
        self.model = model

    def get_all(self):
        return self.model.objects.all()

    def get_by_id(self, instance_id):
        try:
            return self.model.objects.get(id=instance_id)
        except ObjectDoesNotExist:
            return None

    def create(self, **kwargs): 
        instance = self.model(**kwargs)
        instance.save()
        return instance

    def update(self, instance_id, **kwargs):
        instance = self.get_by_id(instance_id)
        if instance:
            for attr, value in kwargs.items():
                setattr(instance, attr, value)
            instance.save()
            return instance
        return None

    def delete(self, instance_id):
        instance = self.get_by_id(instance_id)
        if instance:
            instance.delete()
            return True
        return False
