from modules import webcam, microphone, location

def print_banner():
    banner = """

     __                 __            _______           _        _________  
[  |               [  |          |_   __ \         / \      |  _   _  | 
 | |.--.    .---.   | |   ,--.     | |__) |       / _ \     |_/ | | \_| 
 | '/'`\ \ / /__\\  | |  `'_\ :    |  __ /       / ___ \        | |     
 |  \__/ | | \__.,  | |  // | |,  _| |  \ \_   _/ /   \ \_     _| |_    
[__;.__.'   '.__.' [___] \'-;__/ |____| |___| |____| |____|   |_____|   
                                                                        

"""
    print(banner)



if __name__ == "__main__":
    print_banner()
    webcam.access_webcam()
    microphone.access_microphone()
    loc = location.get_location()
    print(loc)
