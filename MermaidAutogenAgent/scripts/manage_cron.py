# manage_cron.py
from crontab import CronTab
import yaml


def load_config():
    with open("config/config.yaml", "r") as f:
        return yaml.safe_load(f)


def install_cron_job():
    config = load_config()
    cron = CronTab(user=True)  # Use user=True to manage the cron of the current user

    # Look for an existing job
    for job in cron:
        if job.comment == "mermaid_autogen_sync":
            cron.remove(job)  # Remove existing job to avoid duplicates

    # Create a new job
    job = cron.new(
        command=f'python {config["data_directory"]}/scripts/upload_to_s3.py',
        comment="mermaid_autogen_sync",
    )
    job.setall(config["cron_job_frequency"])

    # Write the job to the crontab
    cron.write()
    print("Cron job installed successfully.")


if __name__ == "__main__":
    install_cron_job()
