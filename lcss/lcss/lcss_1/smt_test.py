from z3 import *
import torch.nn as nn

# x1,x2,x3,x4,x5 = Reals('x1 x2 x3 x4 x5')
x1, x2, x3, x4, x5 = Reals('x1 x2 x3 x4 x5')
h = (x1 - x2) * (x1 - x2)

#relu
def relu(x):
    res = If(x>0,x,0)
    return res




#controller
u = -0.298207216353873*x1 - 0.0528853621755564*x3 + 0.298207216353873*x2 + 0.0528853621755564*x4 + x5


#system
f_x1 = x1 + x3 + 0.5 * x5
f_x2 = x2 + x4 + 0.5 * u
f_x3 = x3 + x5
f_x4 = x4 + u

#barrier
# B = -0.186398671354142*x1*x1*x1 + 0.582795549207855*x1*x1*x2 + 0.946421809512145*x1*x1 \
#     - 1.70536780142502*x1*x2*x2 - 2.60168279908074*x1*x2 \
#     + 1.29528270480471*x1 + 0.137937830533062*x2*x2*x2 + 8.7178498673519*x2*x2 \
#     - 6.32656995112874*x2 - 0.107492349181588
#
# B_diff = -0.559196014062427*x1*x1*x1*x2 + 0.559196014062427*x1*x1*x1 + 1.16559109841571*x1*x1*x2*x2 + 0.144456971400725*x1*x1*x2\
#     - 1.89284361902429*x1*x1 - 1.70536780142502*x1*x2*x2*x2 + 2.51442060519431*x1*x2*x2 + 6.49864830296619*x1*x2\
#     - 1.29528270480471*x1 - 0.413813491599185*x2*x2*x2  - 17.4356997347038*x2*x2 + 6.32656995112874*x2
B = 0.761728488417804*relu(-2.64173228697919*x1 + 2.69692933658995*x2 - 0.282396285075753*x3 - 2.06934812991744*x4 - 1.38413674725642)\
    + 0.725904172378083*relu(-2.26278794921797*x1 + 2.28607792989042*x2 + 0.105149210277597*x3 - 2.7781752053849*x4 - 0.793560949625015)\
    + 0.535990634835213*relu(-1.96367046843284*x1 - 0.454889301038031*x2 - 1.0780614206571*x3 + 0.510215549233533*x4 - 1.92415763245706) \
    + 1.08381715545176*relu(-1.85108606183825*x1 + 0.740739331537963*x2 + 1.90359628130072*x3 + 2.51016954543296*x4 - 0.573767399675179)\
    - 0.400615716824092*relu(-1.48244458974475*x1 - 0.0424893930984495*x2 + 1.53849973032765*x3 + 1.11192650002442*x4 - 0.448352284375016)\
    - 1.0592182328688*relu(-1.3829153494715*x1 - 1.31406418791885*x2 - 0.626017167674076*x3 - 2.26177070134379*x4 - 0.273488441495156)\
    - 0.851387539101656*relu(-1.03046214395523*x1 - 0.909555406408806*x2 - 1.38770590200458*x3 + 0.0818228815161483*x4 + 1.40916476956675)\
    + 0.81463407432563*relu(-0.944281004636998*x1 - 0.444123434095368*x2 - 0.206674805636143*x3 - 1.32402123432115*x4 - 0.586393326292978) \
    - 0.780280137415586*relu(-0.801208209551896*x1 + 0.858122861549648*x2 - 1.88289708318564*x3 + 6.84018552562458*x4 - 1.55282168090349)\
    - 0.45153470599557*relu(-0.529137775885506*x1 + 0.579135505005259*x2 - 2.21544668825912*x3 + 1.91341667055687*x4 - 0.777453991345674) \
    - 0.185948286733716*relu(-0.460476439365189*x1 + 0.407989721913868*x2 - 1.67128722270681*x3 + 1.0435274984451*x4 + 0.329521253156993) \
    - 0.518219909749429*relu(-0.413008529611824*x1 + 0.209414557704965*x2 - 1.18580793583636*x3 + 2.12092548344037*x4 - 0.423980877345457) \
    - 0.0935755409786181*relu(-0.360663084810015*x1 + 0.232483589716821*x2 - 0.501057854420878*x3 + 0.775213008710837*x4 + 0.424716137625864)\
    - 0.280631749165809*relu(-0.329960768936088*x1 + 0.281335102981309*x2 + 2.38581998061847*x3 + 1.13126792498832*x4 - 0.567440835118526)\
    + 0.0128433672401342*relu(0.00881356923953485*x1 + 0.0265671237562541*x2 + 0.279826455106706*x3 - 0.0576047998173023*x4 - 0.2557526485123)\
    - 0.179306476388491*relu(0.146664777624099*x1 - 0.795499460693267*x2 - 0.782897034383956*x3 - 0.277835745313809*x4 + 1.57155156941021) \
    + 0.963706701261077*relu(0.179114583699537*x1 - 1.94783442149019*x2 - 1.79864660314496*x3 + 1.40691592693506*x4 - 1.83845934659704) \
    - 0.393498957635352*relu(0.948903199713304*x1 - 1.06352865219377*x2 + 0.348577653264444*x3 - 2.03157792725149*x4 - 0.0842998106314543)\
    - 0.882203311667125*relu(1.1843721136302*x1 - 1.60618846527075*x2 + 1.22289035474955*x3 - 1.95031999477107*x4 + 1.81085797682436) \
    + 1.70719703662305*relu(3.07388659389659*x1 - 3.29160835539298*x2 - 1.87250017156491*x3 + 5.86326181700328*x4 + 0.0374100350433776) \
    - 0.342390288785141
B_f =  0.761728488417804*relu(-2.64173228697919*f_x1 + 2.69692933658995*f_x2 - 0.282396285075753*f_x3 - 2.06934812991744*f_x4 - 1.38413674725642)\
       + 0.725904172378083*relu(-2.26278794921797*f_x1 + 2.28607792989042*f_x2 + 0.105149210277597*f_x3 - 2.7781752053849*f_x4 - 0.793560949625015)\
       + 0.535990634835213*relu(-1.96367046843284*f_x1 - 0.454889301038031*f_x2 - 1.0780614206571*f_x3 + 0.510215549233533*f_x4 - 1.92415763245706)\
       + 1.08381715545176*relu(-1.85108606183825*f_x1 + 0.740739331537963*f_x2 + 1.90359628130072*f_x3 + 2.51016954543296*f_x4 - 0.573767399675179)\
       - 0.400615716824092*relu(-1.48244458974475*f_x1 - 0.0424893930984495*f_x2 + 1.53849973032765*f_x3 + 1.11192650002442*f_x4 - 0.448352284375016)\
       - 1.0592182328688*relu(-1.3829153494715*f_x1 - 1.31406418791885*f_x2 - 0.626017167674076*f_x3 - 2.26177070134379*f_x4 - 0.273488441495156) \
       - 0.851387539101656*relu(-1.03046214395523*f_x1 - 0.909555406408806*f_x2 - 1.38770590200458*f_x3 + 0.0818228815161483*f_x4 + 1.40916476956675)\
       + 0.81463407432563*relu(-0.944281004636998*f_x1 - 0.444123434095368*f_x2 - 0.206674805636143*f_x3 - 1.32402123432115*f_x4 - 0.586393326292978)\
       - 0.780280137415586*relu(-0.801208209551896*f_x1 + 0.858122861549648*f_x2 - 1.88289708318564*f_x3 + 6.84018552562458*f_x4 - 1.55282168090349)\
       - 0.45153470599557*relu(-0.529137775885506*f_x1 + 0.579135505005259*f_x2 - 2.21544668825912*f_x3 + 1.91341667055687*f_x4 - 0.777453991345674) \
       - 0.185948286733716*relu(-0.460476439365189*f_x1 + 0.407989721913868*f_x2 - 1.67128722270681*f_x3 + 1.0435274984451*f_x4 + 0.329521253156993)\
       - 0.518219909749429*relu(-0.413008529611824*f_x1 + 0.209414557704965*f_x2 - 1.18580793583636*f_x3 + 2.12092548344037*f_x4 - 0.423980877345457)\
       - 0.0935755409786181*relu(-0.360663084810015*f_x1 + 0.232483589716821*f_x2 - 0.501057854420878*f_x3 + 0.775213008710837*f_x4 + 0.424716137625864)\
       - 0.280631749165809*relu(-0.329960768936088*f_x1 + 0.281335102981309*f_x2 + 2.38581998061847*f_x3 + 1.13126792498832*f_x4 - 0.567440835118526) \
       + 0.0128433672401342*relu(0.00881356923953485*f_x1 + 0.0265671237562541*f_x2 + 0.279826455106706*f_x3 - 0.0576047998173023*f_x4 - 0.2557526485123) \
       - 0.179306476388491*relu(0.146664777624099*f_x1 - 0.795499460693267*f_x2 - 0.782897034383956*f_x3 - 0.277835745313809*f_x4 + 1.57155156941021) \
       + 0.963706701261077*relu(0.179114583699537*f_x1 - 1.94783442149019*f_x2 - 1.79864660314496*f_x3 + 1.40691592693506*f_x4 - 1.83845934659704)\
       - 0.393498957635352*relu(0.948903199713304*f_x1 - 1.06352865219377*f_x2 + 0.348577653264444*f_x3 - 2.03157792725149*f_x4 - 0.0842998106314543) \
       - 0.882203311667125*relu(1.1843721136302*f_x1 - 1.60618846527075*f_x2 + 1.22289035474955*f_x3 - 1.95031999477107*f_x4 + 1.81085797682436) \
       + 1.70719703662305*relu(3.07388659389659*f_x1 - 3.29160835539298*f_x2 - 1.87250017156491*f_x3 + 5.86326181700328*f_x4 + 0.0374100350433776) \
       - 0.342390288785141

print("start verify")
s = Solver()
s.add(And(0 <= x1, x1 <= 1, 1 <= x2, x2 <= 10,
          0 <= x3, x3 <= 0, 0 <= x4, x4 <= 0,
          (x2 - x1) * (x2 - x1) < 1,
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
# s = Solver()
# s.add(And(0 <= x1, x1 <= 10, 0 <= x2, x2 <= 10,
#           0 <= x3, x3 <= 0.1, 0 <= x4, x4 <= 0.1,
#           # -0.05 <= x5, x5 <= 0.05,-0.05 <= u, u <= 0.05,
#           (x2 - x1) * (x2 - x1) > 1.01*1.01,
#              B < 1),
#          )
# # print(s.check())
# if s.check() == sat: #check()方法用来判断是否有解，sat(satisify)表示满足有解
#     ans = s.model() #model()方法得到解
#     print(s.check())
#     print(ans)
# else:
#     print("no ans!")


print("start verify")
#diff condition
s = Solver()
s.add(And(0 <= x1, x1 <= 10, 0 <= x2, x2 <= 10,
          0 <= x3, x3 <= 0.1, 0 <= x4, x4 <= 0.1,
          -0.05 <= x5, x5 <= 0.05,-0.05 <= u, u <= 0.05,
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