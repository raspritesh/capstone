from datetime import date
def fine(d1,m1,y1,d2,m2,y2):
    d=date(y1,m1,d1)
    e=date(y2,m2,d2)
    delta=e-d-14
    print delta.days
