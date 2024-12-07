const directions = [
  "Up",
  "UpRight",
  "Right",
  "DownRight",
  "Down",
  "DownLeft",
  "Left",
  "UpLeft",
] as const;

type Directions = (typeof directions)[number];

type Surrounding = {
  [key in Directions]: string | null;
};

class WordSearchRow implements Iterable<string> {
  constructor(private row: string) {}

  *[Symbol.iterator](): IterableIterator<string> {
    let counter = 0;
    while (counter < this.row.length) {
      const curr = this.row[counter];
      counter++;
      yield curr;
    }
  }
}

class WordSearch implements Iterable<WordSearchRow> {
  public rows: WordSearchRow[];

  constructor(private wordSearchLines: [string, ...string[]]) {
    this.rows = wordSearchLines.map((l) => new WordSearchRow(l));
  }

  public get maxX() {
    return this.wordSearchLines[0].length - 1;
  }

  public get maxY() {
    return this.wordSearchLines.length - 1;
  }

  public getPos = (x: number, y: number) => {
    if (x < 0 || x > this.maxX) return undefined;
    if (y < 0 || y > this.maxY) return undefined;
    return this.wordSearchLines[y][x];
  };

  public fromPos = (x: number, y: number, offset: number) => {
    // initialize surrounding values to null
    let surrounding: Surrounding = {
      Up: null,
      UpRight: null,
      Right: null,
      DownRight: null,
      Down: null,
      DownLeft: null,
      Left: null,
      UpLeft: null,
    };
    // set x, y steps for each direction we'll move
    const steps: {
      [key in keyof typeof surrounding]: { x: number; y: number };
    } = {
      Up: { x: 0, y: -1 },
      UpRight: { x: 1, y: -1 },
      Right: { x: 1, y: 0 },
      DownRight: { x: 1, y: 1 },
      Down: { x: 0, y: 1 },
      DownLeft: { x: -1, y: 1 },
      Left: { x: -1, y: 0 },
      UpLeft: { x: -1, y: -1 },
    };
    // build an array of step factors based on offset. an offset of 3 would contain factors
    // of: 0, 1, 2, 3, e.g.
    const stepFactors = Array.from(Array(offset + 1).keys());
    // left
    if (x >= offset) {
      const left = stepFactors
        .map<string>((factor) => {
          const useX = factor * steps.Left.x + x;
          return this.getPos(useX, y)!;
        })
        .reduce((acc, curr) => acc + curr, "");
      surrounding.Left = left;
    }
    // right
    if (x <= this.maxX - offset) {
      const right = stepFactors
        .map<string>((factor) => {
          const useX = factor * steps.Right.x + x;
          return this.getPos(useX, y)!;
        })
        .reduce((acc, curr) => acc + curr, "");
      surrounding.Right = right;
    }

    // up
    if (y >= offset) {
      const up = stepFactors
        .map((factor) => {
          const useY = factor * steps.Up.y + y;
          return this.getPos(x, useY)!;
        })
        .reduce((acc, curr) => acc + curr, "");
      surrounding.Up = up;
    }
    // down
    if (y <= this.maxY - offset) {
      const down = stepFactors
        .map((factor) => {
          const useY = factor * steps.Down.y + y;
          return this.getPos(x, useY)!;
        })
        .reduce((acc, curr) => acc + curr, "");
      surrounding.Down = down;
    }
    // up-right
    if (x <= this.maxX - offset && y >= offset) {
      const ur = stepFactors
        .map((factor) => {
          const useY = factor * steps.UpRight.y + y;
          const useX = factor * steps.UpRight.x + x;
          return this.getPos(useX, useY)!;
        })
        .reduce((acc, curr) => acc + curr, "");
      surrounding.UpRight = ur;
    }
    // down-right
    if (x <= this.maxX - offset && y <= this.maxY - offset) {
      const dr = stepFactors
        .map((factor) => {
          const useY = factor * steps.DownRight.y + y;
          const useX = factor * steps.DownRight.x + x;
          return this.getPos(useX, useY)!;
        })
        .reduce((acc, curr) => acc + curr, "");
      surrounding.DownRight = dr;
    }
    // down-left
    if (x >= offset && y <= this.maxY - offset) {
      const dl = stepFactors
        .map((factor) => {
          const useY = factor * steps.DownLeft.y + y;
          const useX = factor * steps.DownLeft.x + x;
          return this.getPos(useX, useY)!;
        })
        .reduce((acc, curr) => acc + curr, "");
      surrounding.DownLeft = dl;
    }
    // up-left
    if (x >= offset && y >= offset) {
      const ul = stepFactors
        .map((factor) => {
          const useY = factor * steps.UpLeft.y + y;
          const useX = factor * steps.UpLeft.x + x;
          return this.getPos(useX, useY)!;
        })
        .reduce((acc, curr) => acc + curr, "");
      surrounding.UpLeft = ul;
    }
    return surrounding;
  };

  *[Symbol.iterator](): IterableIterator<WordSearchRow> {
    let counter = 0;
    while (counter < this.wordSearchLines.length) {
      const curr = this.rows[counter];
      counter++;
      yield curr;
    }
  }
}

const getWordSearch = async (filePath: string) => {
  const file = Bun.file(filePath);
  const text = await file.text();
  const lines = text.split("\n");
  if (lines.length < 1) throw new Error("No lines parsed from input!");
  return new WordSearch(lines as [string, ...string[]]);
};

const part1 = (wordSearch: WordSearch) => {
  let totalXmas = 0;
  let y = 0;
  for (let row of wordSearch) {
    let x = 0;
    for (let val of row) {
      if (val === "X") {
        const surrounding = wordSearch.fromPos(x, y, 3);
        directions.forEach((dir) => {
          if (surrounding[dir] === "XMAS") totalXmas++;
        });
      }
      x++;
    }
    y++;
  }
  return totalXmas;
};

const part2 = (wordSearch: WordSearch) => {
  let totalXmas = 0;
  let y = 0;
  for (let row of wordSearch) {
    let x = 0;
    for (let val of row) {
      if (val === "A") {
        const surrounding = wordSearch.fromPos(x, y, 1);
        let tl_br = false;
        let tr_bl = false;
        if (surrounding.UpLeft === "AM") {
          if (surrounding.DownRight === "AS") tl_br = true;
        }
        if (surrounding.UpLeft === "AS") {
          if (surrounding.DownRight === "AM") tl_br = true;
        }
        if (surrounding.UpRight === "AM") {
          if (surrounding.DownLeft === "AS") tr_bl = true;
        }
        if (surrounding.UpRight === "AS") {
          if (surrounding.DownLeft === "AM") tr_bl = true;
        }
        if (tl_br && tr_bl) totalXmas++;
      }
      x++;
    }
    y++;
  }
  return totalXmas;
};

const wordSearch = await getWordSearch("day04/day04.input");
console.log("Part 1: ", part1(wordSearch));
console.log("Part 1: ", part2(wordSearch));
