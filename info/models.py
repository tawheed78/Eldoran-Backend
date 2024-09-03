import datetime
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
    BLOCKCHAIN_CHOICES = [
    ('bitcoin', 'Bitcoin'),
    ('ethereum', 'Ethereum'),
    ('solana', 'Solana'),
    ('polygon', 'Polygon'),
    ('avalanche', 'Avalanche'),
    ('aptos', 'Aptos'),
    ('cardano', 'Cardano'),
    ('near', 'Near'),
    ('sui', 'Sui'),
    ('algorand', 'Algorand'),
    ('multiversx', 'MultiversX'),
    ('arbitrum', 'Arbitrum'),
    ('sei', 'Sei'),
    ('binance', 'Binance'),
    ('cosmos', 'Cosmos'),
    ('hedera', 'Hedera'),
    ('venom', 'Venom'),
    ('icon', 'Icon'),
    ('immutable', 'Immutable'),
    ('injective', 'Injective'),
    ('ripple', 'Ripple'),
    ('dogecoin', 'Dogecoin'),
    ('base', 'Base'),
    ('wax', 'Wax'),
    ('flow', 'Flow'),
    ('reef', 'Reef'),
    ('internet_computer', 'Internet Computer'),
    ('starknet', 'StarkNet'),
    ('myria', 'Myria'),
    ('monad', 'Monad'),
    ('berachain', 'Berachain'),
    ('stargaze', 'Stargaze'),
    ('blast', 'Blast'),
    ('osmosis', 'Osmosis'),
    ('zksync', 'ZKSync'),
    ('enjin', 'Enjin'),
    ('linea', 'Linea'),
    ('skale_network', 'Skale Network'),
    ('ton', 'Ton'),
    ('oraichain', 'Oraichain'),
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
    blockchain = models.CharField(max_length=100, choices=BLOCKCHAIN_CHOICES, null=False, blank=False, default='Bitcoin')
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=False, default='other')
    supply = models.IntegerField(null=True, blank=True)
    private_mint_price = models.IntegerField(null=True, blank=True)
    public_mint_price = models.IntegerField(null=True, blank=True)
    private_mint_time = models.TimeField(default=datetime.datetime.now)
    public_mint_time = models.TimeField(default=datetime.datetime.now)
    public_mint_date = models.DateField(default=datetime.datetime.now)
    private_mint_date = models.DateField(default=datetime.datetime.now)
    click_count = models.PositiveBigIntegerField(default=0, editable=False)
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