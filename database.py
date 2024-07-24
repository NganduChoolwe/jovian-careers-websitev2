from sqlalchemy import create_engine, text
import os

db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
    db_connection_string,
    connect_args={"connect_timeout": 30})

with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))

print("type(result):", type(result))
result_all = result.all()
print("type(result.all()):", type(result_all))
first_result = result_all[0]
print("type(first_result):", type(first_result))

# Convert the Row object to a dictionary
first_result_dict = dict(first_result._mapping)
print("type(first_result_dict):", type(first_result_dict))
print(first_result_dict)

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("select * from jobs"))
        jobs = []
        for row in result.all():
          jobs.append(dict(row._mapping)) 
        return jobs
