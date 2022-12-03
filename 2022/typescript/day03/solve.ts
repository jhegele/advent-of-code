const alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

const getRucksacks = async (pathToFile: string) => {
  const file = await Deno.readTextFile(pathToFile);
  return file.split("\n");
};

const intersection = (set1: Set<string>, set2: Set<string>) => {
  return new Set([...set1].filter((e) => set2.has(e)));
};

const p1 = async () => {
  const rucksacks = await getRucksacks("input.txt");
  const rucksacksWithCompartments = rucksacks.map((r) => {
    const mid = r.length / 2;
    const compartment1 = new Set(r.slice(0, mid));
    const compartment2 = new Set(r.slice(mid, r.length));
    return [compartment1, compartment2];
  });
  const errors = rucksacksWithCompartments.map(([c1, c2]) =>
    Array.from(intersection(c1, c2))
  );
  return errors
    .flat()
    .map((e) => alpha.indexOf(e) + 1)
    .reduce((a, b) => a + b, 0);
};

const p2 = async () => {
  const rucksacks = await getRucksacks("input.txt");
  const groupSize = 3;
  let priority = 0;
  for (let i = 0; i < rucksacks.length; i += groupSize) {
    const group = rucksacks.slice(i, i + groupSize);
    const [elf1, elf2, elf3] = group.map((e) => new Set(e));
    const badge = [...elf1].filter((i) => elf2.has(i) && elf3.has(i));
    priority += badge
      .map((b) => alpha.indexOf(b) + 1)
      .reduce((a, b) => a + b, 0);
  }
  return priority;
};

const part1 = await p1();
const part2 = await p2();
console.log("Part 1: ", part1);
console.log("Part 2: ", part2);
