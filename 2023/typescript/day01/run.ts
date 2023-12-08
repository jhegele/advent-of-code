const getLines = async (path: string) => {
  const file = Bun.file(path);
  const contents = await file.text();
  return contents.split("\n");
};

const getDigitsFromLine = (line: string) => {
  const pattern = /\d/g;
  const matches = line.match(pattern);
  if (!matches) throw new Error("No numbers found in a line!");
  return parseInt(matches[0]) * 10 + parseInt(matches[matches.length - 1]);
};

const convertWordsToDigits = (line: string) => {
  return line
    .replaceAll("one", "o1e")
    .replaceAll("two", "t2e")
    .replaceAll("three", "t3e")
    .replaceAll("four", "f4r")
    .replaceAll("five", "f5e")
    .replaceAll("six", "s6x")
    .replaceAll("seven", "s7n")
    .replaceAll("eight", "e8t")
    .replaceAll("nine", "n9e");
};

const part1 = async (path: string) => {
  const lines = await getLines(path);
  return lines.map(getDigitsFromLine).reduce((acc, val) => acc + val, 0);
};

const part2 = async (path: string) => {
  const lines = await getLines(path);
  return lines
    .map(convertWordsToDigits)
    .map(getDigitsFromLine)
    .reduce((acc, val) => acc + val, 0);
};

console.log(`P1: ${await part1("./input.txt")}`);
console.log(`P2: ${await part2("./input.txt")}`);
