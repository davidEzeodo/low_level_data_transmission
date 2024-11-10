# This exercise is aimed at showing the workings of how to convert integers to and from host network byte order. One
# might need to write a low-level network application, it may be necessary to handle the low-level data transmission
# over the wire between two machines. This operation requires some conversion of data from the native host operating
# system to the network format and vice versa. This is because each one has its own specific representation of data.

# Key-note
# Python's socket library has two utilities for converting from a network byte order to host byte order and vice versa.
# They include; ntohl()/htonl().

import socket


def convert_integer():
    data = 1234
    print(
        "Original: %s => Long host byte order: %s, Network byte order: %s" % (
            data, socket.ntohl(data), socket.htonl(data)))
    print("Original: %s => Short host byte order: %s, Network byte order: %s" % (
        data, socket.ntohs(data), socket.htons(data)))


if __name__ == '__main__':
    convert_integer()
