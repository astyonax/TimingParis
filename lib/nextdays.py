import datetime

class listdays(object):
    """
        Just map from day name to day index:
        Monday..Sunday -> 0..6

        Examples
        --------
        >>> days = listdays()
        >>> for d in days.__slots__: print getattr(days,d)
        0
        1
        2
        3
        4
        5
        6
        >>> print days.monday
        0
    """
    __slots__=('monday','tuesday','wednesday',
               'thursday','friday','saturday','sunday')
    def __init__(self):
        self.monday=0
        self.tuesday=1
        self.wednesday=2
        self.thursday=3
        self.friday=4
        self.saturday=5
        self.sunday=6

################################################################################

################################################################################

def nextday(when, weekday):
    """
        Returns the date of the first occurence of the day `weekday`
        after the date `when`

        Inspired by
        -----------
        http://stackoverflow.com/questions/6558535/find-the-date-for-the-first-monday-after-a-given-a-date

        Parameters
        ----------
        when : datetime
               The date (and time) to look for `weekday` from
        weekday : int
               Integer between 0..6 for Monday...Sunday

        Examples
        --------
        >>> import datetime
        >>> d = datetime.datetime.now()
        >>> d = d.replace(hour=8,minute=0,second=0,microsecond=0,day=20,month=2,year=1991)
        >>> print d
        1991-02-20 08:00:00
        >>> for j in xrange(0,7): print nextday(d,j)
        1991-02-25 08:00:00
        1991-02-26 08:00:00
        1991-02-27 08:00:00
        1991-02-21 08:00:00
        1991-02-22 08:00:00
        1991-02-23 08:00:00
        1991-02-24 08:00:00
    """

    days_ahead = weekday - when.weekday()
    if days_ahead <= 0: # Target day already happened this week
        days_ahead += 7
    return when + datetime.timedelta(days_ahead)


def nextdayat(day=0,hour=0,minute=0,when=datetime.datetime.now()):
    """
        Returns the next occurence of day, at time hour, minute from `when`

        Parameters
        ----------

        day : int
            day int as in days class (0..6)
        hour, minute : float
        when : datetime
            Date from which we look for day `day`, defaut is `now`


        Examples
        --------
        >>> days = listdays()
        >>> import datetime
        >>> d = datetime.datetime.now()
        >>> d = d.replace(hour=8,minute=0,second=0,microsecond=0,day=24,month=9,year=1985)
        >>> print nextdayat(days.monday,8,30,when=d)
        1985-09-30 08:30:00
        >>> print nextdayat(0,8,30,when=d)
        1985-09-30 08:30:00
    """
    date = nextday(when,day)
    date = date.replace(microsecond=0,second=0,minute=minute,hour=hour)
    return date
