import sys

# Checking octets
def ip_addr_valid(list):

    for ip in list:
        ip = ip.rstrip("\n")
        octets = ip.split('.')

        if (len(octets) == 4) and (1 <= int(octets[0]) <= 223) and (int(octets[0]) != 127) and \
            (int(octets[0]) != 169 or int(octets[1]) != 254) and ( 0 <= int(octets[1]) <= 255) and \
            ( 0 <= int(octets[2]) <= 255) and ( 0 <= int(octets[3]) <= 255):
            continue
        else:
            print('\n* There was an invalid IP address in the file: {}\n'.format(ip))
            sys.exit()
