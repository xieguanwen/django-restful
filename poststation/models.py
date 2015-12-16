from django.db import models

class ShoujiPoststation(models.Model):
    class Meta:
        pass
    attr_id = models.SmallIntegerField(primary_key=True)
    cat_id = models.SmallIntegerField()
    attr_name = models.CharField(max_length=255)
    attr_input_type = models.IntegerField()
    attr_type = models.IntegerField()
    attr_values = models.TextField()
    attr_index = models.IntegerField()
    sort_order = models.IntegerField()
    is_linked = models.IntegerField()
    attr_group = models.IntegerField()
    province = models.CharField(max_length=60, blank=True, null=True)
    city = models.CharField(max_length=60, blank=True, null=True)
    tel = models.CharField(max_length=255, blank=True, null=True)
    addr = models.CharField(max_length=255, blank=True, null=True)
    longitude = models.CharField(max_length=32, blank=True, null=True)
    latitude = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shouji_poststation'
