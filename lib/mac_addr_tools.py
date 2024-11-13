# A MAC address tools library
#

from machine import ADC, Pin

class MAC_Tools():
    
    # Broadcast MAC address is different formats
    MAC_ADDR_BROADCAST_BA = [0xFF, 0xFF, 0xFF, 0xFF, 0xFF, 0xFF]
    MAC_ADDR_BROADCAST_BSTR = const(b'\xff\xff\xff\xff\xff\xff') 
    MAC_ADDR_BROADCAST_STR = const("FF:FF:FF:FF:FF:FF")
        

    # Convert a valid MAC address from a byte string to a string
    def bstr_to_str(mac_addr_bstr):
        string = ("%02X:%02X:%02X:%02X:%02X:%02X") % (mac_addr_bstr[0], mac_addr_bstr[1], mac_addr_bstr[2], mac_addr_bstr[3], mac_addr_bstr[4], mac_addr_bstr[5])
        
        return string    
    
    
    # Find out which cast type the byte array is, for mode details see IEEE 802.3
    def cast_type_ba(ba):
        if ba == MAC_Tools.MAC_ADDR_BROADCAST_BA:
            return "Broadcast"
        elif ba[0] & 0x01 == 0x01:
            return "Multicast"
        else:
            return "Unicast"
        
    
    # Validate a MAC Address, for mode details see IEEE 802.3
    def str_validate(mac_addr_str):
        if len(mac_addr_str) != 17:
            return "Invalid length"
        else:
            mac_addr_str = mac_addr_str.replace("-", ":")
            parts = mac_addr.split(":")
            if len(parts) != 6:
                return "Invalid number of octets"
            else:
                ba = bytearray(6)
                for i in range(6):
                    try:
                        ba[i] = int(parts[i], 16)
                        if ba[i] > 0xFF: # Check if octet valus is to big
                            return "Invalid octet value %X" % ba[i]
                    except:
                        return "Invalid octet %d" % i
                
                if ba == MAC_Tools.MAC_ADDR_BROADCAST_BA:
                    return "Broadcast"
                elif ba[0] & 0x01 == 0x01:
                    return "Multicast"
                else:
                    return "Unicast"


    # Converts a MAC address string to a byte string
    def str_to_bstr(mac_addr_str):
        if len(mac_addr_str) == 17:
            parts = mac_addr_str.split(':')
            if len(parts) == 6:
                ba = bytearray(6)
                for i in range(6):
                    try:
                        ba[i] = int(parts[i], 16)
                        if ba[i] > 0xFF: # Check if octet valus is to big
                            return None                        
                    except:
                        return None        # Not a convertable hex number, so return
                
                # No errors found so pack into a byte-string   
                mac_addr_bstr = bytes([ba[0], ba[1], ba[2], ba[3], ba[4], ba[5]])
                return mac_addr_bstr
        
        return None                        # Invalid length or number of parts
