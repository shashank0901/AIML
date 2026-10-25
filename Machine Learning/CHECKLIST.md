# ML Checklist: CampusX *100 Days of ML*, curated

Source: [CampusX playlist](https://www.youtube.com/playlist?list=PLKnIA16_Rmvbr7zKYQuBfsVkjoLcJgxHH). **86 of 134 videos kept, ~46h 43m of video.** Watch at 1.25–1.5× where it's easy.

Skipped: intro and theory-of-ML-types videos (1–11), Anaconda setup (12), data gathering (CSV/JSON/API/scraping, 15–18), basic EDA and pandas profiling (19–22), the simplest imputation/outlier/encoding variants, intuition-only repeats of the from-scratch videos, and short code demos (e.g. dtreeviz, GridSearch-only videos).

Tick a box with `[x]`. Each section ends with a **🛠 Practice** checkpoint: do it yourself before moving on. That's where the learning happens.

---

## Project 0 · End-to-end warm-up  ·  53m

- [ ] **013** [End to End Toy Project](https://www.youtube.com/watch?v=dr7z7a_8lQw) · 31m
- [ ] **014** [How to Frame a Machine Learning Problem · How to plan a Data Science Project Effectively](https://www.youtube.com/watch?v=A9SezQlvakw) · 22m
- [ ] 🛠 **Practice:** Redo the Day 13 toy project yourself on a different small dataset, without looking at the video code.

## 1 · Feature Engineering  ·  5h 57m

- [ ] **023** [What is Feature Engineering](https://www.youtube.com/watch?v=sluoVhT0ehg) · 25m
- [ ] **024** [Feature Scaling - Standardization](https://www.youtube.com/watch?v=1Yw9sC0PNwY) · 33m
- [ ] **025** [Feature Scaling - Normalization · MinMaxScaling](https://www.youtube.com/watch?v=eBrGyuA2MIg) · 24m
- [ ] **026** [Encoding Categorical Data · Ordinal Encoding](https://www.youtube.com/watch?v=w2GglmYHfmM) · 20m
- [ ] **027** [One Hot Encoding · Handling Categorical Data](https://www.youtube.com/watch?v=U5oCv3JKWKA) · 30m
- [ ] **028** [How to use ColumnTransformer in Sklearn](https://www.youtube.com/watch?v=5TVj6iEBR4I) · 16m
- [ ] **029** [Machine Learning Pipelines A-Z](https://www.youtube.com/watch?v=xOccYkgRV4Q) · 46m
- [ ] **030** [Function Transformer · Log Transform](https://www.youtube.com/watch?v=cTjj3LE8E90) · 32m
- [ ] **031** [Power Transformer · Box - Cox Transform](https://www.youtube.com/watch?v=lV_Z4HbNAx0) · 21m
- [ ] **038** [Missing Indicator · Random Sample Imputation](https://www.youtube.com/watch?v=Ratcir3p03w) · 37m
- [ ] **039** [KNN Imputer · Multivariate Imputation](https://www.youtube.com/watch?v=-fK-xEev2I8) · 24m
- [ ] **040** [Multivariate Imputation by Chained Equations for Missing Value · MICE Algorithm](https://www.youtube.com/watch?v=a38ehxv3kyk) · 19m
- [ ] **041** [What are Outliers](https://www.youtube.com/watch?v=Lln1PKgGr_M) · 17m
- [ ] **043** [Outlier Detection and Removal using the IQR Method · Handing Outliers Part 3](https://www.youtube.com/watch?v=Ccv1-W5ilak) · 14m
- [ ] 🛠 **Practice:** On a messy dataset (Titanic or Ames Housing), build one sklearn `Pipeline` + `ColumnTransformer` with imputation (with missing indicators), encoding, scaling and a power transform. Then fit the imputer/scaler on ALL the data before splitting and compare: the leaky version looks better. Note how big the gap is and why.

## 2 · Dimensionality Reduction  ·  2h 29m

- [ ] **046** [Curse of Dimensionality](https://www.youtube.com/watch?v=ToGuhynu-No) · 15m
- [ ] **047** [Principle Component Analysis  (PCA) · Part 1](https://www.youtube.com/watch?v=iRbsBi5W0-c) · 34m
- [ ] **048** [Principle Component Analysis (PCA) · Part 2](https://www.youtube.com/watch?v=tXXnxjj2wM4) · 56m
- [ ] **049** [Principle Component Analysis(PCA) · Part 3](https://www.youtube.com/watch?v=tofVCUDrg4M) · 43m
- [ ] 🛠 **Practice:** Implement PCA from scratch (covariance → eigendecomposition) and match sklearn's `PCA` on MNIST up to sign. Plot reconstructions with 10, 50 and 150 components.

## 3 · Linear Regression & Gradient Descent  ·  7h 49m

- [ ] **051** [Simple Linear Regression · Mathematical Formulation](https://www.youtube.com/watch?v=dXHIDLPKdmA) · 54m
- [ ] **052** [Regression Metrics · MSE, MAE & RMSE](https://www.youtube.com/watch?v=Ti7c-Hz7GSM) · 44m
- [ ] **054** [Multiple Linear Regression · Part 2](https://www.youtube.com/watch?v=NU37mF5q8VE) · 48m
- [ ] **055** [Multiple Linear Regression · Part 3](https://www.youtube.com/watch?v=VmZWXzxmNrE) · 16m
- [ ] **056** [What are the main Assumptions of Linear Regression? · Top 5 Assumptions of Linear Regression](https://www.youtube.com/watch?v=EmSNAtcHLm8) · 18m
- [ ] **057** [Gradient Descent From Scratch · End to End Gradient Descent](https://www.youtube.com/watch?v=ORyfPJypKuU) · 1h 58m
- [ ] **058** [Batch Gradient Descent with Code Demo](https://www.youtube.com/watch?v=Jyo53pAyVAM) · 1h 05m
- [ ] **059** [Stochastic Gradient Descent](https://www.youtube.com/watch?v=V7KBAa_gh4c) · 50m
- [ ] **060** [Mini-Batch Gradient Descent](https://www.youtube.com/watch?v=_scscQ4HVTY) · 22m
- [ ] **061** [Polynomial Regression](https://www.youtube.com/watch?v=BNWLf3cKdbQ) · 27m
- [ ] **062** [Bias Variance Trade-off](https://www.youtube.com/watch?v=74DU02Fyrhk) · 8m
- [ ] 🛠 **Practice:** From scratch: OLS (normal equation), then batch, stochastic and mini-batch GD. Break it: feed GD unscaled features and a too-large learning rate; write down what happens and why.

## 4 · Regularization  ·  2h 37m

- [ ] **064** [Ridge Regression Part 2 · Mathematical Formulation & Code from scratch](https://www.youtube.com/watch?v=oDlZBQjk_3A) · 44m
- [ ] **065** [Ridge Regression Part 3 · Gradient Descent](https://www.youtube.com/watch?v=Fci_wwMp8G8) · 19m
- [ ] **066** [5 Key Points - Ridge Regression · Part 4](https://www.youtube.com/watch?v=8osKeShYVRQ) · 30m
- [ ] **067** [Lasso Regression · Intuition and Code Sample](https://www.youtube.com/watch?v=HLF4bFbBgwk) · 29m
- [ ] **068** [Why Lasso Regression creates sparsity?](https://www.youtube.com/watch?v=FN4aZPIAfI4) · 24m
- [ ] **069** [ElasticNet Regression · Intuition and Code Example](https://www.youtube.com/watch?v=2g2DBkFhTTY) · 12m
- [ ] 🛠 **Practice:** Implement ridge (closed form + GD) from scratch. Make 3 near-duplicate features and compare which ones Lasso, Ridge and ElasticNet keep across bootstrap samples.

## 5 · Logistic Regression & Classification Metrics  ·  5h 25m

- [ ] **070** [Logistic Regression Part 1 · Perceptron Trick](https://www.youtube.com/watch?v=XNXzVfItWGY) · 47m
- [ ] **072** [Logistic Regression Part 3 · Sigmoid Function](https://www.youtube.com/watch?v=ehO0-6i9qD4) · 41m
- [ ] **073** [Logistic Regression Part 4 · Loss Function](https://www.youtube.com/watch?v=6bXOo0sxY5c) · 29m
- [ ] **074** [Derivative of Sigmoid Function](https://www.youtube.com/watch?v=awjXaFR1jOM) · 6m
- [ ] **075** [Logistic Regression Part 5 · Gradient Descent & Code From Scratch](https://www.youtube.com/watch?v=ABrrSwMYWSg) · 37m
- [ ] **077** [Precision, Recall and F1 Score · Classification Metrics Part 2](https://www.youtube.com/watch?v=iK-kdhJ-7yI) · 43m
- [ ] **078** [ROC-AUC in Machine Learning Simplified](https://www.youtube.com/watch?v=gdW6hj9IXaA) · 1h 11m
- [ ] **079** [Softmax Regression · Multinomial Logistic Regression](https://www.youtube.com/watch?v=Z8noL_0M4tw) · 38m
- [ ] **081** [Logistic Regression Hyperparameters · Logistic Regression Part 8](https://www.youtube.com/watch?v=ay_OcblJasE) · 13m
- [ ] 🛠 **Practice:** From scratch: logistic regression with GD, softmax regression on `load_digits`, and ROC-AUC. Match sklearn. Break it: compute sigmoid + log loss naively at z = −1000 (NaN), then fix it.

## 6 · Naive Bayes, KNN & SVM  ·  3h 12m

- [ ] **087** [Naive Bayes Classifier · Part 6](https://www.youtube.com/watch?v=ZR1_QtLk_4U) · 15m
- [ ] **088** [Naive Bayes Classifier · Part 7](https://www.youtube.com/watch?v=2PVRG45eVrY) · 19m
- [ ] **089** [Naive Bayes Classifier · Part 8](https://www.youtube.com/watch?v=DeeWsqoY4Eo) · 16m
- [ ] **090** [Naive Bayes Part 9 · Handling Numerical Data](https://www.youtube.com/watch?v=TCgK2nBJx9o) · 9m
- [ ] **091** [What is K Nearest Neighbors? · Simple Overview in 1 Video](https://www.youtube.com/watch?v=abnL_GUGub4) · 52m
- [ ] **092** [Support Vector Machines · Geometric Intuition](https://www.youtube.com/watch?v=ugTxMLjLS8M) · 12m
- [ ] **093** [Mathematics of SVM · Support Vector Machines](https://www.youtube.com/watch?v=yCAlHPDgWtM) · 35m
- [ ] **094** [Mathematics of Support Vector Machine · Soft Margin SVM](https://www.youtube.com/watch?v=utqrvIFAE1k) · 15m
- [ ] **095** [Kernel Trick in SVM · Geometric Intuition](https://www.youtube.com/watch?v=egxjT0p7_K8) · 6m
- [ ] **096** [Kernel Trick in SVM · Code Example](https://www.youtube.com/watch?v=pjvmVMDrzVU) · 14m
- [ ] 🛠 **Practice:** Implement Multinomial Naive Bayes from scratch on an SMS spam dataset (with Laplace smoothing) and vectorized KNN. Show KNN accuracy dropping as you add pure-noise features (curse of dimensionality).

## 7 · Decision Trees  ·  2h 01m

- [ ] **097** [Decision Trees Geometric Intuition · Entropy](https://www.youtube.com/watch?v=IZnno-dKgVQ) · 58m
- [ ] **098** [Decision Trees - Hyperparameters · Overfitting and Underfitting in Decision Trees](https://www.youtube.com/watch?v=mDEV0Iucwz0) · 27m
- [ ] **099** [Regression Trees · Decision Trees Part 3](https://www.youtube.com/watch?v=RANHxyAvtM4) · 35m
- [ ] 🛠 **Practice:** Implement `best_split(x, y)` with Gini for one feature, and check it against a depth-1 sklearn tree. Break it: fit a regression tree on a linear trend and predict outside the training range.

## 8 · Ensembles: Voting, Bagging, Random Forest  ·  3h 21m

- [ ] **101** [Introduction to Ensemble Learning](https://www.youtube.com/watch?v=bHK1fE_BUms) · 38m
- [ ] **103** [Voting Ensemble · Classification](https://www.youtube.com/watch?v=pGQnNYdPTvY) · 24m
- [ ] **105** [Bagging · Introduction](https://www.youtube.com/watch?v=LUiBOAy7x6Y) · 31m
- [ ] **108** [Introduction to Random Forest · Intuition behind the Algorithm](https://www.youtube.com/watch?v=F9uESCHGjhA) · 34m
- [ ] **109** [How Random Forest Performs So Well? Bias Variance Trade-Off in Random Forest](https://www.youtube.com/watch?v=jHgG4gjuFAk) · 13m
- [ ] **110** [Bagging Vs Random Forest · What is the difference between Bagging and Random Forest](https://www.youtube.com/watch?v=l93jRojZMqU) · 12m
- [ ] **111** [Random Forest Hyper-parameters](https://www.youtube.com/watch?v=WOFVY_wQ9wU) · 15m
- [ ] **113** [OOB Score · Out of Bag Evaluation in Random Forest](https://www.youtube.com/watch?v=tdDhyFoSG94) · 7m
- [ ] **114** [Feature Importance using Random Forest and Decision Trees · How is Feature Importance calculated](https://www.youtube.com/watch?v=R47JAob1xBY) · 27m
- [ ] 🛠 **Practice:** Build a random forest from sklearn trees + bootstrap + random feature subsets yourself. Plot OOB error vs. number of trees, and see whether impurity importance ranks a random ID column high.

## 9 · Boosting: AdaBoost, Gradient Boosting, XGBoost, Stacking  ·  8h 52m

- [ ] **115** [How Adaboost Classifier Works? · Geometric Intuition](https://www.youtube.com/watch?v=sFKnP0iP0K0) · 17m
- [ ] **116** [AdaBoost - A Step by Step Explanation](https://www.youtube.com/watch?v=RT0t9a3Xnfw) · 19m
- [ ] **117** [AdaBoost Algorithm · Code from Scratch](https://www.youtube.com/watch?v=a20TaKNsriE) · 16m
- [ ] **119** [Bagging Vs Boosting · What is the difference between Bagging and Boosting](https://www.youtube.com/watch?v=7M5oWXCpDEw) · 6m
- [ ] **120** [Gradient Boosting Explained · How Gradient Boosting Works?](https://www.youtube.com/watch?v=fbKz7N92mhQ) · 33m
- [ ] **121** [Gradient Boosting Regression Part 2 · Mathematics of Gradient Boosting](https://www.youtube.com/watch?v=nMNiTZm-qY0) · 57m
- [ ] **122** [Gradient Boosting for Classification · Geometric Intuition](https://www.youtube.com/watch?v=4p5EQtyxSyI) · 1h 05m
- [ ] **123** [Introduction to XGBOOST](https://www.youtube.com/watch?v=C6aDw4y8qJ0) · 1h 20m
- [ ] **124** [XGBoost for Regression · XGBoost Part 2](https://www.youtube.com/watch?v=gmp2tS2joaA) · 47m
- [ ] **125** [XGBoost For Classification · How XGBoost works on Classification Problems](https://www.youtube.com/watch?v=mELtxVUNNrw) · 39m
- [ ] **126** [The Maths Behind XGBoost](https://www.youtube.com/watch?v=0Eo-_5bfers) · 1h 57m
- [ ] **127** [Stacking and Blending Ensembles](https://www.youtube.com/watch?v=O-aDHBGMqXA) · 35m
- [ ] 🛠 **Practice:** Write gradient boosting regression from scratch (fit shallow trees to residuals with a learning rate). Plot test error vs. number of trees for your GBM (lr 1.0 vs. 0.1) and a random forest: which one overfits?

## 10 · Clustering  ·  2h 10m

- [ ] **128** [K-Means Clustering Algorithm · Geometric Intuition](https://www.youtube.com/watch?v=5shTLzwAdEc) · 24m
- [ ] **130** [K-Means Clustering Algorithm From Scratch In Python](https://www.youtube.com/watch?v=MFraC1JObUo) · 34m
- [ ] **131** [Agglomerative Hierarchical Clustering · Python Code Example](https://www.youtube.com/watch?v=Ka5i9TVUT-E) · 37m
- [ ] **132** [DBSCAN Clustering Algorithms · Density Based Clustering](https://www.youtube.com/watch?v=1_bLnsNmhCI) · 34m
- [ ] 🛠 **Practice:** K-means from scratch with k-means++ init. Break it on `make_moons`, then show DBSCAN handling it.

## 11 · Imbalanced Data & Hyperparameter Tuning  ·  1h 57m

- [ ] **133** [Undersampling · Oversampling](https://www.youtube.com/watch?v=yh2AKoJCV3k) · 57m
- [ ] **134** [Hyperparameter Tuning using Optuna · Bayesian Optimization using Optuna](https://www.youtube.com/watch?v=E2b3SKMw934) · 59m

## 🏁 Final Project

- [ ] Pick an imbalanced tabular dataset (e.g. Kaggle Credit Card Fraud or Bank Marketing) and frame the problem: business goal, metric, baseline
- [ ] Leakage-safe preprocessing `Pipeline` (section 1) + proper train/validation/test or CV split
- [ ] Compare logistic regression, random forest and XGBoost; handle imbalance (class weights vs. SMOTE, inside the pipeline)
- [ ] Tune the best model with Optuna; pick a threshold from the PR curve
- [ ] Error analysis + feature importance; write a one-page README: what worked, what failed, why
- [ ] Push to GitHub
