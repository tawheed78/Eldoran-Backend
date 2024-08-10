from django.db import models

# Create your models here.
class Info(models.Model):
    info_id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    desc = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)
    marketplace = models.CharField(max_length=100, null=True, blank=True)
    # front_image
    # background_image
    blockchain = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    supply = models.IntegerField(null=True, blank=True)
    private_mint_price = models.IntegerField(null=True, blank=True)
    public_mint_price = models.IntegerField(null=True, blank=True)
    private_mint_time = models.CharField(max_length=20, null=True, blank=True)
    public_mint_time = models.CharField(max_length=20, null=True, blank=True)
    public_mint_date = models.CharField(max_length=20, null=True, blank=True)
    private_mint_date = models.CharField(max_length=20, null=True, blank=True)
    verified = models.BooleanField(null=True, blank=True, default=True)
    flagged = models.BooleanField(null=True, blank=True, default=False)
    reported = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return self.title
    