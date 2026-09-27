from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, DeathLink, Range, Choice, PerGameCommonOptions, ExcludeLocations  # , OptionGroup


class Goal(Choice):
    """
    Which Titan to defeat in order to complete the randomizer

    Note: Only Kronos and Ares Island for this release
    """
    display_name = "Goal"
    option_defeat_giganto = 0
    option_defeat_wyvern = 1
    #option_defeat_knight = 2
    #option_defeat_supreme = 3
    default = 0
class MemoryTokenSanity(Toggle):
    """
    Set whether All Memory Tokens should be locations
    """
    display_name = "Memory Token Sanity"
    default = 0
class MapChallenges(DefaultOnToggle):
    display_name = "Map Challenge Sanity"
class HarderCyberspaceTimes(Toggle):
    """
    This makes all Cyberspace stages have a harder S-Rank requirement. 

    Note: This is meant for speedrunners, do not enable this unless you're up for a challenge.
    """
    display_name = "Harder Cyberspace Challenge Times"
    default = 0
    
class MusicNotes(Toggle):
    """
    Set whether Music Notes should be locations
    """
    display_name = "Music Notes"
    default = 0
class ChallengeKocos(Toggle):
    """
    Set whether Challenge Kocos should be locations
    """
    display_name = "Challenge Kocos"
    default = 0
class CyberspaceStages(Toggle):
    display_name = "Cyberspace Stages Missions"
    default = 0
class PurpleCoinSanity(Toggle):
    """
    Set whether All Purple Coins should be locations
    """
    display_name = "Purple Coin Sanity"
    default = 0
class KocoSanity(Toggle):
    """
    Set whether All Kocos should be locations
    """
    display_name = "Koco Sanity"
    default = 0

class TrapsEnabled(Toggle):
    """
    Set whether Traps are enabled
    """
    display_name = "Enable Traps"
    default = 0
class BaseTrapWeight(Choice):
    """
    Base Class for Trap Weights
    """
    option_none = 0
    option_low = 1
    option_medium = 2
    option_high = 4
    default = 2
class TrapsEnabled(Toggle):
    """
    Set whether Traps are enabled
    """
    display_name = "Enable Traps"
    default = 0
class WaterTrap(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which causes Water Physics
    """
    display_name = "Water Trap"
class RingTrap(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which causes Sonic to lose rings
    """
    display_name = "Ring Trap"
class AutorunTrap(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which causes Sonic to automatically run
    """
    display_name = "AutoRun Trap"
class FireTrap(BaseTrapWeight):
    """
    Likelihood of a receiving a trap which causes Sonic to catch Fire
    """
    display_name = "Fire Trap"

@dataclass
class SonicFrontiersOptions(PerGameCommonOptions):
    goal: Goal
    death_link: DeathLink
    memory_token_sanity: MemoryTokenSanity
    cyberspace_times: HarderCyberspaceTimes
    music_notes: MusicNotes
    challenge_kocos: ChallengeKocos
    purple_coin_sanity: PurpleCoinSanity
    koco_sanity: KocoSanity
    traps_enabled: TrapsEnabled
    water_trap: WaterTrap
    ring_trap: RingTrap
    autorun_trap: AutorunTrap
    fire_trap: FireTrap
