def format_duration(input):
    y = getRem(input, 31536000)
    d = getRem(y[1], 86400)
    h = getRem(d[1], 3600)
    m = getRem(h[1], 60)
    return assembleString(y[0], d[0], h[0], m[0], m[1] ) 

def assembleString(y,d,h,m,s):
    l = ["","","","",""]
    out = ""
    strCount,temp = 0,0

    if y != 0:  # YEAR SECTION
        if y == 1: l[0] = str(y) + " year"
        else:      l[0] = str(y) + " years"
    if d != 0:  # DAY SECTION
        if d == 1: l[1] = str(d) + " day"
        else:      l[1] = str(d) + " days"     
    if h != 0:  # HOUR SECTION
        if h == 1: l[2] = str(h) + " hour"
        else:      l[2] = str(h) + " hours"
    if m != 0:  # MINUTE SECTION
        if m == 1: l[3] = str(m) + " minute"
        else:      l[3] = str(m) + " minutes"
    if s != 0:  # SECOND SECTION
        if s == 1: l[4] = str(s) + " second"
        else:      l[4] = str(s) + " seconds"
        
    for s in l:
        if s is not "": strCount += 1
    if strCount == 0: return "now"
    elif strCount == 1:
        for s in l:
            if s is not "": out = s
    else:
       for s in l:
          if s is not "":
              if   temp == strCount - 2: s += " and "
              elif temp != strCount:   s += ", "
              temp += 1
              out += s 
    if out.endswith(", "): return out[:len(out) - 2]
    return out
  
def getRem(input, check): 
    l =[0,0]
    if input >= check:
        rem = input % check
        l[0] = int( (input - rem) / check )
        l[1] = rem
        return l
    else:
        l[1] = input
        return l