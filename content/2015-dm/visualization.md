Title: Visualization
Date: 2015-05-28
Tags: lectures
Courseid: 2015-dm
Toc: True

<img src="../2015-ba/images/scientist.png" width="500px"> ([source](http://www.marketingdistillery.com/2014/08/30/data-science-skill-set-explained/))

## What is data visualization?

- The visual representation of information
- Goals of data visualization
    - Effective, clear communication of information
    - Stimulate viewer engagement
    - Exploratory data analysis

## Advantages of visualization

- With many numbers and large datasets, need an efficient way to understand a vast amount of data
- The human visual system is the highest-bandwidth channel to the human brain
> **Example**: Given the income, college degree percentage of each state, try answering the following questions with either a table and a graphic representation. Which method is better in answering the questions?<br>
> - Which state has highest income?<br>
> - Relationship between income and education?<br>
> - Outliers?<br>
<img src="../2015-ba/images/table.png" width="250px">
<img src="../2015-ba/images/graph.png" width="400px"><br>
(Example by [Marti Hearst](http://en.wikipedia.org/wiki/Marti_Hearst))
- Graphs reveal data that statistics may not
> **Example**: [Anscombe's quartet](http://en.wikipedia.org/wiki/Anscombe's_quartet)<br>
<div class="row">
<div class="col-md-6">
{% csv '''
I,,II,,III,,IV
x,y,x,y,x,y,x,y
10.0,8.04,10.0,9.14,10.0,7.46,8.0,6.58
8.0,6.95,8.0,8.14,8.0,6.77,8.0,5.76
13.0,7.58,13.0,8.74,13.0,12.74,8.0,7.71
9.0,8.81,9.0,8.77,9.0,7.11,8.0,8.84
11.0,8.33,11.0,9.26,11.0,7.81,8.0,8.47
14.0,9.96,14.0,8.10,14.0,8.84,8.0,7.04
6.0,7.24,6.0,6.13,6.0,6.08,8.0,5.25
4.0,4.26,4.0,3.10,4.0,5.39,19.0,12.50
12.0,10.84,12.0,9.13,12.0,8.15,8.0,5.56
7.0,4.82,7.0,7.26,7.0,6.42,8.0,7.91
5.0,5.68,5.0,4.74,5.0,5.73,8.0,6.89
''' %}
</div>
<div class="col-md-6">
Simple summary statistics are all identical for four datasets
<img src="../2015-ba/images/stats.png">
However, the four datasets vary considerably when graphed
<img src="../2015-ba/images/anscombe.png">
</div>
</div>

## Data visualization process

1. Classify datatypes
    - Nominal (ex: fruits - apples, oranges, ...)
        - Operations: ==, !=
    - Ordinal (ex: quality of meat - grade A, AA, AAA, ...)
        - Operations: ==, !=, <=, >=
    - Quantitative
        - Interval (ex: dates - May 1st, 2015, location - LAT 38.9 LON 127)
            - Only differences may compared
            - Operations: ==, !=, <=, >=, -
        - Ratio (ex: length - 160cm)
            - Origin is meaningful
            - Operations: ==, !=, <=, >=, -, /
1. Map datasets to visual attributes that represent data types most effectively (also known as *data encoding*)
<img src="../2015-ba/images/cues.png" width="400px">

- Comparisons
<img src="../2015-ba/images/comparison-1.png" width="100%">

(Source: Nathan Yau, [Data points](http://flowingdata.com/data-points/DataPoints-Ch3.pdf))

## Data visualization types

<img src="../2015-ba/images/patterns-1.png" width="500px">
<img src="../2015-ba/images/patterns-2.png" width="500px">
<img src="../2015-ba/images/patterns-3.png" width="500px">

(Source: Joel Laumans, [An introduction to visualizing data](http://piksels.com/wp-content/uploads/2009/01/visualizingdata.pdf))

## Visualizing multi-dimensional data

### Univariate data (1D)

1. Line plot<br><img src="http://matplotlib.org/_images/spectrum_demo.png">
1. Bar plot<br><img src="http://matplotlib.org/_images/xcorr_demo.png">
1. Box-and-whisker plot<br><img src="../2015-ba/images/baw.gif" alt="http://www.statgraphics.com/eda.htm">

### Bivariate data (2D)

1. 2D scatter plot<br><img src="http://upload.wikimedia.org/wikipedia/commons/0/0f/Oldfaithful3.png">

### Trivariate data (3D)

1. Use 3D scatter plot<br><img src="http://scikit-learn.org/stable/_images/plot_pca_iris_001.png">
1. Map two variables [x, y] in 2D space + Map third variable [z] with another visual attribute (ex: color, shape, size)<br><img src="../2015-ba/images/trivariate.png" width="200px">

### Multivariate data (>3D)

- How many variables can be depicted in a image?

> "With up to three rows, a data table can be constructed directly as a single image. However, an image has only three dimensions. And this barrier is impassible." -- Bertin

## In-class Practice: Worldwide Disasters (1900-2008)

- Visualize with the data below<br><img src="../2015-ba/images/assign.png">
- Evaluation
    - Expressiveness
        - Do the mappings show the facts and only the facts?
        - Are visual mappings consistent? (e.g., respect color mappings)
    - Effectiveness
        - Are perceptually effective encodings used?
        - Are the most important data mapped to the most effective visual variables?
    - Cognitive Load (Efficiency)
        - Are there extraneous (unmapped) visual elements?
    - Data Transformation
        - Are transformations (filter, sort, derive, aggregate) appropriate?
    - Guides (Non-Data Elements)
        - Descriptive, consistent: Title, Label, Caption, Source, Annotations
        - Meaningful references: Gridlines, Legend 

## References
- http://selection.datavisualization.ch/
- [Chart and image gallery: 30+ free tools for data visualization and analysis](http://www.computerworld.com/article/2506820/business-intelligence-chart-and-image-gallery-30-free-tools-for-data-visualization-and-analysis.html)
- [NYT the year in graphics: 2012](http://www.nytimes.com/interactive/2012/12/30/multimedia/2012-the-year-in-graphics.html)
- [NYT the year in graphics: 2014](http://www.nytimes.com/interactive/2014/12/29/us/year-in-interactive-storytelling.html)
- Many contents in courtesy of [Cecilia Aragon](https://faculty.washington.edu/aragon/) and [Maneesh Agrawala](http://vis.berkeley.edu/~maneesh/)
- [빅데이터 분석 시각화 분석 : 1장 시각화정의 2장 프로세스](http://www.slideshare.net/neofuture/sds-n2)
- [빅데이터 분석 시각화 분석 : 3장 시각화 방법](http://www.slideshare.net/neofuture/sds-2)
