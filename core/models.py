
from django.db import models
from django.contrib.auth.models import User
import uuid


class Complaint(models.Model):

    CATEGORY_CHOICES = [
        ('power_outage', 'Power Outage'),
        ('voltage', 'Voltage Fluctuation'),
        ('meter', 'Meter Related Issue'),
        ('billing', 'Billing Issue'),
        ('damaged_line', 'Damaged Electrical Line'),
        ('new_connection', 'New Connection'),
        ('other', 'Other'),
    ]

    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('critical', 'Critical'),
    ]

    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('received', 'Received'),
        ('assigned', 'Assigned'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]

    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='complaints'
    )

    complaint_id = models.CharField(
        max_length=20,
        unique=True,
        blank=True
    )

    category = models.CharField(
        max_length=30,
        choices=CATEGORY_CHOICES
    )

    subject = models.CharField(max_length=200)

    description = models.TextField()

    address = models.TextField()

    contact_number = models.CharField(max_length=15)

    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='submitted'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    # GENERATE UNIQUE COMPLAINT ID
    def save(self, *args, **kwargs):

        if not self.complaint_id:
            self.complaint_id = f"VC{uuid.uuid4().hex[:10].upper()}"

        super().save(*args, **kwargs)

    # DISPLAY COMPLAINT ID
    def __str__(self):
        return self.complaint_id or f"Complaint #{self.pk}"
