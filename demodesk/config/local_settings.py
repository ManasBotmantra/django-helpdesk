from .settings import BASE_DIR
import os

# Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'django_helpdesk',
        'USER': 'postgres',
        'PASSWORD': 'Welcome@123', # TODO: Replace this with your actual postgres password
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Custom Ticket Statuses
# 1=Open, 2=Reopened, 3=Resolved, 4=Closed, 5=Duplicate (Defaults)
# We are adding 6=Pending
from django.utils.translation import gettext_lazy as _

HELPDESK_TICKET_STATUS_CHOICES = (
    (1, _("Open")),
    (2, _("Reopened")),
    (3, _("Resolved")),
    (4, _("Closed")),
    (5, _("Duplicate")),
    (6, _("Pending")), # Custom Status
)

# You can also define which statuses are considered "Open" (active)
# If Pending (6) should be considered an active state, add it here:
HELPDESK_TICKET_OPEN_STATUSES = (1, 2, 6)
