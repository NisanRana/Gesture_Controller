import time

last_time = 0

def allowed(cooldown):
    global last_time
    now = time.time()

    if now - last_time >= cooldown:
        last_time = now
        return True

    return False