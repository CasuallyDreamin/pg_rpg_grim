class tile:
   def __init__(self,sprite=None):
      self.sprite = sprite
#gt : Ground tile, at :Air type
gt = tile()
at = tile()
game_map = [
    [at,at,at,at,at,at,at,at,at,at,at,at,at,at,at,at],
    [at,at,at,at,at,at,at,at,at,at,at,at,at,at,at,at],
    [at,at,at,at,at,at,at,at,at,at,at,at,at,at,at,at],
    [at,at,at,at,at,at,at,at,at,at,at,at,at,at,at,at],
    [at,at,at,at,at,at,at,at,at,at,at,at,at,at,at,at],
    [at,at,at,at,at,at,at,at,at,at,at,at,at,at,at,at],
    [gt,gt,gt,gt,gt,gt,gt,gt,gt,gt,gt,gt,gt,gt,gt,gt],
    [gt,gt,gt,gt,gt,gt,gt,gt,gt,gt,gt,gt,gt,gt,gt,gt],
]