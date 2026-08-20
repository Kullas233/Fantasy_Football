import re

INPUT_PATH = 'Fantasy_Football_26/data/rotow/ovr.txt'
OUTPUT_PATH = 'Fantasy_Football_26/data/rotow/data.csv'

# Player rows start with a rank number, e.g. "1\tJahmyr Gibbs\tDET\tRB\t6\t..."
RANK_LINE = re.compile(r'^\d+\t')


def parse_players(lines):
    players = []

    for line in lines:
        line = line.rstrip('\n')
        if not RANK_LINE.match(line):
            continue  # skip the header URL line / any blank lines

        fields = line.split('\t')
        if len(fields) < 5:
            continue  # malformed/incomplete row, skip defensively

        rank, name, team, pos, bye = fields[0:5]

        players.append((rank, name, pos, team, bye))

    return players


with open(INPUT_PATH, 'r') as f:
    lines = f.readlines()

players = parse_players(lines)

out_lines = ["Rank,Name,Pos,Team,Cost,Bye"]
for rank, name, pos, team, bye in players:
    out_lines.append(f"{rank},{name},{pos},{team},-1,{bye}")

with open(OUTPUT_PATH, 'w') as f:
    f.write("\n".join(out_lines) + "\n")

print(f"Parsed {len(players)} players -> {OUTPUT_PATH}")
