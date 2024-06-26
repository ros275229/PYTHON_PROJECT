import numpy as np
De = lambda D0,y,ap,bp:D0-y*np.sin((bp-90)*np.pi/180)*np.tan(ap*np.pi/180)
po = lambda ap,bp: np.arctan(np.cos((bp-90)*np.pi/180)*np.tan(ap*np.pi/180))*180/np.pi
W = lambda D,x,po,th: (D-x*np.tan(po*np.pi/180))*(np.sin((th/2)*np.pi/180)/np.sin((90-po-th/2)*np.pi/180)+np.sin((th/2)*np.pi/180)/np.sin((90+po-th/2)*np.pi/180))*np.cos((po)*np.pi/180)
y = np.arange(0,2.4,0.3)*1852
bp = np.arange(0,360,45)
ap = 1.5
D0 = 120
th = 120
for i in bp:
    if i != 90 and i!= 270:
        print(i)
#         print(De(D0,y,ap,i))
#         print(po(ap,i if i < 180 else i-180))
        print(W(De(D0,y,ap,i),0,po(ap,i if i < 180 else i-180),th))
    else:
        print(i)
        print(W(D0,0,ap,th))