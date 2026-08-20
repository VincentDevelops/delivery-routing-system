# DeliveryStatus.py

from enum import Enum

class DeliveryStatus(Enum):
    DELAYED = 1
    AT_HUB = 2
    EN_ROUTE = 3
    DELIVERED = 4