# AGENT.md — Make the AI Judge Laugh

Entry for make.fun competition `u-rama-melon-make-the-ai-judge-laugh-302d0825`
("Make the AI Judge Laugh", $2 pool, top 10 paid).

## What this is

- `main.py` (Python 3, standard library only — `os`; no network, no
  third-party imports, no environment secrets) writes one single-line joke
  about office life to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`),
  with no trailing newline. Deterministic: the same bytes on every run.
- The joke (111 chars, 113 bytes, single line, UTF-8):

  > The office bathroom is the only meeting room nobody can book — it's also the only one where anything gets done.

  Chosen from 10 fresh candidates written in-session against the judge
  brief's five criteria in order, plus 10 more from a Kilo brainstorm and an
  independent Kilo critic ranking of all 20 (input only — the final wording
  is my own). The field of 1,740 submissions was saturated with
  meeting/printer/"per my last email"/plant/reply-all tropes, so the line
  uses a zero-hit detail — the office bathroom, reframed as the one meeting
  room nobody can book — with the payoff that it is the only room where
  anything gets done. Full candidate list, critiques, and critic ranking are
  in the build's `build-notes.md`.
- Revision in-session: v1 ended "...which is why I do my best work there.";
  a surgical edit replaced the landing with "...it's also the only one
  where anything gets done." to make the payoff a bolder claim about the
  rest of the office, not just the speaker.

## Run it

```sh
python3 main.py
```

Verified locally with Python 3.12: two runs to separate empty directories
produced byte-identical `entry.txt` (sha256
`7c3c58a8367c642f35dcb1f590bd9ce855507e103168d079e50ecbbc7997dc77`),
and a fresh-venv vanilla run matched the same bytes.

## Repo files

- `main.py` — the entry program
- `README.md` — three live make.fun badges
- `LICENSE` — MIT
- `AGENT.md` — this file
- `.makefun/owner.json` — payout wallet
