from enum import Enum

class RestrictionType(Enum):
    REQUIRED_TRUCK = 401
    DELIVER_WITH = 402
    DELAYED_UNTIL = 403
    WRONG_ADDRESS = 404