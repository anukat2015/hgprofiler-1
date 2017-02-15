from datetime import datetime
from sqlalchemy import (DateTime,
                        Column,
                        func,
                        ForeignKey,
                        Integer,
                        String,
                        UniqueConstraint)

from model import Base


class Archive(Base):
    ''' Data model for a results archive. '''

    __tablename__ = 'archive'
    __table_args__ = (
        UniqueConstraint('tracker_id',
                         'zip_file_id',
                         name='tracker_id_zip_file_id'),
    )

    id = Column(Integer, primary_key=True)
    tracker_id = Column(String(255), nullable=False)
    username = Column(String(255), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=True)
    date = Column(DateTime, default=func.current_timestamp())
    site_count = Column(Integer, nullable=False)
    found_count = Column(Integer, nullable=False)
    not_found_count = Column(Integer, nullable=False)
    error_count = Column(Integer, nullable=False)
    zip_file_id = Column(Integer, ForeignKey('file.id', name='fk_zip_file'))
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self,
                 tracker_id,
                 username,
                 category_id,
                 site_count,
                 found_count,
                 not_found_count,
                 error_count,
                 zip_file_id):
        ''' Constructor. '''

        self.tracker_id = tracker_id
        self.username = username
        self.category_id = category_id
        self.site_count = site_count
        self.found_count = found_count
        self.not_found_count = not_found_count
        self.error_count = error_count
        self.zip_file_id = zip_file_id

    def as_dict(self):
        ''' Return dictionary representation of this archive. '''

        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'tracker_id': self.tracker_id,
            'username': self.username,
            'category_id': self.category_id,
            'date': self.date.isoformat(),
            'site_count': self.site_count,
            'found_count': self.found_count,
            'not_found_count': self.not_found_count,
            'error_count': self.error_count,
            'zip_file_url': '/api/files/{}'.format(self.zip_file_id),
            'zip_file_id': self.zip_file_id
        }
