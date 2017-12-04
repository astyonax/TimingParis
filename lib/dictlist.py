class dictlist(dict):
    """A python implementation of a dictionary mapping one key to a list of values.

    Parameters
    ----------
    See the ``update`` method.

    Example
    -------
    >>> from dictlist import dictlist
    >>> dl = dictlist()
    >>> dl['A']='a'
    >>> dl.update({'B':'b','C':'c'})
    >>> dl.update({'B':'b1','C':'c1'})
    >>> dl == {'A': ['a'], 'C': ['c', 'c1'], 'B': ['b', 'b1']}
    True

    """

    def __init__(self,other=None,**kwargs):
        self.update(other,**kwargs)

    def update(self, other=None, **kwargs):
        """
        Updates the dictionary with the keys and values

        --
        Copied from `UserDict`'s implementation
        Modified to use the custom `__setitem__` method

        Parameters
        ----------
        other : None
                Nothing is done
        other : dict
                The dictionary is updated. New keys are created.
                Values are appended to their respective keys
        other : [ (a,b),(c,d),..]
                The dictionary is updated mapping a and c in keys,
                and b and d in values.

        Example
        -------
        >>> from dictlist import dictlist
        >>> dl = dictlist()
        >>> dl.update({'B':'b','C':'c'})
        >>> dl.update({'C':'c1'})
        >>> dl == {'C': ['c', 'c1'], 'B': ['b']}
        True
        """

        # Make progressively weaker assumptions about "other"
        if other is None:
            pass
        elif hasattr(other, 'iteritems'):  # iteritems saves memory and lookups
            for k, v in other.iteritems():
                self.__setitem__(k, v)
        elif hasattr(other, 'keys'):
            for k in other.keys():
                self.__setitem__(k, other[k])
        else:
            for k, v in other:
                self.__setitem__(k, v)
        if kwargs:
            self.update(kwargs)

    def __setitem__(self,key,value):
        """
            Inserts value in the list of values of key.
            If key does not exists, it's created.

            Parameters
            ----------
            key : any hashable object
            value: any object

            Example
            -------
            >>> from dictlist import dictlist
            >>> dl = dictlist()
            >>> dl
            {}
            >>> dl['A']='a'
            >>> dl
            {'A': ['a']}

        """
        insert_value = self[key]
        insert_value.append(value)
        super(dictlist,self).__setitem__(key,insert_value)

    def __missing__(self,key):
        return list()

    def minus(self,other=None,*args,**kwargs):
        """Removes the 1st occurence of ``value`` in ``key``.
        Removal is performed in place, as in :py:list:remove

        Parameters
        ----------
        other : None
                Nothing is done
        other : dict
                For each item key, value, removes the first occurence of value
                in the list of key
        other : [ (a,b),(c,d),..]
                The dictionary is updated mapping a and c in keys,
                and b and d in values.

        Examples
        --------
        >>> from dictlist import dictlist
        >>> dl = dictlist()
        >>> dl.update({'B':'b','C':'c'})
        >>> dl.update({'C':'c1'})
        >>> dl == {'C': ['c', 'c1'], 'B': ['b']}
        True
        >>> dl.minus({'C':'c1'})
        >>> dl == {'C': ['c'], 'B': ['b']}
        True
        >>> dl.update({'C':'c1'})
        >>> dl.minus(C='c1')
        >>> dl == {'C': ['c'], 'B': ['b']}
        True
        >>> dl.update({'C':'c1'})
        >>> dl.minus([('C','c1'),])
        >>> dl == {'C': ['c'], 'B': ['b']}
        True
        """
        if other==None:
            pass
        elif hasattr(other, 'iteritems'):
            for k, v in other.iteritems():
                self[k].remove(v)
        elif hasattr(other, 'keys'):
            for k in other.keys():
                self[k].remove(other[k])
        else:
            for k, v in other:
                self[k].remove(v)

        if kwargs:
            self.minus(kwargs)


    def popkw(self,key,value):
        """Removes all occurences of ``value`` in ``key``

        Parameters
        ----------
            key : a key
            value : a value

        >>> from dictlist import dictlist
        >>> dl = dictlist()
        >>> dl.update({'B':'b','C':'c'})
        >>> dl.update({'C':'c1'})
        >>> dl.update({'C':'c1'})
        >>> dl == {'C': ['c', 'c1','c1'], 'B': ['b']}
        True
        >>> dl.popkw('C','c1')
        >>> dl == {'C': ['c'], 'B': ['b']}
        True
        """
        vlist = self[key]
        vlist_new = [i for i in vlist if i != value]
        super(dictlist,self).__setitem__(key,vlist_new)
