from modules import webcam, microphone, location

if __name__ == "__main__":
    
    webcam.access_webcam()
    microphone.access_microphone()
    loc = location.get_location()
    print(loc)
