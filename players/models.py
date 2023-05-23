from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from django.db import models
from datetime import datetime


# Create your models here.
class Player(models.Model):
    position_choices = (
        ('TOP', 'Top'),
        ('JUG', 'Jungle'),
        ('MID', 'Middle'),
        ('BOT', 'Bottom'),
        ('SUP', 'Support')
    )

    team_choices = (
        ('RNG', 'Royal Never Give Up'),
        ('EDG', 'Edward Gaming Hycan'),
        ('WE', 'Team WE'),
        ('IG', 'Invictus Gaming'),
        ('TES', 'Top Esports'),
        ('FPX', 'FunPlus Phoenix'),
        ('OMG', 'Oh My God'),
        ('JDG', 'JDG Intel Esports Club'),
        ('BLG', 'Bilibili Gaming'),
        ('WBG', 'Weibo Gaming'),
    )

    year_choices = []
    for y in range(2013, (datetime.now().year + 1)):
        year_choices.append((y, y))

    honor_choices = (
        ('WORLD', 'World Champion'),
        ('MSI', 'Mid-Season Invitational Champion'),
        ('LPL', 'LPL Championship'),
        ('Demacia', 'Demacia Cup Championship'),
    )

    honor_map = {
        'WORLD': 'World Champion',
        'MSI': 'Mid-Season Invitational Champion',
        'LPL': 'LPL Championship',
        'Demacia': 'Demacia Cup Championship',
    }

    game_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    position = MultiSelectField(choices=position_choices, max_length=100)
    team = MultiSelectField(choices=team_choices, max_length=100)
    description = RichTextField(default="lpl player")
    photo1 = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    first_show_year = models.IntegerField(choices=year_choices)
    created_date = models.DateTimeField(auto_now_add=True)
    is_retire = models.BooleanField(default=False)
    honor = MultiSelectField(choices=honor_choices, max_length=100, default=[])

    def __str__(self):
        return self.game_id


def get_field_options(field):
    all_values = list(Player.objects.values_list(field, flat=True))
    options = [option for values in all_values for option in values]
    return set(options)
