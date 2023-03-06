from django.db import models

# Create your models here.
class Questions(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    content_length = models.IntegerField(default=100)
    category = models.CharField(max_length=70)
    project = models.CharField(max_length=70)
    spider = models.CharField(max_length=70)
    server = models.CharField(max_length=70)
    date_scraped = models.DateField()
    date_recorded = models.DateTimeField(auto_now_add=True)
    processed = models.CharField(max_length=5, choices=[('True', 'True'), ('False', 'False')], default='False')
    short = models.CharField(max_length=5, choices=[('True', 'True'), ('False', 'False'), ], default='False')
    link_no = models.IntegerField()
    no = models.AutoField(primary_key=True)
    class Meta:
        db_table = 'questions'
    
    def question_titles(self):
        return [self.no, self.title]
    


class StagedQuestions(models.Model):
    link_no = models.IntegerField()
    no = models.AutoField(primary_key=True)
    date_recorded = models.DateTimeField(auto_now_add=True)
    date_processed = models.DateField()
    status = models.CharField(max_length=10, choices=[('Staged', 'Staged'),('Waiting', 'Waiting'), ('Processed', 'Processed')], default='Staged')