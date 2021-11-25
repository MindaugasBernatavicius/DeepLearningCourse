# DeepLearningCourse


## Learning Algorithms table

| Algo name | Impl | Problem | Train. Complexity | Inf. Complexity | Learn type | Implementations | Usage senarios| Acc. Tunning | Perf. Tunning |
|-----------|------|---------|-------------------|-----------------|------------|-----------------|---------------|--------------|---------------|
| Linear Regression | OLS | Regression | x | x | Supervised | Scikit | Linearly separable data, small datasets | 
| Linear Regression | MLE | Regression | x | x | Supervised | ? | ? |
| Linear Regression | GD | Regression | x | x | Supervised | ? | Linearly separable data, large datasets |
| Logistic Regression |  | Classification | x | x | Supervised | ? | ? |
| Support Vector Machine |  | Regression, Classification | x | x | Supervised | ? | ? |
| Decision Tree | CART | Regression, Classification | x | x | Supervised | ? | ? | max_depth | - check if the tree is balanced, try entropy if not - try different feature encoding (index vs OHE) - try presort=True on small datasets  - feature selection | 
