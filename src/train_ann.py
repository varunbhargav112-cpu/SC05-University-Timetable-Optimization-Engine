"""Train a small ANN and save model, metrics, predictions and figures."""
import json
from pathlib import Path

import joblib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.metrics import (ConfusionMatrixDisplay, accuracy_score,
                             confusion_matrix, f1_score)
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler

SEED = 42
ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results" / "step3_ann"
MODELS = ROOT / "models"
RESULTS.mkdir(parents=True, exist_ok=True)
MODELS.mkdir(parents=True, exist_ok=True)

# 1. Data: 60% train, 20% validation, 20% test
data = load_wine()
X, y = data.data, data.target
X_train, X_tmp, y_train, y_tmp = train_test_split(
    X, y, test_size=0.4, random_state=SEED, stratify=y)
X_val, X_test, y_val, y_test = train_test_split(
    X_tmp, y_tmp, test_size=0.5, random_state=SEED, stratify=y_tmp)

scaler = StandardScaler().fit(X_train)
X_train, X_val, X_test = (scaler.transform(a) for a in (X_train, X_val, X_test))

# 2. Train
model = MLPClassifier(hidden_layer_sizes=(32, 16), max_iter=300,
                      random_state=SEED)
model.fit(X_train, y_train)

# 3. Evaluate
rows, preds = [], {}
for name, Xs, ys in [("train", X_train, y_train),
                     ("validation", X_val, y_val),
                     ("test", X_test, y_test)]:
    p = model.predict(Xs)
    preds[name] = (ys, p)
    rows.append({"split": name,
                 "accuracy": accuracy_score(ys, p),
                 "macro_f1": f1_score(ys, p, average="macro")})
pd.DataFrame(rows).to_csv(RESULTS / "step3_ann_metrics.csv", index=False)

for name in ("validation", "test"):
    ys, p = preds[name]
    pd.DataFrame({"y_true": ys, "y_pred": p}).to_csv(
        RESULTS / f"step3_ann_{name}_predictions.csv", index=False)

# 4. Figures
plt.figure(figsize=(6, 4))
plt.plot(model.loss_curve_)
plt.title("ANN training loss curve")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.tight_layout()
plt.savefig(RESULTS / "step3_ann_loss_curve.png", dpi=150)
plt.close()

for name in ("validation", "test"):
    ys, p = preds[name]
    ConfusionMatrixDisplay(confusion_matrix(ys, p),
                           display_labels=data.target_names).plot(cmap="Blues")
    plt.title(f"ANN confusion matrix ({name})")
    plt.tight_layout()
    plt.savefig(RESULTS / f"step3_ann_confusion_matrix_{name}.png", dpi=150)
    plt.close()

# 5. Model and metadata
joblib.dump({"scaler": scaler, "model": model}, MODELS / "step3_ann_model.joblib")
meta = {"dataset": "sklearn wine", "seed": SEED,
        "hidden_layers": [32, 16], "epochs_run": model.n_iter_,
        "classes": list(data.target_names)}
(RESULTS / "step3_ann_metadata.json").write_text(json.dumps(meta, indent=2))

print("Saved model and Step 3 evidence files.")