from modules import webcam, microphone, location

def print_banner():
    banner = """

_____________________________________________   _______________________        
[  |               [  |          |_   __ \         / \      |  _   _  | 
 | |.--.    .---.   | |   ,--.     | |__) |       / _ \     |_/ | | \_| 
 | '/'`\ \ / /__\\  | |  `'_\ :    |  __ /       / ___ \        | |     
 |  \__/ | | \__.,  | |  // | |,  _| |  \ \_   _/ /   \ \_     _| |_    
[__;.__.'   '.__.' [___] \'-;__/ |____| |___| |____| |____|   |_____|   
______________   _______________________________________________________  
                              |                                         |
                              |   Developed by: Abel Mekuriya           |
                              |          Gmail: b3lar00s@gmail.com      |
                              |_________________________________________| 
 """
    print(banner)



if __name__ == "__main__":
    print_banner()
    webcam.access_webcam()
    microphone.access_microphone()
    loc = location.get_location()
    print(loc)
