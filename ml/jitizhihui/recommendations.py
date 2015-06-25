from math import sqrt

critics={'Lisa Rose': {'Lady in the water':2.5, 'Snake on a plane':3.5,'Just My Luck':3.0, 'Super Returns':3.5, 'You, Me and Dupree':2.5, 'The Night Listener':3.0}, 
	'Gene Seymour':{'Lady in the water':3.0, 'Snake on a plane':3.5,'Just My Luck':1.5, 'Super Returns':5.0, 'You, Me and Dupree':3.5, 'The Night Listener':3.5}, 
	'Michae Phillips':{'Lady in the water':2.5, 'Snake on a plane':3.0, 'Super Returns':3.5, 'The Night Listener':4.0}, 
	'Claudia Puig':{'Snake on a plane':3.5,'Just My Luck':3.0, 'Super Returns':4.0, 'The Night Listener':4.5, 'You, Me and Dupree':2.5}, 
	'Mick Lasalle':{'Lady in the water':3.0, 'Snake on a plane':4.0,'Just My Luck':2.0, 'Super Returns':3.0, 'You, Me and Dupree':2.0, 'The Night Listener':3.0}, 
	'Jack Matthews':{'Lady in the water':3.0, 'Snake on a plane':4.0,'Super Returns':5.0, 'You, Me and Dupree':3.5, 'The Night Listener':3.0}, 
	'Toby':{'Snake on a plane':4.5, 'You, Me and Dupree':1.0, 'Super Returns':4.0}}


def sim_distance(prefs,p1,p2):
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1
    if len(si) == 0: return 0
    sum_of_squares = sum([pow(prefs[p1][item]-prefs[p2][item], 2)
                          for item in prefs[p1] if item in prefs[p2]])

def sim_pearson(prefs, p1, p2):
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]: si[item] = 1
    n = len(si)

    if n == 0: return 1
    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    sum1Sq = sum([pow(prefs[p1][it], 2) for it in si])
    sum2Sq = sum([pow(prefs[p2][it], 2) for it in si])

    psum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    num = psum - (sum1 * sum2) / n
    den = sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))
    if den == 0: return 0

    r = num / den
    return r

def topMatches(prefs, p, n=5, s=sim_pearson):
    scores = [(s(prefs, p, o), o) for o in prefs if o != p]

    scores.sort()
    scores.reverse()
    return scores[0:n]

def getRecommendations(prefs, person, similarity=sim_pearson):
    totals = {}
    simsums = {}
    for o in prefs:
        if o == person:
            continue
        sim = similarity(prefs, person, o)

        if sim <= 0:
            continue
        for item in prefs[o]:
            if item not in prefs[person] or prefs[person][item] == 0:
                totals.setdefault(item, 0)
                totals[item] += prefs[o][item] * sim
                simsums.setdefault(item, 0)
                simsums[item] += sim
    ranking = [(total / simsums[item], item) for item, total in totals.items()]
    ranking.sort()
    ranking.reverse()
    return ranking
