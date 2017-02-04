#!/usr/bin/python

import sys
try :
    from functools import reduce
except ImportError :
    pass

# Python-3 doesn't need ord and chr for handling byte-strings
if sys.version_info >= (3,) :
    def b_ord (x) :
        return x
    def b_chr (x) :
        return bytes ((x,))
else :
    def b_ord (x) :
        return ord (x)
    def b_chr (x) :
        return chr (x)


class Secret_Split (object) :
    """ This splits a given message M into n parts, each the same length
        as the message M. We do this by generating m-1 one-time pads Si and
        XOR-ing each with the message M:

        S1 ^ S2 ^ ... M = Sn

        The Si are the secrets given to n persons. Combining all the Si
        together gives the original message M:

        S1 ^ S2 ^ ... ^ Sn = M

        This is done by the combine method.
        See Bruce Scheier, Applied Cryptography 2nd Edition, 3.6 "Secret
        Sharing" p.71f.
    """

    randsrc = "/dev/random"

    def __init__ (self, message = b'', secrets = [], randsrc = randsrc) :
        self.randsrc = randsrc
        self.message = message
        self.secrets = secrets
        assert bool (message) ^ bool (secrets)
        if message :
            self.length = len (message)
        else :
            self.length = len (secrets [0])
    # end def __init__

    def combine (self) :
        """ Combine all secrets to generate message
        """
        # preconditions
        assert self.secrets
        r = []
        for l in zip (* self.secrets) :
            v = b_chr (reduce (lambda x, y : x ^ y, (b_ord (x) for x in l), 0))
            r.append (v)
        if not self.message :
            self.message = b''.join (r)
        else :
            assert self.message == b''.join (r)
        return self.message
    # end def combine

    def generate_one_time_pad (self) :
        f = open (self.randsrc, 'rb')
        r = f.read (self.length)
        f.close ()
        assert len (r) == self.length
        return r
    # end def generate_one_time_pad

    def split (self, n) :
        """ Split self.message into n parts
        """
        n = int (n)
        # preconditions, don't overwrite secrets
        assert n > 1
        assert not self.secrets
        assert self.message
        for i in range (n - 1) :
            self.secrets.append (self.generate_one_time_pad ())
        r = []
        for l in zip (self.message, * self.secrets) :
            v = b_chr (reduce (lambda x, y : x ^ y, (b_ord (x) for x in l), 0))
            r.append (v)
        self.secrets.append (b''.join (r))
    # end def split

# end class Secret_Split

def test () :
    m = b"Hello World\n"
    sp = Secret_Split (message = m)
    sp.split (4)
    sp.combine ()
    j  = Secret_Split (secrets = sp.secrets)
    j.combine ()
    assert j.message == sp.message
    assert j.message == m
# end def test

if __name__ == "__main__" :
    test ()
