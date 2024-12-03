const getMemory = async (filePath: string) => {
  const file = Bun.file(filePath);
  return await file.text();
};

const part2 = (memory: string) => {
  const reValid = /mul\((\d{1,3}),(\d{1,3})\)|don\'t\(\)|do\(\)/g;
  let match: RegExpExecArray | null;
  let enabled = true;
  let total = 0;
  while ((match = reValid.exec(memory))) {
    const val = match[0];
    if (val === "do()") enabled = true;
    else if (val === "don't()") enabled = false;
    else {
      if (enabled) {
        total += Number(match[1]) * Number(match[2]);
      }
    }
  }
  return total;
};

const part1 = (memory: string) => {
  const reValid = /mul\((\d{1,3}),(\d{1,3})\)/g;
  let match: RegExpExecArray | null;
  let total = 0;
  while ((match = reValid.exec(memory))) {
    total += Number(match[1]) * Number(match[2]);
  }
  return total;
};

const mem = await getMemory("day03/day03.input");
console.log("Part 1: ", part1(mem));
console.log("Part 2: ", part2(mem));
