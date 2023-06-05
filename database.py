from sqlalchemy import create_engine, text
from decouple import config

db_connection_string = "mysql+pymysql://"+config("username")+":"+config("password")+"@"+config("host")+ "/"+ config("database")+"?charset=utf8mb4"

engine = create_engine(db_connection_string,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    result_all = result.fetchall()
    column_names = result.keys()
    jobs = []
    for row in result_all:
      jobs.append(dict(zip(column_names, row)))
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    result_all = result.fetchall()
    column_names = result.keys()
    total_rows = result.rowcount
    if (total_rows < int(id)) or (int(id) < 1):
      return None
    else:
      job = dict(zip(column_names, result_all[int(id)-1]))
      return job
    

def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query2 = "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES ("+ job_id  + ",\'" + data['full_name'] + "\',\'" + data['email'] + "\',\'" + data['linkedin_url'] + "\',\'" + data['education'] + "\',\'" + data['work_experience'] + "\',\'" + data['resume_url'] + "\')"
    query = text(query2)
    conn.execute(query)