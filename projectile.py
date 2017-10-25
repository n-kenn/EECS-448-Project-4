angle = math.radians(65)
power = 40
x_pos = 10
y_pos = height-10
x_vel = power * math.cos(angle)
y_vel = -1 * power * math.sin(angle)

def update_pos(xp,yp,xv,yv):
    if (xp + xv > width or xp + xv < 0):
        xv = 0#(-1)*xv
    xp = xp + xv
    if (yp + yv > height or yp + yv < 0):
        yv = 0#(-0.75)*yv
    yv = yv + 2
    yp = yp + yv

    return (int(xp),int(yp),xv,yv)
