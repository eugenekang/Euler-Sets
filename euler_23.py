"""
Non-Abundant Sums

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
INCOMPLETE?
- Seems to perform the sieving on nonabsum integers but takes a while.
*NOTE* As per Wolfram, it seems that actually every number greater than 20161 can be expresed as a sum of two abundant numbers, so I will decrease the limit accordingly from 28123 to 20161.
 - Reference: https://mathworld.wolfram.com/AbundantNumber.html
"""
from Tools.common_tools import get_proper_divisors, get_sum_list, is_prime

# Find Abundant Sums < 20161
# This gets the list of sums, but is also fairly slow.
def get_abundant_sums(start, end):
    for x in range(start, end):
        if get_sum_list(get_proper_divisors(x)) > x:
            yield x

# Sum of all sums
def get_non_absum_int(start, end, list_of_absums):

    for x in range(start, end): # Iterate through the range of positive integers you want to filter.
        diff = 0
        flag = True
        for absum in list_of_absums:
            if x > absum:
                diff = x - absum #determine the difference
                if diff in list_of_absums: # check if the difference is a positive sum as well
                    flag = False
        if flag == True:
            yield x
            

if __name__ == "__main__":
    
    array = [12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72, 78, 80, 84, 88, 90, 96, 100, 102, 104, 108, 112, 114, 120, 126, 132, 138, 140, 144, 150, 156, 160, 162, 168, 174, 176, 180, 186, 192, 196, 198, 200, 204, 208, 210, 216, 220, 222, 224, 228, 234, 240, 246, 252, 258, 260, 264, 270, 272, 276, 280, 282, 288, 294, 300, 304, 306, 308, 312, 318, 320, 324, 330, 336, 340, 342, 348, 350, 352, 354, 360, 364, 366, 368, 372, 378, 380, 384, 390, 392, 396, 400, 402, 408, 414, 416, 420, 426, 432, 438, 440, 444, 448, 450, 456, 460, 462, 464, 468, 474, 476, 480, 486, 490, 492, 498, 500, 504, 510, 516, 520, 522, 528, 532, 534, 540, 544, 546, 550, 552, 558, 560, 564, 570, 572, 576, 580, 582, 588, 594, 600, 606, 608, 612, 616, 618, 620, 624, 630, 636, 640, 642, 644, 648, 650, 654, 660, 666, 672, 678, 680, 684, 690, 696, 700, 702, 704, 708, 714, 720, 726, 728, 732, 736, 738, 740, 744, 748, 750, 756, 760, 762, 768, 770, 774, 780, 784, 786, 792, 798, 800, 804, 810, 812, 816, 820, 822, 828, 832, 834, 836, 840, 846, 852, 858, 860, 864, 868, 870, 876, 880, 882, 888, 894, 896, 900, 906, 910, 912, 918, 920, 924, 928, 930, 936, 940, 942, 945, 948, 952, 954, 960, 966, 968, 972, 978, 980, 
984, 990, 992, 996, 1000, 1002, 1008, 1014, 1020, 1026, 1032, 1036, 1038, 1040, 1044, 1050, 1056, 1060, 1062, 1064, 1068, 1074, 1080, 1086, 1088, 1092, 1098, 1100, 1104, 1110, 1116, 1120, 1122, 1128, 1134, 1140, 1144, 1146, 1148, 1152, 1158, 1160, 1164, 1170, 1176, 1180, 1182, 1184, 1188, 1190, 1194, 1200, 1204, 1206, 1212, 1216, 1218, 1220, 1224, 1230, 1232, 1236, 1240, 1242, 1248, 1254, 1260, 1266, 1272, 1278, 1280, 1284, 1288, 1290, 1296, 1300, 1302, 1308, 1312, 1314, 1316, 1320, 1326, 1330, 1332, 1338, 1340, 1344, 1350, 1352, 1356, 1360, 1362, 1368, 1372, 1374, 1376, 1380, 1386, 1392, 1398, 1400, 1404, 1408, 1410, 1416, 1420, 1422, 1428, 1430, 1434, 1440, 1446, 1452, 1456, 1458, 1460, 1464, 1470, 1472, 1476, 1480, 1482, 1484, 1488, 1494, 1496, 1500, 1504, 1506, 1512, 1518, 1520, 1524, 1530, 1536, 1540, 1542, 1548, 1554, 1560, 1566, 1568, 1572, 1575, 1578, 1580, 1584, 1590, 1596, 1600, 1602, 1608, 1610, 1614, 1620, 1624, 1626, 1632, 1638, 1640, 1644, 1650, 1652, 1656, 1660, 1662, 1664, 1668, 1672, 1674, 1680, 1686, 1692, 1696, 1698, 1700, 1704, 1708, 1710, 1716, 1720, 1722, 1728, 1734, 1736, 1740, 1746, 1750, 1752, 1758, 1760, 1764, 1768, 1770, 1776, 1780, 1782, 1788, 1792, 1794, 1800, 1806, 1812, 1818, 1820, 1824, 1830, 1836, 1840, 1842, 1848, 1854, 1856, 1860, 1866, 1870, 1872, 1876, 1878, 1880, 1884, 1888, 1890, 1896, 1900, 1902, 1904, 1908, 1914, 1920, 1926, 1932, 1936, 1938, 1940, 1944, 1950, 1952, 1956, 1960, 1962, 1968, 1974, 1976, 1980, 1984, 1986, 1988, 1992, 1998, 2000, 2002, 2004, 2010, 2016, 2020, 2022, 2024, 2028, 2030, 2034, 2040, 2044, 2046, 2052, 2058, 2060, 2064, 2070, 2072, 2076, 2080, 2082, 2088, 2090, 2094, 2100, 2106, 2112, 2118, 2120, 2124, 2128, 2130, 2136, 2140, 2142, 2148, 2154, 2156, 2160, 2166, 2170, 2172, 2176, 2178, 2180, 2184, 2190, 2196, 2200, 2202, 2205, 2208, 2210, 2212, 2214, 2220, 2226, 2232, 2238, 2240, 2244, 2250, 2256, 2260, 2262, 2268, 2274, 2280, 2286, 2288, 2292, 2296, 2298, 2300, 2304, 2310, 2316, 2320, 2322, 2324, 2328, 2334, 2340, 2346, 2352, 2358, 2360, 2364, 2368, 2370, 2376, 2380, 2382, 2388, 2392, 2394, 2400, 2406, 2408, 2412, 2418, 2420, 2424, 2430, 2432, 2436, 2440, 2442, 2448, 2450, 2454, 2460, 2464, 2466, 2470, 2472, 2478, 2480, 2484, 2490, 2492, 2496, 2500, 2502, 2508, 2514, 2520, 2526, 2530, 2532, 2538, 2540, 2544, 2548, 2550, 2552, 2556, 2560, 2562, 2568, 2574, 2576, 2580, 2584, 2586, 2590, 2592, 2598, 2600, 2604, 2610, 2616, 2620, 2622, 2624, 2628, 2632, 2634, 2640, 2646, 2652, 2658, 2660, 2664, 2670, 2676, 2680, 2682, 2688, 2694, 2700, 2704, 2706, 2712, 2716, 2718, 2720, 2724, 2728, 2730, 2736, 2740, 2742, 2744, 2748, 2750, 2752, 2754, 2760, 2766, 2772, 2778, 2780, 2784, 2790, 2796, 2800, 2802, 2808, 2814, 2816, 2820, 2826, 2828, 2832, 2835, 2838, 2840, 2844, 2850, 2856, 2860, 2862, 2868, 2870, 2874, 2880, 2884, 2886, 2892, 2898, 2900, 2904, 2910, 2912, 2916, 2920, 2922, 2928, 2934, 2940, 2944, 2946, 2952, 2958, 2960, 2964, 2968, 2970, 2976, 2980, 2982, 2988, 2990, 2992, 2994, 2996, 3000, 3006, 3008, 3010, 3012, 3016, 3018, 3020, 3024, 3030, 3036, 3040, 3042, 3048, 3052, 3054, 3060, 3066, 3072, 3078, 3080, 3084, 3090, 3096, 3100, 3102, 3108, 3114, 3120, 3126, 3128, 3132, 3136, 3138, 3140, 3144, 3150, 3156, 3160, 3162, 3164, 3168, 3174, 3180, 3186, 3190, 3192, 3198, 3200, 3204, 3210, 3216, 3220, 3222, 3224, 3228, 3230, 3234, 3240, 3246, 3248, 3250, 3252, 3256, 3258, 3260, 3264, 3270, 3276, 3280, 3282, 3288, 3290, 3294, 3300, 3304, 3306, 3312, 3318, 3320, 3324, 3328, 3330, 3332, 3336, 3340, 3342, 3344, 3348, 3354, 3360, 3366, 3372, 3378, 3380, 3384, 3388, 3390, 3392, 3396, 3400, 3402, 3408, 3410, 3414, 3416, 3420, 3426, 3430, 3432, 3438, 3440, 3444, 3450, 3456, 3460, 3462, 3465, 3468, 3472, 3474, 3480, 3486, 3492, 3496, 3498, 3500, 3504, 3510, 3516, 3520, 3522, 3528, 3534, 3536, 3540, 3546, 3552, 3556, 3558, 3560, 3564, 3570, 3576, 3580, 3582, 3584, 3588, 3594, 3600, 3606, 3608, 3612, 3618, 3620, 3624, 3630, 3636, 3640, 3642, 3648, 3654, 3660, 3666, 3668, 3672, 3678, 3680, 3684, 3690, 3696, 3700, 3702, 3708, 3710, 3712, 3714, 3720, 3724, 3726, 3732, 3738, 3740, 3744, 3750, 3752, 3756, 3760, 3762, 3768, 3770, 3774, 3776, 3780, 3784, 3786, 3792, 3798, 3800, 3804, 3808, 3810, 3816, 3820, 3822, 3828, 3834, 3836, 3840, 3846, 3848, 3850, 3852, 3858, 3860, 3864, 3870, 3872, 3876, 3880, 3882, 3888, 3892, 3894, 3900, 3904, 3906, 3912, 3918, 3920, 3924, 3930, 3936, 3940, 3942, 3944, 3948, 3952, 3954, 3960, 3966, 3968, 3972, 3976, 3978, 3980, 3984, 3990, 3996, 4000, 4002, 4004, 4008, 4014, 4020, 4026, 4030, 4032, 4038, 4040, 4044, 4048, 4050, 4056, 4060, 4062, 4068, 4070, 4074, 4080, 4086, 4088, 4092, 4095, 4098, 4100, 4104, 4110, 4116, 4120, 4122, 4128, 4130, 4134, 4136, 4140, 4144, 4146, 4152, 4158, 4160, 4164, 4170, 4172, 4176, 4180, 4182, 4188, 4194, 4200, 4206, 4212, 4216, 4218, 4220, 4224, 4228, 4230, 4236, 4240, 4242, 4248, 4254, 4256, 4260, 4264, 4266, 4270, 4272, 4278, 4280, 4284, 4288, 4290, 4296, 4300, 4302, 4308, 4312, 4314, 4320, 4326, 4332, 4338, 4340, 4344, 4350, 4352, 4356, 4360, 4362, 4368, 4374, 4380, 4386, 4392, 4396, 4398, 4400, 4404, 4408, 4410, 4416, 4420, 4422, 4424, 4428, 4434, 4440, 4446, 4452, 4458, 4460, 4464, 4470, 4472, 4476, 4480, 4482, 4488, 4494, 4500, 4506, 4508, 4510, 4512, 4518, 4520, 4524, 4530, 4536, 4540, 4542, 4544, 4548, 4550, 4554, 4560, 4564, 4566, 4572, 4576, 4578, 4580, 4584, 4590, 4592, 4596, 4600, 4602, 4608, 4614, 4620, 4624, 4626, 4632, 4638, 4640, 4644, 4648, 4650, 4656, 4660, 4662, 4664, 4668, 4672, 4674, 4676, 4680, 4686, 4690, 4692, 4698, 4700, 4704, 4710, 4712, 4716, 4720, 4722, 4725, 4728, 4730, 4732, 4734, 4736, 4740, 4746, 4752, 4758, 4760, 4764, 4770, 4776, 4780, 4782, 4784, 4788, 4794, 4800, 4806, 4812, 4816, 4818, 4820, 4824, 4830, 4836, 4840, 4842, 4844, 4848, 4854, 4860, 4864, 4866, 4872, 4878, 4880, 4884, 4888, 4890, 4896, 4900, 4902, 4908, 4914, 4920, 4926, 4928, 4932, 4938, 4940, 4944, 4950, 4956, 4960, 4962, 4968, 4970, 4974, 4980, 4984, 4986, 4992, 4998, 5000, 5004, 5010, 5012, 5016, 5020, 5022, 5028, 5032, 5034, 5040, 5046, 5052, 5056, 5058, 5060, 5064, 5068, 5070, 5076, 5080, 5082, 5088, 5094, 5096, 5100, 5104, 5106, 5110, 5112, 5118, 5120, 5124, 5130, 5136, 5140, 5142, 5148, 5152, 5154, 5160, 5166, 5168, 5170, 5172, 5178, 5180, 5184, 5190, 5192, 5196, 5200, 5202, 5208, 5214, 5220, 5226, 5232, 5236, 5238, 5240, 5244, 5248, 5250, 5256, 5260, 5262, 5264, 5268, 5274, 5280, 5286, 5292, 5298, 5300, 5304, 5310, 5312, 5316, 5320, 5322, 5328, 5334, 5336, 5340, 5346, 5348, 5352, 5355, 5358, 5360, 5364, 5368, 5370, 5376, 5380, 5382, 5388, 5390, 5394, 5400, 5404, 5406, 5408, 5412, 5418, 5420, 5424, 5430, 5432, 5436, 5440, 5442, 5448, 5454, 5456, 5460, 5466, 5472, 5478, 5480, 5484, 5488, 5490, 5496, 5500, 5502, 5504, 5508, 5512, 5514, 5516, 5520, 5526, 5530, 5532, 5538, 5540, 5544, 5550, 5556, 5560, 5562, 5568, 5572, 5574, 5576, 5580, 5586, 5592, 5598, 5600, 5604, 5610, 5616, 5620, 5622, 5624, 5628, 5632, 5634, 5640, 5646, 5652, 5656, 5658, 5660, 5664, 5670, 5676, 5680, 5682, 5684, 5688, 5694, 5696, 5700, 5704, 5706, 5712, 5718, 5720, 5724, 5730, 5736, 5740, 5742, 5748, 5754, 5760, 5766, 5768, 5772, 5775, 5776, 5778, 5780, 5784, 5790, 5796, 5800, 5802, 5808, 5810, 5814, 5820, 5824, 5826, 5830, 5832, 5838, 5840, 5844, 5848, 5850, 5852, 5856, 5860, 5862, 5868, 5874, 5880, 5886, 5888, 5892, 5896, 5898, 5900, 5904, 5908, 5910, 5916, 5920, 5922, 5928, 5934, 5936, 5940, 5946, 5950, 5952, 5958, 5960, 5964, 5970, 5976, 5980, 5982, 5984, 5985, 5988, 5992, 5994, 6000, 6006, 6012, 6016, 6018, 6020, 6024, 6030, 6032, 6036, 6040, 6042, 6048, 6050, 6054, 6060, 6066, 6072, 6076, 6078, 6080, 6084, 6090, 6096, 6100, 6102, 6104, 6108, 6114, 6120, 6126, 6132, 6136, 6138, 6140, 6144, 6150, 6156, 6160, 6162, 6168, 6174, 6180, 6186, 6188, 6192, 6198, 6200, 6204, 6208, 6210, 6216, 6220, 6222, 6228, 6230, 6232, 6234, 6240, 6244, 6246, 6248, 6252, 6256, 6258, 6260, 6264, 6270, 6272, 6276, 6280, 6282, 6288, 6292, 6294, 6300, 6306, 6312, 6318, 6320, 6324, 6328, 6330, 6336, 6340, 6342, 6344, 6348, 6354, 6356, 6360, 6366, 6370, 6372, 6378, 6380, 6384, 6390, 6392, 6396, 6400, 6402, 6408, 6412, 6414, 6420, 6424, 6426, 6432, 6435, 6438, 6440, 6444, 6448, 6450, 6456, 6460, 6462, 6464, 6468, 6474, 6480, 6486, 6492, 6496, 6498, 6500, 6504, 6510, 6512, 6516, 6520, 6522, 6524, 6528, 6534, 6536, 6540, 6546, 6552, 6558, 6560, 6564, 6570, 6576, 6580, 6582, 6588, 6592, 6594, 6600, 6606, 6608, 6612, 6615, 6618, 6620, 6624, 6630, 6636, 6640, 6642, 6648, 6650, 6654, 6656, 6660, 6664, 6666, 6672, 6678, 6680, 6684, 6688, 6690, 6692, 6696, 6700, 6702, 6708, 6714, 6720, 6726, 6732, 6738, 6740, 6744, 6748, 6750, 6756, 6760, 6762, 6768, 6774, 6776, 6780, 6784, 6786, 6790, 6792, 6798, 6800, 6804, 6808, 6810, 6816, 6820, 6822, 6825, 6828, 6832, 6834, 6840, 6846, 6848, 6852, 6858, 6860, 6864, 6870, 6876, 6880, 6882, 6888, 6894, 6900, 6906, 6912, 6916, 6918, 6920, 6924, 6930, 6936, 6940, 6942, 6944, 6948, 6952, 6954, 6960, 6966, 6968, 6972, 6976, 6978, 6980, 6984, 6990, 6992, 6996, 7000, 7002, 7008, 7014, 7020, 7026, 7028, 7032, 7038, 7040, 7044, 7050, 7056, 7060, 7062, 7068, 7070, 7072, 7074, 7080, 7084, 7086, 7092, 7098, 7100, 7104, 7110, 7112, 7116, 7120, 7122, 7128, 7134, 7140, 7144, 7146, 7150, 7152, 7158, 7160, 7164, 7168, 7170, 7176, 7180, 7182, 7188, 7192, 7194, 7196, 7200, 7206, 7208, 7210, 7212, 7216, 7218, 7220, 7224, 7230, 7232, 7236, 7240, 7242, 7245, 7248, 7252, 7254, 7260, 7266, 7272, 7278, 7280, 7284, 7290, 7296, 7300, 7302, 7304, 7308, 7314, 7320, 7326, 7332, 7336, 7338, 7340, 7344, 7350, 7356, 7360, 7362, 7364, 7368, 7374, 7380, 7384, 7386, 7392, 7398, 7400, 7404, 7410, 7416, 7420, 7422, 7424, 7425, 7428, 7434, 7436, 7440, 7446, 7448, 7452, 7458, 7460, 7464, 7470, 7476, 7480, 7482, 7488, 7490, 7494, 7500, 7504, 7506, 7512, 7518, 7520, 7524, 7530, 7532, 7536, 7540, 7542, 7544, 7548, 7552, 7554, 7560, 7566, 7568, 7572, 7578, 7580, 7584, 7588, 7590, 7592, 7596, 7600, 7602, 7608, 7614, 7616, 7620, 7626, 7630, 7632, 7638, 7640, 7644, 7650, 7656, 7660, 7662, 7668, 7672, 7674, 7680, 7686, 7692, 7696, 7698, 7700, 7704, 7710, 7716, 7720, 7722, 7728, 7734, 7740, 7744, 7746, 7752, 7756, 7758, 7760, 7764, 7770, 7776, 7780, 7782, 7784, 7788, 7794, 7800, 7806, 7808, 7812, 7818, 7820, 7824, 7830, 7832, 7836, 7840, 7842, 7848, 7854, 7860, 7866, 7868, 7872, 7875, 7878, 7880, 7884, 7888, 7890, 7896, 7900, 7902, 7904, 7908, 7910, 7912, 7914, 7920, 7924, 7926, 7932, 7936, 7938, 7940, 7944, 7950, 7952, 7956, 7960, 7962, 7968, 7974, 7980, 7986, 7992, 7998, 8000, 8004, 8008, 8010, 8016, 8020, 8022, 8024, 8028, 8034, 8036, 8040, 8046, 8050, 8052, 8056, 8058, 8060, 8064, 8070, 8076, 8080, 8082, 8085, 8088, 8092, 8094, 8096, 8100, 8106, 8112, 8118, 8120, 8124, 8130, 8136, 8140, 8142, 8148, 8154, 8160, 8166, 8172, 8176, 8178, 8180, 8184, 8190, 8196, 8200, 8202, 8204, 8208, 8214, 8216, 8220, 8226, 8228, 8232, 8238, 8240, 8244, 8250, 8256, 8260, 8262, 8268, 8272, 8274, 8280, 8286, 8288, 8292, 8296, 8298, 8300, 8304, 8310, 8316, 8320, 8322, 8328, 8330, 8334, 8340, 8344, 8346, 8352, 8358, 8360, 8364, 8370, 8372, 8376, 8380, 8382, 8388, 8394, 8400, 8406, 8412, 8415, 8418, 8420, 8424, 8428, 8430, 8432, 8436, 8440, 8442, 8448, 8450, 8454, 8456, 8460, 8464, 8466, 8470, 8472, 8478, 8480, 8484, 8490, 8496, 8500, 8502, 8505, 8508, 8512, 8514, 8520, 8526, 8528, 8532, 8536, 8538, 8540, 8544, 8550, 8556, 8560, 8562, 8568, 8574, 8576, 8580, 8586, 8592, 8596, 8598, 8600, 8604, 8610, 8616, 8620, 8622, 8624, 8628, 8632, 8634, 8640, 8646, 8652, 8658, 8660, 8664, 8670, 8676, 8680, 8682, 8688, 8694, 8700, 8704, 8706, 8708, 8712, 8718, 8720, 8724, 8730, 8736, 8740, 8742, 8748, 8750, 8754, 8760, 8764, 8766, 8772, 8778, 8780, 8784, 8790, 8792, 8796, 8800, 8802, 8808, 8814, 8816, 8820, 8826, 8832, 8838, 8840, 8844, 8848, 8850, 8856, 8860, 8862, 8868, 8874, 8876, 8880, 8886, 8888, 8890, 8892, 8898, 8900, 8904, 8910, 8916, 8920, 8922, 8925, 8928, 8932, 8934, 8940, 8944, 8946, 8952, 8958, 8960, 8964, 8968, 8970, 8976, 8980, 8982, 8988, 8994, 9000, 9006, 9012, 9016, 9018, 9020, 9024, 9030, 9036, 9040, 9042, 9044, 9048, 9054, 9060, 9064, 9066, 9072, 9078, 9080, 9084, 9088, 9090, 9096, 9100, 9102, 9108, 9112, 9114, 9120, 9126, 9128, 9132, 9135, 9138, 9140, 9144, 9150, 9152, 9156, 9160, 9162, 9168, 9170, 9174, 9180, 9184, 9186, 9192, 9196, 9198, 9200, 9204, 9210, 9212, 9216, 9220, 9222, 9228, 9234, 9240, 9246, 9248, 9252, 9256, 9258, 9260, 9264, 9268, 9270, 9272, 9276, 9280, 9282, 9288, 9294, 9296, 9300, 9306, 9310, 9312, 9318, 9320, 9324, 9328, 9330, 9336, 9340, 9342, 9344, 9348, 9350, 9352, 9354, 9360, 9366, 9372, 9378, 9380, 9384, 9390, 9396, 9400, 9402, 9408, 9414, 9416, 9420, 9424, 9426, 9432, 9436, 9438, 9440, 9444, 9450, 9456, 9460, 9462, 9464, 9468, 9472, 9474, 9480, 9486, 9492, 9498, 9500, 9504, 9510, 9516, 9520, 9522, 9528, 9534, 9540, 9546, 9548, 9552, 9555, 9558, 9560, 9564, 9568, 9570, 9576, 9580, 9582, 9588, 9590, 9592, 9594, 9600, 9604, 9606, 9612, 9618, 9620, 9624, 9630, 9632, 9636, 9640, 9642, 9648, 9654, 9656, 9660, 9666, 9672, 9678, 9680, 9684, 9688, 9690, 9696, 9700, 9702, 9708, 9714, 9716, 9720, 9724, 9726, 9728, 9730, 9732, 9738, 9740, 9744, 9750, 9756, 9760, 9762, 9765, 9768, 9772, 9774, 9776, 9780, 9786, 9792, 9798, 9800, 9804, 9810, 9816, 9820, 9822, 9828, 9834, 9840, 9846, 9852, 9856, 9858, 9860, 9864, 9870, 9876, 9880, 9882, 9884, 9888, 9894, 9900, 9906, 9912, 9918, 9920, 9924, 9928, 9930, 9936, 9940, 9942, 9944, 9948, 9954, 9960, 9966, 9968, 9972, 9978, 9980, 9984, 9990, 9996, 10000, 10002, 10008, 10010, 10014, 10020, 10024, 10026, 10032, 10038, 10040, 10044, 10050, 10052, 10056, 10060, 10062, 10064, 10068, 10074, 10080, 10086, 10088, 10092, 10098, 10100, 10104, 10108, 10110, 10112, 10116, 10120, 10122, 10128, 10134, 10136, 10140, 10146, 10150, 10152, 10158, 10160, 10164, 10170, 10176, 10180, 10182, 10184, 10188, 10192, 10194, 10200, 10206, 10208, 10212, 10218, 10220, 10224, 10230, 10236, 10240, 10242, 10248, 10254, 10260, 10266, 10272, 10276, 10278, 10280, 10284, 10290, 10296, 
10300, 10302, 10304, 10308, 10314, 10320, 10326, 10332, 10336, 10338, 10340, 10344, 10350, 10356, 10360, 10362, 10368, 10374, 10380, 10384, 10386, 10388, 10392, 10395, 10398, 10400, 10404, 10410, 10416, 10420, 10422, 10428, 10430, 10434, 10440, 10444, 10446, 10450, 10452, 10458, 10460, 10464, 10470, 10472, 10476, 10480, 10482, 10488, 10494, 10496, 10500, 10504, 10506, 10512, 10518, 10520, 10524, 10528, 10530, 10536, 10540, 10542, 10548, 10554, 10556, 10560, 10566, 10570, 10572, 10578, 10580, 10584, 10590, 10596, 10600, 10602, 10608, 10612, 10614, 10620, 10624, 10626, 10632, 10638, 10640, 10644, 10648, 10650, 10656, 10660, 10662, 10668, 10672, 10674, 10680, 10686, 10692, 10696, 10698, 10700, 10704, 10710, 10712, 10716, 10720, 10722, 10724, 10728, 10734, 10736, 10740, 10744, 10746, 10752, 10758, 10760, 10764, 10770, 10776, 10780, 10782, 10788, 10792, 10794, 10800, 10806, 10808, 10812, 10816, 10818, 10820, 10824, 10830, 10836, 10840, 10842, 10848, 10850, 10854, 10860, 10864, 10866, 10868, 10872, 10878, 10880, 10884, 10890, 10892, 10896, 10900, 10902, 10908, 10912, 10914, 10920, 10926, 10932, 10938, 10940, 10944, 10948, 10950, 10956, 10960, 10962, 10968, 10974, 10976, 10980, 10986, 10990, 10992, 10998, 11000, 11004, 11008, 11010, 11016, 11020, 11022, 11024, 11025, 11028, 11032, 11034, 11040, 11046, 11050, 11052, 11058, 11060, 11064, 11070, 11076, 11080, 11082, 11088, 11094, 11096, 11100, 11106, 11112, 11116, 11118, 11120, 11124, 11128, 11130, 11132, 11136, 11140, 11142, 11144, 11148, 11152, 11154, 11160, 11166, 11172, 11176, 11178, 11180, 11184, 11190, 11196, 11200, 11202, 11208, 11214, 11220, 11226, 11228, 11232, 11238, 11240, 11244, 
11248, 11250, 11256, 11260, 11262, 11264, 11268, 11270, 11274, 11280, 11284, 11286, 11288, 11292, 11298, 11300, 11304, 11310, 11312, 11316, 11320, 11322, 11328, 11334, 11336, 11340, 11346, 11352, 11358, 11360, 11364, 11368, 11370, 11376, 11380, 11382, 11388, 11392, 11394, 11396, 11400, 11406, 11408, 11410, 11412, 11418, 11420, 11424, 11430, 11436, 11440, 11442, 11448, 11452, 11454, 11460, 11466, 11472, 11478, 11480, 11484, 11490, 11492, 11496, 11500, 11502, 11508, 11514, 11520, 11526, 11528, 11532, 11536, 11538, 11540, 11544, 11550, 11552, 11556, 11560, 11562, 11564, 11568, 11574, 11580, 11586, 11592, 11598, 11600, 11604, 11610, 11616, 11620, 11622, 11628, 11634, 11640, 11646, 11648, 11652, 11655, 11658, 11660, 11664, 11670, 11676, 11680, 11682, 11688, 11690, 11694, 11696, 11700, 11704, 11706, 11712, 11718, 11720, 11724, 11730, 11732, 11736, 11740, 11742, 11748, 11752, 11754, 11760, 11766, 11772, 11776, 11778, 11780, 11784, 11788, 11790, 11792, 11796, 11800, 11802, 11808, 11814, 11816, 11820, 11826, 11830, 11832, 11838, 11840, 11844, 11850, 11856, 11860, 11862, 11868, 11872, 11874, 11880, 11886, 11892, 11898, 11900, 11904, 11910, 11916, 11920, 11922, 11928, 11934, 11940, 11946, 11952, 11956, 11958, 11960, 11964, 11968, 11970, 11976, 11980, 11982, 11984, 11988, 11994, 12000, 12006, 12012, 12018, 12020, 12024, 12030, 12032, 12036, 12040, 12042, 12048, 12054, 12056, 12060, 12064, 12066, 12068, 12072, 12078, 12080, 12084, 12090, 12096, 12100, 12102, 12104, 12108, 12110, 12114, 12120, 12124, 12126, 12132, 12138, 12140, 12144, 12150, 12152, 12156, 12160, 12162, 12168, 12174, 12180, 12186, 12192, 12198, 12200, 12204, 12208, 12210, 12216, 
12220, 12222, 12228, 12232, 12234, 12236, 12240, 12246, 12250, 12252, 12258, 12260, 12264, 12270, 12272, 12276, 12280, 12282, 12285, 12288, 12292, 12294, 12300, 12306, 12312, 12318, 12320, 12324, 12330, 12336, 12340, 12342, 12348, 12350, 12354, 12360, 12366, 12372, 12376, 12378, 12380, 12384, 12390, 12396, 12400, 12402, 12404, 12408, 12414, 12416, 12420, 12426, 12432, 12438, 12440, 12444, 12450, 12456, 12460, 12462, 12464, 12468, 12474, 12480, 12486, 12488, 12492, 12496, 12498, 12500, 12504, 12510, 12512, 12516, 12520, 12522, 12528, 12530, 12534, 12540, 12544, 12546, 12552, 12558, 12560, 12564, 12570, 12572, 12576, 12580, 12582, 12584, 12588, 12594, 12600, 12606, 12612, 12618, 12620, 12624, 12628, 12630, 12636, 12640, 12642, 12648, 12650, 12654, 12656, 12660, 12666, 12670, 12672, 12678, 12680, 12684, 12688, 12690, 12696, 12700, 12702, 12705, 12708, 12712, 12714, 12716, 12720, 12726, 12732, 12738, 12740, 12744, 12750, 12756, 12760, 12762, 12768, 12774, 12780, 12784, 12786, 12792, 12796, 12798, 12800, 12804, 12810, 12816, 12820, 12822, 12824, 12828, 12834, 12840, 12846, 12848, 12852, 12858, 12860, 12864, 12870, 12876, 12880, 12882, 12888, 12894, 12896, 12900, 12906, 12908, 12912, 12915, 12918, 12920, 12924, 12928, 12930, 12936, 12940, 12942, 12948, 12950, 12954, 12960, 12964, 12966, 12972, 12978, 12980, 12984, 12990, 12992, 12996, 13000, 13002, 13008, 13014, 13020, 13024, 13026, 13032, 13038, 13040, 13044, 13048, 13050, 13056, 13060, 13062, 13068, 13072, 13074, 13076, 13080, 13086, 13090, 13092, 13098, 13100, 13104, 13110, 13112, 13116, 13120, 13122, 13128, 13132, 13134, 13140, 13146, 13152, 13156, 13158, 13160, 13164, 13170, 13176, 
13180, 13182, 13184, 13188, 13192, 13194, 13200, 13206, 13208, 13212, 13216, 13218, 13220, 13224, 13230, 13236, 13240, 13242, 13244, 13248, 13254, 13260, 13266, 13272, 13278, 13280, 13284, 13288, 13290, 13296, 13300, 13302, 13308, 13312, 13314, 13320, 13326, 13328, 13332, 13338, 13340, 13344, 13350, 13356, 13360, 13362, 13368, 13370, 13374, 13376, 13380, 13384, 13386, 13392, 13398, 13400, 13404, 13410, 13412, 13416, 13420, 13422, 13428, 13434, 13440, 13446, 13452, 13456, 13458, 13460, 13464, 13468, 13470, 13476, 13480, 13482, 13488, 13494, 13496, 13500, 13506, 13510, 13512, 13518, 13520, 13524, 13530, 13536, 13540, 13542, 13545, 13548, 13552, 13554, 13560, 13566, 13568, 13572, 13578, 13580, 13584, 13590, 13596, 13600, 13602, 13608, 13614, 13616, 13620, 13624, 13626, 13632, 13636, 13638, 13640, 13644, 13650, 13656, 13660, 13662, 13664, 13668, 13674, 13680, 13686, 13692, 13696, 13698, 13700, 13704, 13710, 13716, 13720, 13722, 13728, 13734, 13736, 13740, 13746, 13748, 13750, 13752, 13758, 13760, 13764, 13770, 13776, 13780, 13782, 13788, 13790, 13794, 13800, 13804, 13806, 13812, 13816, 13818, 13820, 13824, 13830, 13832, 13836, 13840, 13842, 13848, 13854, 13860, 13866, 13872, 13878, 13880, 13884, 13888, 13890, 13896, 13900, 13902, 13904, 13908, 13914, 13916, 13920, 13926, 13930, 13932, 13936, 13938, 13940, 13944, 13950, 13952, 13956, 13960, 13962, 13968, 13972, 13974, 13980, 13984, 13986, 13992, 13998, 14000, 14004, 14008, 14010, 14014, 14016, 14020, 14022, 14028, 14034, 14040, 14046, 14052, 14056, 14058, 14060, 14064, 14070, 14076, 14080, 14082, 14084, 14088, 14094, 14100, 14106, 14112, 14118, 14120, 14124, 14130, 14136, 14140, 14142, 
14144, 14148, 14154, 14160, 14166, 14168, 14172, 14175, 14178, 14180, 14184, 14190, 14196, 14200, 14202, 14208, 14210, 14212, 14214, 14220, 14224, 14226, 14232, 14238, 14240, 14244, 14248, 14250, 14252, 14256, 14260, 14262, 14268, 14274, 14280, 14286, 14288, 14292, 14298, 14300, 14304, 14308, 14310, 14316, 14320, 14322, 14328, 14334, 14336, 14340, 14344, 14346, 14350, 14352, 14358, 14360, 14364, 14370, 14376, 14380, 14382, 14384, 14388, 14392, 14394, 14400, 14406, 14412, 14416, 14418, 14420, 14424, 14430, 14432, 14436, 14440, 14442, 14448, 14454, 14456, 14460, 14464, 14466, 14472, 14476, 14478, 14480, 14484, 14490, 14496, 14500, 14502, 14504, 14508, 14514, 14520, 14526, 14532, 14538, 14540, 14544, 14550, 14552, 14556, 14560, 14562, 14568, 14574, 14580, 14586, 14588, 14592, 14598, 14600, 14604, 14608, 14610, 14616, 14620, 14622, 14628, 14630, 14634, 14640, 14644, 14646, 14652, 14658, 14660, 14664, 14670, 14672, 14676, 14680, 14682, 14688, 14694, 14696, 14700, 14706, 14712, 14718, 14720, 14724, 14728, 14730, 14736, 14740, 14742, 14748, 14754, 14756, 14760, 14766, 14768, 14770, 14772, 14778, 14780, 14784, 14790, 14796, 14800, 14802, 14805, 14808, 14812, 14814, 14820, 14824, 14826, 14832, 14838, 14840, 14844, 14848, 14850, 14856, 14860, 14862, 14868, 14872, 14874, 14880, 14886, 14892, 14896, 14898, 14900, 14904, 14910, 14916, 14920, 14922, 14924, 14928, 14934, 14940, 14946, 14950, 14952, 14958, 14960, 14964, 14970, 14976, 14980, 14982, 14988, 14994, 15000, 15006, 15008, 15012, 15015, 15018, 15020, 15024, 15028, 15030, 15036, 15040, 15042, 15048, 15050, 15054, 15060, 15064, 15066, 15072, 15078, 15080, 15084, 15088, 15090, 15092, 15096, 
15100, 15102, 15104, 15108, 15114, 15120, 15126, 15132, 15136, 15138, 15140, 15144, 15148, 15150, 15156, 15160, 15162, 15168, 15174, 15176, 15180, 15184, 15186, 15190, 15192, 15198, 15200, 15204, 15210, 15216, 15220, 15222, 15224, 15228, 15232, 15234, 15240, 15246, 15252, 15258, 15260, 15264, 15270, 15276, 15280, 15282, 15288, 15294, 15300, 15306, 15312, 15316, 15318, 15320, 15324, 15330, 15336, 15340, 15342, 15344, 15348, 15354, 15360, 15366, 15368, 15372, 15376, 15378, 15380, 15384, 15390, 15392, 15396, 15400, 15402, 15408, 15414, 15420, 15426, 15428, 15432, 15435, 15438, 15440, 15444, 15450, 15456, 15460, 15462, 15468, 15470, 15474, 15480, 15484, 15486, 15488, 15492, 15496, 15498, 15500, 15504, 15510, 15512, 15516, 15520, 15522, 15528, 15534, 15540, 15546, 15552, 15558, 15560, 15564, 15568, 15570, 15576, 15580, 15582, 15588, 15594, 15596, 15600, 15606, 15610, 15612, 15616, 15618, 15620, 15624, 15630, 15636, 15640, 15642, 15648, 15652, 15654, 15660, 15664, 15666, 15672, 15678, 15680, 15684, 15690, 15696, 15700, 15702, 15704, 15708, 15714, 15720, 15726, 15730, 15732, 15736, 15738, 15740, 15744, 15750, 15752, 15756, 15760, 15762, 15764, 15768, 15774, 15776, 15780, 15786, 15792, 15798, 15800, 15804, 15808, 15810, 15816, 15820, 15822, 15824, 15828, 15834, 15840, 15846, 15848, 15852, 15858, 15860, 15864, 15870, 15872, 15876, 15880, 15882, 15884, 15888, 15890, 15894, 15900, 15904, 15906, 15912, 15918, 15920, 15924, 15928, 15930, 15932, 15936, 15940, 15942, 15948, 15950, 15954, 15960, 15966, 15972, 15978, 15980, 15984, 15988, 15990, 15996, 16000, 16002, 16008, 16014, 16016, 16020, 16026, 16030, 16032, 16038, 16040, 16044, 16048, 16050, 
16056, 16060, 16062, 16065, 16068, 16072, 16074, 16080, 16086, 16092, 16098, 16100, 16104, 16110, 16112, 16116, 16120, 16122, 16128, 16134, 16140, 16146, 16150, 16152, 16156, 16158, 16160, 16164, 16170, 16176, 16180, 16182, 16184, 16188, 16192, 16194, 16200, 16206, 16212, 16218, 16220, 16224, 16230, 16236, 16240, 16242, 16248, 16250, 16254, 16256, 16260, 16266, 16268, 16272, 16278, 16280, 16284, 16290, 16296, 16300, 16302, 16308, 16310, 16314, 16320, 16324, 16326, 16328, 16332, 16338, 16340, 16344, 16350, 16352, 16356, 16360, 16362, 16368, 16374, 16380, 16386, 16392, 16398, 16400, 16404, 16408, 16410, 16416, 16420, 16422, 16428, 16432, 16434, 16436, 16440, 16446, 16450, 16452, 16456, 16458, 16460, 16464, 16470, 16476, 16480, 16482, 16488, 16492, 16494, 16500, 16506, 16512, 16518, 16520, 16524, 16530, 16536, 16540, 16542, 16544, 16548, 16554, 16560, 16566, 16572, 16576, 16578, 16580, 16584, 16588, 16590, 16592, 16596, 16600, 16602, 16604, 16608, 16614, 16620, 16626, 16632, 16638, 16640, 16644, 16650, 16656, 16660, 16662, 16668, 16674, 16680, 16686, 16688, 16692, 16695, 16698, 16700, 16704, 16710, 16716, 16720, 16722, 16728, 16730, 16734, 16740, 16744, 16746, 16752, 16758, 16760, 16764, 16768, 16770, 16772, 16776, 16780, 16782, 16788, 16794, 16796, 16800, 16806, 16808, 16812, 16818, 16820, 16824, 16828, 16830, 16836, 16840, 16842, 16848, 16854, 16856, 16860, 16864, 16866, 16870, 16872, 16878, 16880, 16884, 16890, 16896, 16900, 16902, 16908, 16912, 16914, 16920, 16926, 16928, 16932, 16938, 16940, 16944, 16950, 16952, 16956, 16960, 16962, 16968, 16974, 16980, 16984, 16986, 16992, 16996, 16998, 17000, 17004, 17010, 17016, 17020, 17022, 
17024, 17028, 17034, 17040, 17046, 17050, 17052, 17056, 17058, 17060, 17064, 17070, 17072, 17076, 17080, 17082, 17088, 17094, 17100, 17106, 17108, 17112, 17118, 17120, 17124, 17130, 17136, 17140, 17142, 17148, 17150, 17152, 17154, 17160, 17164, 17166, 17168, 17172, 17178, 17180, 17184, 17190, 17192, 17196, 17200, 17202, 17204, 17208, 17214, 17220, 17226, 17232, 17238, 17240, 17244, 17248, 17250, 17256, 17260, 17262, 17264, 17268, 17272, 17274, 17276, 17280, 17286, 17290, 17292, 17296, 17298, 17300, 17304, 17310, 17316, 17320, 17322, 17325, 17328, 17332, 17334, 17336, 17340, 17346, 17352, 17358, 17360, 17364, 17368, 17370, 17376, 17380, 17382, 17388, 17394, 17400, 17406, 17408, 17412, 17416, 17418, 17420, 17424, 17430, 17436, 17440, 17442, 17444, 17448, 17454, 17460, 17466, 17472, 17478, 17480, 17484, 17490, 17496, 17500, 17502, 17508, 17512, 17514, 17520, 17526, 17528, 17532, 17536, 17538, 17540, 17544, 17550, 17556, 17560, 17562, 17568, 17570, 17574, 17576, 17580, 17584, 17586, 17592, 17598, 17600, 17604, 17610, 17612, 17616, 17620, 17622, 17628, 17632, 17634, 17640, 17646, 17652, 17658, 17660, 17664, 17668, 17670, 17676, 17680, 17682, 17688, 17694, 17696, 17700, 17706, 17710, 17712, 17718, 17720, 17724, 17730, 17732, 17736, 17740, 17742, 17748, 17752, 17754, 17760, 17766, 17772, 17776, 17778, 17780, 17784, 17790, 17792, 17796, 17800, 17802, 17808, 17814, 17816, 17820, 17826, 17832, 17836, 17838, 17840, 17844, 17850, 17856, 17860, 17862, 17864, 17868, 17874, 17880, 17886, 17888, 17892, 17898, 17900, 17904, 17910, 17916, 17920, 17922, 17928, 17934, 17936, 17940, 17946, 17948, 17952, 17955, 17958, 17960, 17964, 17970, 17976, 17980, 
17982, 17988, 17990, 17992, 17994, 18000, 18004, 18006, 18012, 18018, 18020, 18024, 18030, 18032, 18036, 18040, 18042, 18048, 18054, 18060, 18066, 18072, 18078, 18080, 18084, 18088, 18090, 18096, 18100, 18102, 18108, 18114, 18116, 18120, 18126, 18128, 18130, 18132, 18138, 18140, 18144, 18150, 18156, 18160, 18162, 18168, 18172, 18174, 18176, 18180, 18186, 18192, 18198, 18200, 18204, 18210, 18216, 18220, 18222, 18224, 18228, 18234, 18240, 18246, 18252, 18256, 18258, 18260, 18264, 18270, 18276, 18280, 18282, 18284, 18288, 18294, 18300, 18304, 18306, 18312, 18318, 18320, 18324, 18326, 18330, 18336, 18340, 18342, 18348, 18352, 18354, 18360, 18366, 18368, 18372, 18378, 18380, 18384, 18390, 18392, 18396, 18400, 18402, 18408, 18410, 18414, 18420, 18424, 18426, 18432, 18438, 18440, 18444, 18450, 18452, 18456, 18460, 18462, 18468, 18474, 18480, 18486, 18492, 18496, 18498, 18500, 18504, 18508, 18510, 18512, 18516, 18520, 18522, 18528, 18534, 18536, 18540, 18544, 18546, 18550, 18552, 18558, 18560, 18564, 18568, 18570, 18576, 18580, 18582, 18585, 18588, 18590, 18592, 18594, 18600, 18606, 18612, 18616, 18618, 18620, 18624, 18630, 18636, 18640, 18642, 18648, 18654, 18656, 18660, 18666, 18672, 18676, 18678, 18680, 18684, 18688, 18690, 18696, 18700, 18702, 18704, 18708, 18714, 18720, 18726, 18732, 18738, 18740, 18744, 18750, 18756, 18760, 18762, 18768, 18774, 18780, 18786, 18788, 18792, 18798, 18800, 18804, 18810, 18816, 18820, 18822, 18824, 18828, 18830, 18832, 18834, 18840, 18844, 18846, 18848, 18850, 18852, 18858, 18860, 18864, 18870, 18872, 18876, 18880, 18882, 18888, 18894, 18900, 18906, 18912, 18918, 18920, 18924, 18928, 18930, 18936, 18940, 
18942, 18944, 18948, 18954, 18956, 18960, 18966, 18970, 18972, 18978, 18980, 18984, 18990, 18996, 19000, 19002, 19008, 19012, 19014, 19020, 19024, 19026, 19032, 19038, 19040, 19044, 19050, 19056, 19060, 19062, 19068, 19072, 19074, 19080, 19086, 19092, 19096, 19098, 19100, 19104, 19110, 19116, 19120, 19122, 19124, 19128, 19134, 19136, 19140, 19146, 19152, 19158, 19160, 19164, 19170, 19176, 19180, 19182, 19184, 19188, 19194, 19200, 19206, 19208, 19212, 19215, 19218, 19220, 19224, 19228, 19230, 19236, 19240, 19242, 19248, 19250, 19254, 19260, 19264, 19266, 19272, 19278, 19280, 19284, 19290, 19292, 19296, 19300, 19302, 19305, 19308, 19312, 19314, 19320, 19326, 19328, 19332, 19338, 19340, 19344, 19348, 19350, 19356, 19360, 19362, 19368, 19374, 19376, 19380, 19386, 19390, 19392, 19398, 19400, 19404, 19410, 19416, 19420, 19422, 19428, 19432, 19434, 19440, 19446, 19448, 19452, 19456, 19458, 19460, 19464, 19470, 19476, 19480, 19482, 19488, 19494, 19500, 19504, 19506, 19512, 19516, 19518, 19520, 19524, 19530, 19536, 19540, 19542, 19544, 19548, 19550, 19552, 19554, 19560, 19566, 19572, 19578, 19580, 19584, 19590, 19596, 19600, 19602, 19608, 19614, 19620, 19624, 19626, 19628, 19632, 19635, 19638, 19640, 19644, 19650, 19656, 19660, 19662, 19668, 19670, 19674, 19680, 19684, 19686, 19692, 19698, 19700, 19704, 19710, 19712, 19716, 19720, 19722, 19728, 19734, 19740, 19746, 19752, 19758, 19760, 19764, 19768, 19770, 19776, 19780, 19782, 19788, 19794, 19796, 19800, 19806, 19810, 19812, 19818, 19820, 19824, 19830, 19836, 19840, 19842, 19845, 19848, 19852, 19854, 19856, 19860, 19864, 19866, 19872, 19878, 19880, 19884, 19888, 19890, 19896, 19900, 19902, 
19908, 19914, 19920, 19926, 19932, 19936, 19938, 19940, 19944, 19950, 19952, 19956, 19960, 19962, 19964, 19968, 19974, 19976, 19980, 19986, 19992, 19998, 20000, 20004, 20010, 20016, 20020, 20022, 20028, 20034, 20040, 20046, 20048, 20052, 20058, 20060, 20064, 20070, 20072, 20076, 20080, 20082, 20088, 20090, 20094, 20096, 20100, 20104, 20106, 20112, 20118, 20120, 20124, 20128, 20130, 20132, 20136, 20140, 20142, 20148, 20150, 20152, 20154, 20160]
    print(get_sum_list(array))
    #sums = list(get_abundant_sums(0, 20161))
    #print(sums)
    #print(get_sum_list(list(get_non_absum_int(1, 20161, sums))))
    #print(get_proper_divisors(13)) # Remember that proper divisors do NOT include the number n itself. Otherwise every single number would be an absum on the basis of all numbers having itself (n) and 1 as divisors. 