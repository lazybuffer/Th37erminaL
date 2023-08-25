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
from colorama import init, Fore

# printing program start message
# print("\nProgram Start!\n")

# # some colors
# init()
# GREEN = Fore.GREEN
# RESET = Fore.RESET
# GRAY = Fore.LIGHTBLACK_EX

# manual text colored
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# flag variable to print the dots and it's value increases inside the while loop.
flag = 1
print(" ")

# clear terminal when its starting 
os.system("clear")

# To print the dots we use while loop. In total, 4 dots will be printed.
while flag < 20:
    print(bcolors.BOLD+bcolors.WARNING+f"\r  Th37erminaL{('.' * flag)} ", end=" "+bcolors.ENDC)
    time.sleep(0.2)
    flag = flag + 1
print(" ")
# after loading terminal then clear
os.system("clear")

# main loop function...
Th37erminaL = True 
while Th37erminaL:
    # banner  
    # print("")
    # print(os.system("cat assets/banner/banner.txt"))
    # # print("")
    
    # logo decoration
    random_obj = ["[ HACKER ]", "[ H4CK3R ]", "[ H@CKE4 ]"]
    print(bcolors.HEADER+'''

     #######         #####  #######                                      #       
        #    #    #       # #    #  ###### #####  #    # # #    #   ##   #       
        #    #    #       #     #   #      #    # ##  ## # ##   #  #  #  #       
        #    ######  #####     #    #####  #    # # ## # # # #  # #    # #       
        #    #    #       #   #     #      #####  #    # # #  # # ###### #       
        #    #    #       #   #     #      #   #  #    # # #   ## #    # #       
        #    #    #  #####    #     ###### #    # #    # # #    # #    # #######
                                                
        '''+bcolors.ENDC+bcolors.BOLD+bcolors.OKBLUE+random.choice(random_obj)+bcolors.ENDC)
    print(" ")
    
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
        print(bcolors.BOLD+bcolors.OKGREEN+"Music will repeat after 1sec.."+bcolors.ENDC)
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
    commands=input(
        bcolors.FAIL+bcolors.BOLD+"1."+bcolors.ENDC+bcolors.BOLD+bcolors.OKGREEN+" IP Address Tracker"+bcolors.ENDC+
        bcolors.FAIL+bcolors.BOLD+"\n2."+bcolors.ENDC+bcolors.BOLD+bcolors.OKGREEN+" GPS Tracking using img file\n"+bcolors.ENDC+
        bcolors.FAIL+bcolors.BOLD+"3."+bcolors.ENDC+bcolors.BOLD+bcolors.OKGREEN+" PINCode Tracking\n"+bcolors.ENDC+
        bcolors.FAIL+bcolors.BOLD+"4."+bcolors.ENDC+bcolors.BOLD+bcolors.OKGREEN+" Find target location"+bcolors.ENDC+
        bcolors.FAIL+bcolors.BOLD+"\n5."+bcolors.ENDC+bcolors.BOLD+bcolors.OKGREEN+" Exit Terminal\n"+bcolors.ENDC+
        bcolors.FAIL+bcolors.BOLD+"6."+bcolors.ENDC+bcolors.BOLD+bcolors.OKGREEN+" Clear Terminal\n\n"+bcolors.ENDC
        +bcolors.FAIL+bcolors.BOLD+"options>_ "+bcolors.ENDC
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
        print(bcolors.BOLD+bcolors.WARNING+"\nInvalid Commands!\n"+bcolors.ENDC)
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
        input(bcolors.BOLD+bcolors.OKGREEN+"Music..On Enter for Off.."+bcolors.ENDC)
        p.terminate()
        p.kill()
        print(bcolors.BOLD+bcolors.OKGREEN+"Music off\n\n"+bcolors.ENDC)
    # elif commands is 5 then terminal will exit
    elif commands == str(5):
        print(bcolors.BOLD+bcolors.OKGREEN+"\nTerminal Exiting..within 3min...\n"+bcolors.ENDC)
        time.sleep(3)
        os.system("clear")
        break
    # elif commands is 5 then terminal will clear
    elif commands == str(6):
        print(bcolors.BOLD+bcolors.OKGREEN+"\nTerminal Will Clear...within 2min..\n"+bcolors.ENDC)
        time.sleep(2)
        os.system("clear")
        continue
    
    # elif commands is 1 then ip address tracking logic will work
    elif commands == str(1):
        # get the ip address from the command line
        try:
            ip_address = str(input(bcolors.BOLD+bcolors.OKGREEN+"\nEnter Your IP Address = "+bcolors.ENDC)).lower()
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
                print(bcolors.BOLD+bcolors.OKGREEN+f"{key}: {value}"+bcolors.ENDC, file=file)
            file.close()
        
        # this section is display output in terminal
        print(" ")
        for key, value in details:
                print(bcolors.BOLD+bcolors.OKGREEN+f"{key}: {value}"+bcolors.ENDC)
        print(" ")
        
        time.sleep(15)
        # clear terminal 
        os.system("clear")
        continue
        
    # elif commands is 2 then tracking gpsphoto location logic will work
    elif commands == str(2):
        # image file path as user input
        filename = str(input(bcolors.BOLD+bcolors.OKGREEN+"\nEnter Your image path = "+bcolors.ENDC)).lower()
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
            print(bcolors.BOLD+bcolors.OKGREEN+"initializing.. file"+bcolors.ENDC)
            time.sleep(1)
           
            text = re.split("[}{':, ]", str(details))
            print(bcolors.BOLD+bcolors.OKGREEN+f"{text}"+bcolors.ENDC, file=file)
            
            file.close()
            print(bcolors.BOLD+bcolors.OKGREEN+"\nfile closed! and output saved in a txt file.\n"+bcolors.ENDC)
            # print image details
            print(bcolors.BOLD+bcolors.OKGREEN+f"{details}"+bcolors.ENDC)
            print(" ")
            
            time.sleep(5)
            # clear terminal
            os.system("clear")
            continue
        
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
        
        try:
            # Zipcode input
            zipcode = str(input(bcolors.BOLD+bcolors.OKGREEN+"\n\nEnter Your ZiPincode = "+bcolors.ENDC)).lower()
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
            print(bcolors.BOLD+bcolors.OKGREEN+"Zipcode:",zipcode+bcolors.ENDC)
            print(bcolors.BOLD+bcolors.OKGREEN+"Details of the Zipcode:"+bcolors.ENDC)
            print(bcolors.BOLD+bcolors.OKGREEN+f"{location}"+bcolors.ENDC)
            print(" ")
            
            time.sleep(20)
            # clear terminal
            os.system("clear")
            continue

        except Exception as Traceback:
            # invalid_alert_sound function value
            invalid_alert_sound = Value("i", 1)
            # multiprcess handling mp3 file
            p = Process(target=invalid_tasks, args=(invalid_alert_sound,))
            # start multiprocess
            p.start()
            # message invalid commands
            print(bcolors.BOLD+bcolors.WARNING+"\nInvalid Commands!\n"+bcolors.ENDC)
            # stop music
            time.sleep(3)
            p.terminate()
            p.kill()
            
            # clear terminal
            os.system("clear")
            continue

    # elif commands is 4 then find target location logic will work
    elif commands == str(4):
        print(bcolors.BOLD+bcolors.OKGREEN+"\nFinding target location using\nYour stored data files"+bcolors.ENDC)
        
        ip_traced_data_filename = "traced_ip_details/traced_ip_details.txt"
        gps_data_filename = "img_gps_details/img_gps_details.txt"
        
        target_data_input = str(input(bcolors.BOLD+bcolors.OKGREEN+"\nselect stored data location [ ip data, image gps data ] == "+bcolors.ENDC)).lower()
        
        if target_data_input != "ip data" and target_data_input != "image gps data":
            # invalid_alert_sound function value
            invalid_alert_sound = Value("i", 1)
            # multiprcess handling mp3 file
            p = Process(target=invalid_tasks, args=(invalid_alert_sound,))
            # start multiprocess
            p.start()
            # message invalid commands
            print(bcolors.BOLD+bcolors.WARNING+"\nInvalid Commands!\n"+bcolors.ENDC)
            # stop music
            time.sleep(3)
            p.terminate()
            p.kill()
            
            # clear terminal
            os.system("clear")
            continue
        
        elif target_data_input == "ip data":
            with open(ip_traced_data_filename, "r") as f:

                for lines in f:
                    print(bcolors.BOLD+bcolors.OKGREEN+"\nTarget data is display in your Terminal..within 3min...\n"+bcolors.ENDC)
                    time.sleep(3)
                    # print(lines)
                    print(os.system(bcolors.BOLD+bcolors.OKGREEN+"cat traced_ip_details/traced_ip_details.txt"+bcolors.ENDC))
                    
                    # target initiated program
                    print(bcolors.BOLD+bcolors.OKGREEN+"Target is initiated within 4min....\n"+bcolors.ENDC)
                    time.sleep(4)
                    
                    # folium module for map content
                    folium_map = folium.Map()
                    
                    try:
                        # pass
                        # get input of latitude cords
                        lati = float(input(bcolors.BOLD+bcolors.OKGREEN+"Enter Target Latitude  == "+bcolors.ENDC))
                        # get input of longitude cords
                        long = float(input(bcolors.BOLD+bcolors.OKGREEN+"Enter Target Longitude  == "+bcolors.ENDC))
                        # get input of location addr
                        address_name = input(bcolors.BOLD+bcolors.OKGREEN+"Address Name / IP Address == "+bcolors.ENDC).lower()
                    except:
                        # pass
                        # invalid_alert_sound function value
                        invalid_alert_sound = Value("i", 1)
                        # multiprcess handling mp3 file
                        p = Process(target=invalid_tasks, args=(invalid_alert_sound,))
                        # start multiprocess
                        p.start()
                        # message invalid commands
                        print(bcolors.BOLD+bcolors.WARNING+"\nInvalid Commands!\n"+bcolors.ENDC)
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
                    
                    print(bcolors.BOLD+bcolors.OKGREEN+"\nfinished within 5min....."+bcolors.ENDC)
                    
    
                    # python object(dictionary) to be dumped as
                    try:
                        dump_data ={ 
                            address_name: { 
                                "ip": address_name, 
                                "latitude": lati, 
                                "longitude": long, 
                            }
                        }
                        
                        print(bcolors.BOLD+bcolors.OKGREEN+"\nfile opening..here\n"+bcolors.ENDC)
                        
                        randnum = random.randint(1, 1000)
                        data_filename = f"dump_data/data{randnum}.json"
                        
                        print(bcolors.BOLD+bcolors.OKGREEN+"process 1st statement.."+bcolors.ENDC)
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
                    
                    print(bcolors.BOLD+bcolors.OKGREEN+"\nTarget is located.... see the output [ run target_location.html file in your browser. ]\n"+bcolors.ENDC)
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
                    print(bcolors.BOLD+bcolors.OKGREEN+"\nTarget data is display in your Terminal..within 3min...\n"+bcolors.ENDC)
                    time.sleep(3)
                    print(bcolors.BOLD+bcolors.OKGREEN+f"{data}"+bcolors.ENDC)
                    
                    # target initiated program
                    print(bcolors.BOLD+bcolors.OKGREEN+"Target is initiated within 4min...."+bcolors.ENDC)
                    time.sleep(4)
                    
                    # folium module for map content
                    folium_map = folium.Map()
                    
                    try:
                        # pass
                        # get input of latitude cords
                        lati = float(input(bcolors.BOLD+bcolors.OKGREEN+"Enter Target Latitude  == "+bcolors.ENDC))
                        # get input of longitude cords
                        long = float(input(bcolors.BOLD+bcolors.OKGREEN+"Enter Target Longitude  == "+bcolors.ENDC))
                        # get input of location addr
                        address_name = input(bcolors.BOLD+bcolors.OKGREEN+"Address Name / IP Address == "+bcolors.ENDC).lower()
                    except:
                        # pass
                        # invalid_alert_sound function value
                        invalid_alert_sound = Value("i", 1)
                        # multiprcess handling mp3 file
                        p = Process(target=invalid_tasks, args=(invalid_alert_sound,))
                        # start multiprocess
                        p.start()
                        # message invalid commands
                        print(bcolors.BOLD+bcolors.WARNING+"\nInvalid Commands!\n"+bcolors.ENDC)
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
                    
                    print(bcolors.BOLD+bcolors.OKGREEN+"\nfinished within 5min....."+bcolors.ENDC)
                    
                    
                    # python object(dictionary) to be dumped as
                    try:
                        dump_data ={ 
                            address_name: { 
                                "ip": address_name, 
                                "latitude": lati, 
                                "longitude": long, 
                            }
                        }
                        
                        print(bcolors.BOLD+bcolors.OKGREEN+"\nfile opening..here\n"+bcolors.ENDC)
                        
                        randnum = random.randint(1, 1000)
                        data_filename = f"dump_data/data{randnum}.json"
                        
                        print(bcolors.BOLD+bcolors.OKGREEN+"process 1st statement.."+bcolors.ENDC)
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
                    print(bcolors.BOLD+bcolors.OKGREEN+"\nTarget is located.... see the output [ run target_location.html file in your browser. ]\n"+bcolors.ENDC)
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
            print(bcolors.BOLD+bcolors.WARNING+"\nInvalid Commands!\n"+bcolors.ENDC)
            # stop music
            time.sleep(3)
            p.terminate()
            p.kill()
            
            # clear terminal 
            os.system("clear")
            continue
    else:
        # invalid_alert_sound function value
        invalid_alert_sound = Value("i", 1)
        # multiprcess handling mp3 file
        p = Process(target=invalid_tasks, args=(invalid_alert_sound,))
        # start multiprocess
        p.start()
        # message invalid commands
        print(bcolors.BOLD+bcolors.WARNING+"\nInvalid Commands!\n"+bcolors.ENDC)
        # stop music
        time.sleep(3)
        p.terminate()
        p.kill()
        
        # clear terminal 
        os.system("clear")
        continue
