from __future__  import absolute_import

try:
    VERSION = __import__('pkg_resources').get_distribution('django-idfield').version
except Exception:
    VERSION = 'unknown'

from .fields import IDField
