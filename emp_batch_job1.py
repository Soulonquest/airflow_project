from pyspark.sql import SparkSession

def process_data():
    spark = SparkSession.builder.appName("GCPDataprocJob").getOrCreate()

    # Defining GCS bucket and paths
    bucket = "airflow-projects_for_practice"
    emp_data_path = f"gs://{bucket}/airflow_project_1/data/employee.csv"
    dept_data_path = f"gs://{bucket}/airflow_project_1/data/department.csv"
    output_path = f"gs://{bucket}/airflow_project_1/output"

    # Read datasets 
    employee = spark.read.csv(emp_data_path, header=True, inferSchema=True)
    department = spark.read.csv(dept_data_path, header=True, inferSchema=True)

    # Filter employee data
    filtered_employee = employee.filter(employee.salary > 50000)

    # Join datasets
    joined_data = filtered_employee.join(department, "dept_id", "inner")

    # Write output
    joined_data.write.csv(output_path, mode="overwrite", header=True)

    spark.stop()

if __name__ == "__main__":
    process_data()
