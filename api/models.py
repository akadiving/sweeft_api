from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Category(models.Model):
    """
    Model for categories
    """
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "categories"

    
class Activity(models.Model):
    """
    Model for activities
    """
    activity = models.CharField(max_length=255, null=True, blank=True)
    type = models.ForeignKey(Category,related_name="activity", on_delete=models.DO_NOTHING, null=True)
    price = models.FloatField(null=True, blank=True)

    def __str__(self) -> str:
        return self.activity

    class Meta:
        verbose_name_plural = "activities"
        ordering = ('price',)

@receiver(post_save, sender=Activity)
def create_category(sender, instance, **kwargs):
    if Category.objects.filter(name=instance.type.name):
        return
    new_category = Category.objects.create(name=instance.type.name)
    new_category.save()