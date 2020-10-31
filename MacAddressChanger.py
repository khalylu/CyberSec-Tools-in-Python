
import subprocess
import optparse


def get_args():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="net_type", help="which interfaces mac address to change")
    parser.add_option("-m", "--macaddress", dest="mac_number", help="relates to mac address number")
    return parser.parse_args()


def get_mac(net_type, mac_number):
    print(f"New MAC address is {mac_number} on a {net_type} connection")
    subprocess.call(["ifconfig", net_type, "down"])
    subprocess.call(["ifconfig", net_type, "hw", "ether", mac_number])
    subprocess.call(["ifconfig", net_type, "up"])


(options, args) = get_args()
get_mac(options.net_type, options.mac_number)
