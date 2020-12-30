cities = ["pecs", "budapest", "debrecen", "sopron", "szolnok", "miszkolc", "eger"]

for i, city in enumerate(cities):  #wybór 4 pierwszych miast z listy za pomocą pętli for które nie są stolicą
    if city == "budapest":
        continue
    if i == 4:
        break
    print(i)
    print("{} spełnia wymagania".format(city))

print()
population_2008 = { 'belgium': 10666866, 'bulgaria': 7518002, 'czechia': 10343422, 'denmark': 5475791, 'germany': 82217837, 'estonia': 1338440, 'ireland': 4457765, 'greece': 11060937, 'spain': 45668939, 'france': 64007193, 'croatia': 4311967, 'italy': 58652875, 'cyprus': 776333, 'latvia': 2191810, 'lithuania': 3212605, 'luxembourg': 483799, 'hungary': 10045401, 'malta': 407832, 'netherlands': 16405399, 'austria': 8307989, 'poland': 38115641, 'portugal': 10553339, 'romania': 20635460, 'slovenia': 2010269, 'slovakia': 5376064, 'finland': 5300484, 'sweden': 9182927, 'united kingdom': 61571647, 'iceland': 315459, 'liechtenstein': 35356, 'norway': 4737171, 'switzerland': 7593494, 'montenegro': 615543, 'north macedonia': 2045177, 'albania': 2958266, 'serbia': 7365507, 'turkey': 70586256, 'andorra': 83137, 'belarus': 9689770, 'bosnia and herzegovina': 3843846, 'kosovo': 2153139, 'moldova': 3572703, 'san marino': 32054, 'ukraine': 46192309, 'armenia': 3230086, 'azerbaijan': 8629900, 'georgia': 4382070 }
population_2018 = { 'belgium': 11398589, 'bulgaria': 7050034, 'czechia': 10610055, 'denmark': 5781190, 'germany': 82792351, 'estonia': 1319133, 'ireland': 4830392, 'greece': 10741165, 'spain': 46658447, 'france': 66926166, 'croatia': 4105493, 'italy': 60483973, 'cyprus': 864236, 'latvia': 1934379, 'lithuania': 2808901, 'luxembourg': 602005, 'hungary': 9778371, 'malta': 475701, 'netherlands': 17181084, 'austria': 8822267, 'poland': 37976687, 'portugal': 10291027, 'romania': 19530631, 'slovenia': 2066880, 'slovakia': 5443120, 'finland': 5513130, 'sweden': 10120242, 'united kingdom': 66273576, 'iceland': 348450, 'liechtenstein': 38114, 'norway': 5295619, 'switzerland': 8484130, 'montenegro': 622359, 'north macedonia': 2075301, 'albania': 2870324, 'serbia': 7001444, 'turkey': 80810525, 'andorra': 74794, 'belarus': 9491823, 'bosnia and herzegovina': 3502550, 'kosovo': 1798506, 'moldova': 3547539, 'san marino': 34453, 'ukraine': 42386403, 'armenia': 2972732, 'azerbaijan': 9898085, 'georgia': 3729633 }

pophun_08 = population_2008["hungary"]
pophun_18 = population_2018["hungary"]
print(("the pop in 2008 is %d") % pophun_08)
print(("the pop in 2018 is %d") % population_2018["hungary"])

print()
change = pophun_18 - pophun_08
print(("the differnece was %d") % change)


print()

#max min value search
max_diff = population_2018['hungary'] - population_2008['hungary']
min_diff = population_2018['poland'] - population_2008['poland'] #nie ma znaczenia jaki klucz się wybierze tip
max_country = 'hungary'
min_country = 'poland'

for key, value in population_2008.items():
    pop_2018 = population_2018[key]
    print("%s, 2008: %d, 2018: %d" % (key, value, pop_2018))
    diff = pop_2018 - value
    print("difference: %d" % diff)

    if diff > max_diff:
        max_diff = diff
        max_country = key
    if diff < min_diff:
        min_diff = diff
        min_country = key

print()
print(max_country)
print(max_diff)
print()
print(min_country)
print(min_diff)

import random

#2.1

numbers = []
odds = []
evens = []
for i in range(20):
    numbers.append(random.randint(1, 100))
print(numbers)

for number in numbers:
    if number % 2 == 0:
        odds.append(number)
    else:
        evens.append(number)

print(odds)
print(evens)

#collatz sequence

collatz = []
num = int(input("wybierz liczbę startową: "))

while num != 1:
    collatz.append(num)
    if num % 2 == 0:
        num = int(num / 2)
    else:
        num = int(3 * num + 1)


print(collatz)

import pandas as pd
companies = ["Walmart", "Berkshire Hathaway", "Apple", "Exxon Mobil", "McKesson", "UnitedHealth Group", "CVS Health", "General Motors", "AT&T", "Ford Motor", "AmerisourceBergen", "Amazon.com", "General Electric", "Verizon", "Cardinal Health", "Costco", "Walgreens Boots Alliance", "Kroger", "Chevron", "Fannie Mae", "J.P. Morgan Chase", "Express Scripts Holding", "Home Depot", "Boeing", "Wells Fargo", "Bank of America Corp.", "Alphabet", "Microsoft", "Anthem", "Citigroup", "Comcast", "IBM", "State Farm Insurance Cos.", "Phillips 66", "Johnson & Johnson", "Procter & Gamble", "Valero Energy", "Target", "Freddie Mac", "Loweâ€™s", "Dell Technologies", "MetLife", "Aetna", "PepsiCo", "Archer Daniels Midland", "UPS", "Intel", "Prudential Financial", "Albertsons Cos.", "United Technologies", "Marathon Petroleum", "Disney", "Humana", "Pfizer", "AIG", "Lockheed Martin", "Sysco", "FedEx", "Hewlett Packard Enterprise", "Cisco Systems", "HP", "Dow Chemical", "HCA Holdings", "Coca-Cola", "New York Life Insurance", "Centene", "American Airlines Group", "Nationwide", "Merck", "Cigna", "Delta Air Lines", "Best Buy", "Honeywell International", "Caterpillar", "Liberty Mutual Insurance Group", "Morgan Stanley", "Massachusetts Mutual Life Insurance", "Goldman Sachs Group", "Energy Transfer Equity", "TIAA", "Oracle", "Tyson Foods", "United Continental Holdings", "Allstate", "Publix Super Markets", "American Express", "TJX", "Nike", "Exelon", "General Dynamics", "Rite Aid", "Gilead Sciences", "CHS", "3M", "Time Warner", "Charter Communications", "Northwestern Mutual", "Facebook", "Travelers Cos.", "Capital One Financial", "Twenty-First Century Fox", "USAA", "World Fuel Services", "Philip Morris International", "Deere", "Kraft Heinz", "Tech Data", "Avnet", "Mondelez International", "Macyâ€™s", "AbbVie", "McDonaldâ€™s", "DuPont", "Northrop Grumman", "ConocoPhillips", "Raytheon", "Tesoro", "Arrow Electronics", "Qualcomm", "Progressive", "Duke Energy", "Enterprise Products Partners", "Amgen", "US Foods Holding", "U.S. Bancorp", "Aflac", "Sears Holdings", "Dollar General", "AutoNation", "Community Health Systems", "Starbucks", "Eli Lilly", "International Paper", "Tenet Healthcare", "Abbott Laboratories", "Dollar Tree", "Whirlpool", "Southwest Airlines", "Emerson Electric", "Staples", "Plains GP Holdings", "Penske Automotive Group", "Union Pacific", "Danaher", "Southern", "ManpowerGroup", "Bristol-Myers Squibb", "Altria Group", "Fluor", "Kohlâ€™s", "Lear", "Jabil Circuit", "Hartford Financial Services Group", "Thermo Fisher Scientific", "Kimberly-Clark", "Molina Healthcare", "PG&E Corp.", "Supervalu", "Cummins", "CenturyLink", "AECOM", "Xerox", "Marriott International", "Paccar", "General Mills", "PNC Financial Services Group", "American Electric Power", "Icahn Enterprises", "Nucor", "NextEra Energy", "Performance Food Group", "PBF Energy", "Halliburton", "CarMax", "Freeport-McMoRan", "Whole Foods Market", "Bank of New York Mellon", "Gap", "Omnicom Group", "Genuine Parts", "DaVita", "Colgate-Palmolive", "PPG Industries", "Goodyear Tire & Rubber", "Synchrony Financial", "DISH Network", "Visa", "Nordstrom", "INTL FCStone", "WestRock", "XPO Logistics", "Aramark", "CBS", "AES", "WellCare Health Plans", "FirstEnergy", "Conagra Brands", "Synnex", "CDW", "Textron", "Waste Management", "Illinois Tool Works", "Office Depot", "Monsanto", "Cognizant Technology Solutions", "Texas Instruments", "Lincoln National", "Newell Brands", "Land Oâ€™Lakes", "Marsh & McLennan", "Ecolab", "C.H. Robinson Worldwide", "Loews", "CBRE Group", "Kinder Morgan", "Kellogg", "Western Digital", "Guardian Life Ins. Co. of America", "Ross Stores", "L Brands", "J.C. Penney", "Farmers Insurance Exchange", "Reynolds American", "Viacom", "Becton Dickinson", "Micron Technology", "Principal Financial", "Arconic", "NRG Energy", "VF", "Devon Energy", "D.R. Horton", "Bed Bath & Beyond", "Consolidated Edison", "Edison International", "Sherwin-Williams", "NGL Energy Partners", "Dominion Energy", "Ameriprise Financial", "ADP", "Hilton Worldwide Holdings", "First Data", "Henry Schein", "Toys â€śRâ€ť Us", "BB&T Corp.", "Reinsurance Group of America", "Core-Mark Holding", "Biogen", "Las Vegas Sands", "Stanley Black & Decker", "Parker-Hannifin", "Stryker", "Estee Lauder", "Celgene", "BlackRock", "Xcel Energy", "CSX", "Unum Group", "Jacobs Engineering Group", "Lennar", "Group 1 Automotive", "Leucadia National", "Entergy", "PayPal Holdings", "Applied Materials", "Voya Financial", "Mastercard", "Priceline Group", "Liberty Interactive", "AutoZone", "State Street Corp.", "DTE Energy", "L3 Technologies", "HollyFrontier", "Praxair", "Universal Health Services", "Discover Financial Services", "Occidental Petroleum", "United States Steel", "Sempra Energy", "Baxter International", "W.W. Grainger", "Autoliv", "Norfolk Southern", "Baker Hughes", "Ally Financial", "Sonic Automotive", "Owens & Minor", "Huntsman", "Laboratory Corp. of America", "Murphy USA", "Advance Auto Parts", "Fidelity National Financial", "Air Products & Chemicals", "Hormel Foods", "Hertz Global Holdings", "MGM Resorts International", "Corning", "Republic Services", "Alcoa", "Fidelity National Information Services", "Pacific Life", "SunTrust Banks", "LKQ", "BorgWarner", "Ball", "CST Brands", "Public Service Enterprise Group", "Eastman Chemical", "eBay", "Mohawk Industries", "Oneok", "Frontier Communications", "Netflix", "American Family Insurance Group", "Thrivent Financial for Lutherans", "Expedia", "Lithia Motors", "Avis Budget Group", "Reliance Steel & Aluminum", "GameStop", "Tenneco", "Oâ€™Reilly Automotive", "Peter Kiewit Sonsâ€™", "United Natural Foods", "salesforce.com", "Boston Scientific", "Newmont Mining", "Genworth Financial", "Live Nation Entertainment", "Veritiv", "News Corp.", "Crown Holdings", "Global Partners", "PVH", "Level 3 Communications", "Navistar International", "Univar", "Campbell Soup", "Dickâ€™s Sporting Goods", "Weyerhaeuser", "Mutual of Omaha Insurance", "Chesapeake Energy", "Anadarko Petroleum", "Interpublic Group", "J.M. Smucker", "Steel Dynamics", "Foot Locker", "Western Refining", "SpartanNash", "Dean Foods", "Zimmer Biomet Holdings", "PulteGroup", "W.R. Berkley", "Quanta Services", "EOG Resources", "Charles Schwab", "Eversource Energy", "Anixter International", "EMCOR Group", "Assurant", "CenterPoint Energy", "Harris", "HD Supply Holdings", "PPL", "Quest Diagnostics", "Williams", "WEC Energy Group", "Hershey", "AGCO", "Ralph Lauren", "Masco", "WESCO International", "LifePoint Health", "National Oilwell Varco", "Kindred Healthcare", "Mosaic", "Alliance Data Systems", "Computer Sciences", "Huntington Ingalls Industries", "Leidos Holdings", "Erie Insurance Group", "Tesla", "Ascena Retail Group", "Darden Restaurants", "Harman International Industries", "Nvidia", "R.R. Donnelley & Sons", "Fifth Third Bancorp", "Quintiles IMS Holdings", "Jones Lang LaSalle", "Dover", "Spirit AeroSystems Holdings", "Ryder System", "A-Mark Precious Metals", "Tractor Supply", "Sealed Air", "Auto-Owners Insurance", "Yum China Holdings", "Calpine", "Owens-Illinois", "Targa Resources", "Jones Financial (Edward Jones)", "JetBlue Airways", "Franklin Resources", "Activision Blizzard", "J.B. Hunt Transport Services", "Constellation Brands", "NCR", "Asbury Automotive Group", "American Financial Group", "Discovery Communications", "Berry Global Group", "Sanmina", "CalAtlantic Group", "Dr Pepper Snapple Group", "Dillardâ€™s", "HRG Group", "CMS Energy", "Graybar Electric", "Builders FirstSource", "Yum Brands", "Caseyâ€™s General Stores", "Amphenol", "Oshkosh", "iHeartMedia", "TreeHouse Foods", "Alleghany", "Expeditors International of Washington", "Avery Dennison", "Ameren", "Hanesbrands", "Motorola Solutions", "St. Jude Medical", "Harley-Davidson", "Regions Financial", "Intercontinental Exchange", "Alaska Air Group", "Old Republic International", "Lam Research", "AK Steel Holding", "Rockwell Automation", "Adobe Systems", "Avon Products", "Terex", "NVR", "Dana", "Realogy Holdings", "American Tower", "Packaging Corp. of America", "Citizens Financial Group", "United Rentals", "Clorox", "Genesis Healthcare", "M&T Bank Corp.", "Ingredion", "UGI", "Owens Corning", "S&P Global", "Markel", "Wyndham Worldwide", "Arthur J. Gallagher", "Burlington Stores", "First American Financial", "Symantec", "Patterson", "Olin", "NetApp", "Raymond James Financial", "TravelCenters of America", "Fiserv", "Host Hotels & Resorts", "Insight Enterprises", "Mattel", "AmTrust Financial Services", "Cincinnati Financial", "Simon Property Group", "Western Union", "KeyCorp", "Delek US Holdings", "Booz Allen Hamilton Holding", "Chemours", "Western & Southern Financial Group", "Celanese", "Windstream Holdings", "Seaboard", "Essendant", "Apache", "Airgas", "Kelly Services", "Liberty Media", "Rockwell Collins", "Robert Half International", "CH2M Hill", "Big Lots", "Michaels Cos.", "Toll Brothers", "Yahoo", "Vistra Energy", "ABM Industries"]
revenue = [485873, 223604, 215639, 205004, 192487, 184840, 177526, 166380, 163786, 151800, 146850, 135987, 126661, 125980, 121546, 118719, 117351, 115337, 107567, 107162, 105486, 100288, 94595, 94571, 94176, 93662, 90272, 85320, 84863, 82386, 80403, 79919, 76132, 72396, 71890, 71726, 70166, 69495, 65665, 65017, 64806, 63476, 63155, 62799, 62346, 60906, 59387, 58779, 58734, 57244, 55858, 55632, 54379, 52824, 52367, 50658, 50367, 50365, 50123, 49247, 48238, 48158, 44747, 41863, 40787, 40721, 40180, 40074, 39807, 39668, 39639, 39403, 39302, 38537, 38308, 37949, 37788, 37712, 37504, 37105, 37047, 36881, 36556, 36534, 34274, 33823, 33184, 32376, 31360, 31353, 30737, 30390, 30347, 30109, 29318, 29003, 28799, 27638, 27625, 27519, 27326, 27131, 27016, 26685, 26644, 26487, 26235, 26219, 25923, 25778, 25638, 24622, 24594, 24508, 24360, 24069, 24005, 23825, 23554, 23441, 23369, 23022, 22991, 22919, 22744, 22559, 22138, 21987, 21609, 21374, 21316, 21222, 21079, 21070, 20853, 20719, 20718, 20425, 20268, 20217, 20182, 20143, 19941, 19912, 19896, 19654, 19427, 19337, 19037, 18686, 18558, 18353, 18300, 18274, 18202, 17782, 17666, 17529, 17509, 17470, 17411, 17126, 17072, 17033, 16563, 16423, 16380, 16348, 16208, 16155, 16105, 15920, 15887, 15833, 15789, 15724, 15683, 15516, 15417, 15340, 15197, 15195, 15178, 15158, 15122, 15095, 15082, 14757, 14755, 14706, 14619, 14416, 14386, 14287, 14237, 14156, 14134, 14062, 13982, 13788, 13609, 13599, 13585, 13502, 13487, 13370, 13330, 13264, 13233, 13211, 13153, 13144, 13105, 13072, 13058, 13014, 12994, 12919, 12867, 12574, 12547, 12513, 12503, 12488, 12483, 12399, 12394, 12394, 12351, 12207, 12197, 12157, 12104, 12075, 11869, 11856, 11742, 11737, 11735, 11668, 11663, 11584, 11572, 11540, 11538, 11522, 11507, 11449, 11410, 11407, 11361, 11325, 11262, 11229, 11155, 11107, 11069, 11047, 10964, 10950, 10888, 10875, 10846, 10842, 10825, 10782, 10776, 10743, 10647, 10636, 10635, 10630, 10597, 10536, 10534, 10508, 10497, 10398, 10261, 10183, 10163, 10137, 10074, 9888, 9841, 9835, 9732, 9723, 9657, 9642, 9633, 9568, 9554, 9524, 9523, 9480, 9455, 9390, 9388, 9318, 9241, 9169, 9161, 9082, 9071, 9061, 9061, 9061, 9008, 8979, 8959, 8921, 8896, 8831, 8829, 8777, 8774, 8678, 8659, 8613, 8608, 8599, 8593, 8573, 8470, 8392, 8386, 8379, 8369, 8355, 8327, 8319, 8284, 8240, 8203, 8172, 8111, 8074, 7961, 7922, 7902, 7899, 7872, 7869, 7847, 7811, 7777, 7766, 7743, 7735, 7710, 7684, 7669, 7654, 7651, 7651, 7644, 7639, 7625, 7552, 7532, 7528, 7527, 7524, 7517, 7515, 7499, 7472, 7440, 7411, 7405, 7357, 7336, 7274, 7251, 7227, 7163, 7138, 7106, 7068, 7043, 7016, 7000, 6995, 6934, 6912, 6910, 6896, 6889, 6878, 6804, 6794, 6793, 6787, 6784, 6780, 6778, 6775, 6752, 6716, 6702, 6691, 6632, 6632, 6618, 6608, 6556, 6548, 6543, 6528, 6498, 6497, 6489, 6481, 6477, 6440, 6418, 6403, 6399, 6385, 6367, 6366, 6304, 6286, 6279, 6274, 6175, 6131, 6098, 6087, 6076, 6063, 6038, 6004, 5997, 5967, 5958, 5931, 5901, 5886, 5883, 5880, 5854, 5853, 5841, 5835, 5826, 5810, 5786, 5779, 5763, 5762, 5761, 5733, 5722, 5704, 5686, 5677, 5661, 5612, 5599, 5595, 5591, 5576, 5568, 5555, 5551, 5546, 5520, 5511, 5505, 5488, 5486, 5457, 5451, 5449, 5435, 5423, 5422, 5414, 5406, 5400, 5398, 5389, 5387, 5379, 5369, 5354, 5314, 5277, 5276, 5259, 5250, 5236, 5200, 5197, 5170, 5169, 5164, 5145]
profit = [13643, 24074, 45687, 7840, 2258, 7017, 5317, 9427, 12976, 4596, 1427.9, 2371, 8831, 13127, 1427, 2350, 4173, 1975, -497, 12313, 24733, 3404.4, 7957, 4895, 21938, 17906, 19478, 16798, 2469.8, 14912, 8695, 11872, 350.3, 1555, 16540, 10508, 2289, 2737, 7815, 3093, -1672, 800, 2271, 6329, 1279, 3431, 10316, 4368, -502.2, 5055, 1174, 9391, 614, 7215, -849, 5302, 949.6, 1820, 3161, 10739, 2496, 4318, 2890, 6527, 1088.1, 562, 2676, 334.3, 3920, 1867, 4373, 1228, 4809, -67, 1006, 5979, 1273.5, 7398, 995, 1492.3, 8901, 1768, 2263, 1877, 2025.7, 5408, 2298.2, 3760, 1134, 2955, 165.5, 13501, 424.2, 5050, 3926, 3522, 818, 10217, 3014, 3751, 2755, 1779.1, 126.5, 6967, 1523.9, 3632, 195.1, 506.5, 1659, 619, 5953, 4686.5, 2513, 2200, -3615, 2211, 734, 522.8, 5705, 1031, 2152, 2513.1, 7722, 209.8, 5888, 2659, -2221, 1251.1, 430.5, -1721, 2817.7, 2737.6, 904, -192, 1400, 896.2, 888, 2244, 1635, -1497, 94, 342.9, 4233, 2553.7, 2448, 443.7, 4457, 14239, 281.4, 556, 975.1, 254.1, 896, 2021.8, 2166, 52, 1393, 178, 1394, 626, 96.1, -477, 780, 521.7, 1697.4, 3903, 610.9, -1128, 796.3, 2912, 68.3, 170.8, -5763, 623.4, -4154, 507, 3547, 676, 1148.6, 687.2, 879.9, 2441, 877, 1264, 2251, 1449.9, 5991, 354, 54.7, -396.3, 69, 287.8, 1261, -1130, 242.1, -6177, -677, 234.9, 424.4, 962, 1182, 2035, 529, 1336, 1553, 3595, 1192, 527.8, 244.9, 1768, 1229.6, 513.4, 654, 572, 708, 694, 242, 263.9, 1117.7, 1158.1, 1, -147.9, 6073, 1438, 976, -276, 1316.5, -941, -774, 1074.1, -3302, 886.3, 841.5, 1245, 1311, 1132.7, -198.9, 2123, 1314, 1492.5, 348, 420, 506.8, -36, 2426, 701.4, 54.2, 3702.8, 1670, 965.3, 806.8, 1647, 1114.6, 1999.2, 3172, 1123.4, 1714, 931.4, 210.5, 911.8, 147.1, 130, -583.6, 1401, 1721, -428, 4059, 2135, 1235, 1241, 2143, 868, 710, -260.5, 1500, 702.4, 2393, -574, -440, 1370, 4965, 605.9, 567.1, 1668, -2738, 1067, 93.2, 108.8, 326, 732.1, 221.5, 459.6, 650, 631.1, 890.1, -491, 1101.4, 3695, 612.6, -400, 568, 824, 1878, 464, 118.5, 263, 324, 887, 854, 7266, 930.4, 352, -373, 186.7, 325.6, 587.8, 281.8, 197.1, 163, 304.3, 353.2, 363, 1037.7, 396, 125.8, 179.6, 347, -627, -277, 2.9, 21, 179, 496, -199.4, 549, 677, -97, -68.4, 563, 287.4, 1027, 356.6, -4401, -3071, 608.5, 688.7, 382.1, 664, 124.9, 56.8, 119.9, 305.9, 602.7, 601.9, 198.4, -1096.7, 1889, 942.3, 120.5, 181.9, 565.4, 432, 324, 196, 1902, 645, -424, 939, 720, 160.1, 396, 491, 101.6, 121.9, -2412, -664.2, 297.8, 515.8, 251, 573, 244, 741.9, -674.9, -11.9, 375, 361.7, 1666, -495.9, 1564, 115, 318.2, 508.9, 469.7, 262.5, 9.3, 437.1, 486.4, 706.3, 502, 92, 209, -187.3, 746, 759, 1726.7, 966, 432.1, 1054.9, 270, 167.2, 649, 1194, 236, 187.8, 484.7, 847, 169.2, -198.8, 551, 93.1, 144.3, 1619, 226, 822.9, 216.4, -296.3, -228.6, 456.9, 430.8, 320.7, 653, 539.4, 560, 734, 692.2, 1163, 1422, 814, 466.9, 914, -7.8, 729.7, 1168.8, -107.6, -176.1, 425.3, 640, 213, 956.4, 449.6, 1045, 566, 648, -64, 1315.1, 484.9, 364.7, 393, 2106, 455.7, 611, 414.4, 215.9, 343, 2488, 187.2, -3.9, 229, 529.4, -2, 930, 762, 84.7, 318, 411, 590.7, 1838.9, 253.2, 791, -153.7, 294.1, 7, 241.2, 900, -383.5, 312, 63.9, -1405, 337.5, 120.8, 680, 728, 343.4, 15, 152.8, 378.2, 382.1, -214.3, -214.3, 57.2]
employees = [2300000, 367700, 116000, 72700, 68000, 230000, 204000, 225000, 268540, 201000, 18500, 341400, 295000, 160900, 37300, 172000, 300000, 443000, 55200, 7000, 243355, 25600, 406000, 150540, 269100, 208024, 72053, 114000, 53000, 219000, 159000, 414400, 68234, 14800, 126400, 105000, 9996, 323000, 5982, 240000, 138000, 58000, 49500, 264000, 31800, 335520, 106000, 49739, 274000, 201600, 44460, 195000, 51600, 96500, 56400, 97000, 51900, 335767, 195000, 73700, 49000, 56000, 210500, 100300, 11320, 30500, 122300, 34320, 68000, 41000, 83756, 125000, 131000, 95400, 50000, 55311, 11737, 34400, 30992, 12997, 136000, 114000, 88000, 43275, 191000, 56400, 235000, 70700, 34396, 98800, 70580, 9000, 12157, 91584, 25000, 91500, 5646, 17048, 30900, 47300, 21500, 29943, 5000, 79500, 56767, 41000, 9500, 17700, 90000, 148300, 30000, 375000, 46000, 67000, 13300, 63000, 6308, 18700, 30500, 31721, 28798, 6800, 19200, 25000, 71191, 10212, 140000, 121000, 26000, 108000, 254000, 41975, 55000, 116475, 75000, 116050, 93000, 53536, 103500, 61503, 5100, 24000, 42919, 62000, 32015, 28000, 25000, 8300, 61551, 85000, 148400, 138000, 16900, 54800, 42000, 21000, 24000, 38000, 55400, 40000, 87000, 133600, 226500, 23000, 39000, 50683, 17634, 90980, 23900, 14700, 13000, 3165, 50000, 22429, 30000, 73515, 52000, 135000, 78500, 40000, 70300, 36700, 47000, 66000, 15000, 16000, 14200, 72500, 1464, 39000, 87000, 217250, 18410, 19000, 7400, 15707, 20900, 110000, 8516, 36000, 41200, 50000, 38000, 22450, 260200, 29865, 9057, 53400, 10000, 60000, 47565, 14125, 15800, 75000, 11121, 37369, 72878, 8876, 78600, 59100, 106000, 13309, 5525, 9650, 50928, 31400, 14854, 41500, 8763, 69000, 3545, 6976, 62000, 14960, 12390, 42550, 3200, 16200, 13195, 57000, 169000, 24000, 21000, 64000, 37500, 2371, 7688, 7400, 49000, 54023, 48950, 33000, 46000, 7132, 13000, 11476, 26628, 9400, 49350, 8335, 13500, 13000, 13513, 18100, 16150, 6700, 11900, 18500, 21080, 66780, 33783, 10000, 38000, 2676, 26498, 70863, 15549, 11000, 29800, 16575, 48000, 25000, 65900, 27856, 33000, 7600, 9800, 7900, 15000, 52000, 6600, 57500, 55219, 18450, 21100, 36000, 66500, 40700, 33000, 14000, 55000, 3628, 24375, 42500, 27000, 18450, 12380, 13065, 14000, 12600, 37800, 2384, 28332, 3850, 10471, 3282, 20075, 11170, 25600, 14500, 41750, 31000, 58397, 20000, 9554, 25000, 27000, 12438, 3400, 11500, 8700, 24000, 23992, 1770, 26650, 12600, 11300, 8700, 16500, 27550, 10400, 5732, 3300, 4500, 49800, 6910, 7695, 32965, 7134, 11500, 17000, 18500, 4623, 7608, 28100, 2650, 16200, 7762, 8900, 31000, 14700, 7727, 21000, 14000, 12689, 43000, 5604, 8074, 17140, 19795, 20500, 26000, 9000, 47000, 36384, 76650, 8700, 17000, 59000, 37000, 32000, 4988, 30025, 41000, 150942, 26000, 10299, 44360, 17844, 50000, 77300, 29000, 14400, 34500, 83, 19500, 23000, 4737, 420000, 2372, 27000, 1970, 43000, 15986, 9059, 9500, 22190, 9000, 33500, 7900, 7600, 7000, 21000, 40178, 3055, 20000, 30800, 16021, 7750, 8500, 14000, 90000, 24724, 62000, 13800, 18700, 16027, 3420, 16000, 25000, 8629, 67800, 14000, 18000, 6000, 22166, 5631, 19112, 8500, 7500, 8500, 22000, 15706, 26400, 18100, 4900, 24900, 11800, 4507, 14000, 17600, 12500, 8000, 82000, 16487, 11000, 13105, 16000, 20000, 10900, 37800, 24790, 40000, 19531, 11000, 7000, 6400, 12030, 11900, 20259, 23000, 220, 5930, 32000, 8000, 4754, 4050, 10700, 15700, 1326, 22600, 7000, 2178, 7293, 11870, 11781, 6600, 3727, 17000, 7500, 3626, 19000, 16400, 20000, 23150, 31000, 4200, 8500, 4431, 110000]

comp = {}

comp['revenue'] = revenue
comp['profit'] = profit
comp['employees'] = employees

df = pd.DataFrame(comp, index=companies)

print(df["revenue"].max())
rev_high = (df['revenue'].idxmax())
print(df.loc[rev_high])

prof = df.sort_values(by = 'profit', ascending = False)

for idx in range(0, len(prof)):
    if idx < 10:
        print(prof.iloc[idx])
    else:
        break


surplus = prof[prof.iloc[:, 1] > 0]
print("Number of companies with a positive profit: %d" % len(surplus))

emp_num = int(input("Pick minimum employee number:"))
emp = df[df.iloc[:, 2] > emp_num]
print(emp)

ratio = []

for i in range(len(df)):
    ratio.append(df['profit'][i] / df['revenue'][i])

df['p/r ratio'] = ratio
print(df)

pr_sorted = df.sort_values(by = 'p/r ratio', ascending = False)
print(pr_sorted["p/r ratio"].max())
ratio_high = (pr_sorted['p/r ratio'].idxmax())
print(pr_sorted.loc[ratio_high])

print('For an argument of a function type a company name you want to search for!')
def search(name):
    print('Here are your results: ')
    search = df.filter(like='%s' % name, axis=0)
    return print(search)

search('General')

lista = []
dicc = {}

for idx in range(0,len(companies)):
    dicc = {
        "name": companies[idx],
        "revenue": revenue[idx],
        "profit": profit[idx],
        "employees": employees[idx]
    }
    lista.append(dicc)
    idx + 1

def revenue_per_employee(company):
    for dic in lista:
        try:
            if dic["name"] == company:
                re = dic["revenue"] / dic["employees"]
                dic["revenue/employees"] = re
                return dic
                break
        except:
            print('nan')

revenue_per_employee("General Mills")

lista2 = [obiekt['name'] for obiekt in lista]
for kutas in range(0, len(lista2)):
    a = (revenue_per_employee(lista2[kutas]))
    lista2.append(a)
    kutas + 1

lista3 = []
lista2 = [obiekt['name'] for obiekt in lista]
for k in range(0, len(lista2)):
    lista3.append(revenue_per_employee(lista2[k]))
    k + 1


def highest_revenue_per_employee(wybrana_lista):
    maksymalna = max(wybrana_lista, key=lambda x: x['revenue/employees'])
    return maksymalna

print(highest_revenue_per_employee(lista3))

import matplotlib.pyplot as plt
import xlrd as x
import pandas as pd

fortune500 = pd.read_csv('C:/Users/Jakub/Downloads/fortune500_2017.csv', delimiter=';')
fortune500.columns = ['rank', 'company', 'sector', 'revenue', 'profit', 'employees']
fortune50 = fortune500.head(50)
#print(fortune50)
#fortune50.sort_values(by = 'profit').plot(kind = 'barh', x = 'company', y = 'profit', figsize = [10,10])
#plt.show()

df = pd.read_csv('C:/Users/Jakub/Downloads/airports.csv', delimiter=';')

df_sort = df.sort_values(by = 'longest', ascending=False)
df_100 = df_sort.head(100)
print(df_100)

#df_100.plot(kind = 'bar', x = 'iata', y = 'longest', figsize = [20,3])
#plt.show()

df_sort_city = df_sort.groupby('city')['longest'].max()
df_sort_city1 = df_sort_city.sort_values(ascending=False)
df_100_city = df_sort_city1.head(100)
df_100_city.columns = ['city', 'longest']

#df_100_city.plot(kind = 'bar', x = 'city', y = 'longest', figsize = [20,3])
#plt.show()

df_count = df.groupby('country').count()
df_count_sorted = df_count.sort_values(by = 'iata', ascending=False)

df_elev = df.groupby('city')['elevation'].mean()
df_elev_sorted = df_elev.sort_values(ascending=False)

df_run1 = df.groupby('city').sum()
df_run_sorted1 = df_run1.sort_values(by = 'runways',ascending=False)
print(df_run_sorted1[df_run_sorted1.runways > 5])

df_run = df.groupby('city')['runways'].sum()
df_run_sorted = df_run.sort_values(ascending=False)
print(df_run_sorted > 5) #displays boolean