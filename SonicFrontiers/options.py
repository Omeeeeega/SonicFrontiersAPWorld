from dataclasses import dataclass
from Options import Toggle, DefaultOnToggle, DeathLink, Range, Choice, PerGameCommonOptions, ExcludeLocations  # , OptionGroup


class Goal(Choice):
    """
    Total Journal Completion: Reach a specific percentage threshold in total journal completion
    (i.e. all fish, all rarities).

    Rank: Reach a specific rank.

    Camp: Unlock all camp tiers and purchase the final tier.
    """
    display_name = "Goal"
    defeat_supreme = 0
    defeat_knight = 1
    defeat_wyvern = 2
    defeat_giganto = 3
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
    default = frozenset(testset)

@dataclass
class SonicFrontiersOptions(PerGameCommonOptions):
    goal: Goal
    death_link: DeathLink
    exclude_locations: ExcludedLocations
