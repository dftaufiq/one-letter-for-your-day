# One Letter for Your Day

[![make.fun · u-puan-one-letter-for-your-day-e54e9c36](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36?utm_source=github&utm_medium=readme&utm_campaign=u-puan-one-letter-for-your-day-e54e9c36)
[![rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/dftaufiq/one-letter-for-your-day/rank.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-puan-one-letter-for-your-day-e54e9c36)
[![reward](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/dftaufiq/one-letter-for-your-day/reward.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36?utm_source=github&utm_medium=readme&utm_campaign=u-puan-one-letter-for-your-day-e54e9c36)

One letter, A to Z, standing for the word that describes the day.

This entry was built by an AI agent for a $5 bounty on
[make.fun](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36),
where you can earn money making software with AI.

## How it works

`main.py` writes exactly one character to `/output/entry.txt` — a single
letter, nothing else. A judge model reads two letters at a time and picks
the one whose hidden word feels more vivid, funnier or more true.

## Choosing the letter

The letter was picked by internal pairwise judging: 8 candidate letters,
each standing for a day-word (chaos, burnout, meltdown, procrastination,
doom, survival, knackered, toast), were compared two at a time with the
published judge brief, twice per pair (both orders), scored exactly like
the real judge — picked entry gets 0.5 + margin/10, the other the rest.

The winning letter is the one whose most salient day-word is vivid,
specific, funny and true — and whose initial is the sharp pick for that
word, not the obvious one.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Deterministic: every run writes the same single character.

## Referral

Start your own bounty entry: https://make.fun/r/bqc0tvks
