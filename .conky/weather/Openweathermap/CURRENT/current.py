# Lock file to tell conky that the script is running
lock_file = "/tmp/script_owmcurrent.lock"
# Check for file lock
try:
    open(lock_file, 'w').close()
    import os, sys
    from PIL import Image
    import requests
    import time
    import urllib.request
    # import module GEOPY
    from geopy.geocoders import Photon
    # initialize Nominatim API or Photon API
    geolocator = Photon(user_agent="measurements")
    ################################ my API url forecast (insert it between apostrophe, DON'T delete apostrophes)
    # set latitude, longitude and APPID
    mylat = 45.80125
    mylon = 11.90124
    myAPPID = ''
    url_current = 'https://api.openweathermap.org/data/2.5/weather?lat=' + str(mylat) + '&lon=' + str(mylon) + '&units=metric&appid=' + myAPPID
    res_current = requests.get(url_current).json()
    datacurrent = res_current
    ################################ get your HOME name automatically
    homepath = os.environ['HOME']
    homename = homepath
    homename = homename[6:]
    ################################ set variables
    vtext = 'n/a'
    temporary = ''
    ################################ set error variables
    coderrcurrent = 0
    ################################ create variables for GENERAL data
    lat = 0
    lon = 0
    tz = ''
    tz_off = 0
    ################################ create variables and array for CURRENT data
    cdt = ''
    csunrise = []
    csunset = []
    ctemp = 0
    ctempfeelslike = 0
    ctempmin = 0
    ctempmax = 0
    cpressure = 0
    chumidity = 0
    cdew_point = 0
    cuvi = 0
    cclouds = 0
    cvisibility = 0
    cwindspeed = 0
    cwinddeg = 0
    cwindgust = 0
    crain1 = 0
    csnow1 = 0
    cidw = 0
    cmain = ""
    cdesc = ""
    cicon = ""
    cidw2 = 0
    cmain2 = ""
    cdesc2 = ""
    cicon2 = ""
    ################################ set the tyemp paths
    home = '/home/'
    conky = '/.conkyGITHUB/'
    ################################ set the paths for the ERROR
    perrcurr = home + homename + conky + 'weather/Openweathermap/CURRENT/-errorcurr.txt'
    ################################ set the paths for the API files
    pgen = home + homename + conky + 'weather/Openweathermap/CURRENT/-general.txt'
    pcur = home + homename + conky + 'weather/Openweathermap/CURRENT/-current.txt'
    pcurclean = home + homename + conky + 'weather/Openweathermap/CURRENT/current.txt'
    ################################ set the paths for the FLAGS
    pflags = home + homename + conky + 'weather/Openweathermap/CURRENT/-flags.txt'
    ################################ set the paths for the GEOPY TIMEZONE data
    pgeopy = home + homename + conky + 'weather/Openweathermap/CURRENT/-geopy.txt'
    ################################ set the paths for the logo
    pathowmlogo = home + homename + conky + 'weather/Openweathermap/CURRENT/owmicon.txt'
    ################################ set the paths for the compass windrose
    pathwindrose = "${image $HOME" + conky + "weather/compass/windsrose.png -p 305,70 -s 100x100}"
    ################################ set the paths for the CURRENT cicon
    pathcicon = home + homename + conky + 'weather/Openweathermap/CURRENT/currenticon.txt'
    ################################ set the paths for the CURRENT cicon2
    pathcicon2 = home + homename + conky + 'weather/Openweathermap/CURRENT/currenticon2.txt'
    ################################ set the paths for the COMPASS
    patharrowt = home + homename + conky + 'weather/compass/arrowt.png'
    patharrowt2 = home + homename + conky + 'weather/compass/arrowt2.png' 
    pathcurcom = home + homename + conky + 'weather/Openweathermap/CURRENT/currentcompass.txt'
    patharrow = home + homename + conky + 'weather/compass/arrow.png'
    patharrow2 = home + homename + conky + 'weather/compass/arrow2.png'
    ################################ set the paths for the icons HOT and COLD
    pathiconhot = home + homename + conky + 'weather/Openweathermap/CURRENT/currenticonhot.txt'
    pathiconcold = home + homename + conky + 'weather/Openweathermap/CURRENT/currenticoncold.txt'
    ################################ set the paths for the CURRENT section
    pathcurconky = home + homename + conky + 'weather/Openweathermap/CURRENT/conky.txt'
    ################################ compass angle
    myd = 72   # <--- insert angle of your North in 'myd'
    tdeg = 0
    ################################ get data for ERROR section CURRENT
    try:
        coderrcurrent = str(datacurrent['cod'])
    except:
        coderrcurrent = 'error'
    ################################ write raw data for ERROR section CURRENT
    fo = open(perrcurr, 'w')
    fo.write('error: {}\n'.format(coderrcurrent))
    fo.close()
    ################################ get data for GENERAL section
    lat = datacurrent['coord']['lat']
    lon = datacurrent['coord']['lon']
    tz = "Europa/Roma" #data['timezone']
    tz = tz + '        '
    tz_off = datacurrent['timezone']
    ################################ write raw data for GENERAL section
    fo = open(pgen, 'w')
    fo.write('lat: {}\n'.format(lat))
    fo.write('lon: {}\n'.format(lon))
    fo.write('TimeZone: {}\n'.format(tz))
    fo.write('TimeZoneoffset: {}\n'.format(tz_off))
    fo.close()
    ############################################### GEOPY NEW SYNTAX
    urlGeopy = 'https://photon.komoot.io/reverse?lon=' + str(lon) + '&lat='  + str(lat)
    resGeopy = requests.get(urlGeopy).json()
    dataGeopy = resGeopy
    location = urllib.request.urlopen(urlGeopy)
    housenumber = "housenumber is old syntax"
    road = "street is old syntax"#dataGeopy['features'][0]['properties']['street']
    suburb = dataGeopy['features'][0]['properties']['district']
    municipality = "municipality is old syntax"
    city = dataGeopy['features'][0]['properties']['city']
    county = dataGeopy['features'][0]['properties']['county']
    state = dataGeopy['features'][0]['properties']['state']
    country = dataGeopy['features'][0]['properties']['country']
    codetemp = dataGeopy['features'][0]['properties']['countrycode']
    code = codetemp.lower()
    zipcode = dataGeopy['features'][0]['properties']['postcode']
    ################################ write raw data for GEOPY
    fo = open(pgeopy, 'w')
    fo.write('lat: {}\n'.format(lat))
    fo.write('lon: {}\n'.format(lon))
    fo.write('TimeZone: {}\n'.format(tz))
    fo.write('TimeZoneoffset: {}\n'.format(tz_off))
    fo.write('house number: {}\n'.format(housenumber))
    fo.write('road: {}\n'.format(road))
    fo.write('suburb: {}\n'.format(suburb))
    fo.write('municipality: {}\n'.format(municipality))
    fo.write('city: {}\n'.format(city))
    fo.write('state: {}\n'.format(state))
    fo.write('county: {}\n'.format(county))
    fo.write('country: {}\n'.format(country))
    fo.write('country_code: {}\n'.format(code))
    fo.write('zip: {}\n'.format(zipcode))
    #                   next row writes geopy data as dict
    fo.write('addressraw: {}\n'.format(location.read()))
    fo.close()
    ################################ create FLAG path
    pi = '${image /home/'
    pi2 = homename
    pi3 = conky + 'flags/'
    pf = '.png -p 381,0 -s 19x13}'
    tot = pi + pi2 + pi3 + code + pf
    if code == vtext:
       fo = open(pflags, 'w')
       tot = 'transparent'
       fo.write('{}\n'.format(tot))
    elif code != vtext:
       fo = open(pflags, 'w')
       fo.write('{}\n'.format(tot))
    fo.close()
    ################################ get data for CURRENT section
    cdt = datacurrent['dt']
    cdt = time.strftime("%d-%B-%Y %H:%M:%S", time.localtime(cdt))
    csunrise = datacurrent['sys']['sunrise']
    csunset = datacurrent['sys']['sunset']
    cdiffss = csunset - csunrise
    cdiffss = time.strftime("%H:%M:%S %Z", time.localtime(cdiffss))
    csunrise = time.strftime("%H:%M:%S %Z", time.localtime(csunrise))
    csunset = time.strftime("%H:%M:%S %Z", time.localtime(csunset))
    ctemp = datacurrent['main']['temp']
    ctempfeelslike = datacurrent['main']['feels_like']
    ctempmin = datacurrent['main']['temp_min']
    ctempmax = datacurrent['main']['temp_max']
    cpressure = datacurrent['main']['pressure']
    chumidity = datacurrent['main']['humidity']
    cdew_point = vtext #data['current']['dew_point']
    cuvi = vtext #data['current']['uvi']
    cclouds = datacurrent['clouds']['all']
    cvisibility = datacurrent['visibility']
    #                   cwindspeed is in m/s as default value
    cwindspeed = datacurrent['wind']['speed']
    #                   transform in Km/h (if you want m/s put a # at the beginning of the next row)
    cwindspeed = round(cwindspeed * 3.6, 2)
    cwinddeg = datacurrent['wind']['deg']
    try:
       cwindgust = datacurrent['wind']['gust']
    #                   transform in Km/h (if you want m/s put a # at the beginning of the next row)
       cwindgust = round(cwindgust * 3.6, 2)
    except:
       cwindgust = vtext
    try:
       crain1 = datacurrent['current']['rain']['1h']
    except:
       crain1 = vtext
    try:
       csnow1 = datacurrent['current']['snow']['1h']
    except:
       csnow1 = vtext
    cidw = datacurrent['weather'][0]['id']
    cmain = datacurrent['weather'][0]['main']
    cdesc = datacurrent['weather'][0]['description']
    cicon = datacurrent['weather'][0]['icon']
    try:
       cidw2 = datacurrent['weather'][1]['id']
    except:
       cidw2 = vtext
    try:
       cmain2 = datacurrent['weather'][1]['main']
    except:
       cmain2 = vtext
    try:
       cdesc2 = datacurrent['weather'][1]['description']
    except:
       cdesc2 = vtext
    try:
       cicon2 = datacurrent['weather'][1]['icon']
    except:
       cicon2 = vtext
    ################################ write raw data for CURRENT section
    fo = open(pcur, 'w')
    fo.write('dt: {}\n'.format(cdt))
    fo.write('SUNRISE: {}\n'.format(csunrise))
    fo.write('SUNSET: {}\n'.format(csunset))
    fo.write('temp: {}\n'.format(ctemp))
    fo.write('feels: {}\n'.format(ctempfeelslike))
    fo.write('tempmin: {}\n'.format(ctempmin))
    fo.write('tempmax: {}\n'.format(ctempmax))
    fo.write('PRESSURE: {}\n'.format(cpressure))
    fo.write('HUMIDITY: {}\n'.format(chumidity))
    fo.write('DEWPOINT: {}\n'.format(cdew_point))
    fo.write('UVI: {}\n'.format(cuvi))
    fo.write('CLOUDS: {}\n'.format(cclouds))
    fo.write('VISIBILITY: {}\n'.format(cvisibility))
    fo.write('windspeed: {}\n'.format(cwindspeed))
    fo.write('winddeg: {}\n'.format(cwinddeg))
    fo.write('windgust: {}\n'.format(cwindgust))
    fo.write('rain1h: {}\n'.format(crain1))
    fo.write('snow1h: {}\n'.format(csnow1))
    fo.write('idw: {}\n'.format(cidw))
    fo.write('main: {}\n'.format(cmain))
    fo.write('description: {}\n'.format(cdesc))
    fo.write('icon: {}\n'.format(cicon))
    fo.write('idw2: {}\n'.format(cidw2))
    fo.write('main2: {}\n'.format(cmain2))
    fo.write('description2: {}\n'.format(cdesc2))
    fo.write('icon2: {}\n'.format(cicon2))
    fo.write('cdiffss: {}\n'.format(cdiffss))
    fo.close()
    ################################ write clean data for CURRENT section
    fo = open(pcurclean, 'w')
    fo.write('{}\n'.format(cdt))
    fo.write('{}\n'.format(csunrise))
    fo.write('{}\n'.format(csunset))
    fo.write('{}\n'.format(ctemp))
    fo.write('{}\n'.format(ctempfeelslike))
    fo.write('{}\n'.format(ctempmin))
    fo.write('{}\n'.format(ctempmax))
    fo.write('{}\n'.format(cpressure))
    fo.write('{}\n'.format(chumidity))
    fo.write('{}\n'.format(cdew_point))
    fo.write('{}\n'.format(cuvi))
    fo.write('{}\n'.format(cclouds))
    fo.write('{}\n'.format(cvisibility))
    fo.write('{}\n'.format(cwindspeed))
    fo.write('{}\n'.format(cwinddeg))
    fo.write('{}\n'.format(cwindgust))
    fo.write('{}\n'.format(crain1))
    fo.write('{}\n'.format(csnow1))
    fo.write('{}\n'.format(cidw))
    fo.write('{}\n'.format(cmain))
    fo.write('{}\n'.format(cdesc))
    fo.write('{}\n'.format(cicon))
    fo.write('{}\n'.format(cidw2))
    fo.write('{}\n'.format(cmain2))
    fo.write('{}\n'.format(cdesc2))
    fo.write('{}\n'.format(cicon2))
    fo.write('{}\n'.format(cdiffss))
    fo.close()
    ################################ create the path for openweathermap logo icon
    pi = '${image /home/'
    pi2 = homename
    pi3 = conky + 'weather/Openweathermap/owmicon'
    est = '.png -p '
    x = 280
    virg = ','
    y = 460
    pf = ' -s 140x140}'
    fo = open(pathowmlogo, 'w')
    tot = pi + pi2 + pi3 + est + str(x) + virg + str(y) + pf
    fo.write('{}\n'.format(tot))
    fo.close()
    ################################ create CURRENT cicon path
    pi = '${image /home/'
    pi2 = homename
    pi3 = conky + 'weather/Openweathermap/icons/'
    icontemp = (cicon[2:3])
    pf = '.png -p 0,30 -s 160x120}'
    tot = pi + pi2 + pi3 + str(cidw) + icontemp + pf
    if icontemp == 'd':
       fo = open(pathcicon, 'w')
       fo.write('{}\n'.format(tot))
    elif icontemp == 'n':
       fo = open(pathcicon, 'w')
       fo.write('{}\n'.format(tot))
    fo.close()
    ################################ create CURRENT cicon2 path
    pi = '${image /home/'
    pi2 = homename
    pi3 = conky + 'weather/Openweathermap/icons/'
    pi4 = conky + 'weather/Openweathermap/owmicon'
    pitest = conky + 'weather/Openweathermap/test2'
    icontemp = (cicon2[2:3])
    pf = '.png -p 240,73 -s 40x28}'
    pfowmiconsmall = '.png -p 245,60 -s 65x65}'
    pfowmiconbig = '.png -p 185,0 -s 75x75}'
    tot = pi + pi2 + pi3 + str(cidw2) + icontemp + pf
    totowmiconsmall = pi + pi2 + pi4 + pfowmiconsmall
    totowmiconbig = pi + pi2 + pi4 + pfowmiconbig
    if cicon2 != vtext:
       if icontemp == 'd':
          fo = open(pathcicon2, 'w')
          fo.write('{}\n'.format(tot + totowmiconbig))
       elif icontemp == 'n':
          fo = open(pathcicon2, 'w')
          fo.write('{}\n'.format(tot + totowmiconbig))
       fo.close()
    elif cicon2 == vtext:
       cidw2 = 'transparent'
       tot2 = pi + pi2 + pi3 + cidw2 + pf
       fo = open(pathcicon2, 'w')
       fo.write('{}\n'.format(totowmiconsmall))
       fo.close()
    ################################ write the path for COMPASS icon
    #grades calculation for cwinddeg, trasparent image if no wind (use negative tdeg to rotate clockwise)
    if cwinddeg == 'empty':
        tdeg = myd
        temp1 = Image.open(patharrowt)
        temp2 = temp1.rotate(-tdeg)
        temp2.save(patharrowt2)
        temp3 = '${image /home/'
        temp4 = homename
        temp5 = conky + 'weather/compass/arrowt2'
        pfcomp = '.png -p 305,70 -s 100x100}'# set this in pathwindrose too
        totcomp = temp3 + temp4 + temp5 + pfcomp
        fo = open(pathcurcom, 'w')
        fo.write('{}\n'.format(totcomp))
        fo.write('{}\n'.format(pathwindrose))
    elif cwinddeg != 'empty':
        tdeg = myd + cwinddeg
        temp1 = Image.open(patharrow)
        temp2 = temp1.rotate(-tdeg)
        temp2.save(patharrow2)
        temp3 = '${image /home/'
        temp4 = homename
        temp5 = conky + 'weather/compass/arrow2'
        pfcomp = '.png -p 305,70 -s 100x100}'# set this in pathwindrose too
        totcomp = temp3 + temp4 + temp5 + pfcomp
        fo = open(pathcurcom, 'w')
        fo.write('{}\n'.format(totcomp))
        fo.write('{}\n'.format(pathwindrose))
    fo.close()
    ################################ write thermo icon HOT path
    pi = '${image /home/'
    pi2 = homename
    pi3 = conky + 'weather/Openweathermap/icons/'
    cicon = 'hot'
    pf = '.png -p 275,100 -s 14x45}'
    if ctempfeelslike >= 38:
       tot = pi + pi2 + pi3 + str(cicon) + pf
       fo = open(pathiconhot, 'w')
       fo.write('{}\n'.format(tot))
       fo.close()
    else:
       cicon = 'transparent'
       tot = pi + pi2 + pi3 + str(cicon) + pf
       fo = open(pathiconhot, 'w')
       fo.write('{}\n'.format(tot))
       fo.close()
    ################################ write thermo icon COLD path
    cicon = 'cold'
    if ctempfeelslike <= 0:
       tot = pi + pi2 + pi3 + str(cicon) + pf
       fo = open(pathiconcold, 'w')
       fo.write('{}\n'.format(tot))
       fo.close()
    else:
       cicon = 'transparent'
       tot = pi + pi2 + pi3 + str(cicon) + pf
       fo = open(pathiconcold, 'w')
       fo.write('{}\n'.format(tot))
       fo.close()
    ################################ create CURRENT section
    owmpylogo = "${image $HOME" + conky + "weather/Openweathermap/python_logo.png -p 145,0 -s 15x15}"
    infotz = "${color2}${font = 'URW Gothic L:size=8'}OPENWEATHERMAP${font}${color1}${alignr}${execpi 900 sed -n '3p' $HOME" + conky + "weather/Openweathermap/CURRENT/-general.txt}"
    infotzerrcurrent = "${color2}${font = 'URW Gothic L:size=8'}OPENWEATHERMAP     ${color4}Ecurrent:" + coderrcurrent + "${font}${color1}${alignr}${execpi 900 sed -n '3p' $HOME" + conky + "weather/Openweathermap/CURRENT/-general.txt}"
    latlon = "${alignr}(${execpi 900 sed -n '1p' $HOME" + conky + "weather/Openweathermap/CURRENT/-general.txt} - ${execpi 900 sed -n '2p' $HOME" + conky + "weather/Openweathermap/CURRENT/-general.txt})${font}${color}"
    curricon = "${execpi 900 sed -n '1p' $HOME" + conky + "weather/Openweathermap/CURRENT/currenticon.txt}"
    firstdesc = "${color4}${goto 190}${execpi 900 sed -n '20p' $HOME" + conky + "weather/Openweathermap/CURRENT/-current.txt | awk '{print $2}'}${color} - ${execpi 900 sed -n '21p' $HOME" + conky + "weather/Openweathermap/CURRENT/-current.txt | awk '{print $2}'}"
    seconddesc = "${color}${goto 190}${execpi 900 sed -n '24p' $HOME" + conky + "weather/Openweathermap/CURRENT/-current.txt | awk '{print $2}'}${color} - ${execpi 900 sed -n '25p' $HOME" + conky + "weather/Openweathermap/CURRENT/-current.txt | awk '{print $2}'}"
    currtemp = "${color}${goto 190}${execpi 900 sed -n '4p' $HOME" + conky + "weather/Openweathermap/CURRENT/-current.txt}${color}°C"
    currtempf = "${goto 190}(${execpi 900 sed -n '5p' $HOME" + conky + "weather/Openweathermap/CURRENT/-current.txt}°C)"
    thermo = "${execpi 900 sed -n '1p' $HOME" + conky + "weather/Openweathermap/CURRENT/currenticonhot.txt}${execpi 900 sed -n '1p' $HOME" + conky + "weather/Openweathermap/CURRENT/currenticoncold.txt}"
    minmax = "${goto 190}${color1}${execpi 900 sed -n '6p' $HOME" + conky + "weather/Openweathermap/CURRENT/-current.txt | awk '{print $2}'}°${color}/${color4}${execpi 900 sed -n '7p' $HOME" + conky + "weather/Openweathermap/CURRENT/-current.txt | awk '{print $2}'}°${color}C"
    winds = "${color}${goto 190}${execpi 900 sed -n '14p' $HOME" + conky + "weather/Openweathermap/CURRENT/-current.txt} Km/h"
    windg = "${color}${goto 190}${execpi 900 sed -n '16p' $HOME" + conky + "weather/Openweathermap/CURRENT/-current.txt} Km/h"
    info1 = "${color2}HUMIDITY: $color${execpi 900 sed -n '9p' $HOME" + conky + "weather/Openweathermap/CURRENT/-current.txt | awk '{print $2}'}%${goto 295}${color2}PRESSURE: $color${execpi 900 sed -n '6p' $HOME" + conky + "weather/Openweathermap/CURRENT/-current.txt | awk '{print $2}'}hPa "
    info2 = "${color2}CLOUD COVER: $color${execpi 900 sed -n '12p' $HOME" + conky + "weather/Openweathermap/CURRENT/-current.txt | awk '{print $2}'}% ${goto 295}${color2}VISIBILITY: $color${execpi 900 sed -n '11p' $HOME" + conky + "weather/Openweathermap/CURRENT/-current.txt | awk '{print $2}'}m"
    info3= "${color2}SUN R/S: $color${execpi 900 sed -n '2p' $HOME" + conky + "weather/Openweathermap/CURRENT/-current.txt | awk '{print $2}'}/${execpi 900 sed -n '3p' $HOME" + conky + "weather/Openweathermap/CURRENT/-current.txt | awk '{print $2}'}${execpi 900 sed -n '3p' $HOME" + conky + "weather/Openweathermap/CURRENT/-current.txt | awk '{print $3}'}${color2}${goto 295}SUN DURAT.: $color${execpi 900 sed -n '27p' $HOME" + conky + "weather/Openweathermap/CURRENT/-current.txt | awk '{print $2}'}${color}"
    fo = open(pathcurconky, 'w')
    if coderrcurrent != '200':
        fo.write('{}\n'.format(owmpylogo + infotzerrcurrent))
    else:
        fo.write('{}\n'.format(owmpylogo + infotz))
        fo.write('{}\n'.format(latlon))
        fo.write('{}\n'.format(firstdesc))
        fo.write('{}\n'.format(seconddesc))
        fo.write('{}\n'.format(currtemp))
        fo.write('{}\n'.format(currtempf + thermo))
        fo.write('{}\n'.format(minmax))
        fo.write('{}\n'.format(winds))
        fo.write('{}\n'.format(windg))
        fo.write('{}\n'.format(info1))
        fo.write('{}\n'.format(info2))
        fo.write('{}\n'.format(info3))
    fo.close()
except Exception as e:
    # Manage exceptions (optional)
    filelockerror = (f"Error during script execution: {e}")
finally:
    # remove lock file
    try:
        os.remove(lock_file)
    except FileNotFoundError:
        pass  # file already removed
