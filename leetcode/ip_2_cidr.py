def ip_2_cidr(ip1, ip2):
    ip1_bin = ip_2_bin(ip1)
    ip2_bin = ip_2_bin(ip2)
    cidr = 0
    for i in range(32):
        if ip1_bin[i] != ip2_bin[i]:
            cidr = i
            break
    result = ip1_bin[:cidr] + '0' * (32 - cidr)
    print len(result)
    print result
    print cidr

def ip_2_bin(ip):
    return ''.join(map(lambda x: bin(int(x))[2:].rjust(8, '0'), ip.split('.')))

ip1 = '192.168.1.254'
ip2 = '192.168.1.255'
ip_2_cidr(ip1, ip2)
