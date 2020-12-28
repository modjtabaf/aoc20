
if 0:
  data = [
    ["se", "se", "nw", "ne", "ne", "ne", "w", "se", "e", "sw", "w", "sw", "sw", "w", "ne", "ne", "w", "se", "w", "sw"],
    ["ne", "e", "e", "ne", "se", "nw", "nw", "w", "sw", "ne", "ne", "w", "nw", "w", "se", "w", "ne", "nw", "se", "sw", "e", "sw"],
    ["se", "sw", "ne", "sw", "sw", "se", "nw", "w", "nw", "se"],
    ["nw", "nw", "ne", "se", "e", "sw", "sw", "ne", "ne", "w", "ne", "sw", "w", "ne", "w", "se", "sw", "ne", "se", "e", "ne"],
    ["sw", "w", "e", "sw", "ne", "sw", "ne", "nw", "se", "w", "nw", "ne", "ne", "se", "e", "nw"],
    ["e", "e", "se", "nw", "se", "sw", "sw", "ne", "nw", "sw", "nw", "nw", "se", "w", "w", "nw", "se", "ne"],
    ["se", "w", "ne", "ne", "ne", "ne", "se", "nw", "se", "w", "ne", "nw", "w", "w", "se"],
    ["w", "e", "nw", "w", "w", "e", "se", "e", "e", "w", "e", "sw", "w", "w", "nw", "w", "e"],
    ["w", "sw", "e", "e", "se", "ne", "ne", "w", "nw", "w", "nw", "se", "ne", "w", "se", "nw", "w", "se", "se", "se", "nw", "ne"],
    ["ne", "e", "sw", "se", "e", "nw", "w", "sw", "nw", "sw", "sw", "nw"],
    ["ne", "nw", "sw", "w", "se", "w", "sw", "ne", "ne", "ne", "w", "se", "nw", "se", "nw", "ne", "se", "se", "ne", "w"],
    ["e", "ne", "w", "nw", "e", "w", "ne", "sw", "se", "w", "nw", "sw", "e", "nw", "e", "sw", "ne", "nw", "se", "nw", "sw"],
    ["sw", "e", "ne", "sw", "ne", "sw", "ne", "ne", "e", "nw", "ne", "w", "e", "ne", "w", "w", "ne", "sw", "sw", "ne", "se"],
    ["sw", "w", "e", "se", "ne", "se", "w", "e", "nw", "ne", "sw", "nw", "w", "ne", "se", "sw", "w", "ne"],
    ["e", "ne", "se", "nw", "sw", "w", "sw", "ne", "ne", "sw", "se", "nw", "ne", "w", "sw", "se", "e", "nw", "se", "se"],
    ["w", "nw", "ne", "se", "ne", "se", "ne", "nw", "w", "ne", "nw", "se", "w", "e", "se", "w", "se", "se", "se", "w"],
    ["ne", "ne", "w", "sw", "nw", "e", "w", "sw", "ne", "ne", "se", "nw", "ne", "se", "w", "e", "sw"],
    ["e", "ne", "sw", "nw", "sw", "nw", "se", "ne", "nw", "nw", "nw", "w", "se", "e", "sw", "ne", "e", "w", "se", "ne", "se"],
    ["ne", "sw", "nw", "e", "w", "nw", "nw", "se", "e", "nw", "se", "e", "se", "w", "se", "nw", "sw", "e", "e", "w", "e"],
    ["w", "se", "w", "e", "e", "e", "nw", "ne", "se", "nw", "w", "w", "sw", "ne", "w"]
  ]
else:
  data = [
    ["nw", "sw", "sw", "ne", "nw", "sw", "sw", "e", "sw", "se", "sw", "sw", "nw", "sw", "sw", "e", "sw", "sw"],
    ["sw", "se", "sw", "se", "nw", "sw", "ne", "nw", "se", "se", "se", "nw", "se", "se", "e", "se", "se", "nw", "e", "nw"],
    ["se", "sw", "se", "sw", "se", "sw", "sw", "se", "sw", "w", "sw", "ne", "se", "sw", "se", "se"],
    ["nw", "w", "w", "se", "w", "e", "nw", "w", "w", "w", "sw", "w", "w", "e"],
    ["se", "sw", "w", "w", "se", "e", "se", "se", "se", "se", "se", "se", "sw", "se", "sw", "ne", "ne", "e", "se", "w"],
    ["e", "e", "ne", "w", "e", "w", "w", "e", "se", "ne", "ne", "ne", "e", "ne", "ne"],
    ["ne", "ne", "ne", "ne", "nw", "nw", "w", "sw", "se", "e", "nw", "w", "ne", "ne", "e", "nw", "ne", "sw", "nw", "nw"],
    ["sw", "ne", "sw", "w", "sw", "w", "ne", "w", "w", "w", "sw", "w", "sw", "w", "w", "w"],
    ["se", "se", "w", "e", "e", "w", "w", "nw", "w", "nw", "w", "se", "w", "w", "nw", "ne", "ne", "w", "nw", "ne"],
    ["nw", "w", "e", "w", "e", "w", "nw", "nw", "w", "w", "w", "nw", "sw", "nw", "w", "se", "nw", "ne", "w", "w"],
    ["se", "w", "ne", "w", "sw", "sw", "w", "se", "nw", "se", "ne", "nw", "ne", "sw", "sw", "se", "sw", "e", "e", "nw"],
    ["nw", "w", "nw", "ne", "nw", "nw", "w", "nw", "se", "w", "nw", "se", "e", "w", "se", "nw", "se", "se", "nw", "nw", "nw"],
    ["e", "nw", "ne", "nw", "nw", "sw", "nw", "ne", "ne", "se", "nw", "ne", "sw", "ne", "nw", "ne", "nw", "w", "ne", "ne", "se"],
    ["ne", "ne", "ne", "ne", "ne", "sw", "ne", "ne", "e", "nw", "e", "ne", "ne", "ne", "ne", "ne", "ne", "w", "nw", "se"],
    ["nw", "e", "nw", "sw", "se", "nw", "w", "nw", "w", "nw", "w", "nw", "w", "nw", "ne", "w", "w"],
    ["w", "nw", "nw", "nw", "nw", "ne", "ne", "nw", "ne", "se", "nw", "nw", "nw", "ne", "sw", "nw", "ne", "nw", "se", "w", "ne"],
    ["w", "nw", "nw", "nw", "se", "se", "nw", "w", "w", "ne", "ne", "w", "nw", "nw", "nw", "nw", "w"],
    ["w", "ne", "w", "w", "w", "sw", "w", "w", "w", "w", "sw"],
    ["ne", "nw", "ne", "ne", "ne", "w", "ne", "nw", "ne", "se", "ne", "se", "ne", "w", "ne", "ne", "nw"],
    ["e", "e", "se", "e", "se", "e", "e", "se", "nw", "e", "se", "se", "se"],
    ["se", "ne", "se", "ne", "ne", "e", "e", "ne", "e", "w", "w", "sw", "e", "nw", "e", "e", "ne", "e", "ne", "e", "ne", "ne"],
    ["w", "sw", "se", "se", "nw", "se", "e", "e", "e", "se", "se", "se", "se", "se", "sw", "ne", "w", "se", "sw", "nw", "nw", "se"],
    ["sw", "ne", "ne", "w", "w", "ne", "ne", "ne", "ne", "ne", "ne", "ne", "se", "e", "ne", "ne", "ne", "ne", "ne", "e"],
    ["sw", "e", "nw", "w", "w", "w", "e", "w", "w", "e", "sw", "sw", "w", "sw", "sw", "w", "sw", "w", "nw", "w"],
    ["ne", "sw", "ne", "ne", "ne", "nw", "sw", "nw", "nw", "nw", "ne", "ne", "ne", "ne", "e", "w", "nw", "ne", "e", "nw"],
    ["e", "e", "e", "se", "w", "sw", "se", "e", "nw", "e", "e", "w", "nw", "w", "e", "e", "se", "e", "ne"],
    ["sw", "nw", "se", "e", "sw", "ne", "e", "nw", "se", "se", "nw", "se", "e", "sw", "nw"],
    ["e", "nw", "w", "nw", "w", "w", "sw", "nw", "nw", "ne", "ne", "ne", "ne", "nw", "ne", "nw", "ne", "se", "se", "se", "nw"],
    ["sw", "w", "w", "w", "w", "w", "ne", "w", "ne", "w", "e", "w", "w", "ne", "w", "w", "se", "sw"],
    ["e", "ne", "se", "sw", "w", "ne", "se", "e", "w", "nw", "nw", "e", "sw", "sw", "w", "w", "ne", "nw", "ne", "nw", "ne"],
    ["se", "w", "se", "se", "se", "se", "nw", "ne", "se", "w", "nw", "e", "e", "sw", "sw", "sw", "ne", "se", "sw", "w", "sw"],
    ["nw", "ne", "sw", "nw", "ne", "ne", "nw", "ne", "nw", "e", "ne", "sw", "ne", "se", "nw", "sw", "ne", "w", "nw"],
    ["se", "ne", "ne", "se", "se", "se", "e", "w", "se", "ne", "nw", "sw", "se", "w", "se", "sw", "sw", "se", "ne", "sw"],
    ["nw", "ne", "se", "ne", "e", "ne", "se", "w", "w", "ne", "se", "ne", "ne"],
    ["sw", "w", "nw", "w", "se", "nw", "e", "w", "sw", "ne", "e", "w", "nw", "e", "w", "e", "sw", "e", "w", "ne", "w", "se"],
    ["ne", "ne", "nw", "se", "ne", "sw", "nw", "nw", "nw", "se", "nw", "w", "nw", "ne", "nw", "ne", "ne", "ne", "nw"],
    ["ne", "ne", "ne", "sw", "ne", "ne", "e", "nw", "e", "e", "sw", "e", "ne", "e", "e", "e", "w", "e", "ne", "nw"],
    ["sw", "sw", "sw", "se", "ne", "w", "se", "se", "se", "e", "w", "sw", "ne", "se", "w", "sw", "sw", "se", "se", "sw", "nw"],
    ["e", "sw", "w", "nw", "nw", "w", "sw", "nw", "w", "w", "nw", "nw", "e", "w", "w", "nw"],
    ["sw", "ne", "se", "sw", "e", "nw", "se", "sw", "se", "se", "se", "nw", "ne", "se", "se", "se", "se", "sw", "se", "se"],
    ["ne", "se", "ne", "se", "ne", "w", "ne", "ne", "ne", "nw", "se", "ne", "w", "ne", "w", "se", "nw", "w", "nw", "ne"],
    ["sw", "sw", "se", "sw", "se", "se", "sw", "sw", "nw", "se", "sw", "se", "ne", "sw", "e", "sw", "sw"],
    ["sw", "nw", "nw", "w", "sw", "w", "sw", "sw", "sw", "sw", "w", "sw", "sw", "e", "ne", "se", "sw", "sw", "ne", "w", "ne"],
    ["ne", "ne", "ne", "ne", "ne", "nw", "sw", "ne", "ne", "sw", "se", "nw", "ne", "se", "ne", "ne", "nw", "ne", "ne", "nw", "ne", "e"],
    ["ne", "w", "nw", "ne", "ne", "e", "sw", "ne", "sw", "ne", "nw", "w", "se", "ne", "nw", "ne", "ne", "e", "nw", "ne", "nw"],
    ["sw", "ne", "e", "e", "se", "se", "ne", "se", "se", "w", "se", "se", "e", "e", "se", "w", "se"],
    ["ne", "nw", "nw", "sw", "se", "e", "e", "nw", "se", "sw", "ne", "e", "ne", "w", "w", "e", "ne"],
    ["e", "ne", "ne", "ne", "ne", "ne", "ne", "nw", "ne", "ne", "sw"],
    ["nw", "w", "sw", "w", "w", "se", "ne", "e", "w", "w", "w", "w", "nw", "w", "w", "sw", "ne", "nw", "e", "w", "w"],
    ["se", "w", "se", "ne", "e", "e", "se", "nw", "e", "se", "se", "se", "se", "w", "ne", "sw", "se", "e", "e", "w"],
    ["sw", "nw", "nw", "e", "ne", "sw", "ne", "ne", "se", "sw", "nw", "ne", "ne", "ne", "ne", "ne", "ne", "nw", "ne", "se"],
    ["nw", "se", "nw", "ne", "se", "sw", "w", "e", "w", "nw", "e", "sw", "ne", "e", "w", "nw", "nw", "nw", "e", "nw"],
    ["w", "se", "nw", "w", "nw", "w", "nw", "e", "nw", "w", "w", "nw", "e", "sw", "nw"],
    ["sw", "sw", "w", "e", "w", "nw", "ne", "ne", "se", "se", "w", "se", "se", "w", "ne", "e", "se", "w", "ne", "ne"],
    ["ne", "sw", "nw", "w", "se", "sw", "e", "ne", "ne", "nw", "ne", "se", "ne", "e", "ne", "e", "ne", "w", "se", "sw", "w"],
    ["nw", "w", "w", "se", "se", "ne", "se", "se", "se", "se", "se", "nw", "se", "ne", "e", "sw", "nw", "se", "ne", "w", "se"],
    ["w", "nw", "sw", "ne", "sw", "sw", "sw", "sw", "e", "sw", "ne"],
    ["e", "ne", "se", "nw", "e", "ne", "sw", "se", "w", "ne", "e", "ne", "ne", "nw", "sw", "ne", "w", "nw", "nw", "sw"],
    ["e", "ne", "nw", "nw", "sw", "se", "ne", "nw", "nw", "sw", "nw", "w", "nw", "nw", "nw", "nw", "w", "nw", "w", "nw"],
    ["w", "sw", "sw", "sw", "w", "sw", "w", "se", "se", "nw", "nw", "sw", "ne", "w", "se", "w", "sw", "sw", "ne", "se"],
    ["sw", "w", "sw", "ne", "sw", "sw", "sw", "ne", "sw", "sw", "sw", "sw"],
    ["sw", "sw", "se", "sw", "se", "se", "se", "nw", "se", "e", "e", "sw", "se", "se", "sw", "nw", "se", "se", "sw", "ne", "w", "sw"],
    ["nw", "se", "e", "se", "se", "se", "sw", "w", "e", "se", "se", "se", "se", "se", "se", "se", "ne", "se", "se", "nw", "e"],
    ["sw", "nw", "e", "w", "e", "w", "w", "w", "nw", "nw", "w", "nw", "ne", "nw", "w", "w", "nw", "se", "w", "nw"],
    ["sw", "sw", "sw", "sw", "nw", "sw", "se", "nw", "sw", "w", "w", "e", "sw", "w", "sw", "sw"],
    ["sw", "e", "nw", "sw", "ne", "se", "nw", "sw", "e", "sw", "e", "se", "sw", "w", "ne", "w", "sw", "e", "nw", "sw", "sw", "nw"],
    ["e", "ne", "w", "sw", "nw", "w", "w", "w", "sw", "sw", "ne", "e", "w", "ne", "e", "w", "sw"],
    ["nw", "se", "w", "ne", "nw", "nw", "w", "nw", "nw", "nw", "e", "nw", "nw", "nw", "nw", "nw", "sw", "se", "se", "nw", "nw"],
    ["w", "ne", "e", "se", "se", "sw", "se", "se", "e", "se", "nw", "e", "e", "se", "e", "nw", "se", "ne", "se", "w", "w", "ne"],
    ["se", "ne", "nw", "nw", "ne", "nw", "nw", "nw", "ne", "w", "nw", "nw", "nw", "nw", "e", "nw", "nw", "sw", "ne", "sw"],
    ["se", "se", "se", "se", "e", "se", "se", "se", "ne", "se", "e", "w", "se"],
    ["ne", "ne", "e", "e", "ne", "e", "w", "w", "e", "e", "ne", "e", "ne", "e", "se", "sw"],
    ["sw", "sw", "nw", "se", "sw", "sw", "w", "ne", "se", "sw", "sw", "sw", "sw", "nw", "ne", "sw", "se", "sw", "w", "sw", "e"],
    ["w", "se", "ne", "nw", "w", "w", "se", "se", "e", "se", "sw", "se", "w", "ne", "ne", "ne", "ne", "se", "sw", "se"],
    ["se", "e", "se", "e", "ne", "e", "e", "sw", "sw", "se", "se", "e", "nw", "ne", "e", "w", "ne", "e", "se", "e", "se"],
    ["e", "e", "se", "e", "e", "e", "sw", "se", "nw", "e", "w", "e", "e", "nw", "ne", "e", "e", "w", "se", "e", "ne"],
    ["w", "ne", "ne", "w", "ne", "ne", "ne", "ne", "se", "se", "ne", "w", "nw", "nw", "ne", "ne", "ne", "nw", "se", "nw", "ne"],
    ["ne", "ne", "ne", "e", "sw", "sw", "ne", "ne", "ne", "ne", "nw", "e", "nw", "ne", "nw", "ne", "ne", "ne", "sw", "ne"],
    ["nw", "nw", "nw", "nw", "sw", "w", "w", "nw", "nw", "w", "ne", "e", "nw", "w", "w", "sw", "nw", "nw", "se", "nw"],
    ["e", "ne", "w", "e", "ne", "e", "ne", "ne", "e", "ne", "sw", "e", "ne", "ne", "ne", "e", "sw", "e", "sw", "nw", "w"],
    ["ne", "se", "se", "se", "se", "sw", "se", "se", "se", "nw", "se", "se", "sw", "se", "se", "se", "se", "sw", "ne", "w"],
    ["se", "se", "se", "sw", "sw", "se", "se", "sw", "se", "w", "ne"],
    ["sw", "nw", "ne", "w", "sw", "e", "sw", "sw", "w", "e", "sw", "sw", "sw", "sw", "w", "sw", "sw", "se", "se", "nw", "sw", "sw"],
    ["ne", "e", "w", "nw", "sw", "nw", "sw", "sw", "e", "w", "sw", "ne", "nw", "se", "sw", "nw", "sw", "sw", "sw", "se", "sw"],
    ["e", "se", "w", "ne", "w", "w", "w", "w", "w", "sw", "w", "w", "w", "w", "nw", "se", "e", "w", "w", "w", "ne"],
    ["sw", "sw", "sw", "nw", "sw", "e", "sw", "e", "sw", "sw", "sw", "e", "sw", "sw", "sw", "sw", "se", "w", "sw", "nw", "sw"],
    ["sw", "ne", "sw", "sw", "w", "nw", "sw", "sw", "sw", "w", "sw", "ne", "sw", "sw", "e", "e", "w", "sw", "sw", "sw"],
    ["sw", "w", "w", "e", "se", "se", "w", "w", "sw", "se", "ne", "se", "ne", "se", "se", "se", "e", "sw", "se", "se", "sw"],
    ["nw", "sw", "nw", "nw", "nw", "e", "sw", "w", "nw", "nw", "e", "nw", "nw", "nw", "nw", "e"],
    ["nw", "w", "w", "ne", "nw", "se", "se", "sw", "ne", "w", "se", "ne", "se", "se", "w", "ne", "sw", "sw", "w", "w", "e"],
    ["nw", "ne", "ne", "ne", "nw", "se", "nw", "w", "ne", "nw", "ne", "w", "se", "ne", "e", "w", "se"],
    ["w", "w", "nw", "sw", "ne", "w", "w", "w", "w", "nw"],
    ["sw", "ne", "ne", "sw", "ne", "se", "ne", "ne", "ne", "w", "ne", "se", "nw", "e", "w", "ne", "w", "ne", "ne", "ne"],
    ["ne", "nw", "ne", "e", "ne", "ne", "e", "se", "nw", "ne", "se", "ne", "w", "sw"],
    ["ne", "se", "se", "e", "e", "w", "sw", "w", "e", "e", "se", "se", "se"],
    ["se", "e", "nw", "se", "se", "se", "nw", "se", "e", "se", "se", "se", "se", "e", "se", "se", "se"],
    ["w", "w", "w", "w", "w", "sw", "ne", "w", "sw", "sw", "w", "w", "w", "nw", "sw", "ne", "w", "e", "sw"],
    ["sw", "sw", "w", "sw", "sw", "se", "sw", "se", "nw", "w", "w", "se", "ne", "e", "ne", "sw", "se", "sw", "nw", "ne", "e", "se"],
    ["ne", "se", "nw", "e", "se", "sw", "e", "se", "w", "se", "nw", "w", "se", "se", "se", "se", "se", "se", "e"],
    ["ne", "sw", "se", "sw", "se", "nw", "sw", "e", "se", "ne", "sw", "sw", "sw", "se", "sw", "sw", "sw", "sw", "sw", "w", "w", "nw"],
    ["se", "se", "se", "w", "sw", "se", "ne", "sw", "nw", "sw", "sw", "sw", "sw", "nw", "se", "se", "nw", "sw", "e", "se", "sw"],
    ["nw", "w", "sw", "e", "se", "ne", "w", "nw", "sw", "sw", "nw", "sw", "w", "nw", "e", "ne", "nw", "ne"],
    ["e", "e", "e", "e", "ne", "e", "w", "e", "e", "e", "ne", "ne", "se", "e", "e", "e", "nw"],
    ["se", "se", "ne", "se", "sw", "w", "se", "w", "nw", "ne", "se", "e", "e", "se", "ne", "se", "sw", "se", "ne", "sw"],
    ["nw", "nw", "ne", "e", "nw", "w", "ne", "w", "e", "w", "e", "nw", "w", "nw", "ne", "nw", "se", "se", "ne", "ne", "nw"],
    ["ne", "ne", "ne", "ne", "sw", "ne", "ne", "nw", "ne", "ne", "ne", "e", "ne", "ne", "sw", "ne", "sw", "sw", "ne", "ne"],
    ["w", "sw", "se", "e", "w", "ne", "ne", "se", "e", "ne", "w", "se", "se", "w", "w", "w", "sw", "nw", "nw", "nw", "nw", "nw"],
    ["nw", "nw", "nw", "nw", "nw", "ne", "nw", "nw", "sw", "nw", "ne", "ne", "nw", "se", "nw", "e"],
    ["sw", "nw", "nw", "e", "sw", "nw", "se", "e", "e", "e", "e", "nw", "se", "se", "w", "sw", "w", "ne", "ne", "sw"],
    ["e", "w", "sw", "se", "sw", "nw", "w", "nw", "w", "nw", "nw", "sw", "e", "w", "e", "e", "e", "nw", "ne", "nw"],
    ["w", "ne", "w", "w", "nw", "ne", "sw", "se", "nw", "se", "w", "w", "e", "ne", "w", "nw", "nw", "w", "w", "w", "w"],
    ["nw", "ne", "ne", "ne", "ne", "w", "nw", "se", "nw", "ne", "nw", "nw", "ne", "se", "w", "ne", "nw", "nw", "nw", "nw", "se"],
    ["sw", "se", "ne", "w", "ne", "sw", "ne", "ne", "ne", "e", "nw", "nw"],
    ["sw", "e", "se", "sw", "ne", "e", "e", "ne", "e", "se", "nw", "nw", "ne", "ne", "e", "nw", "ne", "se", "nw", "w"],
    ["se", "sw", "sw", "ne", "sw", "sw", "se", "sw", "w", "se", "sw", "ne", "nw", "se", "se", "ne", "sw", "sw", "sw", "sw", "se"],
    ["ne", "nw", "se", "ne", "nw", "ne", "ne", "e", "w", "ne", "ne", "ne", "ne", "ne", "ne", "sw", "sw", "e", "ne"],
    ["w", "se", "w", "w", "w", "w", "w", "ne", "w", "w", "w", "w", "w", "w", "w", "nw"],
    ["sw", "sw", "se", "se", "e", "sw", "sw", "sw", "w", "sw", "se", "se", "se", "se", "w", "ne", "ne", "se", "sw", "nw"],
    ["ne", "nw", "e", "sw", "nw", "ne", "ne", "nw", "nw", "ne", "nw", "ne", "w", "se", "w", "w", "ne", "ne", "nw", "e"],
    ["ne", "e", "e", "w", "ne", "nw", "nw", "nw", "nw", "nw", "se", "nw", "nw", "nw", "sw", "w", "nw", "nw", "nw", "nw"],
    ["sw", "se", "nw", "sw", "sw", "ne", "se", "sw", "e", "ne", "w", "e", "w", "se", "nw", "w", "ne", "se", "w", "se", "nw", "ne"],
    ["w", "sw", "w", "sw", "w", "w", "e", "e", "sw", "sw", "w", "sw", "sw", "nw", "nw", "nw", "e", "ne"],
    ["nw", "ne", "ne", "ne", "ne", "se", "sw", "ne", "nw", "ne", "sw", "e", "sw", "ne", "ne", "nw", "ne", "ne", "se", "ne"],
    ["w", "se", "se", "sw", "sw", "se", "w", "se", "ne", "e", "sw", "ne", "e", "w", "sw", "se", "se", "sw", "se", "ne"],
    ["sw", "se", "nw", "e", "e", "ne", "sw", "sw", "se", "se", "se", "ne"],
    ["w", "e", "sw", "sw", "se", "ne", "w", "nw", "w", "e", "w", "w", "sw", "sw", "e", "nw", "se", "w", "nw", "ne", "sw"],
    ["ne", "sw", "ne", "w", "se", "nw", "e", "w", "ne", "se", "nw", "sw", "e", "se", "e", "se", "e", "ne"],
    ["se", "sw", "sw", "se", "se", "sw", "w", "ne", "sw", "se", "e", "nw", "e", "sw", "sw", "sw", "sw", "sw", "nw", "nw"],
    ["e", "se", "sw", "sw", "sw", "e", "e", "sw", "se", "sw", "sw", "se", "nw", "sw", "sw", "sw", "sw", "se", "w", "se", "nw"],
    ["e", "ne", "w", "nw", "sw", "se", "sw", "e", "ne", "sw", "se", "sw", "se", "e", "nw", "se", "w", "nw", "se", "e"],
    ["ne", "se", "ne", "sw", "se", "w", "e", "se", "e", "nw", "e", "e", "w", "e", "e", "sw", "e", "e", "e", "ne", "w"],
    ["w", "nw", "e", "ne", "se", "nw", "sw", "nw", "ne", "w", "se", "nw", "nw", "sw", "nw", "ne", "se", "w", "nw", "w", "e", "se"],
    ["sw", "nw", "sw", "sw", "se", "e", "se", "se", "e", "ne", "sw", "sw", "sw", "sw", "sw", "sw", "sw", "sw", "sw", "w"],
    ["w", "se", "se", "w", "w", "ne", "se", "sw", "sw", "sw", "se", "sw", "nw", "sw", "se", "e", "sw", "ne", "sw", "e", "w", "sw"],
    ["nw", "ne", "ne", "nw", "nw", "e", "nw", "sw", "nw", "ne", "ne", "w", "nw", "nw", "sw", "nw", "se", "se", "nw", "nw", "w"],
    ["e", "sw", "se", "se", "sw", "se", "w", "se", "se", "sw", "se", "se", "se", "se", "ne", "se"],
    ["nw", "sw", "sw", "se", "e", "sw", "sw", "se", "sw", "sw", "se", "nw", "e", "se", "e", "w", "nw", "se", "se", "se"],
    ["se", "se", "e", "e", "e", "e", "ne", "w", "sw", "nw", "w", "nw", "sw", "se", "nw", "ne", "nw", "nw", "nw", "w", "se", "sw"],
    ["ne", "e", "w", "e", "e", "w", "ne", "nw", "ne", "e", "nw", "nw", "se", "nw", "se", "nw", "se", "se", "se", "ne"],
    ["ne", "nw", "se", "e", "se", "e", "nw", "e", "nw", "se", "e", "sw", "sw", "nw", "e", "e", "e", "ne", "e", "sw", "se"],
    ["sw", "sw", "se", "sw", "sw", "sw", "sw", "sw", "e", "nw", "w", "w", "sw", "nw", "sw", "ne", "sw", "sw", "e", "sw", "w"],
    ["sw", "sw", "ne", "sw", "nw", "sw", "sw", "sw", "sw", "sw", "se", "e", "w", "sw", "e", "w", "sw", "w", "ne", "ne"],
    ["nw", "ne", "e", "ne", "e", "nw", "ne", "w", "sw", "ne", "nw", "ne", "nw", "sw", "ne", "nw", "nw", "nw", "e", "nw", "ne"],
    ["ne", "ne", "ne", "ne", "nw", "ne", "ne", "sw", "e", "ne", "se", "ne", "ne", "ne", "sw", "nw", "ne", "ne", "ne", "nw"],
    ["e", "w", "se", "e", "sw", "e", "e", "nw", "e", "ne", "se", "e", "nw", "e", "sw", "e", "e", "w", "w", "e", "w"],
    ["e", "se", "se", "e", "se", "se", "se", "e", "w", "e", "e", "se", "w", "se", "e", "se", "se", "ne"],
    ["w", "ne", "e", "ne", "ne", "e", "nw", "w", "e", "sw", "e", "nw", "w", "se", "ne", "e", "e", "ne", "se", "se", "se"],
    ["nw", "nw", "ne", "ne", "se", "ne", "ne", "nw", "w", "nw", "w", "nw", "se", "nw", "nw", "nw", "ne", "ne", "nw", "se"],
    ["se", "ne", "w", "nw", "se", "e", "se", "nw", "w", "se", "se", "sw", "e", "se", "w", "e", "se", "se", "ne", "ne", "sw"],
    ["se", "ne", "e", "e", "w", "nw", "w", "w", "se", "w", "ne", "nw", "e", "w", "nw", "sw", "sw", "se"],
    ["ne", "sw", "w", "e", "w", "w", "w", "w", "w", "w", "w", "sw", "sw", "e", "e", "w", "w", "w", "w", "w"],
    ["w", "w", "sw", "e", "sw", "w", "sw", "e", "w", "w", "se", "ne", "w", "w", "sw", "w", "sw", "sw", "sw", "nw"],
    ["nw", "nw", "nw", "nw", "ne", "ne", "sw", "nw", "se", "nw", "e", "nw", "nw", "nw", "ne", "e", "ne", "w", "nw", "nw"],
    ["se", "nw", "w", "nw", "ne", "ne", "e", "sw", "ne", "ne", "e", "e", "w", "e", "e", "e", "ne", "ne", "ne", "sw"],
    ["nw", "e", "ne", "sw", "ne", "ne", "sw", "ne", "e", "nw", "ne", "w", "nw", "nw", "nw", "nw", "ne", "ne", "nw", "ne", "se", "nw"],
    ["se", "w", "ne", "sw", "nw", "e", "w", "e", "sw", "ne", "se", "w", "nw", "w", "w", "w", "ne", "w", "sw", "sw", "w"],
    ["w", "ne", "sw", "sw", "sw", "w", "sw", "se", "w", "sw", "w", "sw", "sw", "sw", "e", "w", "sw", "sw"],
    ["se", "nw", "ne", "se", "sw", "se", "e", "se", "sw", "ne", "se", "sw", "ne", "sw", "sw", "sw", "sw", "sw", "se", "nw"],
    ["e", "w", "w", "sw", "e", "ne", "e", "nw", "se", "ne"],
    ["se", "e", "ne", "e", "se", "e", "e", "ne", "w", "nw", "e", "w", "sw", "nw", "sw", "sw", "se", "se", "nw", "w"],
    ["w", "se", "se", "w", "w", "se", "w", "w", "sw", "w", "ne", "w", "sw", "w", "ne", "w", "w", "w", "w", "w", "ne", "w"],
    ["w", "nw", "se", "w", "w", "w", "nw", "w", "ne", "w", "se", "nw", "nw", "ne", "w", "nw", "ne", "se", "nw", "nw"],
    ["sw", "sw", "se", "se", "sw", "se", "ne", "w", "se", "se", "se", "se", "se", "se", "se", "se", "nw", "se", "nw", "se"],
    ["nw", "w", "w", "w", "ne", "sw", "w", "w", "w", "w", "se", "sw", "e", "w", "w", "w", "w", "ne", "ne", "w"],
    ["se", "e", "w", "ne", "e", "e", "e", "se", "e", "nw", "se", "w", "e", "nw", "se", "sw"],
    ["nw", "ne", "nw", "w", "ne", "ne", "se", "sw", "nw", "e", "w"],
    ["ne", "e", "e", "nw", "e", "nw", "e", "sw", "e", "e", "e", "e", "e", "e", "e", "se", "e", "sw"],
    ["nw", "nw", "w", "sw", "e", "w", "sw", "nw", "ne", "nw", "nw", "nw", "nw", "se", "ne", "ne"],
    ["e", "w", "nw", "se", "se", "se", "se", "nw", "sw", "e", "se", "se", "se", "w", "sw", "se", "e", "se", "se", "se"],
    ["ne", "e", "nw", "w", "se", "w", "se", "nw", "se", "e", "e", "e", "e", "w", "w", "sw", "ne", "e", "ne", "sw", "ne"],
    ["sw", "se", "nw", "se", "e", "sw", "se", "w", "nw", "w", "e", "ne", "se", "ne", "se", "e", "sw", "se", "se", "se", "e"],
    ["sw", "se", "nw", "nw", "e", "se", "sw", "se", "e", "nw", "se", "sw", "se", "se", "se", "e", "nw", "w", "se", "se", "ne"],
    ["e", "se", "e", "ne", "ne", "nw", "ne", "sw", "nw", "nw", "ne", "e", "e", "e", "ne", "se", "ne", "e", "ne", "w"],
    ["sw", "ne", "ne", "sw", "e", "e", "e", "sw", "ne", "sw", "e", "ne", "nw", "sw", "ne", "e", "e", "e", "se", "sw", "se"],
    ["se", "w", "se", "se", "sw", "e", "e", "e", "e", "w", "e", "e", "ne", "e", "ne", "se", "sw", "e", "se", "e"],
    ["sw", "w", "w", "w", "w", "w", "e", "w", "nw", "nw", "w", "w", "e", "w", "w", "w", "w", "nw"],
    ["se", "sw", "sw", "e", "ne", "nw", "nw", "e", "e", "ne", "ne", "ne", "ne", "sw", "w", "e", "ne", "ne", "ne", "ne", "nw", "ne"],
    ["se", "se", "e", "e", "se", "sw", "w", "ne", "e", "e", "se", "nw", "w"],
    ["nw", "nw", "nw", "sw", "ne", "e", "nw", "ne", "nw", "ne", "ne", "sw", "nw", "sw", "nw", "sw"],
    ["sw", "sw", "sw", "sw", "se", "sw", "ne", "sw", "sw", "sw", "sw", "nw", "se", "sw", "sw", "w"],
    ["w", "nw", "w", "nw", "w", "se", "nw", "nw", "w", "ne", "e", "nw", "nw", "nw", "se", "se", "nw", "nw", "e", "nw", "w"],
    ["e", "se", "e", "se", "e", "e", "se", "w", "se", "se", "sw", "e", "se", "se", "nw", "ne", "nw", "e", "se", "se"],
    ["sw", "sw", "ne", "nw", "ne", "ne", "nw", "ne", "nw", "e", "ne", "ne", "nw", "e", "ne", "nw", "nw", "sw", "nw", "nw", "sw", "ne"],
    ["ne", "w", "w", "se", "w", "w", "w", "nw", "w", "ne", "w", "se", "w"],
    ["sw", "sw", "sw", "se", "se", "sw", "w", "se", "sw", "sw", "ne", "sw", "ne", "ne", "sw", "nw", "nw", "sw", "se", "sw"],
    ["e", "e", "e", "e", "se", "nw", "sw", "se", "e", "e", "e", "e", "w", "w", "se", "e", "ne", "e", "e", "e", "e"],
    ["ne", "sw", "sw", "se", "sw", "ne", "e", "sw", "sw", "ne", "sw", "sw", "se", "sw", "sw", "w", "w"],
    ["ne", "se", "e", "e", "se", "se", "se", "w", "nw", "se", "sw", "se", "se", "se", "w", "se", "se", "sw", "w", "nw", "se", "e"],
    ["nw", "nw", "ne", "se", "ne", "nw", "nw", "se", "sw", "e", "sw", "sw", "e", "nw", "nw", "nw", "e", "w", "nw", "w", "se"],
    ["e", "sw", "sw", "sw", "sw", "sw", "se", "e", "e", "sw", "w", "se", "e", "w", "se", "ne", "nw", "w", "se", "sw", "w"],
    ["ne", "w", "w", "ne", "se", "se", "sw", "e", "e", "ne", "e", "w", "w", "e", "ne", "e"],
    ["sw", "nw", "sw", "w", "nw", "sw", "se", "e", "ne", "e", "se", "e", "ne", "sw", "sw", "e", "nw", "sw", "w", "ne", "sw"],
    ["se", "se", "sw", "e", "e", "se", "sw", "se", "e", "se", "se", "e", "nw", "e", "se", "e", "sw", "ne", "se", "ne", "nw"],
    ["w", "w", "w", "w", "w", "w", "se", "e", "w", "w", "w", "w", "w", "w", "w", "w", "sw", "w", "ne", "se", "ne"],
    ["sw", "nw", "nw", "ne", "nw", "e", "sw", "e", "sw", "sw", "se", "nw", "w", "ne", "ne", "e", "nw", "nw", "nw", "w"],
    ["sw", "nw", "nw", "e", "w", "e", "nw", "e", "nw", "e", "e", "nw", "nw", "sw", "w", "w", "nw", "nw", "nw", "w", "w"],
    ["w", "sw", "e", "sw", "sw", "sw", "sw", "nw", "sw", "sw", "sw", "e", "sw", "sw", "sw", "sw", "sw", "sw", "sw", "ne"],
    ["ne", "ne", "ne", "sw", "w", "nw", "ne", "nw", "nw", "ne", "sw", "ne", "e", "nw", "se", "se", "ne", "ne"],
    ["sw", "e", "w", "sw", "se", "ne", "sw", "nw", "sw", "se", "sw", "sw", "se", "se", "e", "nw", "sw", "sw", "se", "e"],
    ["e", "nw", "e", "e", "e", "sw", "e", "se", "se", "w", "e", "e", "e", "e", "e", "e", "nw", "sw", "e", "e"],
    ["se", "w", "se", "se", "sw", "ne", "ne", "se", "w", "e", "nw", "ne", "e", "ne", "ne", "ne", "e", "w", "ne", "w", "ne", "w"],
    ["e", "se", "nw", "sw", "e", "w", "ne", "sw", "ne", "sw", "nw", "ne", "nw", "nw", "nw", "e", "nw", "e", "nw", "nw"],
    ["sw", "ne", "sw", "w", "sw", "w", "sw", "sw", "sw", "w", "w", "w", "e", "nw", "sw", "sw", "sw", "e", "sw", "sw"],
    ["ne", "w", "se", "sw", "se", "sw", "nw", "se", "se", "ne", "e", "sw", "se", "nw", "w", "sw", "nw"],
    ["w", "w", "e", "sw", "e", "e", "w", "sw", "sw", "nw", "w", "e", "w", "e", "w", "w", "w", "e", "nw", "ne", "se", "nw"],
    ["se", "sw", "e", "nw", "se", "sw", "e", "nw", "w", "se", "e", "w", "ne", "ne", "nw", "ne", "se", "nw", "se", "se"],
    ["w", "w", "w", "w", "ne", "w", "w", "w", "sw", "sw", "w", "w"],
    ["nw", "w", "nw", "nw", "sw", "ne", "se", "ne", "ne", "nw", "w", "e", "nw", "e", "nw", "w", "nw", "nw", "se", "nw", "w", "nw"],
    ["nw", "se", "w", "e", "se", "se", "w", "sw", "se", "sw", "e", "se", "se", "ne", "se", "ne", "se", "sw", "ne", "se"],
    ["e", "se", "e", "e", "e", "e", "nw", "se", "e", "se", "sw", "e"],
    ["sw", "se", "e", "nw", "se", "sw", "w", "ne", "ne", "sw", "sw", "e", "se", "sw", "se", "sw", "nw", "w", "ne", "ne"],
    ["e", "e", "nw", "e", "w", "e", "sw", "e", "se", "ne", "w", "e", "sw", "ne", "nw", "sw", "se", "w", "e", "ne", "e"],
    ["w", "e", "w", "w", "w", "w", "w", "w", "w", "w", "w", "ne", "w", "se", "w", "w", "w", "w", "se", "nw"],
    ["w", "w", "w", "se", "w", "w", "w", "w", "ne", "w", "w"],
    ["se", "nw", "ne", "ne", "e", "ne", "nw", "se", "nw", "ne", "se", "ne", "ne", "ne", "ne", "w", "ne", "w", "se", "sw"],
    ["e", "w", "e", "e", "e", "e", "e", "e", "e", "e"],
    ["nw", "ne", "w", "ne", "ne", "ne", "se", "ne", "ne", "e", "ne", "w", "se", "ne", "ne", "sw", "se", "ne", "nw", "ne", "nw"],
    ["sw", "se", "w", "sw", "nw", "ne", "e", "e", "nw", "se", "w", "e", "se", "e", "nw", "w", "w", "e", "ne", "sw", "w"],
    ["sw", "sw", "nw", "sw", "ne", "ne", "sw", "se", "se", "w", "sw", "se", "sw", "se", "w", "sw", "ne", "se", "se"],
    ["ne", "w", "w", "nw", "nw", "w", "w", "w", "nw", "sw", "sw", "ne", "nw", "nw", "ne", "e", "nw", "nw", "sw", "nw"],
    ["e", "e", "nw", "se", "nw", "ne", "w", "w", "ne", "ne", "e", "ne", "nw", "ne", "nw", "se", "w", "w", "w", "se", "e"],
    ["e", "se", "e", "se", "nw", "e", "e", "se", "se", "sw", "se", "e", "ne", "se", "nw", "e", "e", "e", "w", "sw", "nw", "e"],
    ["nw", "e", "nw", "e", "ne", "w", "nw", "w", "w", "nw", "sw", "w", "sw", "e", "sw", "se", "sw", "nw", "w", "e"],
    ["nw", "se", "ne", "e", "sw", "sw", "se", "se", "se", "sw", "sw", "sw", "se", "sw", "se", "e", "e", "w", "sw", "nw"],
    ["se", "e", "e", "e", "nw", "e", "e", "w", "e", "e", "e", "e", "e", "sw", "e", "e", "e", "ne", "e"],
    ["e", "ne", "w", "e", "sw", "ne", "se", "ne", "ne", "w", "ne", "ne", "w", "ne", "sw", "ne", "ne", "se", "sw", "w"],
    ["nw", "w", "ne", "w", "sw", "nw", "w", "w", "nw", "e"],
    ["sw", "sw", "sw", "sw", "sw", "se", "sw", "sw", "sw", "sw", "w", "sw", "sw", "ne", "sw"],
    ["w", "w", "w", "se", "w", "ne", "nw", "w", "w", "w", "nw", "se", "w", "nw"],
    ["ne", "e", "e", "se", "se", "e", "se", "w", "se", "se", "e", "se", "se", "w", "se", "se", "se", "ne"],
    ["nw", "nw", "sw", "sw", "ne", "sw", "w", "sw", "se", "sw", "sw", "sw", "sw", "e", "sw", "sw", "se", "ne", "sw", "sw", "sw"],
    ["se", "se", "se", "ne", "w", "se", "w", "se", "se", "sw", "se", "se", "se", "se", "sw", "ne", "se", "se", "se"],
    ["se", "ne", "se", "sw", "sw", "se", "sw", "se", "e", "e", "se", "e", "nw", "nw", "se", "e", "ne", "se", "w", "nw", "se"],
    ["nw", "w", "nw", "w", "w", "w", "w", "nw", "w", "e", "w", "e"],
    ["sw", "se", "sw", "w", "sw", "e", "sw", "sw", "sw", "nw", "sw", "sw", "e", "sw", "sw", "sw", "sw", "ne", "sw", "se"],
    ["sw", "se", "e", "sw", "sw", "sw", "sw", "sw", "sw", "sw", "w", "nw", "nw", "sw", "w", "ne", "se", "se", "nw", "sw", "sw"],
    ["se", "nw", "se", "se", "sw", "se", "se", "ne", "se", "ne", "nw", "se", "se", "se", "w", "se", "se", "se", "se", "se"],
    ["e", "w", "sw", "w", "sw", "nw", "se", "ne", "sw", "se", "sw", "ne", "nw", "sw", "se", "nw", "se", "se", "sw", "sw", "ne"],
    ["sw", "e", "sw", "se", "sw", "se", "sw", "w", "w", "se", "ne", "ne", "e", "ne", "se", "nw", "se", "sw", "nw", "se", "nw"],
    ["nw", "w", "w", "e", "sw", "nw", "sw", "nw", "sw", "sw", "se", "e", "se", "sw", "se", "ne", "nw", "se", "sw", "w"],
    ["se", "se", "w", "se", "e", "se", "nw", "e", "sw", "e", "se", "e", "ne", "se", "e", "ne", "se", "sw", "ne", "w", "e", "se"],
    ["e", "se", "w", "se", "e", "e", "e", "se", "w", "e", "nw", "se", "e", "w", "e", "e", "ne", "se", "w", "e", "w"],
    ["e", "ne", "se", "ne", "sw", "ne", "se", "w", "w", "ne", "e", "nw", "ne", "ne", "sw", "e", "w", "se", "w", "ne", "sw"],
    ["ne", "w", "ne", "w", "e", "e", "se", "e", "ne", "sw", "e", "ne", "e", "e", "se", "e", "nw", "ne", "e", "sw", "e"],
    ["se", "sw", "se", "se", "ne", "sw", "sw", "sw", "sw", "sw", "sw", "sw"],
    ["w", "se", "se", "se", "se", "se", "ne", "se", "se", "nw", "se", "e", "se", "nw", "se", "se", "se", "se", "se", "se"],
    ["ne", "ne", "ne", "ne", "se", "ne", "ne", "w", "ne", "ne", "ne", "ne"],
    ["se", "sw", "w", "nw", "sw", "w", "se", "se", "sw", "e", "sw", "sw", "e", "sw", "e", "ne", "se", "nw", "e", "ne"],
    ["ne", "sw", "e", "se", "ne", "ne", "se", "ne", "nw", "e", "e", "sw", "se", "e", "e", "nw", "ne", "w", "nw", "ne", "ne"],
    ["e", "e", "e", "e", "e", "e", "e", "e", "nw", "e", "e", "ne", "sw", "e", "ne", "nw", "nw", "e", "sw", "sw"],
    ["se", "ne", "e", "ne", "ne", "sw", "e", "ne", "sw", "ne", "e", "w", "nw", "sw", "ne", "ne"],
    ["sw", "sw", "w", "sw", "sw", "sw", "w", "sw", "sw", "nw", "w", "w", "nw", "e", "e", "nw", "w", "se", "sw", "w", "w"],
    ["sw", "sw", "w", "sw", "ne", "sw", "se", "ne", "sw", "sw", "sw", "se", "ne", "sw"],
    ["sw", "w", "sw", "sw", "sw", "sw", "sw", "sw", "e", "sw", "sw", "sw", "sw", "sw"],
    ["se", "ne", "se", "se", "se", "e", "nw", "nw", "sw", "e", "sw", "nw", "se", "se", "sw", "se", "sw", "w", "ne", "sw", "sw", "sw"],
    ["ne", "nw", "nw", "sw", "ne", "nw", "e", "w", "ne", "sw", "nw", "ne", "w", "ne", "ne", "ne", "se", "ne", "ne", "e"],
    ["nw", "se", "se", "e", "se", "nw", "w", "sw", "se", "e", "e", "ne", "se", "se", "se", "se", "nw", "nw", "e", "w"],
    ["sw", "nw", "sw", "se", "e", "ne", "w", "sw", "w", "sw", "sw", "sw", "w", "w", "w", "w", "nw", "sw", "w", "e"],
    ["nw", "ne", "e", "ne", "se", "nw", "ne", "e", "w", "ne", "w", "ne", "se", "e", "ne", "ne", "e", "sw"],
    ["ne", "sw", "nw", "w", "ne", "nw", "e", "sw", "ne", "ne", "ne", "ne", "sw", "ne", "nw", "w", "ne", "e", "nw", "ne", "e", "ne"],
    ["ne", "e", "ne", "ne", "sw", "w", "se", "nw", "nw", "ne", "ne", "ne", "se", "e", "ne", "ne", "ne", "w", "se", "ne"],
    ["sw", "sw", "ne", "w", "se", "se", "se", "sw", "sw", "se", "sw", "ne", "sw", "nw", "se", "e", "se", "sw", "se", "se"],
    ["sw", "nw", "w", "sw", "se", "sw", "w", "nw", "sw", "e", "e", "sw", "w", "nw", "e", "e", "ne", "w", "nw", "sw"],
    ["ne", "nw", "e", "e", "e", "e", "sw", "ne", "w", "e", "se", "sw", "ne", "sw", "ne"],
    ["w", "e", "ne", "e", "nw", "ne", "ne", "ne", "ne", "nw", "ne", "nw", "sw", "ne", "w", "ne", "e", "ne", "ne", "e", "ne", "sw"],
    ["sw", "ne", "nw", "nw", "w", "w", "sw", "w", "w", "ne", "ne", "w", "w", "nw", "se", "w", "ne", "se", "w", "nw"],
    ["ne", "sw", "sw", "w", "sw", "sw", "se", "e", "sw", "e", "ne", "sw", "sw", "se", "w", "sw", "sw", "w", "sw", "se"],
    ["ne", "ne", "ne", "nw", "w", "se", "nw", "nw", "ne", "nw", "nw", "ne", "nw", "se", "ne", "nw", "nw", "nw", "se", "nw"],
    ["nw", "se", "se", "sw", "se", "e", "se", "nw", "se", "sw", "sw", "se", "nw", "e", "se"],
    ["w", "sw", "ne", "sw", "nw", "ne", "ne", "sw", "se", "se", "sw", "w", "nw", "se", "sw", "sw", "ne", "se", "nw", "se", "se", "w"],
    ["w", "e", "e", "e", "e", "w", "sw", "e", "e", "e", "ne", "ne", "ne", "sw", "e", "se", "nw", "sw", "e", "e"],
    ["se", "nw", "nw", "w", "w", "nw", "se", "nw", "nw", "w", "w", "nw", "se", "se", "ne", "se", "se", "ne", "w", "se", "ne"],
    ["w", "w", "w", "e", "se", "w", "w", "se", "nw", "w", "w", "w", "sw", "w", "e", "sw", "w", "sw", "ne", "nw", "w"],
    ["sw", "w", "ne", "ne", "se", "sw", "sw", "w", "sw", "se", "w", "w", "w", "sw"],
    ["e", "ne", "nw", "ne", "ne", "e", "ne", "e", "se", "ne", "sw", "nw", "ne", "e", "ne", "sw", "ne", "se", "ne", "ne"],
    ["e", "se", "e", "se", "ne", "ne", "ne", "w", "w", "ne", "ne", "se", "e", "ne", "ne", "w", "ne", "ne", "ne", "w", "ne", "ne"],
    ["w", "e", "nw", "sw", "e", "w", "nw", "e", "w", "nw", "e", "sw", "se", "e", "e", "ne", "e", "ne", "e", "ne", "sw"],
    ["ne", "ne", "ne", "ne", "sw", "ne", "ne", "w", "se", "nw", "ne", "se", "ne", "e", "ne", "nw", "ne", "sw", "ne", "ne", "w", "ne"],
    ["e", "ne", "sw", "ne", "ne", "e", "se", "e", "sw", "e", "ne", "w", "ne", "e", "e", "e", "e", "e", "nw", "ne", "e"],
    ["e", "sw", "sw", "se", "nw", "ne", "se", "e", "se", "e", "e", "e", "e", "sw", "nw", "e", "e", "e", "e", "w", "ne"],
    ["nw", "e", "w", "w", "w", "w", "e", "nw", "w", "w", "w", "e", "w", "nw", "w", "nw", "w", "e", "w", "sw"],
    ["nw", "w", "w", "w", "nw", "ne", "se", "nw", "w", "se", "e", "nw", "sw", "nw", "e", "w", "nw", "sw", "w", "ne", "w", "nw"],
    ["se", "w", "e", "e", "w", "e", "e", "e", "nw", "se", "e", "e", "e", "e", "nw", "se", "e", "e", "e", "ne"],
    ["w", "sw", "se", "ne", "ne", "w", "w", "w", "w", "w", "w", "w", "sw", "w", "sw", "w", "w", "ne", "se", "w", "w"],
    ["ne", "ne", "ne", "nw", "e", "e", "se", "ne", "ne", "ne", "e", "e", "e", "e", "w", "e", "e", "w", "sw", "se"],
    ["ne", "ne", "ne", "ne", "e", "nw", "e", "se", "e", "ne", "sw", "sw", "ne", "ne", "nw", "e", "e", "ne", "sw", "e", "e"],
    ["se", "sw", "e", "e", "e", "sw", "e", "nw", "ne", "se"],
    ["e", "nw", "e", "se", "ne", "ne", "ne", "ne", "e", "nw", "ne", "e", "nw", "ne", "sw", "ne", "sw", "ne", "sw", "ne", "w"],
    ["se", "ne", "nw", "e", "se", "ne", "ne", "sw", "se", "se", "nw", "se", "sw", "sw", "nw", "w", "sw", "nw", "se", "w", "se"],
    ["nw", "nw", "nw", "e", "nw", "nw", "nw", "nw", "nw", "nw", "nw", "sw", "nw", "nw", "nw", "se", "se", "nw", "nw", "nw"],
    ["w", "w", "w", "nw", "nw", "w", "e", "nw", "nw", "nw", "nw", "se", "nw", "sw", "w", "w"],
    ["nw", "nw", "nw", "e", "sw", "ne", "ne", "nw", "ne", "se", "nw", "w", "sw", "ne", "ne", "ne", "nw", "ne", "se", "nw", "e"],
  ]

cmds = {
  "e": [2, 0],
  "w": [-2, 0],
  "ne": [1, 1],
  "nw": [-1, 1],
  "se": [1, -1],
  "sw": [-1, -1],
  }

blacks = []

for tile in data:
  dest = [0, 0]
  for cmd in tile:
    foo = cmds[cmd]
    dest[0] += foo[0]
    dest[1] += foo[1]

  found = False
  for k, black in enumerate(blacks):
    if dest == black:
      blacks.pop(k)
      found = True
      break
  
  if not found:
    blacks.append(dest)

print(len(blacks))
