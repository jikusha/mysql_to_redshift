from pyspark.sql import SparkSession


spark = SparkSession.builder.master("local[*]"). \
    config("spark.jars.packages", "mysql:mysql-connector-java:8.0.13").appName("Spark_demo"). \
    getOrCreate()

print(spark)

df = spark.read \
    .format("jdbc") \
    .option("driver","com.mysql.cj.jdbc.Driver") \
    .option("url", "jdbc:mysql://localhost:3307/classicmodels?useSSL=false") \
    .option("query", "select * from customers limit 10") \
    .option("user", "root") \
    .option("password", "example") \
    .load()

df.cache()

df.show()
df = df.selectExpr("to_json(struct(*))").show(truncate=False)

