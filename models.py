# coding: utf-8
from sqlalchemy import BigInteger, Column, DateTime, Integer, JSON, LargeBinary, String, text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class AnalysisReportInfo(Base):
    __tablename__ = 'analysis_report_info'

    seq = Column(BigInteger, nullable=False, unique=True)
    pulicid = Column(String(64), primary_key=True, nullable=False)
    context = Column(String)
    e_context = Column(String)
    m_context = Column(String)
    o_m_context = Column(String)
    file = Column(LargeBinary)
    o_file = Column(LargeBinary)
    date = Column(String(64), primary_key=True, nullable=False)
    o_date = Column(String(64))
    other_context = Column(String)
    o_other_context = Column(String)
    desc = Column(String(512))
    createuser = Column(String(20))
    createtime = Column(DateTime)
    updateuser = Column(String(20), server_default=text("'csg_cc'"))
    updatetime = Column(DateTime)
    Remark = Column(String(50), server_default=text("'csg_cc'"))


class BrainStudyInfo(Base):
    __tablename__ = 'brain_study_info'

    seq = Column(BigInteger, nullable=False, unique=True)
    body_part = Column(String(64), nullable=False)
    internalid = Column(BigInteger, nullable=False)
    date = Column(String(64), primary_key=True, nullable=False)
    publicid = Column(String(64), primary_key=True, nullable=False)
    resourcetype = Column(Integer, nullable=False)
    desc = Column(String(512))
    createuser = Column(String(20), server_default=text("'csg_cc'"))
    createtime = Column(DateTime)
    updateuser = Column(String(20), server_default=text("'csg_cc'"))
    updatetime = Column(DateTime)
    Remark = Column(String(50))


class ChestStudyInfo(Base):
    __tablename__ = 'chest_study_info'

    seq = Column(BigInteger, nullable=False, unique=True)
    body_part = Column(String(64))
    internalid = Column(BigInteger, nullable=False)
    date = Column(String(64), primary_key=True, nullable=False)
    publicid = Column(String(64), primary_key=True, nullable=False)
    resourcetype = Column(Integer, nullable=False)
    desc = Column(String(512))
    createuser = Column(String(20), server_default=text("'csg_cc'"))
    createtime = Column(DateTime)
    updateuser = Column(String(20), server_default=text("'csg_cc'"))
    updatetime = Column(DateTime)
    Remark = Column(String(50))


class DicomKeyword(Base):
    __tablename__ = 'dicom_keyword'

    seq = Column(BigInteger, primary_key=True)
    internalid = Column(BigInteger, nullable=False)
    date = Column(String(64), nullable=False)
    publicid = Column(String(64), nullable=False)
    resourcetype = Column(Integer, nullable=False)
    createuser = Column(String(20), server_default=text("'csg_cc'"))
    createtime = Column(DateTime)
    updateuser = Column(String(20), server_default=text("'csg_cc'"))
    updatetime = Column(DateTime)
    Remark = Column(String(50))


class DicomProgressRate(Base):
    __tablename__ = 'dicom_progress_rate'

    seq = Column(BigInteger, nullable=False, unique=True)
    publicid = Column(String(64), primary_key=True, nullable=False)
    percentage = Column(Integer, nullable=False, server_default=text("'0'"))
    date = Column(String(64), primary_key=True, nullable=False)
    cc_date = Column(DateTime)
    status = Column(Integer, server_default=text("'0'"))
    createuser = Column(String(20), server_default=text("'csg_cc'"))
    createtime = Column(DateTime)
    updateuser = Column(String(20), server_default=text("'csg_cc'"))
    updatetime = Column(DateTime)
    Remark = Column(String(50))


class ImageInfo(Base):
    __tablename__ = 'image_info'

    seq = Column(BigInteger, nullable=False, unique=True)
    pulicid = Column(String(64), primary_key=True, nullable=False)
    file_type = Column(Integer, server_default=text("'0000000000'"))
    file = Column(LargeBinary)
    date = Column(String(64), primary_key=True, nullable=False)
    desc = Column(String(512))
    createuser = Column(String(20), server_default=text("'csg_cc'"))
    createtime = Column(DateTime)
    updateuser = Column(String(20), server_default=text("'csg_cc'"))
    updatetime = Column(DateTime)
    Remark = Column(String(50))


class NoticeInfo(Base):
    __tablename__ = 'notice_info'

    seq = Column(BigInteger, nullable=False, unique=True)
    title = Column(String(256), primary_key=True, nullable=False)
    context = Column(String, nullable=False)
    date = Column(DateTime, primary_key=True, nullable=False)
    createuser = Column(String(20), server_default=text("'csg_cc'"))
    createtime = Column(DateTime)
    updateuser = Column(String(20), server_default=text("'csg_cc'"))
    updatetime = Column(DateTime)
    Remark = Column(String(50))


class NotifyInfo(Base):
    __tablename__ = 'notify_info'

    seq = Column(BigInteger, nullable=False, unique=True)
    publicid = Column(String(64), primary_key=True)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime)
    result = Column(JSON)
    desc = Column(String(512))
    createuser = Column(String(20), server_default=text("'csg_cc'"))
    createtime = Column(DateTime)
    updateuser = Column(String(20), server_default=text("'csg_cc'"))
    updatetime = Column(DateTime)
    Remark = Column(String(50))


class OperatingLog(Base):
    __tablename__ = 'operating_log'

    seq = Column(BigInteger, primary_key=True)
    name = Column(String(32), nullable=False)
    table_name = Column(String(64), nullable=False)
    publicid = Column(String(64))
    date = Column(String(64), server_default=text("''"))
    operation = Column(Integer, server_default=text("'0000000000'"))
    desc = Column(String(256))
    createuser = Column(String(20), server_default=text("'csg_cc'"))
    createtime = Column(DateTime)
    updateuser = Column(String(20), server_default=text("'csg_cc'"))
    updatetime = Column(DateTime)
    Remark = Column(String(50))


class ParameterSettingInfo(Base):
    __tablename__ = 'parameter_setting_info'

    seq = Column(BigInteger, nullable=False, unique=True)
    root = Column(String(256), primary_key=True, nullable=False)
    value = Column(JSON, nullable=False)
    date = Column(DateTime, primary_key=True, nullable=False)
    createuser = Column(String(20), server_default=text("'csg_cc'"))
    createtime = Column(DateTime)
    updateuser = Column(String(20), server_default=text("'csg_cc'"))
    updatetime = Column(DateTime)
    Remark = Column(String(50))


class PatientsKeyword(Base):
    __tablename__ = 'patients_keyword'

    seq = Column(BigInteger, nullable=False, unique=True)
    internalid = Column(BigInteger, nullable=False)
    date = Column(String(64), primary_key=True, nullable=False)
    publicid = Column(String(64), primary_key=True, nullable=False)
    resourcetype = Column(Integer, nullable=False)
    desc = Column(String(512))
    createuser = Column(String(20), server_default=text("'csg_cc'"))
    createtime = Column(DateTime)
    updateuser = Column(String(20), server_default=text("'csg_cc'"))
    updatetime = Column(DateTime)
    Remark = Column(String(50))


class PerfLog(Base):
    __tablename__ = 'perf_log'

    seq = Column(BigInteger, primary_key=True)
    perf_type = Column(Integer, server_default=text("'0000000000'"))
    perf_value = Column(String(32), nullable=False)
    from_date = Column(String(64))
    to_date = Column(String(64))
    desc = Column(String(512))
    createuser = Column(String(20), server_default=text("'csg_cc'"))
    createtime = Column(DateTime)
    updateuser = Column(String(20), server_default=text("'csg_cc'"))
    updatetime = Column(DateTime)
    Remark = Column(String(50))


class PulmonaryNodulesInfo(Base):
    __tablename__ = 'pulmonary_nodules_info'

    seq = Column(BigInteger, nullable=False, unique=True)
    body_part = Column(String(64), nullable=False)
    internalid = Column(BigInteger, nullable=False)
    date = Column(String(64), primary_key=True, nullable=False)
    publicid = Column(String(64), primary_key=True, nullable=False)
    resourcetype = Column(Integer, nullable=False)
    desc = Column(String(512))
    createuser = Column(String(20), server_default=text("'csg_cc'"))
    createtime = Column(DateTime)
    updateuser = Column(String(20), server_default=text("'csg_cc'"))
    updatetime = Column(DateTime)
    Remark = Column(String(50))


class RecordLog(Base):
    __tablename__ = 'record_log'

    seq = Column(BigInteger, primary_key=True)
    name = Column(String(32), nullable=False)
    publicid = Column(String(64))
    operation = Column(Integer, server_default=text("'0000000000'"))
    desc = Column(String(512))
    createuser = Column(String(20), server_default=text("'csg_cc'"))
    createtime = Column(DateTime)
    updateuser = Column(String(20), server_default=text("'csg_cc'"))
    updatetime = Column(DateTime)
    Remark = Column(String(50))


class ReportTemplateInfo(Base):
    __tablename__ = 'report_template_info'

    seq = Column(BigInteger, nullable=False, unique=True)
    id = Column(String(256), primary_key=True, nullable=False)
    context = Column(String, nullable=False)
    file = Column(LargeBinary, nullable=False)
    date = Column(DateTime, primary_key=True, nullable=False)
    createuser = Column(String(20), server_default=text("'csg_cc'"))
    createtime = Column(DateTime)
    updateuser = Column(String(20), server_default=text("'csg_cc'"))
    updatetime = Column(DateTime)
    Remark = Column(String(50))


class ShowDequeInfo(Base):
    __tablename__ = 'show_deque_info'

    seq = Column(BigInteger, nullable=False, unique=True)
    publicid = Column(String(64), primary_key=True, nullable=False)
    date = Column(String(64), primary_key=True, nullable=False)
    desc = Column(String(512))
    createuser = Column(String(20), server_default=text("'csg_cc'"))
    createtime = Column(DateTime)
    updateuser = Column(String(20), server_default=text("'csg_cc'"))
    updatetime = Column(DateTime)
    Remark = Column(String(50))


class StrokeInfo(Base):
    __tablename__ = 'stroke_info'

    seq = Column(BigInteger, nullable=False, unique=True)
    body_part = Column(String(64))
    internalid = Column(BigInteger, nullable=False)
    date = Column(String(64), primary_key=True, nullable=False)
    publicid = Column(String(64), primary_key=True, nullable=False)
    resourcetype = Column(Integer, nullable=False)
    desc = Column(String(512))
    createuser = Column(String(20), server_default=text("'csg_cc'"))
    createtime = Column(DateTime)
    updateuser = Column(String(20), server_default=text("'csg_cc'"))
    updatetime = Column(DateTime)
    Remark = Column(String(50))


class StudiesKeyword(Base):
    __tablename__ = 'studies_keyword'

    seq = Column(BigInteger, nullable=False, unique=True)
    internalid = Column(BigInteger, nullable=False)
    date = Column(String(64), primary_key=True, nullable=False)
    publicid = Column(String(64), primary_key=True, nullable=False)
    resourcetype = Column(Integer, nullable=False)
    desc = Column(String(512))
    createuser = Column(String(20), server_default=text("'csg_cc'"))
    createtime = Column(DateTime)
    updateuser = Column(String(20), server_default=text("'csg_cc'"))
    updatetime = Column(DateTime)
    Remark = Column(String(50))


class TeethStudyInfo(Base):
    __tablename__ = 'teeth_study_info'

    seq = Column(BigInteger, nullable=False, unique=True)
    body_part = Column(String(64), nullable=False)
    internalid = Column(BigInteger, nullable=False)
    date = Column(String(64), primary_key=True, nullable=False)
    publicid = Column(String(64), primary_key=True, nullable=False)
    resourcetype = Column(Integer, nullable=False)
    desc = Column(String(512))
    createuser = Column(String(20), server_default=text("'csg_cc'"))
    createtime = Column(DateTime)
    updateuser = Column(String(20), server_default=text("'csg_cc'"))
    updatetime = Column(DateTime)
    Remark = Column(String(50))


class TotalLog(Base):
    __tablename__ = 'total_log'

    seq = Column(BigInteger, primary_key=True)
    total_type = Column(Integer, server_default=text("'0000000000'"))
    total_value = Column(String(32), nullable=False)
    from_date = Column(String(64))
    to_date = Column(String(64))
    desc = Column(String(512))
    createuser = Column(String(20), server_default=text("'csg_cc'"))
    createtime = Column(DateTime)
    updateuser = Column(String(20), server_default=text("'csg_cc'"))
    updatetime = Column(DateTime)
    Remark = Column(String(50))


class TrackLog(Base):
    __tablename__ = 'track_log'

    seq = Column(BigInteger, primary_key=True)
    name = Column(String(32), nullable=False)
    table_name = Column(String(64), nullable=False)
    publicid = Column(String(64))
    field_list = Column(JSON)
    o_field_list = Column(JSON)
    date = Column(String(64))
    operation = Column(Integer, server_default=text("'0000000000'"))
    desc = Column(String(512))
    createuser = Column(String(20), server_default=text("'csg_cc'"))
    createtime = Column(DateTime)
    updateuser = Column(String(20), server_default=text("'csg_cc'"))
    updatetime = Column(DateTime)
    Remark = Column(String(50))


class UserLoginInfo(Base):
    __tablename__ = 'user_login_info'

    seq = Column(BigInteger, nullable=False, unique=True)
    name = Column(String(32), primary_key=True)
    password = Column(String(64), nullable=False)
    o_password = Column(String(64))
    date = Column(DateTime)
    status = Column(Integer, server_default=text("'0000000000'"))
    createuser = Column(String(20), server_default=text("'csg_cc'"))
    createtime = Column(DateTime)
    updateuser = Column(String(20), server_default=text("'csg_cc'"))
    updatetime = Column(DateTime)
    Remark = Column(String(50))


class UserPriorityInfo(Base):
    __tablename__ = 'user_priority_info'

    seq = Column(BigInteger, nullable=False, unique=True)
    name = Column(String(32), primary_key=True)
    priority = Column(Integer, server_default=text("'0'"))
    date = Column(DateTime)
    createuser = Column(String(20), server_default=text("'csg_cc'"))
    createtime = Column(DateTime)
    updateuser = Column(String(20), server_default=text("'csg_cc'"))
    updatetime = Column(DateTime)
    Remark = Column(String(50))


class UserRegisterInfo(Base):
    __tablename__ = 'user_register_info'

    seq = Column(BigInteger, nullable=False, unique=True)
    name = Column(String(32), primary_key=True)
    password = Column(String(64), nullable=False)
    tel = Column(String(64))
    idcard = Column(String(64))
    status = Column(Integer, server_default=text("'0000000000'"))
    date = Column(DateTime)
    region = Column(String(64))
    createuser = Column(String(20), server_default=text("'csg_cc'"))
    createtime = Column(DateTime, nullable=False)
    updateuser = Column(String(20), server_default=text("'csg_cc'"))
    updatetime = Column(DateTime)
    Remark = Column(String(50))


class UserTest(Base):
    __tablename__ = 'user_test'

    id = Column(BigInteger, primary_key=True)
    name = Column(String(20))
    createuser = Column(String(20), server_default=text("'csg_cc'"))
    createtime = Column(DateTime)
    updateuser = Column(String(20), server_default=text("'csg_cc'"))
    updatetime = Column(DateTime)
    Remark = Column(String(50))
