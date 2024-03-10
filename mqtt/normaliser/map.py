from ..enums import MessageTypes
from .deregister import Deregister
from .register import Register
from .update import Update

NORMALISER_MAPPING = {
    MessageTypes.REGISTER.value: Register,
    MessageTypes.DEREGISTER.value: Deregister,
    MessageTypes.UPDATE.value: Update,
}
