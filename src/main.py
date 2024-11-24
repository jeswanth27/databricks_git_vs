from pyspark.sql import SparkSession

def main():
    # Initialize Spark session
    spark = SparkSession.builder.appName("DatabricksJob").getOrCreate()

    # Example: Create a DataFrame
    data = [("Alice", 34), ("Bob", 45), ("Cathy", 29)]
    columns = ["Name", "Age"]
    df = spark.createDataFrame(data, columns)

    # Print the DataFrame
    df.show()

    # Save DataFrame to CSV (example)
    df.write.csv("/dbfs/tmp/example_output.csv", header=True)

if __name__ == "__main__":
    main()
