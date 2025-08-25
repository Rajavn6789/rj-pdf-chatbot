import click
import os
from flask_sqlalchemy import SQLAlchemy
from flask import current_app
from pinecone import Pinecone
db = SQLAlchemy()


@click.command("init-db")
def init_db_command():
    with current_app.app_context():
        try:
            os.makedirs(current_app.instance_path)
        except OSError:
            pass
        db.drop_all()
        db.create_all()

        
        # --- Drop Pinecone index if exists ---
        pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        index_name = os.getenv("PINECONE_INDEX_NAME")

        indexes = [i["name"] for i in pc.list_indexes()]
        if index_name in indexes:
            pc.delete_index(index_name)
            click.echo(f"Deleted Pinecone index: {index_name}")

    click.echo("Initialized the database.")
