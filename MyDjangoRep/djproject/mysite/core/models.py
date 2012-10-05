from django.db import models

class dobase(models.Model): #Table name, has to wrap models.Model to get the functionality 
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)#Like a VARCHAR field
    description = models.TextField() #Like a TEXT field
    created = models.DateTimeField() #Like a DATETIME field
    preview =''
    num_comm =''
    
    def __unicode__(self): #Tell it to return as a unicode string (The name ofthe to-do item) rather than just Object.
        return self.name

class comment(models.Model):
    name = models.CharField(max_length=100)
    opinion = models.TextField(default='')
    checked = models.BooleanField(blank=True,default=False)
    article = models.ForeignKey(dobase)
    
    def __unicode__(self): #Tell it to return as a unicode string (The name ofthe to-do item) rather than just Object.
        return '%s' % self.opinion[:151]
