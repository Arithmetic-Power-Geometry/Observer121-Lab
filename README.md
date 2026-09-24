# Observer121-Lab

**121 system-observer worlds; a reproducible falsification laboratory for testing apparent gains in adaptive observation.**

## Research status

Observer121 deliberately preserves negative results. The project began with 11 diagonal observations and 110 cross-observer intersections, then progressively strengthened its baselines rather than renaming failed mechanisms.

See **SEQUENCE.md** for the v3 → v6 convergence record.

### v3 — ZGTC
Compared random, zigzag-only, disagreement-greedy, rectangle attack, and Zigzag→Gap→Target→Crash. Disagreement-greedy was stronger than ZGTC.

### v4 — Greedy-trap attack
A planted cross-rectangle construction was designed to favor coordinated system-observer reasoning. Greedy disagreement still won.

### v5 — Decision-relative attack
The stopping rule was changed from exact world identification to decision resolution. Ordinary decision-aware tests resolved the construction, eliminating the proposed advantage.

### v6 — Final AESHO compilation attack
A generated balanced intervention beats a restricted primitive equality-test library, but the advantage disappears when the same balanced tests are available in a fixed compiled library.

Run:

```bash
python src/final_aesho_test.py
```

The workflow stores:
- scaling results and summaries,
- selected complete sequential traces,
- compilation audit,
- final report.

**Current conclusion:** the tested branch does not establish a new information-theoretic observation principle. It does expose the distinction between a restricted primitive library, a succinct experiment generator, and an equivalently expressive compiled library. This negative result is retained as part of the scientific record.

## Earlier benchmark

The original exact-certificate benchmark remains available through `src/run_benchmark.py` and `.github/workflows/benchmark.yml`.

## License

Apache License 2.0.

Copyright (C) 2026 Mohammad Amir Khusru Akhtar
