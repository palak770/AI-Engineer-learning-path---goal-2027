# Supervised Learning

Supervised learning is a type of machine learning where a model is trained on **labeled data**—meaning each input is paired with the correct output.  
The model learns by comparing its predictions with the actual answers provided in the training data. Over time, it adjusts itself to minimize errors and improve accuracy.  

The goal of supervised learning is to make **accurate predictions** when given new, unseen data.

> **Key Idea:** Supervised machine learning involves training a model on labeled data to learn patterns and relationships, which it then uses to make accurate predictions on new data.

---

## Phases of Supervised Learning

1. **Training Phase (Algorithm)**  
   - Involves feeding the algorithm **labeled data**, where each data point is paired with its correct output.  
   - The algorithm learns to identify patterns and relationships between the input and output data.

2. **Testing Phase (Logic)**  
   - Involves feeding the algorithm **new, unseen data** and evaluating its ability to predict the correct output based on the learned patterns.

---

## Types of Supervised Learning

1. **Classification (Defined Labels)**  
   - Output is a **categorical variable** (e.g., spam vs. non-spam emails, yes vs. no).  
   - Teaches a machine to sort things into categories. After learning, it can decide which category new items belong to.

2. **Regression (Continuous Values)**  
   - Output is a **continuous variable** (e.g., predicting house prices, stock prices).  
   - Predicts values instead of categories.

---

## Types of Classification

1. **Binary Classification**  
   - Goal: Sort data into **two distinct categories**.  
   - Example: spam vs. not spam.

2. **Multiclass Classification**  
   - Goal: Sort data into **more than two categories**.  
   - Example: cat, dog, bird.

3. **Multi-Label Classification**  
   - A single data point can belong to **multiple categories at once**.  
   - Example: A movie tagged as both action and comedy.

---

## How Classification Works in Machine Learning

1. **Data Collection:** Dataset with labeled items (e.g., "cat" or "dog").  
2. **Feature Extraction:** Identify features (color, shape, texture) that help distinguish classes.  
3. **Model Training:** Algorithm learns to map features to correct classes.  
4. **Model Evaluation:** Test on new data to check accuracy.  
5. **Prediction:** Model predicts class for new data using learned features.  

> Evaluating a classification model ensures it performs well on unseen data. Different metrics can be used depending on the problem.

---

## Classification Modeling

- **Class Separation:** Distinguish between classes.  
- **Decision Boundaries:** Linear or non-linear boundaries to separate classes.  
- **Sensitivity to Data Quality:** High-quality, representative data improves performance.  
- **Handling Imbalanced Data:** Use techniques like resampling or weighting.  
- **Interpretability:** Some models, like Decision Trees, are easier to interpret.

---

## Classification Algorithms

- **Linear Classifiers:** Create a **linear decision boundary**. Examples:  
  - Logistic Regression  
  - Support Vector Machines (kernel = linear)  
  - Single-layer Perceptron  
  - Stochastic Gradient Descent (SGD) Classifier

### Logistic Regression

- Predicts the **probability** that an input belongs to a specific class.  
- Used for **binary classification** (Yes/No, True/False, 0/1).  
- Uses the **sigmoid function** to convert inputs into a probability between 0 and 1.

#### Types of Logistic Regression
1. **Binomial Logistic Regression:** Two possible categories (Yes/No, Pass/Fail).  
2. **Multinomial Logistic Regression:** Three or more categories (e.g., cat, dog, sheep).  
3. **Ordinal Logistic Regression:** Categories with a natural order (low, medium, high).

#### Assumptions of Logistic Regression
- Independent observations  
- Binary dependent variables (for binary logistic regression)  
- Linear relationship between independent variables and log odds  
- No extreme outliers  
- Large sample size

#### Sigmoid Function
- Converts raw model output into a probability between 0 and 1.  
- **Threshold (usually 0.5):**  
  - ≥ 0.5 → Class 1  
  - < 0.5 → Class 0  
- Transforms continuous input into meaningful class predictions.
