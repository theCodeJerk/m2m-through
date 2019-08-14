import string

from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


def custom_filename(instance, filename):
    #author = instance.publishers[0]
    #return 'papers/{0}.pdf'.format(author.pseudonum)
    return filename;


class Submission(models.Model):
    name = models.CharField(
        max_length=200, 
        blank=False
        )
    upload = models.FileField(
        blank=True, 
        upload_to=custom_filename
        )
    publishers = models.ManyToManyField(
        'Publisher', 
        related_name='publisher_of',
        through='SubmissionPublisher'
        )


class Publisher(models.Model):
    user = models.ForeignKey(
        User, blank=False, 
        on_delete=models.CASCADE
        )
    pseudonym = models.CharField(
        max_length=200,
        blank=False
        )


class SubmissionPublisher(models.Model):
    publisher = models.ForeignKey(
        Publisher, 
        blank=False, 
        related_name='published_of',
        on_delete=models.CASCADE
        )
    submission = models.ForeignKey(
        Submission, 
        blank=False, 
        related_name='published_by',
        on_delete=models.CASCADE
        )
