import teslapy
import json
from os import system, name 
from getpass import getpass
from time import sleep 

#Client info needed for TeslaPy Library. Super annoying.
CLIENT_ID='e4a9949fcfa04068f59abb5a658f2bac0a3428e4652315490b659d5ab3f35a9e'
CLIENT_SECRET='c75f14bbadc8bee3a7594412c31416f8300256d7668ea7e6e7f06727bfb9d220'

# make it clean
def clear(): 

    # winduwz
    if name == 'nt': 
        _ = system('cls') 

    # nix
    else: 
        _ = system('clear') 


#clear the garbage
clear()

#plug
print('-----------------------------------------------------')
print('-----------------------------------------------------')
print('*****[[ Safekeep Cybersecurity: Tesla Connect ]]*****')
print('-----------------------------------------------------')
print('-----------------------------------------------------\n\n')

while True:


    #creds 
    print('Please input your Tesla Credentials:\n')
    EMAIL = input('Username:\n')
    PASSWORD = getpass()
    clear()
    print('Testing Connection ... ... ...\n')
    
    try:
        with teslapy.Tesla(EMAIL, PASSWORD, CLIENT_ID, CLIENT_SECRET) as tesla:
            tesla.fetch_token()
            vehicles = tesla.vehicle_list()
            vehicles[0].sync_wake_up()
        print('... ... ... Connection Successful!\n')
        break
    except teslapy.HTTPError as e:
        print(e)
        pass
        
while True:
    #dictionary inception - wtf - get data
    
    data = vehicles[0].get_vehicle_data()
    datadumped = json.dumps(data)
    dataloaded = json.loads(datadumped)
    charge_state = dataloaded.get('charge_state')
    climate_state = dataloaded.get('climate_state')
    drive_state = dataloaded.get('drive_state')
    gui_settings = dataloaded.get('gui_settings')
    vehicle_config = dataloaded.get('vehicle_config')
    vehicle_state = dataloaded.get('vehicle_state')  

    print('*****[[ Safekeep Cybersecurity: Tesla Connect ]]*****\n')

    print('-------------Connected to: '+ vehicle_state.get('vehicle_name') + ' | ' + vehicle_config.get('car_type'))
    print('\n')
    print('\n')

    print('--------Please select one of the following:----------')
    print('0: Unlock Vehicle')
    print('1: Lock Vehicle')
    print('2: Honk Horn')
    print('3: Flash Lights')
    print('4: Climate On')
    print('5: Climate Off')
    print('6: Max Defrost')
    print('7: Change Climate Temperature Settings')
    print('8: Change Charge Limit')
    print('9: Window Control')
    print('10: Open Frunk')
    print('11: Open Trunk')
    print('12: Vehicle Remote Start')
    print('13: Trigger Homelink')
    print('14: Chargeport Control')
    print('15: Charge Control')
    print('16: Sentry Mode Control')
    print('17: Deactivate Device Token')
    print('18: Valet Controls')


    selection = input('Please select a number:')

    if selection == '0':
        try:
            vehicles[0].sync_wake_up()
            vehicles[0].command('UNLOCK')
            clear()
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')
            print('Success: ' + vehicle_state.get('vehicle_name') + ' Unlocked')
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')

        except teslapy.HTTPError as e:
            print(e)
            pass

    elif selection == '1':
        try:
            vehicles[0].sync_wake_up()
            vehicles[0].command('LOCK')
            clear()
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')
            print('Success: ' + vehicle_state.get('vehicle_name') + ' Locked')
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')

        except teslapy.HTTPError as e:
            print(e)
            pass

    elif selection == '2':
        try:
            vehicles[0].sync_wake_up()
            vehicles[0].command('HONK_HORN')
            clear()
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')
            print('Success: ' + vehicle_state.get('vehicle_name') + ' Honk Initiated')
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')

        except teslapy.HTTPError as e:
            print(e)
            pass

    elif selection == '3':
        try:
            vehicles[0].sync_wake_up()
            vehicles[0].command('FLASH_LIGHTS')
            clear()
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')
            print('Success: ' + vehicle_state.get('vehicle_name') + ' Flash Initiated')
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')

        except teslapy.HTTPError as e:
            print(e)
            pass

    elif selection == '4':
        try:
            vehicles[0].sync_wake_up()
            vehicles[0].command('CLIMATE_ON')
            clear()
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')
            print('Success: ' + vehicle_state.get('vehicle_name') + ' Climate On')
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')

        except teslapy.HTTPError as e:
            print(e)
            pass

    elif selection == '5':
        try:
            vehicles[0].sync_wake_up()
            vehicles[0].command('CLIMATE_OFF')
            clear()
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')
            print('Success: ' + vehicle_state.get('vehicle_name') + ' Climate Off')
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')

        except teslapy.HTTPError as e:
            print(e)
            pass

    elif selection == '6':
        try:
            vehicles[0].sync_wake_up()
            vehicles[0].command('MAX_DEFROST',on='true')
            clear()
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')
            print('Success: ' + vehicle_state.get('vehicle_name') + ' Defrost On')
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')

        except teslapy.HTTPError as e:
            print(e)
            pass

    elif selection == '7':
        try:
            
            d_temp = input('Please input Driver Temp: ')
            p_temp = input('Please input Passenger Temp: ')
            
            vehicles[0].sync_wake_up()
            vehicles[0].command('CHANGE_CLIMATE_TEMPERATURE_SETTING', driver_temp=d_temp, passenver_temp=p_temp)
            clear()
            print('-----------------------------------------------------')
            print('Success: ' + vehicle_state.get('vehicle_name') + ' Temperature Set')
            print('Driver Temp:'+d_temp)
            print('Passenger Temp:'+p_temp)
            print('-----------------------------------------------------')           

        except teslapy.HTTPError as e:
            print(e)
            pass

    elif selection == '8':
        try:
            charge_limit = input('Please input charge limit %:')
            
            vehicles[0].sync_wake_up()
            vehicles[0].command('CHANGE_CHARGE_LIMIT', percent=charge_limit)
            clear()
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')
            print('Success: ' + vehicle_state.get('vehicle_name') + ' Charge Limit Set to: '+charge_limit+'%')
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')

        except teslapy.HTTPError as e:
            print(e)
            pass

    elif selection == '9':
        try:
            if vehicle_state.get('fd_window')==1:

                vehicles[0].sync_wake_up()
                vehicles[0].command('WINDOW_CONTROL', command='close')
                clear()
                print('-----------------------------------------------------')
                print('-----------------------------------------------------')
                print('Success: ' + vehicle_state.get('vehicle_name') + ' Windows Closed:')
                print('-----------------------------------------------------')
                print('-----------------------------------------------------')
                #wait for the car to update status n shit
                sleep(3)
              
                
            else:
                vehicles[0].sync_wake_up()
                vehicles[0].command('WINDOW_CONTROL', command='vent')
                clear()
                print('-----------------------------------------------------')
                print('-----------------------------------------------------')
                print('Success: ' + vehicle_state.get('vehicle_name') + ' Windows Vented:')
                print('-----------------------------------------------------')
                print('-----------------------------------------------------')
                #also waiting for status update
                sleep(3)
                
                
        except teslapy.HTTPError as e:
            print(e)
            pass

    elif selection == '10':
        try:
            vehicles[0].sync_wake_up()
            vehicles[0].command('ACTUATE_TRUNK', which_trunk='front')
            clear()
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')
            print('Success: ' + vehicle_state.get('vehicle_name') + ' Frunk Unlocked')
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')

        except teslapy.HTTPError as e:
            print(e)
            pass

    elif selection == '11':
        try:
            vehicles[0].sync_wake_up()
            vehicles[0].command('ACTUATE_TRUNK', which_trunk='rear')
            clear()
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')
            print('Success: ' + vehicle_state.get('vehicle_name') + ' Trunk Unlocked')
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')

        except teslapy.HTTPError as e:
            print(e)
            pass
            
    elif selection == '12':
        try:
            vehicles[0].sync_wake_up()
            vehicles[0].command('REMOTE_START', password=PASSWORD)
            clear()
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')
            print('Success: ' + vehicle_state.get('vehicle_name') + ' Remotely Started')
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')

        except teslapy.HTTPError as e:
            print(e)
            pass
            
    elif selection == '13':
        try:
            vehicles[0].sync_wake_up()
            vehicles[0].command('TRIGGER_HOMELINK', lat=drive_state.get('latitude'),lon=drive_state.get('longitude'))
            clear()
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')
            print('Success:  ' + vehicle_state.get('vehicle_name') + ' Triggered Homelink')
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')

        except teslapy.HTTPError as e:
            print(e)
            pass
            
    elif selection == '14':
        try:
            if charge_state.get('charge_port_door_open')==True:

                vehicles[0].sync_wake_up()
                vehicles[0].command('CHARGE_PORT_DOOR_CLOSE')
                clear()
                print('-----------------------------------------------------')
                print('-----------------------------------------------------')
                print('Success: ' + vehicle_state.get('vehicle_name') + ' Charge Port Closed:')
                print('-----------------------------------------------------')
                print('-----------------------------------------------------')
                sleep(3)
              
                
            else:
                vehicles[0].sync_wake_up()
                vehicles[0].command('CHARGE_PORT_DOOR_OPEN')
                clear()
                print('-----------------------------------------------------')
                print('-----------------------------------------------------')
                print('Success: ' + vehicle_state.get('vehicle_name') + ' Charge Port Opened:')
                print('-----------------------------------------------------')
                print('-----------------------------------------------------')
                sleep(3)
                
                
        except teslapy.HTTPError as e:
            print(e)
            pass
            
    elif selection == '15':
        try:
            if charge_state.get('charging_state')=="Disconnected":
                
                print('-----------------------------------------------------')
                print('-----------------------------------------------------')
                print('Error: ' + vehicle_state.get('vehicle_name') + ' is not connected to charger.')
                print('-----------------------------------------------------')
                print('-----------------------------------------------------')
                
            elif charge_state.get('charging_state')=="Charging":

                vehicles[0].sync_wake_up()
                vehicles[0].command('STOP_CHARGE')
                clear()
                print('-----------------------------------------------------')
                print('-----------------------------------------------------')
                print('Success: ' + vehicle_state.get('vehicle_name') + ' Charging Stopped.')
                print('-----------------------------------------------------')
                print('-----------------------------------------------------')
                sleep(3)
              
                
            else:
                vehicles[0].sync_wake_up()
                vehicles[0].command('START_CHARGE')
                clear()
                print('-----------------------------------------------------')
                print('-----------------------------------------------------')
                print('Success: ' + vehicle_state.get('vehicle_name') + ' Charging Started.')
                print('-----------------------------------------------------')
                print('-----------------------------------------------------')
                sleep(3)
                
                
        except teslapy.HTTPError as e:
            print(e)
            pass
            
    elif selection == '16':
        try:
            if vehicle_state.get('sentry_mode')==False:

                vehicles[0].sync_wake_up()
                vehicles[0].command('SET_SENTRY_MODE', on='true')
                clear()
                print('-----------------------------------------------------')
                print('-----------------------------------------------------')
                print('Success: ' + vehicle_state.get('vehicle_name') + ' Enabled Sentry Mode')
                print('-----------------------------------------------------')
                print('-----------------------------------------------------')
                #wait for the car to update status n shit
                sleep(3)
              
                
            else:
                vehicles[0].sync_wake_up()
                vehicles[0].command('SET_SENTRY_MODE', on='false')
                clear()
                print('-----------------------------------------------------')
                print('-----------------------------------------------------')
                print('Success: ' + vehicle_state.get('vehicle_name') + ' Disabled Sentry Mode')
                print('-----------------------------------------------------')
                print('-----------------------------------------------------')
                #also waiting for status update
                sleep(3)
                
                
        except teslapy.HTTPError as e:
            print(e)
            pass
            
    elif selection == '17':
        try:
            vehicles[0].sync_wake_up()
            clear()
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')
            print(vehicles[0].command('DEACTIVATE_DEVICE_TOKEN', device_token=vehicles[0].get_vehicle_data('tokens[0]')))
            #print(charge_state.get('charge_port_door_open'))
            #print(dataloaded.get('drive_state'))
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')

        except teslapy.HTTPError as e:
            print(e)
            pass

    elif selection == '18':
        try:
            vehicles[0].sync_wake_up()
            clear()
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')
            #print(vehicles[0].get_vehicle_data())
            #print(charge_state.get('charge_port_door_open'))
            #print(dataloaded.get('drive_state'))
            print(vehicles[0].get_vehicle_data('tokens'))
            print('-----------------------------------------------------')
            print('-----------------------------------------------------')

        except teslapy.HTTPError as e:
            print(e)
            pass