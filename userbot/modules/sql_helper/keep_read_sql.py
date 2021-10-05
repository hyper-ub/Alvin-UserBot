try:
    from userbot.modules.sql_helper import SESSION, BASE
except ImportError:
    raise AttributeError

from sqlalchemy import Column, String


class KeepRead(BASE):
    __tablename__ = "keepread"
    groupid = Column(String(14), primary_key=True)

    def __init__(self, sender):
        self.groupid = str(sender)


KeepRead.__table__.create(checkfirst=True)


def is_kread():
    try:
        return SESSION.query(KeepRead).all()
    except BaseException:
        return None
    finally:
        SESSION.close()


def kread(chat):
    adder = KeepRead(str(chat))
    SESSION.add(adder)
    SESSION.commit()


def unkread(chat):
    rem = SESSION.query(KeepRead).get((str(chat)))
    if rem:
        SESSION.delete(rem)
        SESSION.commit()
