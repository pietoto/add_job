from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorer_1.db")
    session = db_session.create_session()

    job = Jobs()
    job.team_leader = 1
    job.job = 'worker 1'
    job.work_size = 4
    job.collaborators = '2'
    job.is_finished = False

    session.add(job)

    job = Jobs()
    job.team_leader = 2
    job.job = 'worker 2'
    job.work_size = 7
    job.collaborators = '4'
    job.is_finished = True

    session.add(job)

    job = Jobs()
    job.team_leader = 3
    job.job = 'worker 3'
    job.work_size = 54
    job.collaborators = '5'
    job.is_finished = False

    session.add(job)
    session.commit()


if __name__ == '__main__':
    main()
