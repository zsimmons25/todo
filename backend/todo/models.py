# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Todo(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField()
	completed = models.BooleanField(default=False)

	def _str_(self):
		return self.title

# Create your models here.
