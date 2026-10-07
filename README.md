# neurocode

Open, on-device tools for paediatric brain tumour imaging, starting with **diffuse midline glioma (DMG/DIPG)**.

> Research software. Outputs are predictions for research use only, not for diagnosis or treatment decisions.

## Status

| Version | What | State |
|---|---|---|
| `v1-meg` (tag) | MEG decoding experiments on BCI Competition IV, dataset 3 | Archived; base for a future EEG/MEG functional-mapping module |
| v2 | Paediatric DMG MRI segmentation + viewer, running models on device | Planned (from Oct 2027); setup underway now |

## v2 goals

- **Segment and measure** DMG on MRI (trained on BraTS-PEDs), and compare automated tumour volume with standard 2D RAPNO measurements.
- **Viewer** for researchers and radiologists: NiiVue on the web, plus a native Mac/iPad app.
- **On-device inference** with Apple Core AI, so patient scans never leave the machine.
- Later: maps of contrast leakage (blood–brain barrier opening) and infused-drug spread.

## v1 (archived)

To look at the MEG work:

```bash
git checkout v1-meg
```

`datastructure.py` and `notebooks/` explore the BCI Competition IV dataset 3 `.mat` files. The data is not in the repo; download it from the [BCI Competition IV page](https://www.bbci.de/competition/iv/) into `dataset/`.

## Setup

```bash
git clone https://github.com/AnuOluwatomiwa/neurocode.git
cd neurocode
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Research log

What I read, tried and got wrong is in [RESEARCH_LOG.md](RESEARCH_LOG.md).

## License

MIT, see [LICENSE](LICENSE).
