# Importing required module
import ipinfo
import sys,os,subprocess
import socket
import json, re, random
import time
from GPSPhoto import gpsphoto
from geopy.geocoders import Nominatim
import folium
from folium import plugins
import multiprocessing
from multiprocessing import Process, Value
from time import sleep
from playsound import playsound


# '''
# #######                                      #       
# #    #  ###### #####  #    # # #    #   ##   #       
#     #   #      #    # ##  ## # ##   #  #  #  #       
#    #    #####  #    # # ## # # # #  # #    # #       
#   #     #      #####  #    # # #  # # ###### #       
#   #     #      #   #  #    # # #   ## #    # #       
#   #     ###### #    # #    # # #    # #    # #######

# '''

# printing program start message
# print("\nProgram Start!\n")
# flag variable to print the dots and it's value increases inside the while loop.
flag = 1
print(" ")
# To print the dots we use while loop. In total, 4 dots will be printed.
while flag < 20:
    print(f"\r7erminaL is loading [ {('.' * flag)} ]", end=" ")
    time.sleep(0.1)
    flag = flag + 1
print(" ")
# after loading terminal then clear
os.system("clear")

# main loop function...
Terminal = True 
while Terminal:
    # banner
    print("")
    print(os.system("cat assets/banner/banner.txt"))
    print("")
    # play music with this "loading_done" function
    def loading_done():
        playsound("assets/bullet_shell_fall.mp3")
        sleep(1)
    # run play object using this "done" function
    def done(do):
        while True:
            if do.value:
                loading_done()
    # end music function!!
    
    
    # play music with this "do_work" function
    def do_work():
        playsound("blessthefall.mp3")
        print("Music will repeat after 1sec..")
        sleep(1)
    # run play object using this "worker" function
    def worker(run):
        while True:
            if run.value:
                do_work()
    # end music function!!
    
    
    # play sound when tasks is done with this "ip_trace_tasks" function
    def play_sound_done_tasks():
        playsound("assets/gunfire.mp3")
        # print("Music will play after 1sec..")
        sleep(1)
    # play object using this "trace_tasks" function
    def done_tasks(done_sound):
        while True:
            if done_sound.value:
                play_sound_done_tasks()
    # end music function!!
    
    # play sound when commands are invalid with "invalid_alert_tasks" function
    def invalid_alert_tasks():
        playsound("assets/invalid_cmand_beep-beep-6151.mp3")
        # print("Music will play after 1sec..")
        sleep(1)
    
    # play object using this "invalid_alert_sound_tasks" function
    def invalid_tasks(invalid_alert_sound):
        while True:
            if invalid_alert_sound.value:
                invalid_alert_tasks()
    # end music function
    
    # this section is starting the whole program by this sound statements
    # done_sound function value
    do = Value("i", 1)
    # multiprcess handling mp3 file
    p = Process(target=done, args=(do,))
    # start multiprocess
    p.start()
        
    # stop music
    time.sleep(2)
    p.terminate()
    p.kill()
    
    # naviget options by user commands
    commands = input(
        "1. IP Address Tracker\n2. GPS Tracking using img file\n3. PINCode Tracking\n"+
        "4. Find target location\n5. Exit Terminal\n6. Clear Terminal\n\noptions>_ "
        )
    
    # if user input commands are not equal or string numbers are above 6 then this statements work.
    if commands > str(6) and commands != commands:
                
        # invalid_alert_sound function value
        invalid_alert_sound = Value("i", 1)
        # multiprcess handling mp3 file
        p = Process(target=invalid_tasks, args=(invalid_alert_sound,))
        # start multiprocess
        p.start()
        # message invalid commands
        print("\nInvalid Commands!\n")
        # stop music
        time.sleep(3)
        p.terminate()
        p.kill()
        
        # clear terminal 
        os.system("clear")
        continue
    
    # elif commands is 0 then music function ( above functions near starting while loop ) will work
    elif commands == str(0):
        # run function value
        run = Value("i", 1)
        # multiprcess handling mp3 file
        p = Process(target=worker, args=(run,))
        # start multiprocess
        p.start()
        
        # stop music
        input("Music..On Enter for Off..")
        p.terminate()
        p.kill()
        print("Music off\n\n")
    # elif commands is 5 then terminal will exit
    elif commands == str(5):
        print("\nTerminal Exiting..within 3min...\n")
        time.sleep(3)
        os.system("clear")
        break
    # elif commands is 5 then terminal will clear
    elif commands == str(6):
        print("\nTerminal Will Clear...within 2min..\n")
        time.sleep(2)
        os.system("clear")
        continue
    # elif commands is 1 then ip address tracking logic will work
    elif commands == str(1):
        # get the ip address from the command line
        try:
            ip_address = str(input("\nEnter Your IP Address = ")).lower()
        except IndexError:
            ip_address = None
        # access token for ipinfo.io
        access_token = '1b03fdb5ae3ab3' # your access token [ ipinfo.io you can access from there ]
        # create a client object with the access token
        handler = ipinfo.getHandler(access_token)
        # get the ip info
        details = handler.getDetails(ip_address).all.items()
        
        # done_sound function value
        done_sound = Value("i", 1)
        # multiprcess handling mp3 file
        p = Process(target=done_tasks, args=(done_sound,))
        # start multiprocess
        p.start()
        
        # stop music
        time.sleep(2)
        p.terminate()
        p.kill()
        
        # saving output the ip info
        with open("traced_ip_details/traced_ip_details.txt", "w") as file:
            for key, value in details:
                print(f"{key}: {value}", file=file)
            file.close()
        
        # this section is display output in terminal
        print(" ")
        for key, value in details:
                print(f"{key}: {value}")
        print(" ")
        
    # elif commands is 2 then tracking gpsphoto location logic will work
    elif commands == str(2):
        # image file path as user input
        filename = str(input("\nEnter Your image path = ")).lower()
        # getting image data usng gpsphoto
        details = gpsphoto.getGPSData(filename)
        
        # done_sound function value
        done_sound = Value("i", 1)
        # multiprcess handling mp3 file
        p = Process(target=done_tasks, args=(done_sound,))
        # start multiprocess
        p.start()
        
        # stop music
        time.sleep(2)
        p.terminate()
        p.kill()
                
        file = open("img_gps_details/img_gps_details.txt", "w")
        if file:
            print(" ")
            print("initializing.. file")
            time.sleep(1)
           
            text = re.split("[}{':, ]", str(details))
            print(text, file=file)
            
            file.close()
            print("\nfile closed! and output saved in a txt file.\n")
            # print image details
            print(details)
            print(" ")
        
        # else:
        #     print("file does't exists...")
        #     time.sleep(1)
        #     print("creating file.. as img_gps_details/img_gps_details.txt")
        #     os.system("touch img_gps_details/img_gps_details.txt")
        #     time.sleep(1)
        #     print("created.. run again program!")
        #     break

    # elif commands is 3 then pincode tracking logic will work
    elif commands == str(3):
        # Using Nominatim Api
        geolocator = Nominatim(user_agent="geoapiExercises")
        # Zipcode input
        zipcode = str(input("\nEnter Your ZiPincode = ")).lower()
        # Using geocode()
        location = geolocator.geocode(zipcode)
        
        # done_sound function value
        done_sound = Value("i", 1)
        # multiprcess handling mp3 file
        p = Process(target=done_tasks, args=(done_sound,))
        # start multiprocess
        p.start()
        
        # stop music
        time.sleep(2)
        p.terminate()
        p.kill()
        
        # Displaying address details
        print(" ")
        print("Zipcode:",zipcode)
        print("Details of the Zipcode:")
        print(location)
        print(" ")

    # elif commands is 4 then find target location logic will work
    elif commands == str(4):
        print("\nFinding target location using\nYour stored data files")
        
        ip_traced_data_filename = "traced_ip_details/traced_ip_details.txt"
        gps_data_filename = "img_gps_details/img_gps_details.txt"
        
        target_data_input = str(input("\nselect stored data location [ ip data, image gps data ] == ")).lower()
        
        if target_data_input != "ip data" and target_data_input != "image gps data":
            # invalid_alert_sound function value
            invalid_alert_sound = Value("i", 1)
            # multiprcess handling mp3 file
            p = Process(target=invalid_tasks, args=(invalid_alert_sound,))
            # start multiprocess
            p.start()
            # message invalid commands
            print("\nInvalid Commands!\n")
            # stop music
            time.sleep(3)
            p.terminate()
            p.kill()
            continue
        
        elif target_data_input == "ip data":
            with open(ip_traced_data_filename, "r") as f:

                for lines in f:
                    print("\nTarget data is display in your Terminal..within 3min...\n")
                    time.sleep(3)
                    # print(lines)
                    print(os.system("cat traced_ip_details/traced_ip_details.txt"))
                    
                    # target initiated program
                    print("Target is initiated within 4min....\n")
                    time.sleep(4)
                    
                    # folium module for map content
                    folium_map = folium.Map()
                    
                    try:
                        # pass
                        # get input of latitude cords
                        lati = float(input("Enter Target Latitude  == "))
                        # get input of longitude cords
                        long = float(input("Enter Target Longitude == "))
                        # get input of location addr
                        address_name = input("Address Name / IP Address == ").lower()
                    except:
                        # pass
                        # invalid_alert_sound function value
                        invalid_alert_sound = Value("i", 1)
                        # multiprcess handling mp3 file
                        p = Process(target=invalid_tasks, args=(invalid_alert_sound,))
                        # start multiprocess
                        p.start()
                        # message invalid commands
                        print("\nInvalid Commands!\n")
                        # stop music
                        time.sleep(3)
                        p.terminate()
                        p.kill()
                        break
                    
                    
                    # Latitude, Longitude
                    LOCATION_DATA = [
                        (lati, long)
                        # ("41.90093256", "12.48331626")
                        # ("41.89018285", "12.49235900"),
                        # ("41.89868519", "12.47684474"),
                        # ("41.89454167", "12.48303163"),
                        # ("41.90226256", "12.45739340"),
                        # ("41.90269661", "12.46635787"),
                        # ("41.91071023", "12.47635640"),
                        # ("41.90266442", "12.49624457")
                    ]
                    for cords in LOCATION_DATA:
                        folium.Marker(location=[cords[0], cords[1]]).add_to(folium_map)

                    # folium_map = folium.Map(location=[LOCATION_DATA[0][0], LOCATION_DATA[1][1]], )
                    south_west_corner = min(LOCATION_DATA)
                    north_east_corner = max(LOCATION_DATA)
                    folium_map.fit_bounds([south_west_corner, north_east_corner])

                    LOCATION_NAMES = [
                        address_name
                        # "Trevi Fountain"
                        # "Colosseum",
                        # "Pantheon",
                        # "Piazza Venezia",
                        # "St. Peter's Square",
                        # "Mausoleum of Hadrian",
                        # "Piazza del Popolo",
                        # "Fountain of the Naiads"
                    ]

                    for cords, name in zip(LOCATION_DATA, LOCATION_NAMES):
                        folium.Marker(location=[cords[0], cords[1]],
                                    popup=f"Lattitude:<br>{cords[0]}<br>"
                                            f"Longitude:<br>{cords[1]}<br>"
                                            f"Name:<br>{name}"
                                    ).add_to(folium_map)
                    
                    print("\nfinished within 5min.....")
                    
    
                    # python object(dictionary) to be dumped as
                    try:
                        dump_data ={ 
                            address_name: { 
                                "ip": address_name, 
                                "latitude": lati, 
                                "longitude": long, 
                            }
                        }
                        
                        print("\nfile opening..here\n")
                        
                        randnum = random.randint(1, 1000)
                        data_filename = f"dump_data/data{randnum}.json"
                        
                        print("process 1st statement..")
                        with open(data_filename, mode="w", encoding='utf-8') as final:
                            json.dump(dump_data, final, indent=5)
                            final.close()
                        #
                        # new_data = {"ip":address_name, "latitude":lati, "long":long}
                        # with open(data_filename, mode="r", encoding='utf-8') as feedsjson:
                        #     load_it = json.load(feedsjson)
                        #     load_it[address_name].append(new_data)
                        #     with open(data_filename, mode="w", encoding='utf-8') as final:
                        #         json.dump(new_data, final, indent=5)
                    except:
                        pass
                    
                    
                    # output_data = open("dump_data/data.json", mode="w")
                    # json.dump(dump_data, output_data, indent=5)
                    # output_data.close()
                    
                    time.sleep(5)
                    
                    print("\nTarget is located.... see the output [ run target_location.html file in your browser. ]\n")
                    folium_map.save("target_location.html")
                    
                    # done_sound function value
                    done_sound = Value("i", 1)
                    # multiprcess handling mp3 file
                    p = Process(target=done_tasks, args=(done_sound,))
                    # start multiprocess
                    p.start()
                    
                    # stop music
                    time.sleep(2)
                    p.terminate()
                    p.kill()
                    break
        elif target_data_input == "image gps data":
            with open(gps_data_filename, "r") as f:
                line = f.readlines()

                for i in line:
                    data = i.replace(",", " ")
                    print("\nTarget data is display in your Terminal..within 3min...\n")
                    time.sleep(3)
                    print(data)
                    
                    # target initiated program
                    print("Target is initiated within 4min....")
                    time.sleep(4)
                    
                    # folium module for map content
                    folium_map = folium.Map()
                    
                    try:
                        # pass
                        # get input of latitude cords
                        lati = float(input("Enter Target Latitude  == "))
                        # get input of longitude cords
                        long = float(input("Enter Target Longitude == "))
                        # get input of location addr
                        address_name = input("Address Name / IP Address == ").lower()
                    except:
                        # pass
                        # invalid_alert_sound function value
                        invalid_alert_sound = Value("i", 1)
                        # multiprcess handling mp3 file
                        p = Process(target=invalid_tasks, args=(invalid_alert_sound,))
                        # start multiprocess
                        p.start()
                        # message invalid commands
                        print("\nInvalid Commands!\n")
                        # stop music
                        time.sleep(3)
                        p.terminate()
                        p.kill()
                        break
                    
                    # Latitude, Longitude
                    LOCATION_DATA = [
                        (lati, long)
                        # ("41.90093256", "12.48331626")
                        # ("41.89018285", "12.49235900"),
                        # ("41.89868519", "12.47684474"),
                        # ("41.89454167", "12.48303163"),
                        # ("41.90226256", "12.45739340"),
                        # ("41.90269661", "12.46635787"),
                        # ("41.91071023", "12.47635640"),
                        # ("41.90266442", "12.49624457")
                    ]
                    for cords in LOCATION_DATA:
                        folium.Marker(location=[cords[0], cords[1]]).add_to(folium_map)

                    # folium_map = folium.Map(location=[LOCATION_DATA[0][0], LOCATION_DATA[1][1]], )
                    south_west_corner = min(LOCATION_DATA)
                    north_east_corner = max(LOCATION_DATA)
                    folium_map.fit_bounds([south_west_corner, north_east_corner])

                    LOCATION_NAMES = [
                        address_name
                        # "Trevi Fountain"
                        # "Colosseum",
                        # "Pantheon",
                        # "Piazza Venezia",
                        # "St. Peter's Square",
                        # "Mausoleum of Hadrian",
                        # "Piazza del Popolo",
                        # "Fountain of the Naiads"
                    ]

                    for cords, name in zip(LOCATION_DATA, LOCATION_NAMES):
                        folium.Marker(location=[cords[0], cords[1]],
                                    popup=f"Lattitude:<br>{cords[0]}<br>"
                                            f"Longitude:<br>{cords[1]}<br>"
                                            f"Name:<br>{name}"
                                    ).add_to(folium_map)
                    
                    print("\nfinished within 5min.....")
                    
                    
                    # python object(dictionary) to be dumped as
                    try:
                        dump_data ={ 
                            address_name: { 
                                "ip": address_name, 
                                "latitude": lati, 
                                "longitude": long, 
                            }
                        }
                        
                        print("\nfile opening..here\n")
                        
                        randnum = random.randint(1, 1000)
                        data_filename = f"dump_data/data{randnum}.json"
                        
                        print("process 1st statement..")
                        with open(data_filename, mode="w", encoding='utf-8') as final:
                            json.dump(dump_data, final, indent=5)
                            final.close()
                        #
                        # new_data = {"ip":address_name, "latitude":lati, "long":long}
                        # with open(data_filename, mode="r", encoding='utf-8') as feedsjson:
                        #     load_it = json.load(feedsjson)
                        #     load_it[address_name].append(new_data)
                        #     with open(data_filename, mode="w", encoding='utf-8') as final:
                        #         json.dump(new_data, final, indent=5)
                    except:
                        pass
                    
                    time.sleep(5)
                    print("\nTarget is located.... see the output [ run target_location.html file in your browser. ]\n")
                    folium_map.save("target_location.html")
                    # done_sound function value
                    done_sound = Value("i", 1)
                    # multiprcess handling mp3 file
                    p = Process(target=done_tasks, args=(done_sound,))
                    # start multiprocess
                    p.start()
                    
                    # stop music
                    time.sleep(2)
                    p.terminate()
                    p.kill()
                    break
        else:
            # invalid_alert_sound function value
            invalid_alert_sound = Value("i", 1)
            # multiprcess handling mp3 file
            p = Process(target=invalid_tasks, args=(invalid_alert_sound,))
            # start multiprocess
            p.start()
            # message invalid commands
            print("\nInvalid Commands!\n")
            # stop music
            time.sleep(3)
            p.terminate()
            p.kill()
            continue
    else:
        # invalid_alert_sound function value
        invalid_alert_sound = Value("i", 1)
        # multiprcess handling mp3 file
        p = Process(target=invalid_tasks, args=(invalid_alert_sound,))
        # start multiprocess
        p.start()
        # message invalid commands
        print("\nInvalid Commands!\n")
        # stop music
        time.sleep(3)
        p.terminate()
        p.kill()
        
        # clear terminal 
        os.system("clear")
        continue