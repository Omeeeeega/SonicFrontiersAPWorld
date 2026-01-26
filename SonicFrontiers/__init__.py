import settings
from typing import Dict, Any
from BaseClasses import MultiWorld, Region, Item
from worlds.AutoWorld import World
from Utils import visualize_regions
from worlds.generic.Rules import set_rule
from .items import (SonicFrontiersItem, SonicFrontiersItemData, item_list, kronos_amount, ares_amount, chaos_amount, ouranos_amount, fillers)
from .locations import (kronosRegion, SonicFrontiersAdvancement, aresRegion, chaosRegion, ouranosRegion, kronosMemoryTokenSet, 
                        aresMemoryTokenSet, chaosMemoryTokenSet, ouranosMemoryTokenSet, kronosPurpleSet, kronosKocoSet, aresKocoSet, 
                        aresPurpleSet, chaosKocoSet, chaosPurpleSet, ouranosKocoSet, ouranosPurpleSet, kronosNewKocoSet,
                        kronosMusicSet, aresMusicSet, aresNewKocoSet, chaosMusicSet, chaosNewKocoSet, ouranosMusicSet, ouranosNewKocoSet, all_items)
from .options import SonicFrontiersOptions

class SonicFrontiersWorld(World):
    game = "Sonic Frontiers"
    topology_present = False

    item_name_to_id = {name: data.id for name, data in item_list.items()}
    location_name_to_id = {name: data.id for name, data in all_items.items()}

    options_dataclass = SonicFrontiersOptions
    options: SonicFrontiersOptions
    def create_kronos_island(self) -> Region:
        return
    def create_ares_island(self) -> Region:
        return
    
    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)

        kronos_region = Region("Kronos", self.player, self.multiworld)
        kronos_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, kronos_region)for loc_name, loc_data in kronosRegion.items()]

        if(self.options.memory_token_sanity):
            kronos_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, kronos_region)for loc_name, loc_data in kronosMemoryTokenSet.items()]
        if(self.options.challenge_kocos):
            kronos_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, kronos_region)for loc_name, loc_data in kronosNewKocoSet.items()]
        if(self.options.music_notes):
            kronos_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, kronos_region)for loc_name, loc_data in kronosMusicSet.items()]
        if(self.options.purple_coin_sanity):
            kronos_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, kronos_region)for loc_name, loc_data in kronosPurpleSet.items()]
        if(self.options.koco_sanity):
            kronos_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, kronos_region)for loc_name, loc_data in kronosKocoSet.items()]
        menu_region.connect(kronos_region)
        self.multiworld.regions += [menu_region, kronos_region]

        if(self.options.goal > 0):
            ares_region = Region("Ares", self.player, self.multiworld)
            ares_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, ares_region)for loc_name, loc_data in aresRegion.items()]

            if(self.options.memory_token_sanity):
                ares_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, ares_region)for loc_name, loc_data in aresMemoryTokenSet.items()]
            if(self.options.challenge_kocos):
                ares_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, ares_region)for loc_name, loc_data in aresNewKocoSet.items()]
            if(self.options.music_notes):
                ares_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, ares_region)for loc_name, loc_data in aresMusicSet.items()]
            if(self.options.purple_coin_sanity):
                ares_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, ares_region)for loc_name, loc_data in aresPurpleSet.items()]
            if(self.options.koco_sanity):
                ares_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, ares_region)for loc_name, loc_data in aresKocoSet.items()]
            self.multiworld.regions += [ares_region]
            kronos_region.add_exits({"Ares": "Ares Entrance"})
        
        if(self.options.goal > 1):
            chaos_region = Region("Chaos", self.player, self.multiworld)
            chaos_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, chaos_region)for loc_name, loc_data in chaosRegion.items()]
            if(self.options.memory_token_sanity):
                chaos_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, chaos_region)for loc_name, loc_data in chaosMemoryTokenSet.items()]
            if(self.options.challenge_kocos):
                chaos_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, chaos_region)for loc_name, loc_data in chaosNewKocoSet.items()]
            if(self.options.music_notes):
                chaos_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, chaos_region)for loc_name, loc_data in chaosMusicSet.items()]
            if(self.options.purple_coin_sanity):
                chaos_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, chaos_region)for loc_name, loc_data in chaosPurpleSet.items()]
            if(self.options.koco_sanity):
                chaos_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, chaos_region)for loc_name, loc_data in chaosKocoSet.items()]
            self.multiworld.regions += [chaos_region]
            ares_region.add_exits({"Chaos": "Chaos Entrance"})

        if(self.options.goal > 2):
            ouranos_region = Region("Ouranos", self.player, self.multiworld)
            ouranos_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, ouranos_region)for loc_name, loc_data in ouranosRegion.items()]
            if(self.options.memory_token_sanity):
                ouranos_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, ouranos_region)for loc_name, loc_data in ouranosMemoryTokenSet.items()]
            if(self.options.challenge_kocos):
                ouranos_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, ouranos_region)for loc_name, loc_data in ouranosNewKocoSet.items()]
            if(self.options.music_notes):
                ouranos_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, ouranos_region)for loc_name, loc_data in ouranosMusicSet.items()]
            if(self.options.purple_coin_sanity):
                ouranos_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, ouranos_region)for loc_name, loc_data in ouranosPurpleSet.items()]
            if(self.options.koco_sanity):
                ouranos_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, ouranos_region)for loc_name, loc_data in ouranosKocoSet.items()]
            self.multiworld.regions += [ouranos_region]
            chaos_region.add_exits({"Ouranos": "Ouranos Entrance"})




    def set_rules(self) -> None:

        for i in range(7):
            set_rule(self.multiworld.get_location((f"1-2 All Missions ({i+1})"), self.player), lambda state: state.has("1-2 Unlocked", self.player, 1))
            set_rule(self.multiworld.get_location((f"1-3 All Missions ({i+1})"), self.player), lambda state: state.has("1-3 Unlocked", self.player, 1))
            set_rule(self.multiworld.get_location((f"1-4 All Missions ({i+1})"), self.player), lambda state: state.has("1-4 Unlocked", self.player, 1))
            set_rule(self.multiworld.get_location((f"1-5 All Missions ({i+1})"), self.player), lambda state: state.has("1-5 Unlocked", self.player, 1))
            set_rule(self.multiworld.get_location((f"1-6 All Missions ({i+1})"), self.player), lambda state: state.has("1-6 Unlocked", self.player, 1))
            set_rule(self.multiworld.get_location((f"1-7 All Missions ({i+1})"), self.player), lambda state: state.has("1-7 Unlocked", self.player, 1))
            if(self.options.goal > 0):
                set_rule(self.multiworld.get_location((f"2-1 All Missions ({i+1})"), self.player), lambda state: state.has("2-1 Unlocked", self.player, 1))
                set_rule(self.multiworld.get_location((f"2-2 All Missions ({i+1})"), self.player), lambda state: state.has("2-2 Unlocked", self.player, 1))
                set_rule(self.multiworld.get_location((f"2-3 All Missions ({i+1})"), self.player), lambda state: state.has("2-3 Unlocked", self.player, 1))
                set_rule(self.multiworld.get_location((f"2-4 All Missions ({i+1})"), self.player), lambda state: state.has("2-4 Unlocked", self.player, 1))
                set_rule(self.multiworld.get_location((f"2-5 All Missions ({i+1})"), self.player), lambda state: state.has("2-5 Unlocked", self.player, 1))
                set_rule(self.multiworld.get_location((f"2-6 All Missions ({i+1})"), self.player), lambda state: state.has("2-6 Unlocked", self.player, 1))
                set_rule(self.multiworld.get_location((f"2-7 All Missions ({i+1})"), self.player), lambda state: state.has("2-7 Unlocked", self.player, 1))
            if(self.options.goal > 1):
                set_rule(self.multiworld.get_location((f"3-1 All Missions ({i+1})"), self.player), lambda state: state.has("3-1 Unlocked", self.player, 1))
                set_rule(self.multiworld.get_location((f"3-2 All Missions ({i+1})"), self.player), lambda state: state.has("3-2 Unlocked", self.player, 1))
                set_rule(self.multiworld.get_location((f"3-3 All Missions ({i+1})"), self.player), lambda state: state.has("3-3 Unlocked", self.player, 1))
                set_rule(self.multiworld.get_location((f"3-4 All Missions ({i+1})"), self.player), lambda state: state.has("3-4 Unlocked", self.player, 1))
                set_rule(self.multiworld.get_location((f"3-5 All Missions ({i+1})"), self.player), lambda state: state.has("3-5 Unlocked", self.player, 1))
                set_rule(self.multiworld.get_location((f"3-6 All Missions ({i+1})"), self.player), lambda state: state.has("3-6 Unlocked", self.player, 1))
                set_rule(self.multiworld.get_location((f"3-7 All Missions ({i+1})"), self.player), lambda state: state.has("3-7 Unlocked", self.player, 1) 
                        and state.can_reach_location("Chaos Cyan Emerald", self.player))
            if(self.options.goal > 2):
                set_rule(self.multiworld.get_location((f"4-1 All Missions ({i+1})"), self.player), lambda state: state.has("4-1 Unlocked", self.player, 1))
                set_rule(self.multiworld.get_location((f"4-2 All Missions ({i+1})"), self.player), lambda state: state.has("4-2 Unlocked", self.player, 1))
                set_rule(self.multiworld.get_location((f"4-3 All Missions ({i+1})"), self.player), lambda state: state.has("4-3 Unlocked", self.player, 1))
                set_rule(self.multiworld.get_location((f"4-4 All Missions ({i+1})"), self.player), lambda state: state.has("4-4 Unlocked", self.player, 1))
                set_rule(self.multiworld.get_location((f"4-5 All Missions ({i+1})"), self.player), lambda state: state.has("4-5 Unlocked", self.player, 1))
                set_rule(self.multiworld.get_location((f"4-6 All Missions ({i+1})"), self.player), lambda state: state.has("4-6 Unlocked", self.player, 1))
                set_rule(self.multiworld.get_location((f"4-7 All Missions ({i+1})"), self.player), lambda state: state.has("4-7 Unlocked", self.player, 1))
                set_rule(self.multiworld.get_location((f"4-8 All Missions ({i+1})"), self.player), lambda state: state.has("4-8 Unlocked", self.player, 1))
                set_rule(self.multiworld.get_location((f"4-9 All Missions ({i+1})"), self.player), lambda state: state.has("4-9 Unlocked", self.player, 1))

        set_rule(self.multiworld.get_location(("Kronos Blue Emerald"), self.player), lambda state: state.has("Kronos Vault Key", self.player, 2))
        set_rule(self.multiworld.get_location(("Kronos Red Emerald"), self.player), lambda state: state.has("Kronos Vault Key", self.player, 5))
        set_rule(self.multiworld.get_location(("Kronos Green Emerald"), self.player), lambda state: state.has("Kronos Vault Key", self.player, 5) 
                 and state.has("Kronos Memory Treasure", self.player, 3) and state.has("Progressive Chaos Emerald", self.player, 2))
        set_rule(self.multiworld.get_location(("Kronos Yellow Emerald"), self.player), lambda state: state.has("Kronos Vault Key", self.player, 13))
        set_rule(self.multiworld.get_location(("Kronos Cyan Emerald"), self.player), lambda state: state.has("Kronos Vault Key", self.player, 13) 
                 and state.has("Kronos Memory Treasure", self.player, 6) and state.has("Progressive Chaos Emerald", self.player, 4))
        set_rule(self.multiworld.get_location(("Kronos White Emerald"), self.player), lambda state: state.has("Kronos Vault Key", self.player, 20))
        if(self.options.goal > 0):
            set_rule(self.multiworld.get_location(("Ares Blue Emerald"), self.player), lambda state: state.has("Ares Vault Key", self.player, 7))
            set_rule(self.multiworld.get_location(("Ares Red Emerald"), self.player), lambda state: state.has("Ares Vault Key", self.player, 14))
            set_rule(self.multiworld.get_location(("Ares Green Emerald"), self.player), lambda state: state.has("Ares Vault Key", self.player, 14) and state.has("Progressive Chaos Emerald", self.player, 8))
            set_rule(self.multiworld.get_location(("Ares Yellow Emerald"), self.player), lambda state: state.has("Ares Vault Key", self.player, 20))
            set_rule(self.multiworld.get_location(("Ares Cyan Emerald"), self.player), lambda state: state.has("Ares Vault Key", self.player, 20) and state.has("Progressive Chaos Emerald", self.player, 10))
            set_rule(self.multiworld.get_location(("Ares White Emerald"), self.player), lambda state: state.has("Ares Vault Key", self.player, 25))

        if(self.options.goal > 1):
            set_rule(self.multiworld.get_location(("Chaos Blue Emerald"), self.player), lambda state: state.has("Chaos Vault Key", self.player, 7))
            set_rule(self.multiworld.get_location(("Chaos Red Emerald"), self.player), lambda state: state.has("Chaos Vault Key", self.player, 14))
            set_rule(self.multiworld.get_location(("Chaos Green Emerald"), self.player), lambda state: state.has("Chaos Vault Key", self.player, 14) and state.has("Progressive Chaos Emerald", self.player, 14))
            set_rule(self.multiworld.get_location(("Chaos Yellow Emerald"), self.player), lambda state: state.has("Chaos Vault Key", self.player, 20))
            set_rule(self.multiworld.get_location(("Chaos Cyan Emerald"), self.player), lambda state: state.has("Chaos Vault Key", self.player, 20) and state.has("Progressive Chaos Emerald", self.player, 16))
            set_rule(self.multiworld.get_location(("Chaos White Emerald"), self.player), lambda state: state.has("Chaos Vault Key", self.player, 25))
        if(self.options.goal > 2):
            set_rule(self.multiworld.get_location(("Ouranos Blue Emerald"), self.player), lambda state: state.has("Ouranos Vault Key", self.player, 3))
            set_rule(self.multiworld.get_location(("Ouranos Red Emerald"), self.player), lambda state: state.has("Ouranos Vault Key", self.player, 9))
            set_rule(self.multiworld.get_location(("Ouranos Green Emerald"), self.player), lambda state: state.has("Ouranos Vault Key", self.player, 16))
            set_rule(self.multiworld.get_location(("Ouranos Yellow Emerald"), self.player), lambda state: state.has("Ouranos Vault Key", self.player, 23))
            set_rule(self.multiworld.get_location(("Ouranos Cyan Emerald"), self.player), lambda state: state.has("Ouranos Vault Key", self.player, 30))
            set_rule(self.multiworld.get_location(("Ouranos White Emerald"), self.player), lambda state: state.has("Ouranos Vault Key", self.player, 33))
        
        set_rule(self.multiworld.get_entrance("Ares Entrance", self.player), lambda state: state.has("Progressive Chaos Emerald", self.player, 6) 
                 and state.has("Kronos Memory Treasure", self.player, 9) and state.has("Stomp Attack", self.player) 
                 and state.has("Parry", self.player))

        set_rule(self.multiworld.get_entrance("Chaos Entrance", self.player),
        lambda state: state.has("Progressive Chaos Emerald", self.player, 12) and state.has("Ares Memory Treasure", self.player, 32))

        set_rule(self.multiworld.get_entrance("Ouranos Entrance", self.player), 
        lambda state: state.has("Progressive Chaos Emerald", self.player, 18) and state.has("Chaos Memory Treasure", self.player, 20)) 

    def create_items(self) -> None:
        numItems = 0
        for name, quantity in kronos_amount.items():
            for i in range(quantity):
                item = self.create_item(name)
                self.multiworld.itempool.append(item)
                numItems += 1
        if self.options.goal > 0:
            for name, quantity in ares_amount.items():
                for i in range(quantity):
                    item = self.create_item(name)
                    self.multiworld.itempool.append(item)
                    numItems += 1
        if self.options.goal > 1:
            for name, quantity in chaos_amount.items():
                for i in range(quantity):
                    item = self.create_item(name)
                    self.multiworld.itempool.append(item)
                    numItems += 1
        if self.options.goal > 2:
            for name, quantity in ouranos_amount.items():
                for i in range(quantity):
                    item = self.create_item(name)
                    self.multiworld.itempool.append(item)
                    numItems += 1
        filler = len(self.multiworld.get_locations(self.player)) - len(self.multiworld.get_items())
        for _ in range(filler):
            name = self.random.choices(list(fillers.keys()), weights = list(fillers.values()))[0]
            item = self.create_item(name)
            self.multiworld.itempool.append(item)
    def create_item(self, name: str) -> Item:
        item_data = item_list[name]
        item = SonicFrontiersItem(name, item_data.item_class, item_data.id, self.player)
        return item
    def fill_slot_data(self) -> Dict[str, Any]:
        return {
            "death_link": self.options.death_link.value,
            "goal": self.options.goal.value,
            "memory_token_sanity": self.options.memory_token_sanity.value,
            "cyberspace_times": self.options.cyberspace_times.value,
            "music_notes": self.options.music_notes.value,
            "challenge_kocos": self.options.challenge_kocos.value,
            "purple_coin_sanity": self.options.purple_coin_sanity.value,
            "koco_sanity": self.options.koco_sanity.value,
        }
    

