from django.db import models



class MyPicture(models.Model):

    img = models.CharField(max_length=255)
    detail = models.CharField(max_length=550)

    def __str__(self):
        return f'{self.img} , {self.detail}'

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.question_text}'

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.question.question_text} - {self.choice_text} - {self.votes}'

#class inputPicture(models.Model):
    #img = models.CharField(max_length=255)
    #Description = models.CharField(max_length=1000)
    #def __str__(self):
        #return f'{self.img} - {self.Description}'