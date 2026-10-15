# Step 3: ANN Model

## Goal
Show a small neural network (ANN) that can be trained again by anyone with one command. This documents what the model does so a reviewer does not need to read all the code.

## Inputs
The model uses 13 numeric measurements per sample (the scikit-learn wine dataset): alcohol, malic acid, ash, alkalinity of ash, magnesium, total phenols, flavanoids, nonflavanoid phenols, proanthocyanins, color intensity, hue, OD280/OD315 ratio and proline.

## Output
One of 3 classes (class_0, class_1, class_2). The model predicts the class of each sample.

## ANN architecture
- Type: multi-layer perceptron (scikit-learn MLPClassifier)
- Two hidden layers: 32 neurons, then 16 neurons
- Maximum 300 training rounds (epochs)
- Inputs are scaled with StandardScaler

## Data strategy
- Split: 60% training, 20% validation, 20% test
- The split keeps the same class mix in each part
- The scaler is fitted on training data only
- Fixed random seed (42), so results can be repeated

## Evidence files
Run `python src/train_ann.py`. It saves:
- models/step3_ann_model.joblib
- results/step3_ann/step3_ann_metrics.csv
- results/step3_ann/step3_ann_validation_predictions.csv
- results/step3_ann/step3_ann_test_predictions.csv
- results/step3_ann/step3_ann_metadata.json
- results/step3_ann/step3_ann_loss_curve.png
- results/step3_ann/step3_ann_confusion_matrix_validation.png
- results/step3_ann/step3_ann_confusion_matrix_test.png

## Limitations
- The dataset is small and clean, so results will look better than real-world use.
- This ANN is a learning demo and does not use the timetable data.
- The model does not replace laboratory testing or expert checking.