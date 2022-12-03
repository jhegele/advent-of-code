const rules = {
  rock: {
    beats: "scissors",
    val: 1,
  },
  paper: {
    beats: "rock",
    val: 2,
  },
  scissors: {
    beats: "paper",
    val: 3,
  },
};

const outcomes = {
  lose: 0,
  draw: 3,
  win: 6,
};

const getRounds = async (pathToInput: string) => {
  const lines = await (await Deno.readTextFile(pathToInput)).split("\n");
  return lines.map((r) => r.split(" "));
};

const p1 = async () => {
  const rounds = await getRounds("input.txt");
  const codes: { [key: string]: "rock" | "paper" | "scissors" } = {
    A: "rock",
    X: "rock",
    B: "paper",
    Y: "paper",
    C: "scissors",
    Z: "scissors",
  };
  const results = rounds.map(([oppCode, meCode]) => {
    const [opp, me] = [codes[oppCode], codes[meCode]];
    const playedScore = rules[me].val;
    if (opp === me) return outcomes["draw"] + playedScore;
    if (rules[me].beats === opp) return outcomes["win"] + playedScore;
    return playedScore;
  });
  return results.reduce((a, b) => a + b, 0);
};

const part1 = await p1();
console.log("Part 1: ", part1);
