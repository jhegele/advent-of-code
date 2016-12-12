import re

class Bot(object):
  """Our bot object. This can also be an output bin."""

  def __init__(self, id):
    self.id = id
    self.chips = []
    self.trade = None

  def ready(self):
    """Can't do anything until we have 2 chips"""
    return len(self.chips) == 2

  def low(self):
    """Find the lowest chip, remove it, and return the value"""
    l = min(self.chips)
    self.chips.pop(self.chips.index(l))
    return l

  def high(self):
    """Find the highest chip, remove it, and return the value"""
    h = max(self.chips)
    self.chips.pop(self.chips.index(h))
    return h

def add_bot(bots, id):
  """Add a bot if it doesn't exist"""
  if id not in bots:
    bots[id] = Bot(id)
  return bots

bots = {}
outputs = {}
with open('input.txt', 'r') as input_file:
  # Initialize our bots first
  for instruction in input_file:
    # Add chips during initialization if necessary
    if instruction[:5] == 'value':
      m = re.search(r'value (\d+) goes to bot (\d+)', instruction)
      bot_id, chip_id = int(m.group(2)), int(m.group(1))
      bots = add_bot(bots, bot_id)
      bots[bot_id].chips.append(chip_id)
    # Otherwise, initialize the bot/output if needed and add the relevant trade instructions
    else:
      m = re.search(r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)', instruction)
      bot_id, low_to_type, low_to_id, high_to_type, high_to_id = int(m.group(1)), m.group(2), int(m.group(3)), m.group(4), int(m.group(5))
      bots = add_bot(bots, bot_id)
      bots[bot_id].trade = instruction
      if low_to_type == 'bot':
        bots = add_bot(bots, low_to_id)
      else:
        outputs = add_bot(outputs, low_to_id)
      if high_to_type == 'bot':
        bots = add_bot(bots, high_to_type)
      else:
        outputs = add_bot(outputs, high_to_id)

# Get all the bots that have 2 chips
ready = [b for i, b in bots.items() if b.ready()]
while len(ready) > 0:
  # Execute all the trades for bots with 2 chips
  for bot in ready:
    m = re.search(r'bot (\d+) gives low to (bot|output) (\d+) and high to (bot|output) (\d+)', bot.trade)
    low_to_type, low_to_id, high_to_type, high_to_id = m.group(2), int(m.group(3)), m.group(4), int(m.group(5))
    if low_to_type == 'bot':
      bots[low_to_id].chips.append(bot.low())
    else:
      outputs[low_to_id].chips.append(bot.low())
    if high_to_type == 'bot':
      bots[high_to_id].chips.append(bot.high())
    else:
      outputs[high_to_id].chips.append(bot.high())
  ready = [b for i, b in bots.items() if b.ready()]
  # If one of our bots has the specified chips, we can stop
  matches = [b for i, b in bots.items() if 61 in b.chips and 17 in b.chips]
  if len(matches):
    print('{0}'.format([b.id for b in matches]))
    break
