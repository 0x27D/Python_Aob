from Memory import notifi, MemoryScan


class Aobscan(object):

    
    def aobscan():
        scan = bytes.fromhex('79 44 20 46 36 F2 E0 FB A7 F1 50 01 20 46')
        rep = bytes.fromhex('00 20 70 47')        

        try:
            MemoryScan(scan, rep)
            
            notifi('Done')

        except Exception as e:
            notifi('error')

    
