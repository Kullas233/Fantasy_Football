import re

INPUT_PATH = 'Fantasy_Football_26/data/yahoo/ovr.txt'
OUTPUT_PATH = 'Fantasy_Football_26/data/yahoo/data.csv'

# A rank line looks like "157\t" (rank number followed by a tab, nothing else)
RANK_LINE = re.compile(r'^\d+\t?$')

# A pos/team line looks like "RB\tDET"
POS_TEAM_LINE = re.compile(r'^([A-Z]+)\t([A-Z]+)$')


def parse_players(lines):
    players = []
    i, n = 0, len(lines)

    while i < n:
        line = lines[i].rstrip('\n')

        if not RANK_LINE.match(line):
            i += 1
            continue

        rank = line.split('\t')[0]
        i += 1
        if i >= n:
            break

        name = lines[i].rstrip('\n').strip()
        i += 1
        if i >= n:
            break

        pos_team_line = lines[i].rstrip('\n')
        i += 1
        match = POS_TEAM_LINE.match(pos_team_line)
        if not match:
            continue  # malformed row, skip defensively
        pos, team = match.group(1), match.group(2)

        players.append((rank, name, pos, team))

    return players


with open(INPUT_PATH, 'r') as f:
    lines = f.readlines()

players = parse_players(lines)

out_lines = ["Rank,Name,Pos,Team,Cost"]
for rank, name, pos, team in players:
    out_lines.append(f"{rank},{name},{pos},{team},-1")

with open(OUTPUT_PATH, 'w') as f:
    f.write("\n".join(out_lines) + "\n")

print(f"Parsed {len(players)} players -> {OUTPUT_PATH}")
