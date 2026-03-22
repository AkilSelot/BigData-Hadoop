## 💾 BigData-Hadoop
Demonstrates experience with the Hadoop ecosystem, focusing on distributed storage and processing.

### ✨ Features
- **HDFS:** Hands-on experience storing and accessing large-scale datasets.
- **MapReduce:** Writing custom jobs to process data across clusters.
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

Official Apache Hadoop Documentation

🔄 Data-Pipelines
Demonstrates the creation of robust ETL (Extract, Transform, Load) pipelines for downstream analytics.

✨ Features
Extract: Automating data retrieval from diverse sources (CSVs, APIs, SQL).

Transform: Cleaning and aggregating data using Python (Pandas) or SQL.

Load: Shipping processed data to databases or analytics-ready files.

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

Core ETL Concepts & Best Practices

🛠️ Technologies Used
Languages: Python, SQL

Big Data: HDFS, MapReduce, Apache Spark

Libraries: Pandas, MRJob
