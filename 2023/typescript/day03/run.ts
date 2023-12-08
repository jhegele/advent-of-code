type SchematicData = {
  val: string;
  isNumeric: boolean;
  startIndex: number;
};

const getLines = async (path: string) => {
  return (await Bun.file(path).text()).split("\n");
};

const getLineContents = (line: string) => {
  const pattern = /(\d+|[^\.\s])/g;
  let match: RegExpExecArray | null;
  const contents: SchematicData[] = [];
  while ((match = pattern.exec(line.trim())) !== null) {
    const val = match[0];
    const startIndex = match.index;
    const isNumeric = "0123456789".includes(val[0]);
    contents.push({ val, isNumeric, startIndex });
  }
  return contents;
};

const getDataCoordinates = (y: number, data: SchematicData) => {
  const coords: [number, number][] = [];
  for (let x = data.startIndex; x < data.startIndex + data.val.length; x++) {
    coords.push([x, y]);
  }
  return coords;
};

const adjacentContents = (
  y: number,
  data: SchematicData,
  schematic: string[]
) => {
  const dataCoords = getDataCoordinates(y, data);
  console.log(dataCoords);
  const yMin = Math.max(y - 1, 0);
  const yMax = Math.min(y + 1, schematic.length);
  const xMin = Math.max(Math.min(...dataCoords.map((d) => d[0])), 0);
  const xMax = Math.min(
    Math.max(...dataCoords.map((d) => d[0])),
    schematic[0].length
  );
  const adjacentCoords: [number, number][] = [];
  for (let y = yMin; y <= yMax; y++) {
    for (let x = xMin; x <= xMax; x++) {
      if (!dataCoords.includes([x, y])) {
        adjacentCoords.push([x, y]);
      }
    }
  }
  console.log(adjacentCoords);
};

const part1 = async (path: string) => {
  const schematic = await getLines(path);
  const lines = schematic.map(getLineContents);
  adjacentContents(0, lines[0][0], schematic);
};

part1("./sample.txt");
