"""
Meetup date finder module.

This module helps find specific meetup dates based on weekday and week descriptor.
"""

from datetime import date
import calendar


class MeetupDayException(ValueError):
    """Exception raised when the Meetup weekday and count do not result in a valid date."""
    
    def __init__(self, message):
        self.message = message
        super().__init__(message)


def meetup(year, month, week, day_of_week):
    """
    Find the date of a meetup given year, month, week descriptor, and weekday.
    
    Args:
        year (int): The year of the meetup.
        month (int): The month of the meetup (1-12).
        week (str): Week descriptor ('first', 'second', 'third', 'fourth', 
                    'fifth', 'last', or 'teenth').
        day_of_week (str): Day of the week ('Monday', 'Tuesday', etc.).
    
    Returns:
        date: The date object for the meetup.
    
    Raises:
        MeetupDayException: If the specified week/day combination doesn't exist.
    """
    weekdays = {
        'Monday': 0,
        'Tuesday': 1,
        'Wednesday': 2,
        'Thursday': 3,
        'Friday': 4,
        'Saturday': 5,
        'Sunday': 6
    }
    
    target_weekday = weekdays[day_of_week]
    
    if week == 'teenth':
        for day in range(13, 20):
            test_date = date(year, month, day)
            if test_date.weekday() == target_weekday:
                return test_date
    
    elif week == 'last':
        last_day = calendar.monthrange(year, month)[1]
        
        for day in range(last_day, 0, -1):
            test_date = date(year, month, day)
            if test_date.weekday() == target_weekday:
                return test_date
    
    else:
        week_map = {
            'first': 1,
            'second': 2,
            'third': 3,
            'fourth': 4,
            'fifth': 5
        }
        
        week_number = week_map[week]
        occurrences = []
        last_day = calendar.monthrange(year, month)[1]
        
        for day in range(1, last_day + 1):
            test_date = date(year, month, day)
            if test_date.weekday() == target_weekday:
                occurrences.append(test_date)
        
        if week_number > len(occurrences):
            raise MeetupDayException("That day does not exist.")
        
        return occurrences[week_number - 1]
    
    raise MeetupDayException(f"Unable to find {week} {day_of_week} in {month}/{year}")
