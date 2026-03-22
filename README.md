## 💾 BigData-Hadoop
Demonstrated experience with distributed storage and processing using the Hadoop framework.

### ✨ Features
- **HDFS:** Experience managing and storing large-scale datasets.
- **MapReduce:** Custom Python-based jobs for distributed data processing.
- **Spark:** Basic integration for high-speed, in-memory analytics.

### 🐍 MapReduce Python Code
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

MRJob Documentation

🔄 Data-Pipelines
Creation of robust ETL (Extract, Transform, Load) pipelines for downstream analytics.

✨ Features
Extract: Retrieval from diverse sources like CSVs and SQL databases.

Transform: Data cleaning and feature engineering using Pandas.

Load: Outputting processed data for business intelligence tools.

🐍 Example ETL Python Code
Python
import pandas as pd

# Extract
data = pd.read_csv("raw_data.csv")

# Transform
# Calculating total revenue per row
data['total'] = data['quantity'] * data['price']

# Load
data.to_csv("processed_data.csv", index=False)
Resources:

ETL Concepts & Best Practices

Pandas Documentation

🛠️ Technologies Used
Languages: Python, SQL

Big Data: HDFS, MapReduce, Apache Spark

Libraries: Pandas, MRJob
