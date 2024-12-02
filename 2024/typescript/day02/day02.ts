const getInputLines = async (fileName: string) => {
  const file = Bun.file(fileName);
  const fileText = await file.text();
  return fileText.split("\n");
};

const getReportsFromLines = (lines: string[]) => {
  return lines.map((line) => line.split(" ").map(Number));
};

const pairwiseDiffs = (report: number[]) => {
  const diffs: number[] = [];
  for (let i = 1; i < report.length; i++) {
    diffs.push(report[i] - report[i - 1]);
  }
  return diffs;
};

const isSafe = (reportDiffs: number[]) => {
  const countNegatives = reportDiffs.filter((v) => v < 0).length;
  if (countNegatives > 0 && countNegatives !== reportDiffs.length) return false;
  const countOutOfBounds = reportDiffs.filter(
    (v) => Math.abs(v) < 1 || Math.abs(v) > 3
  ).length;
  if (countOutOfBounds > 0) return false;
  return true;
};

const part1 = (lines: string[]) => {
  const reports = getReportsFromLines(lines);
  const diffs = reports.map(pairwiseDiffs);
  const safe = diffs.filter((d) => isSafe(d));
  return safe.length;
};

const part2 = (lines: string[]) => {
  let countSafe = 0;
  const reports = getReportsFromLines(lines);
  for (const report of reports) {
    const reportDiffs = pairwiseDiffs(report);
    if (isSafe(reportDiffs)) {
      countSafe++;
    } else {
      for (let i = 0; i < report.length; i++) {
        const updatedReport = report.toSpliced(i, 1);
        const updatedDiffs = pairwiseDiffs(updatedReport);
        if (isSafe(updatedDiffs)) {
          countSafe++;
          break;
        }
      }
    }
  }
  return countSafe;
};

const lines = await getInputLines("day02/day02.input");
console.log("Part 1: ", part1(lines));
console.log("Part 2: ", part2(lines));
