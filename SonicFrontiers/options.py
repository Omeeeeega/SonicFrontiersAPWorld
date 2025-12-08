from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, DeathLink, Range, Choice, PerGameCommonOptions, ExcludeLocations  # , OptionGroup


class Goal(Choice):
    """
    Which Titan to defeat in order to complete the randomizer
    """
    display_name = "Goal"
    option_defeat_supreme = 0
    option_defeat_knight = 1
    option_defeat_wyvern = 2
    option_defeat_giganto = 3
    default = 0
class MemoryTokenSanity(Toggle):
    """
    Set whether All Memory Tokens should be locations
    """
    display_name = "Memory Token Sanity"
    default = 0
class MemoryTokenBundles(Toggle):
    """
    Set whether Memory Tokens should come as individual items or bundles of 8. Default is Bundles
    """
    display_name = "Memory Token Bundle"
    default = 0
class HarderCyberspaceTimes(Toggle):
    display_name = "Harder Cyberspace Challenge Times"
    default = 0
class MusicNotes(Toggle):
    display_name = "Harder Cyberspace Challenge Times"
    default = 0
class ChallengeKocos(Toggle):
    display_name = "Harder Cyberspace Challenge Times"
    default = 0
class CyberspaceStages(Toggle):
    display_name = "Harder Cyberspace Challenge Times"
    default = 0
class CyberspaceStages(Toggle):
    display_name = "Harder Cyberspace Challenge Times"
    default = 0
class ExcludedLocations(ExcludeLocations):
    testset = set()
    for i in range(91):
        testset.add(f"Kronos Memory Token {i+1}")
    for i in range(285):
        testset.add(f"Ares Memory Token {i+1}")
    for i in range(252):
        testset.add(f"Chaos Memory Token {i+1}")
    for i in range(200):
        testset.add(f"Ouranos Memory Token {i+1}")
    default = testset

@dataclass
class SonicFrontiersOptions(PerGameCommonOptions):
    goal: Goal
    death_link: DeathLink
    cyberspace_stages: CyberspaceStages
    memory_token_bundle: MemoryTokenBundles
    memory_token_sanity: MemoryTokenSanity
    cyberspace_times: HarderCyberspaceTimes
    music_notes: MusicNotes
    challenge_kocos: ChallengeKocos
    exclude_locations: ExcludedLocations
