const getElves = async (path: string) => {
  const f = await Deno.readTextFile(path);
  return f
    .split("\n\n")
    .map((elf) => elf.split("\n").map((cal) => Number(cal)));
};

const p1 = async () => {
  const elves = await getElves("input.txt");
  const totalCals = elves.map((e) => e.reduce((a, b) => a + b, 0));
  return Math.max(...totalCals);
};

const p2 = async () => {
  const elves = await getElves("input.txt");
  const totalCals = elves.map((e) => e.reduce((a, b) => a + b, 0));
  totalCals.sort((a, b) => b - a);
  return totalCals[0] + totalCals[1] + totalCals[2];
};

const part1 = await p1();
const part2 = await p2();
console.log("Part 1: ", part1);
console.log("Part 2: ", part2);
