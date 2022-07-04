"""     Adrian SZKLARSKI, 12.2021r,
          Task Simple Robot Simulator:
Manual control: guiding the X, Y position where the robot should go.
The distance traveled is calculated. This case simulates manual guidance of the robot.
Automatic: simulates driving the robot along the X-axis in increments of 1
and along the Y-axis in increments of 1 and an imposed randomization factor.
3 and 4 Failure and waiting status, lead to the home page, are not saved in the database.

    Returns:      The robot's x,y position, speed and angle.
    Parameters:   Initial points of the robot's position x0 and y0
    Error:        Reference to homepage
    Idle:         Reference to homepage
"""



from django.db import models
CHOOSE = (
    (1, 'Manual'),
    (2, 'Automatic'),
    (3, 'Error'),
    (4, 'Idle'),
)

class CleanRobot(models.Model):
    """Robot Position and Speed Simulator"""
    name = models.IntegerField(choices=CHOOSE)
    velocity = models.FloatField(null=True, blank=True)
    positionX = models.FloatField(null=True, blank=True)
    positionY = models.FloatField(null=True, blank=True)
    angleTHETA = models.FloatField(null=True, blank=True)

    class Meta:
        verbose_name = "CleanRobot"
        verbose_name_plural = "CleanRobots"

    def __str__(self):
        return str(self.name)