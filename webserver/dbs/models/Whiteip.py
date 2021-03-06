# -*- coding:utf-8 -*-
""" 蜜罐日志表 """

from dbs.initdb import Base, engine
from sqlalchemy import Column, String


class Whiteip(Base):
    __tablename__ = "Whiteip"
    src_host = Column(String(50), nullable=False, primary_key=True)


def init_db():
    Base.metadata.create_all(engine)


def drop_db():
    Base.metadata.drop_all(engine)


if __name__ == "__main__":
    init_db()
    # drop_db()
    # whiteip_data = Whiteip()
    # whiteip_data.src_host = '172.18.222.170'
    # DBSession.add(whiteip_data)
    # DBSession.flush()
    # DBSession.commit()
    print("create OpencanaryLog table")
"""
CREATE TABLE `Whiteip` (
	src_host VARCHAR(50) NOT NULL,
	PRIMARY KEY (src_host)
)

mysql> select * from Whiteip;
+----------------+
| src_host       |
+----------------+
| 172.18.222.170 |
+----------------+
1 row in set (0.01 sec)

"""
