Title: Wrap-up
Date: 2015-06-05 15:00
Status: draft

https://twitter.com/echojuliett/status/491451029859213312

## Everything is a function
- What we're trying to do, is to find appropriate weight values

## So, is there a one-size-fits-all algorithm?
No!
The best algorithm depends on the characteristics of the trainin data.

{% csv '''
,Logistic Regression,Decision Tree
Does it require variables to be normally distributed?,No,No
Does it suffer multicollinearity issue?,Yes,No
Does it do as well with categorical variables?,Yes,Yes
Does it conduct variable selection without stepwise?,,
Does it apply to sparse data?,,
''' %}

- http://www.quora.com/What-are-the-advantages-of-different-classification-algorithms

## "There's no such thing as a free lunch"

### Bias-variance tradeoff

- Bias-variance decomposition
http://scott.fortmann-roe.com/docs/BiasVariance.html

### Time-performance tradeoff

- TBD
