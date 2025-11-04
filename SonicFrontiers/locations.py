from BaseClasses import Location
import typing
class AdvData(typing.NamedTuple):
        id: typing.Optional[int]

class SonicFrontiersAdvancement(Location):
    game: str = "Sonic Frontiers"
def create_locations():
    counter = 0
    kronosItems = [
        "Kronos Memory Token", "Kronos Memory Token Treasure", "Kronos Portal Gear", "Kronos Vault Key" "Kronos Map Challenge"
    ]
    aresItems = [
        "Ares Memory Token", "Ares Memory Token Treasure", "Ares Portal Gear", "Ares Vault Key", "Ares Map Challenge"
    ]
    chaosItems = [
        "Chaos Memory Token", "Chaos Memory Token Treasure", "Chaos Portal Gear", "Chaos Vault Key", "Chaos Map Challenge"
    ]
    ouranosItems = [
        "Ouranos Memory Token", "Ouranos Portal Gear", "Ouranos Vault Key", "Ouranos Map Challenge"
    ]
    kronosStages = [
        "1-1",
        "1-2",
        "1-3",
        "1-4",
        "1-5",
        "1-6",
        "1-7",
    ]
    aresStages = [
        "2-1",
        "2-2",
        "2-3",
        "2-4",
        "2-5",
        "2-6",
        "2-7",
    ]
    chaosStages = [
        "3-1",
        "3-2",
        "3-3",
        "3-4",
        "3-5",
        "3-6",
        "3-7",
    ]
    ouranosStages = [
        "4-1",
        "4-2",
        "4-3",
        "4-4",
        "4-5",
        "4-6",
        "4-7",
        "4-8",
        "4-9",
    ]
    skills = [
        "Phantom Rush", "Air Trick", "Stomp Attack",
        "Quick Cyloop", "Loop Kick", "Sonic Boom",
        "Wild Rush", "Homing Shot", "Spin Slash",
        "Recovery Smash", "Cyclone Kick","Cross Slash",
        "Grand Slam"
    ]
    kronosEmeralds = [
        "Kronos Blue Chaos Emerald", 
        "Kronos Red Chaos Emerald",
        "Kronos Green Chaos Emerald",
        "Kronos Yellow Chaos Emerald",
        "Kronos Cyan Chaos Emerald",
        "Kronos White Chaos Emerald"
    ]
    aresEmeralds = [
        "Ares Blue Chaos Emerald", 
        "Ares Red Chaos Emerald",
        "Ares Green Chaos Emerald",
        "Ares Yellow Chaos Emerald",
        "Ares Cyan Chaos Emerald",
        "Ares White Chaos Emerald"
    ]
    chaosEmeralds = [
        "Chaos Blue Chaos Emerald", 
        "Chaos Red Chaos Emerald",
        "Chaos Green Chaos Emerald",
        "Chaos Yellow Chaos Emerald",
        "Chaos Cyan Chaos Emerald",
        "Chaos White Chaos Emerald"
    ]
    ouranosEmeralds = [
        "Ouranos Blue Chaos Emerald", 
        "Ouranos Red Chaos Emerald",
        "Ouranos Green Chaos Emerald",
        "Ouranos Yellow Chaos Emerald",
        "Ouranos Cyan Chaos Emerald",
        "Ouranos White Chaos Emerald"
    ]
    sonicItems = [
        "Skill Points (200)",
        "Red Power Seed",
        "Blue Power Seed",
        "Kocos (20)"
    ]

    ##
    ## Kronos
    ##

    #10000
    counter = 0
    for i in range(91):
        kronosRegion[f"Kronos Memory Token {counter+1}"] = AdvData(kronosOff + counter)
        counter += 1
    #10091
    counter = 0
    for i in range(9):
        kronosRegion[f"Kronos Memory Treasure {counter+1}"] = AdvData(kronosOff + tokenDigOffset + counter)
        counter += 1
    counter = 0
    for i in range(17):
        kronosRegion[f"Kronos Portal Gear {i+1}"] = AdvData(kronosOff + gearOffset + counter)
        counter += 1
    counter = 0
    for i in range(5):
        kronosRegion[f"Kronos Vault Key {1+i}"] = AdvData(kronosOff+keyOffset+counter)
        counter += 1
    counter = 0

    for emerald in kronosEmeralds:
        kronosRegion[f"{emerald}"] = AdvData(kronosOff+counter+emeraldOffset)
        counter += 1
    counter = 0
    mapCounter = 1
    for i in range(25):
        if(mapCounter< 10):
            kronosRegion[f"Map Challenge M-00{mapCounter}"] = AdvData(kronosOff+counter+mapChallengeOffset)
            counter += 1
            mapCounter += 1
        else:
            kronosRegion[f"Map Challenge M-0{mapCounter}"] = AdvData(kronosOff+counter+mapChallengeOffset)
            counter += 1
            mapCounter += 1

    ##
    ## Ares
    ##
    counter = 0

    for i in range(285):
        aresRegion[f"Ares Memory Token {i+1}"] = AdvData(aresOff + counter)
        counter += 1
    for i in range(26):
            aresRegion[f"Ares Memory Treasure {i}"] = AdvData(aresOff + tokenDigOffset + i)
    counter = 0
    for i in range(11):
        aresRegion[f"Ares Portal Gear {i+1}"] = AdvData(aresOff + gearOffset+counter)
        counter += 1
    counter = 0
    for i in range(7):
        aresRegion[f"Ares Vault Key {1+i}"] = AdvData(aresOff+keyOffset+counter)
        counter += 1
    counter = 0
    for emerald in aresEmeralds:
        aresRegion[f"{emerald}"] = AdvData(aresOff+emeraldOffset+counter)
        counter += 1
    counter = 0
    for i in range(29):
        aresRegion[f"Map Challenge M-0{mapCounter}"] = AdvData(aresOff+mapChallengeOffset+counter)
        counter += 1
        mapCounter += 1

    ##
    ## Chaos
    ##

    counter = 0

    for i in range(252):
        chaosRegion[f"Chaos Memory Token {counter+1}"] = AdvData(chaosOff + counter)
        counter += 1
    for i in range(20):
        chaosRegion[f"Chaos Memory Treasure {i+1}"] = AdvData(chaosOff + tokenDigOffset+i)
    counter = 0
    for emerald in chaosEmeralds:
        chaosRegion[f"{emerald}"] = AdvData(chaosOff+emeraldOffset+counter)
        counter += 1
    counter = 0
    for i in range(8):
        chaosRegion[f"Chaos Vault Key {1+i}"] = AdvData(chaosOff+keyOffset+counter)
        counter += 1
    counter = 0
    for i in range(13):
        chaosRegion[f"Chaos Portal Gear {i+1}"] = AdvData(chaosOff +gearOffset+ counter)
        counter += 1
    counter = 0
    for i in range(24):
        chaosRegion[f"Map Challenge M-0{mapCounter}"] = AdvData(chaosOff+mapChallengeOffset+counter)
        counter += 1
        mapCounter += 1
    counter = 0

    ##
    ## Ouranos
    ##
    counter = 0

    for i in range(200):
        ouranosRegion[f"Ouranos Memory Token {counter+1}"] = AdvData(ouranosOff + counter)
        counter += 1
    for i in range(16):
        ouranosRegion[f"Ouranos Memory Treasure {i+1}"] = AdvData(ouranosOff + tokenDigOffset+i)
    counter = 0
    for i in range(21):
        ouranosRegion[f"Ouranos Portal Gear {i+1}"] = AdvData(ouranosOff + gearOffset+counter)
        counter += 1
    counter = 0
    for i in range(8):
        ouranosRegion[f"Ouranos Vault Key {1+i}"] = AdvData(ouranosOff+keyOffset+counter)
        counter += 1
    counter = 0
    for emerald in ouranosEmeralds:
        ouranosRegion[f"{emerald}"] = AdvData(ouranosOff+emeraldOffset+counter)
        counter += 1
    counter = 0
    for i in range(27):
        if(mapCounter > 100):
            ouranosRegion[f"Map Challenge M-{mapCounter}"] = AdvData(ouranosOff+mapChallengeOffset+counter)
            counter += 1
            mapCounter += 1
        else:
            ouranosRegion[f"Map Challenge M-0{mapCounter}"] = AdvData(ouranosOff+mapChallengeOffset+counter)
            counter += 1
            mapCounter += 1
    counter = 0
    for stage in kronosStages:
        for i in range(7):
            kronosRegion[f"{stage} All Missions ({i+1})"] = AdvData(cyberspaceOffset + counter)
            counter += 1
    for stage in aresStages:
        for i in range(7):
            aresRegion[f"{stage} All Missions ({i+1})"] = AdvData(cyberspaceOffset + counter)
            counter += 1
    for stage in chaosStages:
        for i in range(7):
            chaosRegion[f"{stage} All Missions ({i+1})"] = AdvData(cyberspaceOffset+counter)
            counter += 1
    for stage in ouranosStages:
        for i in range(7):
            ouranosRegion[f"{stage} All Missions ({i+1})"] = AdvData(cyberspaceOffset+ counter)
            counter += 1



##Essentially add all of these into a region. How do I add them? idfk
kronosRegion = {}
aresRegion = {}
chaosRegion = {}
ouranosRegion = {}
victoryRegion = {}

kronosOff: int = 10000
aresOff: int = 20000
chaosOff: int = 30000
ouranosOff: int = 40000
cyberspaceOffset: int = 50000

tokenDigOffset: int = 500
emeraldOffset: int = 1000
gearOffset: int = 2000
keyOffset: int = 3000
mapChallengeOffset: int = 5000



create_locations()

all_items = kronosRegion | aresRegion | chaosRegion | ouranosRegion | victoryRegion