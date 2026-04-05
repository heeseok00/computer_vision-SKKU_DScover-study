# SKKU DScover — 컴퓨터 비전 정규 스터디

텐서플로우와 딥러닝 기초, CV 예제를 **주차별**로 정리한 저장소입니다. 각 항목은 예제 코드·노트북·**필기 마크다운**으로 바로 이동할 수 있도록 링크를 붙였습니다.

---

## Week 1 — 오리엔테이션 · 스터디 소개

---

- 스터디 목표 및 진행 방식 (자료 추가 예정)

---

## Week 2 — 선형 회귀 (Linear Regression)

---

- 선형 회귀 알고리즘 실습 ([Notebook](DScover_CV_2주차/linear_regression.ipynb))

---

## Week 3 — (주차 제목 · 배울 내용 정리 예정)

---

- 항목을 추가한 뒤, 아래 형식처럼 링크를 붙이면 됩니다.  
  `- 주제 이름 ([Notebook](경로))` 또는 `([TF v2 Keras Code](경로))`

---

## Week 4 — CNN과 MNIST 숫자 분류

---

- CNN + `tf.train.CheckpointManager`를 이용한 MNIST 분류 ([TF v2 Keras Code](DScover_CV_4주차_CNN/01.mnist_classification_using_cnn_with_tfsaver_v2_keras.py)) ([필기 노트](DScover_CV_4주차_CNN/01.mnist_classification_using_cnn_with_tfsaver_v2_keras.md))
- CNN + TensorBoard 로깅 ([TF v2 Keras Code](DScover_CV_4주차_CNN/02.mnist_classification_using_cnn_v2_keras_with_tensorboard.py.py)) ([필기 노트](DScover_CV_4주차_CNN/02.mnist_classification_using_cnn_v2_keras_with_tensorboard.md))
- ResNet (ILSVRC, degradation, residual block, ImageNet·CIFAR 실험 요약) ([필기 노트](DScover_CV_4주차_CNN/03.resnet.md))
- EfficientNet (compound scaling, B0–B7, 논문·실험 요약) ([필기 노트](DScover_CV_4주차_CNN/04.efficientnet.md))
- Fine-Tuning · Transfer Learning (헤드 교체, 동결 범위, 데이터 규모·유사도) ([필기 노트](DScover_CV_4주차_CNN/05.finetuning_transfer_learning.md))
- TensorFlow 2.0 — high-level(`fit`) vs low-level(GradientTape) ([필기 노트](DScover_CV_4주차_CNN/06.tensorflow2_high_level_low_level.md))
- `tf.keras.applications` 사전 학습 모델 표 · Dogs vs Cats ([필기 노트](DScover_CV_4주차_CNN/07.tf_keras_applications_pretrained.md))
- Keras Callbacks (`ModelCheckpoint`, `TensorBoard`, `EarlyStopping` 등) ([필기 노트](DScover_CV_4주차_CNN/08.keras_callbacks.md))
- TensorFlow GPU 확인 스크립트 `gpu_setting.py`는 **로컬 전용** (`.gitignore`로 제외)

---

## Appendix

---

- 주차별로 공통으로 쓰는 스크립트·실험 노트를 여기에 모을 수 있습니다.

---

## Revision History

---

### 2026-04-06

- Week 4 Keras Callbacks 필기(`08.keras_callbacks.md`) 및 `images/keras_callbacks/` 슬라이드 9장 추가, README 목차 링크

### 2026-04-05

- `.gitignore`에 `*.pdf`, `.cursor/rules/`, `gpu_setting.py` 추가 및 기존 추적 해제
- Week 4 TensorBoard 예제 필기 마크다운(`02…tensorboard.md`) README에서 링크
- Week 4 ResNet 강의 필기(`03.resnet.md`) README에서 링크 — 슬라이드 PNG는 `images/resnet/` 에 포함
- Week 4 EfficientNet 필기(`04.efficientnet.md`) 및 `images/efficientnet/` 슬라이드 추가
- Week 4 Fine-Tuning·전이학습 필기(`05.finetuning_transfer_learning.md`) 및 `images/finetuning/` 슬라이드 추가
- Week 4 TF2.0 구현 두 가지 방법 필기(`06.tensorflow2_high_level_low_level.md`) 및 `images/tf2_impl/` 슬라이드 추가
- Week 4 `applications`·Dogs vs Cats 필기(`07.tf_keras_applications_pretrained.md`) 및 `images/tf_keras_pretrained/` 슬라이드 추가
- `07` 필기에 VGG Fine-Tuning 2단계·Colab·TF 튜토리얼·슬라이드 `04_vgg_finetuning_dogs_cats.png` 보강
- README에 주차별 목차와 코드·노트북 상대 경로 링크 추가
- Week 4 CheckpointManager 예제 필기 마크다운(`01…keras.md`) README에서 링크
- Cursor 에이전트용 규칙(`.cursor/rules/`)은 **로컬 전용**으로 두고 Git에는 포함하지 않음
