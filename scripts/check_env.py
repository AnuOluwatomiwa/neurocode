"""Check the neurocode research environment: imports and Apple GPU (MPS)."""
import importlib
import sys

PACKAGES = ["numpy", "pandas", "scipy", "matplotlib", "rdkit", "sklearn",
            "xgboost", "scanpy", "torch", "monai", "nibabel", "SimpleITK"]

print(f"Python {sys.version.split()[0]}")
failed = []
for name in PACKAGES:
    try:
        mod = importlib.import_module(name)
        print(f"  ok   {name} {getattr(mod, '__version__', '')}")
    except Exception as e:
        failed.append(name)
        print(f"  FAIL {name}: {e}")

try:
    import torch
    mps = torch.backends.mps.is_available()
    print(f"Apple GPU (MPS): {'available' if mps else 'NOT available'}")
    if mps:
        x = torch.ones(1000, 1000, device="mps")
        print(f"  MPS test: {(x @ x).sum().item():.0f} (expect 1000000000)")
except Exception as e:
    print(f"MPS check failed: {e}")

sys.exit(1 if failed else 0)
