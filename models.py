from django.db import models
CHOOSE = (
    (1, 'Manual'),
    (2, 'Automatic'),
    (3, 'Error'),
    (4, 'Idle'),
)

class CleanRobot(models.Model):
    """..."""
    name = models.IntegerField(choices=CHOOSE)
    velocity = models.FloatField(null=True, blank=True)
    positionX = models.FloatField(null=True, blank=True)
    positionY = models.FloatField(null=True, blank=True)
    angleTHETA = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = "CleanRobot"
        verbose_name_plural = "CleanRobots"

    def __str__(self):
        return self.name