from z3 import *
import torch.nn as nn

x1,x2,x3,x4,x5 = Reals('x1 x2 x3 x4 x5')

#relu
def relu(x):
    res = If(x>0,x,0)
    return res

#para
alpha = 0.05
Te=15
ah=0.0036
Th=55
ae=0.008


#controller
u = 0.0143379026676509*relu(-2.21801327198751*x1 + 0.608987506966011*x2 - 0.159782977232819*x3 + 1.13602202061367*x4 - 0.15323684435639*x5 + 0.780617509600508) \
    - 2.3018101339414*relu(-2.20260997854742*x1 - 0.603691792199*x2 - 0.00688892786135139*x3 + 0.087072064966515*x4 + 0.613646110092748*x5 - 0.256389876487182) \
    - 0.172818766627278*relu(-1.2934254365899*x1 - 0.43222805344087*x2 - 0.108759618665069*x3 + 0.680043756040046*x4 + 1.65614584137767*x5 + 1.36347426212959) \
    + 0.497231670741281*relu(-1.20264961333652*x1 + 1.43973915101838*x2 - 0.926096984689167*x3 - 0.706644011272381*x4 + 0.800682508479248*x5 - 0.849793865303617) \
    - 1.9369525021431*relu(-0.997360669391999*x1 + 0.856572395832525*x2 - 1.59462043443214*x3 + 0.279291608974659*x4 - 0.670840863452957*x5 + 0.557600887029567) \
    + 0.0107409622385375*relu(-0.164092234044053*x1 + 0.432244185515137*x2 + 1.37635639901042*x3 - 1.87185871823846*x4 - 0.276132911909607*x5 - 0.372000109236498) \
    - 0.388295842770235*relu(-0.0990986356851934*x1 - 1.76549479612685*x2 - 0.143685605561645*x3 + 0.0752138123046792*x4 + 0.755646405663635*x5 + 0.398466459474539) \
    - 0.0615750989015717*relu(0.145591404642246*x1 - 1.51404471352838*x2 + 0.349039360971036*x3 + 0.415732444194857*x4 + 1.32681813247835*x5 + 0.60454384460111) \
    + 0.546819885262192


#system
f_x1 = (1-2*alpha-ae-ah*x5)*x1+ alpha*x3+ ae*Te + ah*Th*x5
f_x2 =  (1-2*alpha-ae-ah*u)*x2+ alpha*x4+ ae*Te + ah*Th*u
f_x3 = (1-2*alpha-ae-ah*x5)*x3+ alpha*x1+ ae*Te + ah*Th*x5
f_x4 = (1-2*alpha-ae-ah*u)*x4+ alpha*x2+ ae*Te + ah*Th*u


#barrier
B = -0.138190554466862*relu(-2.2309662617618*x1 - 2.05965160557376*x2 - 0.632225623045555*x3 - 0.709284532891474*x4 + 1.36503105864152)\
    + 0.0506217903115477*relu(-1.96982965805247*x1 + 0.838561011042413*x2 + 0.807898906185505*x3 + 0.374233099808135*x4 - 0.118083988661764)\
    - 2.13834716099841*relu(-1.51598696262983*x1 - 0.619436940636597*x2 + 0.147875203855781*x3 + 0.831484992162891*x4 + 1.02682643688143)\
    + 2.59218409985988*relu(-1.12308566713163*x1 - 0.259722884310301*x2 - 0.811010918624873*x3 + 0.82318775887454*x4 - 1.85238559404093)\
    + 1.0784932469892*relu(-0.911803354537572*x1 - 2.06497029566196*x2 - 1.14574932823113*x3 - 0.835705017752579*x4 + 0.521786017627252) \
    + 0.056066212216846*relu(-0.799342261315341*x1 + 2.36052741138813*x2 + 0.514639667292021*x3 - 2.08612114154922*x4 - 0.280635621904722)\
    + 0.107537537527184*relu(-0.736135152128668*x1 + 0.617588105016102*x2 - 1.01061434416795*x3 - 0.262199393026597*x4 - 0.0311845815211528) \
    - 1.31723064877535*relu(-0.405048400535377*x1 - 0.106325827264228*x2 + 0.0583695815953973*x3 - 1.06993231060012*x4 + 0.0640000838407807)\
    - 1.54767401340737*relu(-0.206063812216086*x1 - 1.47719198949782*x2 + 1.09261691866409*x3 - 0.49700657480565*x4 - 0.948761507202659) \
    + 0.0500798740118673*relu(-0.0909265188594093*x1 + 0.470090253327209*x2 - 0.954583255292317*x3 + 0.577671207180085*x4 - 0.575209955141366) \
    + 0.0830115147027033*relu(0.226760477629661*x1 - 0.287708854547598*x2 + 0.930841604307839*x3 - 0.988794006362033*x4 - 0.586951235921896)\
    + 0.084269019464378*relu(0.455364536100336*x1 - 2.35813885481486*x2 + 0.727484397828276*x3 + 1.10702876952514*x4 - 0.868851771621342) \
    + 0.0626527603733885*relu(0.459099128927179*x1 + 0.0283070118324721*x2 + 1.00953279281753*x3 - 1.53668774638797*x4 - 0.16644426871129) \
    + 1.28200890361065*relu(0.480910002687703*x1 - 0.408191231621827*x2 + 1.3436734675467*x3 - 2.44177838858406*x4 - 0.714669899335886)\
    + 0.0661973340209232*relu(0.550299542978888*x1 - 0.614043208666017*x2 + 1.61249059857945*x3 - 1.5502147372646*x4 + 0.532933501871903)\
    + 0.0631575782303137*relu(0.785658931787931*x1 - 0.182082694722195*x2 - 1.96509081712717*x3 + 1.42109059569181*x4 + 0.598067538494637)\
    + 0.751339880434209

B_f =  -0.138190554466862*relu(-2.2309662617618*f_x1 - 2.05965160557376*f_x2 - 0.632225623045555*f_x3 - 0.709284532891474*f_x4 + 1.36503105864152)\
       + 0.0506217903115477*relu(-1.96982965805247*f_x1 + 0.838561011042413*f_x2 + 0.807898906185505*f_x3 + 0.374233099808135*f_x4 - 0.118083988661764)\
       - 2.13834716099841*relu(-1.51598696262983*f_x1 - 0.619436940636597*f_x2 + 0.147875203855781*f_x3 + 0.831484992162891*f_x4 + 1.02682643688143) \
       + 2.59218409985988*relu(-1.12308566713163*f_x1 - 0.259722884310301*f_x2 - 0.811010918624873*f_x3 + 0.82318775887454*f_x4 - 1.85238559404093)\
       + 1.0784932469892*relu(-0.911803354537572*f_x1 - 2.06497029566196*f_x2 - 1.14574932823113*f_x3 - 0.835705017752579*f_x4 + 0.521786017627252) \
       + 0.056066212216846*relu(-0.799342261315341*f_x1 + 2.36052741138813*f_x2 + 0.514639667292021*f_x3 - 2.08612114154922*f_x4 - 0.280635621904722)\
       + 0.107537537527184*relu(-0.736135152128668*f_x1 + 0.617588105016102*f_x2 - 1.01061434416795*f_x3 - 0.262199393026597*f_x4 - 0.0311845815211528)\
       - 1.31723064877535*relu(-0.405048400535377*f_x1 - 0.106325827264228*f_x2 + 0.0583695815953973*f_x3 - 1.06993231060012*f_x4 + 0.0640000838407807)\
       - 1.54767401340737*relu(-0.206063812216086*f_x1 - 1.47719198949782*f_x2 + 1.09261691866409*f_x3 - 0.49700657480565*f_x4 - 0.948761507202659) \
       + 0.0500798740118673*relu(-0.0909265188594093*f_x1 + 0.470090253327209*f_x2 - 0.954583255292317*f_x3 + 0.577671207180085*f_x4 - 0.575209955141366)\
       + 0.0830115147027033*relu(0.226760477629661*f_x1 - 0.287708854547598*f_x2 + 0.930841604307839*f_x3 - 0.988794006362033*f_x4 - 0.586951235921896)\
       + 0.084269019464378*relu(0.455364536100336*f_x1 - 2.35813885481486*f_x2 + 0.727484397828276*f_x3 + 1.10702876952514*f_x4 - 0.868851771621342) \
       + 0.0626527603733885*relu(0.459099128927179*f_x1 + 0.0283070118324721*f_x2 + 1.00953279281753*f_x3 - 1.53668774638797*f_x4 - 0.16644426871129)\
       + 1.28200890361065*relu(0.480910002687703*f_x1 - 0.408191231621827*f_x2 + 1.3436734675467*f_x3 - 2.44177838858406*f_x4 - 0.714669899335886) \
       + 0.0661973340209232*relu(0.550299542978888*f_x1 - 0.614043208666017*f_x2 + 1.61249059857945*f_x3 - 1.5502147372646*f_x4 + 0.532933501871903) \
       + 0.0631575782303137*relu(0.785658931787931*f_x1 - 0.182082694722195*f_x2 - 1.96509081712717*f_x3 + 1.42109059569181*f_x4 + 0.598067538494637) \
       + 0.751339880434209

print("start verify")
s = Solver()
s.add(And(21.5 <= x1, x1 <= 22, 21 <= x2, x2 <= 21.5,
          21 <= x3, x3 <= 22, 21 <= x4, x4 <= 22,
          (x4 - x3) * (x4 - x3) <= 0.7*0.7,
          B > 1))
# print(s.check())
if s.check() == sat: #check()方法用来判断是否有解，sat(satisify)表示满足有解
    ans = s.model() #model()方法得到解
    print(s.check())
    print(ans)
    #也可以用变量名作为下标得到解
else:
    print("no ans!")

print("start verify")
#unsafe condition
s = Solver()
s.add(And(15 <= x1, x1 <= 30, 15 <= x2, x2 <= 30,
          15 <= x3, x3 <= 30, 15 <= x4, x4 <= 30,
          (x4 - x3) * (x4 - x3) > 1.3*1.3,
             B < 1),
         )
# print(s.check())
if s.check() == sat: #check()方法用来判断是否有解，sat(satisify)表示满足有解
    ans = s.model() #model()方法得到解
    print(s.check())
    print(ans)
else:
    print("no ans!")


print("start verify")
#diff condition
s = Solver()
s.add(And(15 <= x1, x1 <= 30, 15 <= x2, x2 <= 30,
          15 <= x3, x3 <= 30, 15 <= x4, x4 <= 30,
          0 <= x5, x5 <= 1,0 <= u, u <= 1,
          15 <= f_x1, f_x1 <= 30, 15 <= f_x2, f_x2 <= 30,
          15 <= f_x3, f_x3 <= 30, 15 <= f_x4, f_x4 <= 30,
          B_f - B > 0 ))
# print(s.check())
if s.check() == sat: #check()方法用来判断是否有解，sat(satisify)表示满足有解
    ans = s.model() #model()方法得到解
    print(s.check())
    print(ans)
    #也可以用变量名作为下标得到解
else:
    print("no ans!")


print("success")