Title: Dimensionality reduction
Status: draft

## Variable selection in regression

- Why should we select a subset of variables?
    - May be expensive or not feasible to collect a full complement of predictors for future prediction.
    - May be able to measure fewer predictors more accurately (e.g. in surveys)
    - More predictors, more missing values
    - Parsimony (a.k.a. Occam’s Razor): the simpler, the better.
    - Multicollinearity: presence of two or more predictors sharing the same linear relationship with the outcome variables
- Goal: 일반화 성능 향상
    - More robust
    - Higher predictive accuracy

### Methods

- Exhaustive search: 모든 변수 조합의 성능을 살펴봄
    - ${x_1}, {x_2}, {x_3}, ..., {x_1, x_2}, {x_2, x_3}, ..., {x_1, x_2, x_3}, ...$
- Partial search
    - Forward selection: 유의성이 큰 변수는 하나씩 더함
        - ${x_4} \to {x_4, x_5} \to {x_1, x_4, x_5} \to {x_1, x_3, x_4, x_5} \to {x_1, x_2, x_3, x_4, x_5}$
    - Backward elimination: 유의성이 작은 변수를 하나씩 제거
        - ${x_1, x_2, x_3, x_4, x_5} \to {x_1, x_3, x_4, x_5} \to {x_1, x_4, x_5} \to {x_4, x_5} to{x_4}$
    - Stepwise selection: 유의성이 큰 변수를 더하거나 작은 변수를 하나씩 제거
        - ${x_4} \to {x_4, x_5} \to {x_1, x_4, x_5} \to {x_1, x_5} \to ...$
