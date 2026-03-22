# 💾 BigData-Hadoop
Demonstrates Hadoop ecosystem experience: HDFS, MapReduce, and Spark basics

## Features
- Hands-on experience with **HDFS** (storing and accessing big data)
- **MapReduce jobs** for processing large datasets
- Basic **Spark integration** for faster analytics

## MapReduce Python Code

```python
from mrjob.job import MRJob

class MRWordCount(MRJob):
    def mapper(self, _, line):
        for word in line.split():
            yield word.lower(), 1

    def reducer(self, word, counts):
        yield word, sum(counts)

if __name__ == '__main__':
    MRWordCount.run()

Resources:

Apache Hadoop Official Website

---

### 🔄 Data-Pipelines

```markdown
# 🔄 Data-Pipelines
This project demonstrates my experience creating **ETL/Data Pipelines** for analytics.

## Features
- Extract data from **various sources**
- Transform data using **Python or SQL**
- Load cleaned data into **databases or analytics tools**

## Example ETL Python Code

```python
import pandas as pd

# Extract
data = pd.read_csv("raw_data.csv")

# Transform
data['total'] = data['quantity'] * data['price']

# Load
data.to_csv("processed_data.csv", index=False)

Resources:

ETL Concepts Wiki
