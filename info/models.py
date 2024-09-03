from django.db import models

# Create your models here.
class Info(models.Model):
    CATEGORY_CHOICES = [
        ('free_mint', 'Free Mint'),
        ('pfp', 'PFP'),
        ('collectible', 'Collectible'),
        ('charity', 'Charity'),
        ('3d', '3D'),
        ('art', 'Art'),
        ('pixel', 'Pixel'),
        ('metaverse', 'Metaverse'),
        ('membership', 'Membership'),
        ('music', 'Music'),
        ('gaming', 'Gaming'),
        ('alpha', 'Alpha'),
        ('utility', 'Utility'),
        ('memecoin', 'Memecoin'),
        ('defi', 'Defi'),
        ('dex', 'Dex'),
        ('dao', 'Dao'),
        ('generative', 'Generative'),
        ('giveaway', 'Giveaway'),
        ('sports', 'Sports'),
        ('other', 'Other'),
    ]
    info_id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    desc = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=100, null=True, blank=True)
    marketplace = models.CharField(max_length=100, null=True, blank=True)
    # front_image
    front_image = models.ImageField(upload_to ='uploads/% Y/% m/% d/',null=True, blank=True)
    # background_image
    background_image= models.ImageField(upload_to ='uploads/% Y/% m/% d/',null=True, blank=True)
    blockchain = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=False, default='other')
    supply = models.IntegerField(null=True, blank=True)
    private_mint_price = models.IntegerField(null=True, blank=True)
    public_mint_price = models.IntegerField(null=True, blank=True)
    private_mint_time = models.CharField(max_length=20, null=True, blank=True)
    public_mint_time = models.CharField(max_length=20, null=True, blank=True)
    public_mint_date = models.CharField(max_length=20, null=True, blank=True)
    private_mint_date = models.CharField(max_length=20, null=True, blank=True)
    click_count = models.PositiveBigIntegerField(default=0)
    paid_status = models.BooleanField(default=False)
    verified = models.BooleanField(null=True, blank=True, default=True)
    flagged = models.BooleanField(null=True, blank=True, default=False)
    reported = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return self.title

class VoterIp(models.Model):
    nft = models.ForeignKey(Info,on_delete=models.CASCADE,related_name='votes',null=True)
    ip = models.CharField(max_length=100)

    def __str__(self):
        return self.ip