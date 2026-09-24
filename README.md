# Observer121-Lab

**121 system-observer worlds; 11 diagonal observations; 110 cross-observer intersections.**

## v3: Zigzag -> Gap -> Target -> Crash (ZGTC)

The v3 benchmark starts with 32 rival hypotheses deliberately identical on all 11 diagonal cells. A solver must identify the hidden true world using off-diagonal intersections.

ZGTC combines four pressures:

1. **Zigzag** - move away from already explored geometry and the diagonal.
2. **Gap** - target cells where surviving hypotheses disagree most strongly.
3. **Target** - prefer one observation that can eliminate many hypotheses at once.
4. **Crash** - reward falsification; cross-swap 2x2 rectangles receive explicit pressure.

Internal baselines:
- random sampling
- zigzag-only
- disagreement-greedy
- rectangle-attack
- ZGTC composite

Run:

```bash
python src/zgtc_benchmark.py
```

Generated artifacts:
- `artifacts/comparison_results.csv`
- `artifacts/comparison_summary.csv`
- `artifacts/comparison_summary.json`
- `artifacts/REPORT.md`

See `COMPARISON.md` for the prior-art-oriented comparison.

The repository is a falsification laboratory. It does not claim that zigzag search, hypothesis disagreement, factorial interactions, active model discrimination, or falsification are individually novel.

## License

Apache License 2.0.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
