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
        "Kronos Blue Emerald", 
        "Kronos Red Emerald",
        "Kronos Green Emerald",
        "Kronos Yellow Emerald",
        "Kronos Cyan Emerald",
        "Kronos White Emerald"
    ]
    aresEmeralds = [
        "Ares Blue Emerald", 
        "Ares Red Emerald",
        "Ares Green Emerald",
        "Ares Yellow Emerald",
        "Ares Cyan Emerald",
        "Ares White Emerald"
    ]
    chaosEmeralds = [
        "Chaos Blue Emerald", 
        "Chaos Red Emerald",
        "Chaos Green Emerald",
        "Chaos Yellow Emerald",
        "Chaos Cyan Emerald",
        "Chaos White Emerald"
    ]
    ouranosEmeralds = [
        "Ouranos Blue Emerald", 
        "Ouranos Red Emerald",
        "Ouranos Green Emerald",
        "Ouranos Yellow Emerald",
        "Ouranos Cyan Emerald",
        "Ouranos White Emerald"
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
    for i in range(8):
        kronosRegion[f"Challenge Koco {i}"] = AdvData(kronosOff+i+newKocoOffset)
    for i in range(13):
        kronosRegion[f"Music Note {i}"] = AdvData(kronosOff+i+musicOffset)

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
    for i in range(8):
        aresRegion[f"Challenge Koco {i+8}"] = AdvData(aresOff+i+newKocoOffset)
    for i in range(13):
        aresRegion[f"Music Note {i+13}"] = AdvData(aresOff+i+musicOffset)

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

    for i in range(8):
        chaosRegion[f"Challenge Koco {i+16}"] = AdvData(chaosOff+i+newKocoOffset)
    for i in range(13):
        chaosRegion[f"Music Note {i+26}"] = AdvData(chaosOff+i+musicOffset)
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
    
    for i in range(8):
        ouranosRegion[f"Challenge Koco {i+24}"] = AdvData(ouranosOff+i+newKocoOffset)
    for i in range(13):
        ouranosRegion[f"Music Note {i+39}"] = AdvData(ouranosOff+i+musicOffset)



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
musicOffset: int = 1500
gearOffset: int = 2000
newKocoOffset: int = 2500
keyOffset: int = 3000
purpleCoinOffset: int = 4000
mapChallengeOffset: int = 5000
kocoOffset: int = 6000


create_locations()

all_items = kronosRegion | aresRegion | chaosRegion | ouranosRegion | victoryRegion