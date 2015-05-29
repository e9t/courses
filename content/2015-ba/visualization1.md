Title: Visualization
Date: 2015-05-01
Tags: lectures
Courseid: 2015-ba
Toc: True

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
<img src="images/table.png" width="250px">
<img src="images/graph.png" width="400px"><br>
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
<img src="images/stats.png">
However, the four datasets vary considerably when graphed
<img src="images/anscombe.png">
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
    - Bertin's visual variables (Bertin, *Semiology of Graphics*, 1967|1983)
        <div class="row">
        <div class="col-md-8">
        - Position
        - Size
        - Value
        - Texture
        - Color
        - Orientation
        - Shape
        </div>
        <div class="col-md-4">
        <img src="images/bertin.png">
        </div>
        </div>

# Data encoding
- Objective
    - Assume 7 visual encodings and n data attributes
    - Pick the best encoding from the exponential number of possibilities
- Principle of Consistency
    - The properties of the image (visual variables) should match the properties of the data
- Principle of Importance Ordering
    - Encode the most important information in the most effective way
- Mackinlay’s expressiveness criteria
    - A set of facts is expressible in a visual language if the sentences (i.e. the visualizations) in the language express all the facts in the set of data, and only the facts in the data. 
- Mackinlay’s effectiveness criteria
    - A visualization is more effective than another visualization if the information conveyed by one visualization is more readily perceived than the information in the other visualization.<br>
    <img src="http://www.softviscollection.org/intro/a-thousand-words/images/ali-mackinlay.png" width="500px">
    <img src="images/viz-accuracy.png" width="400px">
- Bertin's visual variables and their syntactics. Figure derived from Bertin (1967|1983), MacEachren (1995), and MacEachren et al. (2012)<br>
<img src="images/va.png" width="500px">

## Data combinations and dimensions

### Univariate data (1D)

1. Line plot<br><img src="http://matplotlib.org/_images/spectrum_demo.png">
1. Bar plot<br><img src="http://matplotlib.org/_images/xcorr_demo.png">
1. Box-and-whisker plot<br><img src="images/baw.gif" alt="http://www.statgraphics.com/eda.htm">

### Bivariate data (2D)

1. 2D scatter plot<br><img src="http://upload.wikimedia.org/wikipedia/commons/0/0f/Oldfaithful3.png">

### Trivariate data (3D)

1. Use 3D scatter plot<br><img src="http://scikit-learn.org/stable/_images/plot_pca_iris_001.png">
1. Map two variables [x, y] in 2D space + Map third variable [z] with another visual attribute (ex: color, shape, size)<br><img src="images/trivariate.png" width="200px">

### Multivariate data (>3D)

- How many variables can be depicted in a image?

> "With up to three rows, a data table can be constructed directly as a single image. However, an image has only three dimensions. And this barrier is impassible." -- Bertin

## Examples
### [Iris dataset](http://en.wikipedia.org/wiki/Iris_flower_data_set)
<img src="images/irisdata.png" width="400px">
<img src="http://www.nature.com/nmeth/journal/v9/n10/images/nmeth.2186-F1.jpg" width="400px">

### [How to lie with visualization](http://data.heapanalytics.com/how-to-lie-with-data-visualization/)

1. Truncated Y-Axis<br><img src="images/lie1.png" width="400px">
1. Cumulative graphs<br><img src="images/lie2-1.png" width="300px"><img src="images/lie2-2.png" width="300px">
1. Ignoring conventions<br><img src="https://s3.amazonaws.com/heapdatablog/misleading3_pie.png" width="400px"><img src="https://s3.amazonaws.com/heapdatablog/misleading3_deaths.jpg" width="400px">
1. For more, see [WTF visualizations](http://viz.wtf/)

### Awesome visualization examples

1. Words<br><img src="http://i2.wp.com/flowingdata.com/wp-content/uploads/2008/12/wordle.png?zoom=2&resize=545%2C333" width="400px">
1. Web pages
    - [http://internet-map.net/](http://internet-map.net/)
1. World refugees
    - [http://www.therefugeeproject.org/](http://www.therefugeeproject.org/)
1. Movie revenues
    - [http://www.nytimes.com/interactive/2008/02/23/movies/20080223_REVENUE_GRAPHIC.html](http://www.nytimes.com/interactive/2008/02/23/movies/20080223_REVENUE_GRAPHIC.html)
1. Others
    - [http://infosthetics.com/](http://infosthetics.com/)
    - [http://www.visualcomplexity.com/](http://www.visualcomplexity.com/)
    - [http://datavisualization.ch/showcases/](http://datavisualization.ch/showcases/)

## In-class Practice: Worldwide Disasters (1900-2008)

- Visualize with the data below<br><img src="images/assign.png">
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
