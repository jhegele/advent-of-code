const getLines = async (path: string) => {
  const contents = await Bun.file(path).text();
  return contents.split("\n");
};

const getRound = (
  line: string
): [number, { r: number; g: number; b: number }[]] => {
  const [gamePart, cubesPart] = line.split(": ");
  const gameId = parseInt(gamePart.replace("Game ", ""));
  const turns: { r: number; g: number; b: number }[] = [];
  for (const turn of cubesPart.trim().split(";")) {
    const res = { r: 0, g: 0, b: 0 };
    for (const cube of turn.split(", ")) {
      const [count, color] = cube.trim().split(" ");
      if (color.trim() === "red") res.r += parseInt(count);
      if (color.trim() === "green") res.g += parseInt(count);
      if (color.trim() === "blue") res.b += parseInt(count);
    }
    turns.push(res);
  }
  return [gameId, turns];
};

const part1 = async (path: string) => {
  const lines = await getLines(path);
  const rounds = lines.map(getRound);
  return rounds
    .map((round) => {
      const [id, results] = round;
      if (Math.max(...results.map((r) => r.r)) > 12) return 0;
      if (Math.max(...results.map((r) => r.g)) > 13) return 0;
      if (Math.max(...results.map((r) => r.b)) > 14) return 0;
      return id;
    })
    .reduce((acc, val) => acc + val, 0);
};

const part2 = async (path: string) => {
  const lines = await getLines(path);
  const rounds = lines.map(getRound);
  return rounds
    .map((round) => {
      const [id, results] = round;
      return (
        Math.max(...results.map((r) => r.r)) *
        Math.max(...results.map((r) => r.g)) *
        Math.max(...results.map((r) => r.b))
      );
    })
    .reduce((acc, val) => acc + val, 0);
};

console.log(`P1: ${await part1("./input.txt")}`);
console.log(`P2: ${await part2("./input.txt")}`);
