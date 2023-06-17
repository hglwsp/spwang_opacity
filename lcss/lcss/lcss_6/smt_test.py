from z3 import *
import torch.nn as nn

x1,x2,x3,x4,x5 = Reals('x1 x2 x3 x4 x5')
h = (x1 - x2) * (x1 - x2)

#relu
def relu(x):
    res = If(x>0,x,0)
    return res




#controller
u = 0.832433007700432*relu(-1.12456409524418*x1 - 0.263179175136874*x2 + 0.433022184894504*x3 + 0.815551504531684*x4 + 0.680434967945528*x5 + 2.37311805020158) \
    - 1.30184791837149*relu(-0.171927308019478*x1 - 1.34090004512726*x2 - 0.0588668607724427*x3 + 0.94902105143312*x4 + 2.63458457624514*x5 + 0.577266599724117) \
    + 0.00456800060890005*relu(0.136393078088464*x1 - 0.295607274075329*x2 + 0.594882946881839*x3 - 0.281342452546535*x4 + 1.53847320299925*x5 - 0.61273057235153) \
    + 0.0057011129291951*relu(0.201534118824842*x1 - 0.64914926298727*x2 - 0.0530429007910108*x3 + 0.0859172131735381*x4 + 0.676285912775779*x5 - 0.128290103204473) \
    + 0.246595566613335*relu(0.20478596191026*x1 - 0.615166896256835*x2 + 1.15844408862393*x3 + 0.620583999006847*x4 - 0.228041032568787*x5 - 0.827343234343067)\
    - 0.168634905332023*relu(0.2939550596634*x1 - 1.44972011391949*x2 - 1.14269208876186*x3 - 0.70509690046894*x4 + 0.682917501567917*x5 - 0.389893486993104) \
    - 0.00266579350916666*relu(0.404087619510594*x1 - 1.60927191658007*x2 + 1.64489959772563*x3 - 0.0555268106093291*x4 + 0.729299798372966*x5 - 0.19034402197673) \
    + 0.216529923921669*relu(0.543209569741348*x1 - 2.52050813295566*x2 + 1.09365981877348*x3 - 0.993761856253931*x4 + 0.0218198270090313*x5 - 0.60454876658351) \
    - 0.0499870184989014


#system
f_x1 = x1 + x3 + 0.5 * x5
f_x2 = x2 + x4 + 0.5 * u
f_x3 = x3 + x5
f_x4 = x4 + u

#barrier
B = 0.171421531709435*relu(-1.11046104201459*x1 - 0.0429018780446157*x2 - 0.668133912025131*x3 - 0.559078078745575*x4 + 0.34222349768835) \
    + 0.370783733619935*relu(-0.754331164696267*x1 + 0.0781975441613557*x2 - 0.000684199812701952*x3 + 0.205681898039798*x4 - 0.117126714701871) \
    - 0.0281277784320569*relu(-0.685253729342021*x1 - 0.794735877033946*x2 - 0.232374418852627*x3 - 0.522762401154525*x4 - 0.678299686825973) \
    - 0.4756301556869*relu(-0.525870423022494*x1 + 0.0290708165422955*x2 - 0.232796221376759*x3 + 0.00129566712567777*x4 + 0.55818885875868)\
    + 0.0852923708787852*relu(-0.371632648816771*x1 - 0.0605971518647636*x2 + 0.367497785007348*x3 + 0.335507230440722*x4 + 0.183113023093721)\
    + 0.232033181915253*relu(-0.185976337972576*x1 + 0.326289630764087*x2 + 0.814317986420176*x3 - 0.42729995829042*x4 + 0.130632661206557)\
    - 0.502854964074462*relu(-0.0992717598784976*x1 + 0.04958080156546*x2 + 0.702499872742331*x3 - 0.162690826743752*x4 - 0.333759392757669)\
    + 0.448777820042357*relu(-0.0431379988500844*x1 - 0.437949763670654*x2 + 0.0110659798696593*x3 + 0.736534386108853*x4 - 0.438335340362051)\
    + 0.453832683173586*relu(-0.0268118876831194*x1 + 0.548278241277263*x2 - 0.65134124408807*x3 + 1.30214930276518*x4 - 0.260475142756586)\
    + 0.118736021573519*relu(0.049613629699187*x1 - 0.551404733489632*x2 - 0.366216761851526*x3 - 0.330424616382733*x4 - 0.19092986627983)\
    - 0.00841420768685923*relu(0.11846122794484*x1 - 0.0879629172497863*x2 + 0.102081717028951*x3 + 0.00489748678553396*x4 + 0.0682555917901156) \
    + 0.381245013235469*relu(0.269902830236604*x1 - 1.07634780518328*x2 + 0.114471780107926*x3 + 0.358475415070586*x4 - 0.29334185741474) \
    - 0.422788294143531*relu(0.737801881253611*x1 - 0.817074862688695*x2 - 0.717589386587659*x3 + 0.73620466957271*x4 + 1.20579318629734) \
    - 0.210583846967856*relu(0.747018602832464*x1 - 0.49090409084326*x2 - 0.356836909132612*x3 - 0.0481782732466592*x4 + 0.0484796885867729) \
    - 0.460782643240568*relu(0.803989213594415*x1 - 0.578498092924885*x2 - 1.64494070452766*x3 - 0.436305249604547*x4 + 0.316013792542674) \
    + 1.41030217083297*relu(1.33939586466372*x1 - 0.997482102718597*x2 - 0.0156271818253995*x3 + 0.566421674794753*x4 - 0.378749737740602) \
    + 0.417974411417338

B_f =  0.171421531709435*relu(-1.11046104201459*f_x1 - 0.0429018780446157*f_x2 - 0.668133912025131*f_x3 - 0.559078078745575*f_x4 + 0.34222349768835) \
       + 0.370783733619935*relu(-0.754331164696267*f_x1 + 0.0781975441613557*f_x2 - 0.000684199812701952*f_x3 + 0.205681898039798*f_x4 - 0.117126714701871)\
       - 0.0281277784320569*relu(-0.685253729342021*f_x1 - 0.794735877033946*f_x2 - 0.232374418852627*f_x3 - 0.522762401154525*f_x4 - 0.678299686825973) \
       - 0.4756301556869*relu(-0.525870423022494*f_x1 + 0.0290708165422955*f_x2 - 0.232796221376759*f_x3 + 0.00129566712567777*f_x4 + 0.55818885875868) \
       + 0.0852923708787852*relu(-0.371632648816771*f_x1 - 0.0605971518647636*f_x2 + 0.367497785007348*f_x3 + 0.335507230440722*f_x4 + 0.183113023093721)\
       + 0.232033181915253*relu(-0.185976337972576*f_x1 + 0.326289630764087*f_x2 + 0.814317986420176*f_x3 - 0.42729995829042*f_x4 + 0.130632661206557) \
       - 0.502854964074462*relu(-0.0992717598784976*f_x1 + 0.04958080156546*f_x2 + 0.702499872742331*f_x3 - 0.162690826743752*f_x4 - 0.333759392757669) \
       + 0.448777820042357*relu(-0.0431379988500844*f_x1 - 0.437949763670654*f_x2 + 0.0110659798696593*f_x3 + 0.736534386108853*f_x4 - 0.438335340362051) \
       + 0.453832683173586*relu(-0.0268118876831194*f_x1 + 0.548278241277263*f_x2 - 0.65134124408807*f_x3 + 1.30214930276518*f_x4 - 0.260475142756586) \
       + 0.118736021573519*relu(0.049613629699187*f_x1 - 0.551404733489632*f_x2 - 0.366216761851526*f_x3 - 0.330424616382733*f_x4 - 0.19092986627983)\
       - 0.00841420768685923*relu(0.11846122794484*f_x1 - 0.0879629172497863*f_x2 + 0.102081717028951*f_x3 + 0.00489748678553396*f_x4 + 0.0682555917901156)\
       + 0.381245013235469*relu(0.269902830236604*f_x1 - 1.07634780518328*f_x2 + 0.114471780107926*f_x3 + 0.358475415070586*f_x4 - 0.29334185741474) \
       - 0.422788294143531*relu(0.737801881253611*f_x1 - 0.817074862688695*f_x2 - 0.717589386587659*f_x3 + 0.73620466957271*f_x4 + 1.20579318629734) \
       - 0.210583846967856*relu(0.747018602832464*f_x1 - 0.49090409084326*f_x2 - 0.356836909132612*f_x3 - 0.0481782732466592*f_x4 + 0.0484796885867729) \
       - 0.460782643240568*relu(0.803989213594415*f_x1 - 0.578498092924885*f_x2 - 1.64494070452766*f_x3 - 0.436305249604547*f_x4 + 0.316013792542674) \
       + 1.41030217083297*relu(1.33939586466372*f_x1 - 0.997482102718597*f_x2 - 0.0156271818253995*f_x3 + 0.566421674794753*f_x4 - 0.378749737740602) \
       + 0.417974411417338

print("start verify")
s = Solver()
s.add(And(2 <= x1, x1 <= 2.8, 2.8 <= x2, x2 == x1 + 0.7,
          x3 == 0, x4 == 0,
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
s.add(And(2 <= x1, x1 <= 10, 2 <= x2, x2 <= 10,
          -0.2 <= x3, x3 <= 0, -0.2 <= x4, x4 <= 0,
          (x2 - x1) * (x2 - x1) > 1.5*1.5,
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
s.add(And(2 <= x1, x1 <= 10, 2 <= x2, x2 <= 10,
          -0.2 <= x3, x3 <= 0, -0.2 <= x4, x4 <= 0,
          -0.05 <= x5, x5 <= -0.03,-0.05 <= u, u <= -0.03,
          2 <= f_x1, f_x1 <= 10, 2 <= f_x2, f_x2 <= 10,
          -0.2 <= f_x3, f_x3 <= 0, -0.2 <= f_x4, f_x4 <= 0,
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