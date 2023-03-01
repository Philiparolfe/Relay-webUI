from gpiozero import OutputDevice
import time

# BCM PINS:
# see if on or off: print(relay.value)

relay1 = OutputDevice(4, active_high=True, initial_value=False)
relay2 = OutputDevice(22, active_high=True, initial_value=False)
relay3 = OutputDevice(6, active_high=True, initial_value=False)
relay4 = OutputDevice(26, active_high=True, initial_value=False)
relays = [relay1, relay2, relay3, relay4]

def blinker(time_delay, relay_sel, blinks):
    
    for i in range(0, blinks):
        relays[relay_sel].on()
        
        time.sleep(time_delay)
        print(f'Relay:{relay_sel}\tStatus:{relays[relay_sel].value}\tCount:{i}')
        relays[relay_sel].off()
        time.sleep(time_delay)
        print(f'Relay:{relay_sel}\tStatus:{relays[relay_sel].value}')
        
def switchOn(relay_sel):
    if relays[relay_sel].is_active == False:
        relays[relay_sel].on()
        print(f'Relay:{relay_sel}\tStatus:{relays[relay_sel].value}')
    else:
        print('Invalid relay selection !!!')
    
def switchOff(relay_sel):
    if relays[relay_sel].is_active:
        relays[relay_sel].off()
        print(f'Relay:{relay_sel}\tStatus:{relays[relay_sel].value}')
    else:
        print('Invalid relay selection !!!')
