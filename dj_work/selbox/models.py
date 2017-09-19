from django.db import models

# Create your models here.
class RunHistory(models.Model):
	run_name = models.CharField(max_length=50)
	run_time = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.run_name
	
class RunValues(models.Model):
	run_history = models.ForeignKey(RunHistory, 
	on_delete=models.CASCADE)
	value_dt = models.DateTimeField()
	value_val = models.FloatField()
	
	def __str__(self):
		return ", ".join((str(self.run_history), str(self.value_dt),
		str(self.value_val)))
	
	class Meta:
		unique_together = (('run_history', 'value_dt'),)
