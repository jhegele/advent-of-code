const getInputLines = async (fileName: string) => {
  const file = Bun.file(fileName);
  const fileText = await file.text();
  return fileText.split("\n");
};

const getListsFromLines = (lines: string[]) => {
  const left: number[] = [];
  const right: number[] = [];
  for (const line of lines) {
    const [l, r] = line.split("   ").map(Number);
    left.push(l);
    right.push(r);
  }
  return [left, right];
};

const countOccurrences = (value: number, list: number[]) => {
  return list.filter((v) => v === value).length;
};

const part1 = (lines: string[]) => {
  const [left, right] = getListsFromLines(lines);
  left.sort();
  right.sort();
  const totalDistance = left
    .map((val, idx) => Math.abs(val - right[idx]))
    .reduce((acc, curr) => acc + curr, 0);
  return totalDistance;
};

const part2 = (lines: string[]) => {
  const [left, right] = getListsFromLines(lines);
  const totalSimilarity = left
    .map((val) => val * countOccurrences(val, right))
    .reduce((acc, curr) => acc + curr, 0);
  return totalSimilarity;
};

const lines = await getInputLines("day01/day01.input");

console.log("Part 1: ", part1(lines));
console.log("Part 2: ", part2(lines));
