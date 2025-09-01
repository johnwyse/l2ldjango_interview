from django import template
from datetime import datetime

register = template.Library()

@register.filter
def l2l_dt(value):
    """
    Custom template filter for formatting dates/times.
    
    Should handle both input types:
    - datetime objects 
    - ISO date strings
    Returns formatted string "YYYY-MM-DD HH:MM:SS" or original value on error.

    """
    try:
        # if value is datetime object
        if isinstance(value, datetime):
            return value.strftime("%Y-%m-%d %H:%M:%S")
        
        # if value is ISO date string
        elif isinstance(value, str):
            dt = datetime.fromisoformat(value)
            return dt.strftime("%Y-%m-%d %H:%M:%S")

    except (ValueError, TypeError, AttributeError) as e:
        # We expect these when parsing bad date strings
        # consider logging with logger library. ie:
        # log.warning(f"l2l_dt filter couldn't parse value: {value}, exception: {e}")
        return value
    
    except Exception as e:
        # consider logging error with logger library. ie:
        # log.error(f"Error in l2l_dt filter: {e}")
        raise
