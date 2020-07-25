import hid

def detect():
    known_pids = [0x8008, 0x8009, 0xa292, 0xa293];
    vid = 0x04d9
    for pid in known_pids:
        try:
            with hid.Device(vid, pid) as h:
                keeb = (
                    f'\nDevice manufacturer: {h.manufacturer}'
                    f'\n\nProduct: {h.product}\n'
                    f'\nSerial Number: {h.serial}\n'
                 )       
                return [keeb,vid,pid]
        except:
            pass
    return "No AnnePro2 keeb found"