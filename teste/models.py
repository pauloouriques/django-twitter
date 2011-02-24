from django.db import models

class Teste(models.Model):
    tweet = models.CharField(max_length=144)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1)
    pub_date = models.DateTimeField('date published')
    
    def __unicode__(self):
        return self.tweet

