# standard
import os


# base directory
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)


# path to important file
DATABASE_NAME = 'blog.db'
DATABASE_PATH = os.path.join(BASE_DIR,'database/blog.db')
