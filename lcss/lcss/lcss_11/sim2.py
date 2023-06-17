import numpy as np
from sympy import *


x1 = symbols("x1")  # 符号x，自变量
x2 = symbols("x2")
x3 = symbols("x3")
x4 = symbols("x4")
x5 = symbols("x5")
x6 = symbols("x6")



z = symbols("relu")

# y = 0.792*pow(x1-1,2)#公式
# apart(y,x1)



w1=np.array([
    [-0.14384338360528412, -0.19365812367091725, -0.7630815433491408, 0.5691910729185066, 0.5040765743715406,
     -1.6179561045451873],
    [-0.7821166802587907, 0.6125774684155862, -0.4145337121675724, -0.3364887400233039, 0.7261425955899949,
     -0.26089161829939345],
    [0.9633318044659209, -0.2068358608326355, 0.2991849386948364, -0.1118577370828062, 0.24221038085337537,
     -0.43159445827188486],
    [0.4453169395876828, 0.15995655444135326, -0.1453884272301132, 0.11224849299081477, -0.7538114637747114,
     0.47508818377969064],
    [0.820383246453341, -0.8285101930883471, -0.5965387566475783, -0.09108773338971618, 0.8610452583691415,
     -0.013341711394155605],
    [1.2393415618878467, -1.1318650474337628, 0.17704427750752968, 0.12883379713697873, 1.1008920727230762,
     -0.8784563614335105],
    [-0.822962133666937, 0.06296284341944892, 0.495193455396589, -0.3903889434762517, -0.30218197255019064,
     0.428790876465855],
    [-0.5052183400971474, -0.2734243928560281, 0.5781802089671461, 1.0423893589859479, -0.00919437950545891,
     0.0925599086902691],
    [-0.35854438012204304, 0.42483323575423654, -1.1352233156713503, 0.6704113473922563, 1.5676370522487233,
     -0.8465945926877901],
    [-0.0398260760173541, -0.003053679177571655, -0.13828414846047538, -1.2571555349014898, -0.8489015530057603,
     -1.0546297715819994],
    [-0.14878374090437474, 0.43200708633373514, -0.5748224406086729, -0.9989608664983523, -0.4405208142175,
     0.15625499111144298],
    [-0.15126797533970654, -0.4252318385535543, -0.06254600525747854, 0.7393047322611551, -0.910461616023621,
     -0.688608722408536],
    [-1.771629388083709, 1.0394665048237992, 0.16220878349024823, 0.6280406262043712, -0.6994730329700928,
     0.9859823789785512],
    [-0.7442951773062965, -0.5444145343822241, 0.4487429537188804, -0.45620534261128876, -1.058398163133986,
     0.3260001088388323],
    [-1.4432643080341434, -0.8900309560579303, 0.7369139936468676, -0.9757429875608774, 0.8812480614901215,
     1.2533339675122113],
    [0.276505171982443, 0.12476978505819561, -0.657510967372051, 1.877444890736601, 0.408590611236859,
     -0.05070767167114454]
]).T
b1= \
    [-0.22046306063062046, -1.2404873350279948, -0.9911975645716549, -0.33509743131257336, -0.5718468142420059,
     -0.5102801038487875, -1.1310987373033603, -0.9097098791238957, 0.7129799690935353, 0.3037672197690764,
     -0.9158387799125783, -1.260084891725497, 0.566265935319902, -0.7348276551111691, 0.8558247695946528,
     0.11095703040012911]

expr1 = z * (np.matmul([[x1,x2,x3,x4,x5,x6]],w1)+b1)
#expr1 = -0.0001711589065517019 *pow(expr1,4)+ -0.01447711943585072 *pow(expr1,3)+ 0.002849795794085815 *pow(expr1,2)+ 0.5071116596907747 *expr1+ -0.00508383030596129
# expr1_1 = 0.25 * expr1 * expr1 + 0.001
# expr1 = 0.5 * expr1 + pow(expr1_1,0.5)


w2 =np.array(
    [-1.4602927816084026, -0.13617974138076488, -0.5257368872140094, 0.0777713378236458, 0.4554650071992758,
     0.40751597513792975, -1.30618541738983, 0.05150583082145506, -0.06495819433563474, -1.0008932242617654,
     -0.015995002773688618, 0.8179395797343364, 0.44815143147569514, 0.12955638179759602, 0.005841518952169388,
     0.6841477842105249]
).T
b2=  [-0.07235212297552189]

expr2=np.matmul(expr1,w2)+b2
print(expr2)
# expr3 = simplify(expr2)
# print(expr3)