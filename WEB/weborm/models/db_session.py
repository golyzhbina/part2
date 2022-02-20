import sqlalchemy as sl
import sqlalchemy.orm as orm
import sqlalchemy.ext.declarative as dec

SqlAlcBase = dec.declarative_base()
__factory = None


def global_init(connection_string):
    global __factory
    if __factory:
        return

    engine = sl.create_engine(connection_string)
    __factory = orm.sessionmaker(bind=engine)

    from . import __all_models

    SqlAlcBase.metadata.create_all(engine)


def create_session():
    global __factory
    return __factory()



