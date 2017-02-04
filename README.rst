Secret Splitting
================

This programs implement the secret splitting protocol detailed in Bruce
Schneiers "Applied Cryptography", Chapter 3.6 p.70 of the second
edition.

The idea is to split a plaintext into N pieces shared by N people. Only
if the N people meet later can they re-create the original plaintext.
This is done by producing N-1 one-time pads the length of the original
plaintext. These are XORed with the plaintext yielding the Nth secret
piece. If the N pieces are later XORed we get the original plaintext.

The implementation provides a class that does the encryption but doesn't
deal with file-I/O (except for the random-number source which is
implemented as a file on most operating systems, we're using
``/dev/random`` by default but this can be specified as an option).

There are two command-line tools, ``secret-split`` and
``secret-combine``. The first takes a plaintext file and produces the N
parts. The second combines N parts into the original plaintext.

Example
-------

The following is a command-line example that splits the secret string
"Hello World" into 5 pieces and then combines them again::

  % echo "Hello World" > message
  % secret-split -n 5 message
  % ls
  message        message.part1  message.part3
  message.part0  message.part2  message.part4
  % secret-combine -o combined-message message.part?
  % cmp message combined-message


