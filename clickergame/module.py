def Game_tick(time_waiting):
    global pretime
    loop=True
    try:#checks if time is imported
        import time
    except:
        pass
    #module starts
    while loop == True:#repeting loop
        current=time.time()
        try:
            if current >= pretime + time_waiting or current +90000<pretime:#second loop
                loop = False
                pretime = current
        except:#first loop
            pretime = current
            time.sleep(time_waiting)
            loop = False
        #print(current)
        #print(pretime)