import settings
from typing import Dict, Any
from BaseClasses import MultiWorld, Region, Item
from worlds.AutoWorld import World
from Utils import visualize_regions
from worlds.generic.Rules import set_rule
from .items import (SonicFrontiersItem, SonicFrontiersItemData, item_list, fixed_amount, fillers)
from .locations import (kronosRegion, SonicFrontiersAdvancement, aresRegion, chaosRegion, ouranosRegion, all_items)
from .options import SonicFrontiersOptions

class SonicFrontiersWorld(World):
    game = "Sonic Frontiers"
    topology_present = False

    item_name_to_id = {name: data.id for name, data in item_list.items()}
    location_name_to_id = {name: data.id for name, data in all_items.items()}
    options_dataclass = SonicFrontiersOptions
    options: SonicFrontiersOptions

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)

        kronos_region = Region("Kronos", self.player, self.multiworld)
        kronos_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, kronos_region)for loc_name, loc_data in kronosRegion.items()]

        ares_region = Region("Ares", self.player, self.multiworld)
        ares_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, ares_region)for loc_name, loc_data in aresRegion.items()]

        chaos_region = Region("Chaos", self.player, self.multiworld)
        chaos_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, chaos_region)for loc_name, loc_data in chaosRegion.items()]

        ouranos_region = Region("Ouranos", self.player, self.multiworld)
        ouranos_region.locations += [SonicFrontiersAdvancement(self.player, loc_name, loc_data.id, ouranos_region)for loc_name, loc_data in ouranosRegion.items()]

        self.multiworld.regions += [menu_region, kronos_region, ares_region, chaos_region, ouranos_region]

        menu_region.connect(kronos_region)
        kronos_region.add_exits({"Ares": "Ares Entrance"})

        ares_region.add_exits({"Chaos": "Chaos Entrance"})
        chaos_region.add_exits({"Ouranos": "Ouranos Entrance"})

    def set_rules(self) -> None:

        for i in range(7):
            set_rule(self.multiworld.get_location((f"1-2 All Missions ({i+1})"), self.player), lambda state: state.has("1-2 Unlocked", self.player, 1))
            set_rule(self.multiworld.get_location((f"1-3 All Missions ({i+1})"), self.player), lambda state: state.has("1-3 Unlocked", self.player, 1))
            set_rule(self.multiworld.get_location((f"1-4 All Missions ({i+1})"), self.player), lambda state: state.has("1-4 Unlocked", self.player, 1))
            set_rule(self.multiworld.get_location((f"1-5 All Missions ({i+1})"), self.player), lambda state: state.has("1-5 Unlocked", self.player, 1))
            set_rule(self.multiworld.get_location((f"1-6 All Missions ({i+1})"), self.player), lambda state: state.has("1-6 Unlocked", self.player, 1))
            set_rule(self.multiworld.get_location((f"1-7 All Missions ({i+1})"), self.player), lambda state: state.has("1-7 Unlocked", self.player, 1))
            set_rule(self.multiworld.get_location((f"2-1 All Missions ({i+1})"), self.player), lambda state: state.has("2-1 Unlocked", self.player, 1))
            set_rule(self.multiworld.get_location((f"2-2 All Missions ({i+1})"), self.player), lambda state: state.has("2-2 Unlocked", self.player, 1))
            set_rule(self.multiworld.get_location((f"2-3 All Missions ({i+1})"), self.player), lambda state: state.has("2-3 Unlocked", self.player, 1))
            set_rule(self.multiworld.get_location((f"2-4 All Missions ({i+1})"), self.player), lambda state: state.has("2-4 Unlocked", self.player, 1))
            set_rule(self.multiworld.get_location((f"2-5 All Missions ({i+1})"), self.player), lambda state: state.has("2-5 Unlocked", self.player, 1))
            set_rule(self.multiworld.get_location((f"2-6 All Missions ({i+1})"), self.player), lambda state: state.has("2-6 Unlocked", self.player, 1))
            set_rule(self.multiworld.get_location((f"2-7 All Missions ({i+1})"), self.player), lambda state: state.has("2-7 Unlocked", self.player, 1))

            set_rule(self.multiworld.get_location((f"3-1 All Missions ({i+1})"), self.player), lambda state: state.has("3-1 Unlocked", self.player, 1))
            set_rule(self.multiworld.get_location((f"3-2 All Missions ({i+1})"), self.player), lambda state: state.has("3-2 Unlocked", self.player, 1))
            set_rule(self.multiworld.get_location((f"3-3 All Missions ({i+1})"), self.player), lambda state: state.has("3-3 Unlocked", self.player, 1))
            set_rule(self.multiworld.get_location((f"3-4 All Missions ({i+1})"), self.player), lambda state: state.has("3-4 Unlocked", self.player, 1))
            set_rule(self.multiworld.get_location((f"3-5 All Missions ({i+1})"), self.player), lambda state: state.has("3-5 Unlocked", self.player, 1))
            set_rule(self.multiworld.get_location((f"3-6 All Missions ({i+1})"), self.player), lambda state: state.has("3-6 Unlocked", self.player, 1))
            set_rule(self.multiworld.get_location((f"3-7 All Missions ({i+1})"), self.player), lambda state: state.has("3-7 Unlocked", self.player, 1) 
                     and state.can_reach_location("Chaos Cyan Emerald", self.player))
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
        set_rule(self.multiworld.get_location(("Kronos Green Emerald"), self.player), lambda state: state.has("Kronos Vault Key", self.player, 5))
        set_rule(self.multiworld.get_location(("Kronos Yellow Emerald"), self.player), lambda state: state.has("Kronos Vault Key", self.player, 13))
        set_rule(self.multiworld.get_location(("Kronos Cyan Emerald"), self.player), lambda state: state.has("Kronos Vault Key", self.player, 13))
        set_rule(self.multiworld.get_location(("Kronos White Emerald"), self.player), lambda state: state.has("Kronos Vault Key", self.player, 20))
        set_rule(self.multiworld.get_location(("Ares Blue Emerald"), self.player), lambda state: state.has("Ares Vault Key", self.player, 7))
        set_rule(self.multiworld.get_location(("Ares Red Emerald"), self.player), lambda state: state.has("Ares Vault Key", self.player, 14))
        set_rule(self.multiworld.get_location(("Ares Green Emerald"), self.player), lambda state: state.has("Ares Vault Key", self.player, 14))
        set_rule(self.multiworld.get_location(("Ares Yellow Emerald"), self.player), lambda state: state.has("Ares Vault Key", self.player, 20))
        set_rule(self.multiworld.get_location(("Ares Cyan Emerald"), self.player), lambda state: state.has("Ares Vault Key", self.player, 20))
        set_rule(self.multiworld.get_location(("Ares White Emerald"), self.player), lambda state: state.has("Ares Vault Key", self.player, 25))

        set_rule(self.multiworld.get_location(("Chaos Blue Emerald"), self.player), lambda state: state.has("Chaos Vault Key", self.player, 7))
        set_rule(self.multiworld.get_location(("Chaos Red Emerald"), self.player), lambda state: state.has("Chaos Vault Key", self.player, 14))
        set_rule(self.multiworld.get_location(("Chaos Green Emerald"), self.player), lambda state: state.has("Chaos Vault Key", self.player, 14))
        set_rule(self.multiworld.get_location(("Chaos Yellow Emerald"), self.player), lambda state: state.has("Chaos Vault Key", self.player, 20))
        set_rule(self.multiworld.get_location(("Chaos Cyan Emerald"), self.player), lambda state: state.has("Chaos Vault Key", self.player, 20))
        set_rule(self.multiworld.get_location(("Chaos White Emerald"), self.player), lambda state: state.has("Chaos Vault Key", self.player, 25))
        set_rule(self.multiworld.get_location(("Ouranos Blue Emerald"), self.player), lambda state: state.has("Ouranos Vault Key", self.player, 3))
        set_rule(self.multiworld.get_location(("Ouranos Red Emerald"), self.player), lambda state: state.has("Ouranos Vault Key", self.player, 9))
        set_rule(self.multiworld.get_location(("Ouranos Green Emerald"), self.player), lambda state: state.has("Ouranos Vault Key", self.player, 16))
        set_rule(self.multiworld.get_location(("Ouranos Yellow Emerald"), self.player), lambda state: state.has("Ouranos Vault Key", self.player, 23))
        set_rule(self.multiworld.get_location(("Ouranos Cyan Emerald"), self.player), lambda state: state.has("Ouranos Vault Key", self.player, 30))
        set_rule(self.multiworld.get_location(("Ouranos White Emerald"), self.player), lambda state: state.has("Ouranos Vault Key", self.player, 33))

        set_rule(self.multiworld.get_entrance("Ares Entrance", self.player), 
        lambda state: state.has("Kronos White Emerald", self.player) and state.has("Kronos Blue Emerald", self.player) and
        state.has("Kronos Red Emerald", self.player) and state.has("Kronos Green Emerald", self.player) and state.has("Kronos Yellow Emerald", self.player) and
        state.has("Kronos Cyan Emerald", self.player) and state.has("Kronos Memory Treasure", self.player, 9) and state.has("Stomp Attack", self.player) 
        and state.has("Parry", self.player))

        set_rule(self.multiworld.get_entrance("Chaos Entrance", self.player),
        lambda state: state.has("Ares White Emerald", self.player) and state.has("Ares Blue Emerald", self.player) and
        state.has("Ares Red Emerald", self.player) and state.has("Ares Green Emerald", self.player) and state.has("Ares Yellow Emerald", self.player) and
        state.has("Ares Cyan Emerald", self.player) and state.has("Ares Memory Treasure", self.player, 32))
    
        set_rule(self.multiworld.get_entrance("Ouranos Entrance", self.player), 
        lambda state: state.has("Chaos White Emerald", self.player) and state.has("Chaos Blue Emerald", self.player) and
        state.has("Chaos Red Emerald", self.player) and state.has("Chaos Green Emerald", self.player) and state.has("Chaos Yellow Emerald", self.player) and
        state.has("Chaos Cyan Emerald", self.player) and state.has("Chaos Memory Treasure", self.player, 20)) 

    def create_items(self) -> None:
        for name, quantity in fixed_amount.items():
            for i in range(quantity):
                item = self.create_item(name)
                self.multiworld.itempool.append(item)
        filler = len(all_items) - sum(fixed_amount.values())
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
            "cyberspace_stages": self.options.cyberspace_stages.value,
            "memory_token_sanity": self.options.memory_token_sanity.value,
            "memory_token_bundle": self.options.memory_token_bundle.value,
            "cyberspace_times": self.options.cyberspace_times.value,
            "music_notes": self.options.music_notes.value,
            "challenge_kocos": self.options.challenge_kocos.value,
        }