# fmt: off
"""Logic file for Crystal Caves."""

from randomizer.Enums.Events import Events
from randomizer.Enums.Exits import Exits
from randomizer.Enums.Kongs import Kongs
from randomizer.Enums.Levels import Levels
from randomizer.Enums.Locations import Locations
from randomizer.Enums.Regions import Regions
from randomizer.LogicClasses import Event, Exit, LocationLogic, Region

LogicRegions = {
    Regions.CrystalCavesMain: Region("Crystal Caves Main", Levels.CrystalCaves, True, None, [
        LocationLogic(Locations.CavesDonkeyMedal, lambda l: l.ColoredBananas[Levels.CrystalCaves][Kongs.donkey] >= 75),
        LocationLogic(Locations.CavesDiddyMedal, lambda l: l.ColoredBananas[Levels.CrystalCaves][Kongs.diddy] >= 75),
        LocationLogic(Locations.CavesLankyMedal, lambda l: l.ColoredBananas[Levels.CrystalCaves][Kongs.lanky] >= 75),
        LocationLogic(Locations.CavesTinyMedal, lambda l: l.ColoredBananas[Levels.CrystalCaves][Kongs.tiny] >= 75),
        LocationLogic(Locations.CavesChunkyMedal, lambda l: l.ColoredBananas[Levels.CrystalCaves][Kongs.chunky] >= 75),
        LocationLogic(Locations.CavesDonkeyBaboonBlast, lambda l: l.blast and l.donkey),
        LocationLogic(Locations.CavesDiddyJetpackBarrel, lambda l: l.jetpack and l.diddy),
        LocationLogic(Locations.CavesTinyKrazyKongKlamour, lambda l: l.mini and l.tiny),
        LocationLogic(Locations.CavesTinyMonkeyportIgloo, lambda l: l.monkeyport and l.mini and l.twirl and l.tiny),
        LocationLogic(Locations.CavesChunkyGorillaGone, lambda l: l.punch and l.gorillaGone and l.chunky),
        LocationLogic(Locations.CavesDonkeyKasplat, lambda l: l.donkey),
        LocationLogic(Locations.CavesDiddyKasplat, lambda l: l.mini and l.twirl and l.tiny and l.diddy),
        LocationLogic(Locations.CavesLankyKasplat, lambda l: l.jetpack and l.diddy and l.lanky),
        LocationLogic(Locations.CavesTinyKasplat, lambda l: l.tiny),
    ], [
        Event(Events.CavesEntered, lambda l: True),
        Event(Events.CavesSmallBoulderButton, lambda l: l.chunky),
    ], [
        Exit(Regions.CrystalCavesLobby, lambda l: True, Exits.CavesToIsles),
        Exit(Regions.BoulderIgloo, lambda l: l.punch),
        Exit(Regions.CavesLankyRace, lambda l: l.superSlam and l.balloon and l.islanky, Exits.CavesMainToRace),
        Exit(Regions.FrozenCastle, lambda l: l.superSlam and l.islanky, Exits.CavesMainToCastle),
        Exit(Regions.IglooArea, lambda l: True),
        Exit(Regions.CabinArea, lambda l: True),
        Exit(Regions.Funky, lambda l: True),
        Exit(Regions.Cranky, lambda l: True),
        Exit(Regions.Snide, lambda l: l.punch),
        Exit(Regions.CavesBossLobby, lambda l: l.punch),
    ]),

    Regions.BoulderIgloo: Region("Boulder Igloo", Levels.CrystalCaves, True, None, [], [
        Event(Events.CavesLargeBoulderButton, lambda l: Events.CavesSmallBoulderButton in l.Events and l.hunkyChunky and l.chunky),
    ], [
        Exit(Regions.CrystalCavesMain, lambda l: True),
        Exit(Regions.CavesBossLobby, lambda l: True),
    ]),

    Regions.CavesLankyRace: Region("Caves Lanky Race", Levels.CrystalCaves, False, None, [
        LocationLogic(Locations.CavesLankyBeetleRace, lambda l: l.sprint and l.islanky),
    ], [], [
        Exit(Regions.CrystalCavesMain, lambda l: True, Exits.CavesRaceToMain),
    ]),

    Regions.FrozenCastle: Region("Frozen Castle", Levels.CrystalCaves, False, None, [
        LocationLogic(Locations.CavesLankyCastle, lambda l: l.Slam and l.islanky),
    ], [], [
        Exit(Regions.CrystalCavesMain, lambda l: True, Exits.CavesCastleToMain),
    ]),

    Regions.IglooArea: Region("Igloo Area", Levels.CrystalCaves, True, None, [
        LocationLogic(Locations.CavesChunkyTransparentIgloo, lambda l: Events.CavesLargeBoulderButton in l.Events and l.chunky),
        LocationLogic(Locations.CavesChunkyKasplat, lambda l: l.chunky),
    ], [], [
        Exit(Regions.CrystalCavesMain, lambda l: True),
        Exit(Regions.GiantKosha, lambda l: Events.CavesLargeBoulderButton in l.Events and l.monkeyport and l.istiny),
        Exit(Regions.DonkeyIgloo, lambda l: l.jetpack and l.bongos and l.isdonkey, Exits.CavesIglooToDonkey),
        Exit(Regions.DiddyIgloo, lambda l: l.jetpack and l.guitar and l.isdiddy, Exits.CavesIglooToDiddy),
        Exit(Regions.LankyIgloo, lambda l: l.jetpack and l.trombone and l.islanky, Exits.CavesIglooToLanky),
        Exit(Regions.TinyIgloo, lambda l: l.jetpack and l.saxophone and l.istiny, Exits.CavesIglooToTiny),
        Exit(Regions.ChunkyIgloo, lambda l: l.jetpack and l.triangle and l.ischunky, Exits.CavesIglooToChunky),
    ]),

    Regions.GiantKosha: Region("Giant Kosha", Levels.CrystalCaves, False, -1, [], [
        Event(Events.GiantKoshaDefeated, lambda l: l.shockwave or l.saxophone),
    ], []),

    # Deaths in Donkey and Diddy's igloos take you back to them, the others to the beginning of the level
    Regions.DonkeyIgloo: Region("Donkey Igloo", Levels.CrystalCaves, False, None, [
        LocationLogic(Locations.CavesDonkey5DoorIgloo, lambda l: l.isdonkey),
    ], [], [
        Exit(Regions.IglooArea, lambda l: True, Exits.CavesDonkeyToIgloo),
    ]),

    Regions.DiddyIgloo: Region("Diddy Igloo", Levels.CrystalCaves, False, None, [
        LocationLogic(Locations.CavesDiddy5DoorIgloo, lambda l: l.isdiddy),
    ], [], [
        Exit(Regions.IglooArea, lambda l: True, Exits.CavesDiddyToIgloo),
    ]),

    Regions.LankyIgloo: Region("Lanky Igloo", Levels.CrystalCaves, False, -1, [
        LocationLogic(Locations.CavesLanky5DoorIgloo, lambda l: l.balloon and l.islanky),
    ], [], [
        Exit(Regions.IglooArea, lambda l: True, Exits.CavesLankyToIgloo),
    ]),

    Regions.TinyIgloo: Region("Tiny Igloo", Levels.CrystalCaves, False, -1, [
        LocationLogic(Locations.CavesTiny5DoorIgloo, lambda l: l.Slam and l.istiny),
        LocationLogic(Locations.CavesBananaFairyIgloo, lambda l: l.camera),
    ], [], [
        Exit(Regions.IglooArea, lambda l: True, Exits.CavesTinyToIgloo),
    ]),

    Regions.ChunkyIgloo: Region("Chunky Igloo", Levels.CrystalCaves, False, -1, [
        LocationLogic(Locations.CavesChunky5DoorIgloo, lambda l: l.ischunky),
    ], [], [
        Exit(Regions.IglooArea, lambda l: True, Exits.CavesChunkyToIgloo),
    ]),

    Regions.CabinArea: Region("Cabin Area", Levels.CrystalCaves, True, None, [], [], [
        Exit(Regions.CrystalCavesMain, lambda l: True),
        Exit(Regions.RotatingCabin, lambda l: l.bongos and l.isdonkey, Exits.CavesCabinToRotating),
        Exit(Regions.DonkeyCabin, lambda l: l.bongos and l.isdonkey, Exits.CavesCabinToDonkey),
        Exit(Regions.DiddyLowerCabin, lambda l: l.guitar and l.isdiddy, Exits.CavesCabinToDiddyLower),
        Exit(Regions.DiddyUpperCabin, lambda l: l.guitar and l.isdiddy, Exits.CavesCabinToDiddyUpper),
        Exit(Regions.LankyCabin, lambda l: l.trombone and l.balloon and l.islanky, Exits.CavesCabinToLanky),
        Exit(Regions.TinyCabin, lambda l: l.saxophone and l.istiny, Exits.CavesCabinToTiny),
        Exit(Regions.ChunkyCabin, lambda l: l.triangle and l.ischunky, Exits.CavesCabinToChunky),
        Exit(Regions.Candy, lambda l: True),
        Exit(Regions.CavesBossLobby, lambda l: l.jetpack or l.balloon),
    ]),

    Regions.RotatingCabin: Region("Rotating Cabin", Levels.CrystalCaves, False, None, [
        LocationLogic(Locations.CavesDonkeyRotatingCabin, lambda l: l.Slam and l.isdonkey),
        LocationLogic(Locations.CavesBattleArena, lambda l: l.Slam),
    ], [], [
        Exit(Regions.CabinArea, lambda l: True, Exits.CavesRotatingToCabin),
    ]),

    # Lanky's and Diddy's cabins take you to the beginning of the level, others respawn there
    Regions.DonkeyCabin: Region("Donkey Cabin", Levels.CrystalCaves, False, None, [
        LocationLogic(Locations.CavesDonkey5DoorCabin, lambda l: l.isdonkey),
    ], [], [
        Exit(Regions.CabinArea, lambda l: True, Exits.CavesDonkeyToCabin),
    ]),

    Regions.DiddyLowerCabin: Region("Diddy Lower Cabin", Levels.CrystalCaves, False, -1, [
        # You're supposed to use the jetpack to get up the platforms,
        # but you can just backflip onto them
        LocationLogic(Locations.CavesDiddy5DoorCabinLower, lambda l: l.isdiddy),
    ], [], [
        Exit(Regions.CabinArea, lambda l: True, Exits.CavesDiddyLowerToCabin),
    ]),

    Regions.DiddyUpperCabin: Region("Diddy Upper Cabin", Levels.CrystalCaves, False, -1, [
        LocationLogic(Locations.CavesDiddy5DoorCabinUpper, lambda l: (l.guitar or l.shockwave) and l.spring and l.jetpack and l.isdiddy),
        LocationLogic(Locations.CavesBananaFairyCabin, lambda l: l.camera and (l.guitar or l.shockwave) and l.spring and l.jetpack and l.isdiddy),
    ], [], [
        Exit(Regions.CabinArea, lambda l: True, Exits.CavesDiddyUpperToCabin),
    ]),

    Regions.LankyCabin: Region("Lanky Cabin", Levels.CrystalCaves, False, -1, [
        LocationLogic(Locations.CavesLanky1DoorCabin, lambda l: l.sprint and l.balloon and l.islanky),
    ], [], [
        Exit(Regions.CabinArea, lambda l: True, Exits.CavesLankyToCabin),
    ]),

    Regions.TinyCabin: Region("Tiny Cabin", Levels.CrystalCaves, False, None, [
        LocationLogic(Locations.CavesTiny5DoorCabin, lambda l: l.istiny),
    ], [], [
        Exit(Regions.CabinArea, lambda l: True, Exits.CavesTinyToCabin),
    ]),

    Regions.ChunkyCabin: Region("Chunky Cabin", Levels.CrystalCaves, False, None, [
        LocationLogic(Locations.CavesChunky5DoorCabin, lambda l: l.gorillaGone and l.Slam and l.ischunky),
    ], [], [
        Exit(Regions.CabinArea, lambda l: True, Exits.CavesChunkyToCabin),
    ]),

    Regions.CavesBossLobby: Region("Caves Boss Lobby", Levels.CrystalCaves, True, None, [], [], [
        Exit(Regions.CavesBoss, lambda l: l.isdonkey and sum(l.ColoredBananas[Levels.CrystalCaves]) >= l.settings.BossBananas[Levels.CrystalCaves - 1]),
    ]),

    Regions.CavesBoss: Region("Caves Boss", Levels.CrystalCaves, False, None, [
        LocationLogic(Locations.CavesKey, lambda l: l.isdonkey),
    ], [], []),
}
