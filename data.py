from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName('readParquet').getOrCreate()



path = "/Users/marwensmida/Downloads/DatasetToCompleteTheSixSparkExercises/products_parquet"

df = spark.read.parquet(path)

df.sort(col("price").desc()).show()
