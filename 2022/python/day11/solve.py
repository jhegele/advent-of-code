from functools import reduce

class Monkey:
    """Monkey object to keep track of what items a specific monkey has and 
    how that specific monkey processes a single round."""

    # Map math operators parsed from inputs to actual functionality
    operations = {
        '+': lambda old, mod: old + mod,
        '*': lambda old, mod: old * mod,
        # The inputs don't actually use the ^ input but we use it
        # to make parsing old * old easier
        '^': lambda old, _: old * old
    }

    def __init__(self, init):
        """Parse lines from the input into usable properties"""
        lines = init.split('\n')
        self.number = int(lines[0].split()[1][:-1])
        self.items = [int(l) for l in lines[1].split(': ')[1].split(', ')]
        op = lines[2].split('new = ')[1]
        _, s, m = op.split()
        if m == 'old':
            if s == '*':
                self.operation = "^"
            if s == "+":
                self.operation = "*"
            self.operation_modifier = 2
        else:
            self.operation = s
            self.operation_modifier = int(m)
        self.test = int(lines[3].replace('Test: divisible by ', ''))
        self.test_true = int(lines[4].split('to monkey ')[1])
        self.test_false = int(lines[5].split('to monkey ')[1])
        self.items_inspected = 0

    def process_round(self, part = 1, mod = 1):
        """Process a single round for this monkey"""
        if len(self.items) == 0:
            return None
        throws = []
        # iterate through each item, in order
        while len(self.items) > 0:
            # for part 1, we should use a mod of 1 to keep the raw number value
            # but for part 2, where we cannot use the divide by 3 to keep 
            # number values small, we use a "supermod" value which is equivalent
            # to every monkey's test value multiplied together to keep values
            # small enough to actually run the process 10,000 times.
            item = self.operations[self.operation](self.items.pop(0), self.operation_modifier) % mod
            if part == 1:
                item = item // 3
            if item % self.test == 0:
                throws.append((self.test_true, item,))
            else:
                throws.append((self.test_false, item,))
            self.items_inspected += 1
        return throws

    def catch(self, item):
        """Allow this monkey to catch an item thrown to it"""
        self.items.append(item)

    def __str__(self) -> str:
        """Convenience function that prints the monkey object in the same format as the puzzle input"""
        return 'Monkey {}:\n\tStarting items: {}\n\tOperation: new = old {} {}\n\tTest: divisible by {}\n\t\tIf true: throw to monkey: {}\n\t\tIf false: throw to monkey: {}'.format(self.number, ', '.join([str(i) for i in self.items]), self.operation, self.operation_modifier, self.test, self.test_true, self.test_false)

def get_monkeys(path):
    with open(path, 'r') as f:
        return f.read().split('\n\n')

def p1():
    monkey_inits = get_monkeys('input.txt')
    monkeys = [Monkey(init) for init in monkey_inits]
    # part 1 does 20 rounds
    for i in range(20):
        for monkey in monkeys:
            throws = monkey.process_round()
            if throws is not None:
                for throw_to, item in throws:
                    monkeys[throw_to].catch(item)
    # get the list of items inspected by each monkey and 
    # multiply the top two monkeys together
    monkeys_items = [m.items_inspected for m in monkeys]
    monkeys_items.sort(reverse=True)
    return monkeys_items[0] * monkeys_items[1]

def p2():
    # biggest difference from part 1 is we have to use
    # the supermod value to prevent values from growing
    # too large and making processing impossible. the
    # supermod is the product of all monkeys' test
    # values and, during each cycle we set the item
    # being tested to item % supermod to reduce its size
    # but allow the tests to still function as expected
    monkey_inits = get_monkeys('input.txt')
    monkeys = [Monkey(init) for init in monkey_inits]
    tests = [m.test for m in monkeys]
    supermod = reduce(lambda a, b: a * b, tests, 1)
    for i in range(10000):
        for monkey in monkeys:
            throws = monkey.process_round(2, supermod)
            if throws is not None:
                for throw_to, item in throws:
                    monkeys[throw_to].catch(item)
    monkeys_items = [m.items_inspected for m in monkeys]
    monkeys_items.sort(reverse=True)
    return monkeys_items[0] * monkeys_items[1]

print('Part 1: ', p1())
print('Part 2: ', p2())