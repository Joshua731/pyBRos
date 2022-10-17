from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

URL = "mysql+mysqlconnector://aluno:aluno123@localhost:3306/ORM_pyBRos"

# $ cd C:\Program Files\MySQL\MySQL Server 8.0\bin
# $ .\mysql.exe -u aluno -p
# mysql> CREATE DATABASE ORM;
# mysql> USE ORM;
# mysql> SHOW TABLES;
Base = declarative_base()


class Projeto(Base):
    __tablename__ = "Projeto"
    id_projeto = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)

    Dashboard = relationship("Dashboard", backref="projeto")
    Usuario = relationship("Usuario", backref="projeto")

    id_participante = Column(Integer, ForeignKey("Participante.id_participante"))



    def __str__(self):
        return "Projeto(id_projeto={}, nome=\"{}\")".format(
            self.id_projeto, self.nome)


class Dashboard(Base):
    __tablename__ = "Dashboard"
    id_dashboard = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)

    pagina = relationship("Pagina", backref="dashboard")

    id_projeto = Column(Integer, ForeignKey("Projeto.id_projeto"))
    id_participante = Column(Integer, ForeignKey("Participante.id_participante"))

    def __str__(self):
        return "Dashboard(id_dashboard={}, nome=\"{}\")".format(
            self.id_dashboard, self.nome)


class Pagina(Base):
    __tablename__ = "Pagina"
    id_pagina = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)

    id_dashboard = Column(Integer, ForeignKey("Dashboard.id_dashboard"))

    def __str__(self):
        return "Dashboard(id_pagina={}, nome=\"{}\")".format(
            self.id_pagina, self.nome)


class Usuario(Base):
    __tablename__ = "Usuario"
    id_usuario = Column(Integer, primary_key=True)
    nome = Column(String(150), nullable=False)

    id_participante = Column(Integer, ForeignKey("Participante.id_participante"))
    id_projeto = Column(Integer, ForeignKey("Projeto.id_projeto"))

    def __str__(self):
        return "Dashboard(id_usuario={}, nome=\"{}\")".format(
            self.id_usuario, self.nome)


class Participantes(Base):
    __tablename__ = "Participantes"
    id_participante = Column(Integer, primary_key=True)
    usuario = relationship("Usuario", backref="participantes")
    projeto = relationship("Projeto", backref="participantes")


    def __str__(self):
        return "Dashboard(id_dashboard={}\")".format(
            self.id_participante)


def main():
    engine = create_engine(url=URL)
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    # mysql> DESC Pessoa;

    Session = sessionmaker(engine, expire_on_commit=False)

    with Session.begin() as session:
        projeto = Projeto(nome="Usina Solar")
        projeto.Usuario.append(
            Usuario(nome="Joshua"))
        projeto.Dashboard.append(nome="Inversores")

        session.add(projeto)


    with Session.begin() as session:

        print("============================================")

        projeto = session.query(Projeto).get(1)

        print(projeto)

        for usuario in projeto.Usuario:
            print("   * " + str(usuario))
        for dashboard in projeto.Dashboard:
            print("   * " + str(dashboard))

    with Session.begin() as session:

        print("\n============================================")

        usuario = session.query(Usuario).get(1)

        print(usuario)
        print(usuario.nome)

    with Session.begin() as session:

        print("\n============================================")

        dashboard = session.query(Dashboard).get(1)

        print(dashboard)
        print(dashboard.nome)


if __name__ == "__main__":
    main()
