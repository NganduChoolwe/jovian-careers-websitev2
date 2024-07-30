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
        
def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("select * from jobs where id = :val"),
            {'val': id}
        )

        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return dict(rows[0]._mapping)

def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)")

    conn.execute(query, 
         {'job_id': job_id, 
          'full_name': data['full_name'], 
          'email': data['email'], 
          'education': data['education'],
          'work_experience': data['work_experience'], 
          'linkedin_url': data['linkedin_url'],
          'resume_url': data['resume_url']})
