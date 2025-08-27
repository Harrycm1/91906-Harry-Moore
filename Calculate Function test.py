#Calculation function
def calc():
    global NA_total, A_total, M_total, E_total
    
    try:
        na = int(NA_entry.get())
    except:
        na = 0
    try:
        a = int(A_entry.get())
    except:
        a = 0
    try:
        m = int(M_entry.get())
    except:
        m = 0
    try:
        e = int(E_entry.get())
    except:
        e = 0